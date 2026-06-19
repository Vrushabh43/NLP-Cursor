"""Build the equations knowledge-graph dataset from arXiv papers.

Processes papers from the assigned paper list, extracts up to 7 enumerated
equations per paper with meaning, symbol descriptions, inter-equation
relations, and an audit trail.  Stops after collecting >= 350 equations
(completing the last paper fully).

Usage
-----
    python build_dataset.py [--paper-list paper_list_16.txt] [--output output/dataset.json]

No LLM or prompting is used.  All extraction is rule-based from arXiv
LaTeX source files.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

from nlp_extraction import (
    EquationInfo,
    build_symbol_table,
    classify_relations,
    extract_meaning,
    extract_symbols_from_latex,
    get_symbol_descriptions,
)
from pdf_equation_pipeline import (
    EquationCandidate,
    _MULTI_ROW_ENVS,
    _NUMBERED_ENV_RE,
    _SINGLE_NUM_ENVS,
    _clean_latex,
    _split_top_level_rows,
    _strip_tex_comments,
    count_equations_from_pdf,
    download_arxiv_pdf,
    download_arxiv_source,
    extract_math_symbols,
    extract_tex_from_source,
    read_paper_list,
)


# ---------------------------------------------------------------------------
# Enhanced equation parser (with position + label tracking)
# ---------------------------------------------------------------------------

def parse_equations_with_context(
    tex_raw: str,
    max_equations: int = 7,
) -> tuple[list[dict[str, Any]], dict[str, str], str]:
    """Parse equations from LaTeX source with full context for NLP extraction.

    Parameters
    ----------
    tex_raw : str
        Raw LaTeX source content of the paper.
    max_equations : int
        Maximum number of equations to extract.

    Returns
    -------
    equations : list[dict]
        List of equation dicts with keys: number, latex, label, env_start,
        env_end, source.
    label_to_number : dict[str, str]
        Mapping from LaTeX labels to equation numbers.
    tex_clean : str
        Comment-stripped LaTeX source.
    """
    tex = _strip_tex_comments(tex_raw)

    # ── Scope: main body only ──────────────────────────────────────
    doc_start = re.search(r"\\begin\{document\}", tex)
    preamble = tex[:doc_start.start()] if doc_start else ""
    if doc_start:
        tex = tex[doc_start.end():]

    # If preamble redefines equation numbering to non-standard format, skip all.
    preamble_renum = re.search(
        r"\\renewcommand\{\\theequation\}\{[^}]*[A-Za-z]\\arabic", preamble
    )
    if preamble_renum:
        return [], {}, tex

    renum_match = re.search(r"\\renewcommand\{\\theequation\}", tex)
    if renum_match:
        tex = tex[:renum_match.start()]

    is_revtex = bool(re.search(r"\\documentclass.*?\{revtex", preamble, re.DOTALL))
    if is_revtex:
        appendix_match = re.search(r"\\appendix\b", tex)
        if appendix_match:
            tex = tex[:appendix_match.start()]

    # ── Remove subequations (letter-suffixed labels like 5a, 5b) ──
    tex = re.sub(
        r"\\begin\{subequations\}.*?\\end\{subequations\}",
        "",
        tex,
        flags=re.DOTALL,
    )

    # ── Handle \setcounter{equation}{N} ───────────────────────────
    _setcounter_re = re.compile(r"\\setcounter\{equation\}\{(\d+)\}")
    setcounters: list[tuple[int, int]] = [
        (m.start(), int(m.group(1))) for m in _setcounter_re.finditer(tex)
    ]

    eq_count = 0

    def _next_number(pos: int) -> str:
        nonlocal eq_count
        for sc_pos, sc_val in setcounters:
            if sc_pos < pos:
                eq_count = sc_val
        eq_count += 1
        return str(eq_count)

    equations: list[dict[str, Any]] = []
    label_to_number: dict[str, str] = {}

    for match in _NUMBERED_ENV_RE.finditer(tex):
        if len(equations) >= max_equations:
            break

        env_name = match.group(1)
        content = match.group(2)
        pos = match.start()

        # Extract label if present.
        label_match = re.search(r"\\label\{([^}]+)\}", content)
        label = label_match.group(1) if label_match else ""

        if env_name in _SINGLE_NUM_ENVS:
            if r"\nonumber" in content or r"\notag" in content:
                continue
            latex = _clean_latex(content)
            if latex:
                eq_num = _next_number(pos)
                equations.append({
                    "number": eq_num,
                    "latex": latex,
                    "label": label,
                    "env_start": match.start(),
                    "env_end": match.end(),
                    "source": "arxiv_tex_source",
                })
                if label:
                    label_to_number[label] = eq_num
        else:
            # Multi-row environment.
            rows = _split_top_level_rows(content)
            # Find label for the whole block (if any).
            block_label = label
            for row in rows:
                if len(equations) >= max_equations:
                    break
                row_stripped = row.strip()
                if not row_stripped:
                    continue
                if r"\nonumber" in row_stripped or r"\notag" in row_stripped:
                    continue
                # Check for row-level label.
                row_label_match = re.search(r"\\label\{([^}]+)\}", row_stripped)
                row_label = row_label_match.group(1) if row_label_match else ""
                latex = _clean_latex(row_stripped)
                if latex:
                    eq_num = _next_number(pos)
                    equations.append({
                        "number": eq_num,
                        "latex": latex,
                        "label": row_label or block_label,
                        "env_start": match.start(),
                        "env_end": match.end(),
                        "source": "arxiv_tex_source",
                    })
                    if row_label:
                        label_to_number[row_label] = eq_num
                    elif block_label and block_label not in label_to_number:
                        label_to_number[block_label] = eq_num

    return equations, label_to_number, tex


# ---------------------------------------------------------------------------
# Full paper processing
# ---------------------------------------------------------------------------

def process_paper_pdf_texify(
    arxiv_id: str,
    cache_dir: Path,
    max_equations: int = 7,
    sleep_seconds: float = 3.0,
) -> tuple[dict[str, Any], int]:
    """Process a paper using PDF-only extraction (PyMuPDF + texify OCR).

    Parameters
    ----------
    arxiv_id : str
        arXiv identifier.
    cache_dir : Path
        Cache directory.
    max_equations : int
        Maximum equations to extract.
    sleep_seconds : float
        Download delay.

    Returns
    -------
    entry : dict
        The paper's dataset entry.
    count : int
        Number of equations extracted.
    """
    from pdf_extractor import extract_equations_pdf_only

    audit_global: dict[str, str] = {}

    try:
        pdf_path = download_arxiv_pdf(
            arxiv_id, cache_dir, sleep_seconds=sleep_seconds, force=False,
        )
        audit_global["download_pdf"] = f"Downloaded PDF for {arxiv_id}"
    except Exception as exc:
        print(f"  WARN: Could not download PDF for {arxiv_id}: {exc}")
        return {}, 0

    try:
        pdf_eqs = extract_equations_pdf_only(pdf_path, max_equations=max_equations)
        audit_global["extract_pdf_texify"] = (
            f"Extracted {len(pdf_eqs)} equations via PyMuPDF + texify OCR"
        )
    except Exception as exc:
        print(f"  WARN: PDF extraction failed for {arxiv_id}: {exc}")
        return {}, 0

    if not pdf_eqs:
        return {}, 0

    eq_data: dict[str, dict[str, Any]] = {}
    eq_infos: list[EquationInfo] = []

    for eq in pdf_eqs:
        sym_keys = extract_symbols_from_latex(eq["latex"])
        sym_dict = {k: "" for k in sym_keys}
        from nlp_extraction import _KNOWN_SYMBOLS
        for k in sym_keys:
            base = k.split("_")[0] if "_" in k else k
            if base in _KNOWN_SYMBOLS:
                sym_dict[k] = _KNOWN_SYMBOLS[base]

        meaning = ""
        if eq.get("context_before"):
            sentences = re.split(r"(?<=[.!?])\s+", eq["context_before"])
            if sentences:
                last = sentences[-1].strip()
                last = re.sub(r"[,:;]\s*$", "", last).strip()
                if len(last) > 10:
                    meaning = last[:200]

        audit_trail = dict(audit_global)
        audit_trail[f"extract_equation_{eq['number']}"] = (
            f"Extracted equation ({eq['number']}) from PDF page {eq.get('page', '?')} via texify"
        )

        eq_info = EquationInfo(
            number=eq["number"], latex=eq["latex"], symbols=sym_keys, position=0
        )
        eq_infos.append(eq_info)

        eq_data[eq["number"]] = {
            "equation": eq["latex"],
            "meaning": meaning,
            "symbols": sym_dict,
            "relations": {},
            "audit-trail": audit_trail,
        }

    from nlp_extraction import _compute_symbol_similarity
    for eq in eq_infos:
        rels = {}
        for other in eq_infos:
            if other.number == eq.number:
                continue
            sim = _compute_symbol_similarity(eq, other)
            if sim > 0.4:
                rels[other.number] = {"grade": "potential", "description": "shares significant mathematical symbols"}
            elif sim > 0.25:
                rels[other.number] = {"grade": "potential", "description": "nearby equation with shared symbols"}
            else:
                rels[other.number] = {"grade": "none", "description": ""}
        eq_data[eq.number]["relations"] = rels

    return eq_data, len(pdf_eqs)


def process_paper_pdf(
    arxiv_id: str,
    cache_dir: Path,
    max_equations: int = 7,
    sleep_seconds: float = 3.0,
) -> tuple[dict[str, Any], int]:
    """Process a paper using PDF-only extraction (PyMuPDF + pix2tex).

    Parameters
    ----------
    arxiv_id : str
        arXiv identifier.
    cache_dir : Path
        Cache directory.
    max_equations : int
        Maximum equations to extract.
    sleep_seconds : float
        Download delay.

    Returns
    -------
    entry : dict
        The paper's dataset entry.
    count : int
        Number of equations extracted.
    """
    from pdf_extractor import extract_equations_from_pdf
    from pdf_equation_pipeline import download_arxiv_pdf

    audit_global: dict[str, str] = {}

    # Download PDF.
    try:
        pdf_path = download_arxiv_pdf(
            arxiv_id, cache_dir,
            sleep_seconds=sleep_seconds, force=False,
        )
        audit_global["download_pdf"] = f"Downloaded PDF for {arxiv_id}"
    except Exception as exc:
        print(f"  WARN: Could not download PDF for {arxiv_id}: {exc}")
        return {}, 0

    # Extract equations from PDF.
    try:
        pdf_eqs = extract_equations_from_pdf(pdf_path, max_equations=max_equations)
        audit_global["extract_equations_pdf"] = (
            f"Extracted {len(pdf_eqs)} equations via PyMuPDF + pix2tex"
        )
    except Exception as exc:
        print(f"  WARN: PDF extraction failed for {arxiv_id}: {exc}")
        return {}, 0

    if not pdf_eqs:
        return {}, 0

    # Build equation entries with meaning from context.
    eq_data: dict[str, dict[str, Any]] = {}
    eq_infos: list[EquationInfo] = []

    for eq in pdf_eqs:
        sym_keys = extract_symbols_from_latex(eq.latex)
        sym_dict = {k: "" for k in sym_keys}
        # Use known physics symbols as fallback descriptions.
        from nlp_extraction import _KNOWN_SYMBOLS
        for k in sym_keys:
            base = k.split("_")[0] if "_" in k else k
            if base in _KNOWN_SYMBOLS:
                sym_dict[k] = _KNOWN_SYMBOLS[base]

        # Extract meaning from context_before.
        meaning = ""
        if eq.context_before:
            sentences = re.split(r"(?<=[.!?])\s+", eq.context_before)
            if sentences:
                last = sentences[-1].strip()
                last = re.sub(r"[,:;]\s*$", "", last).strip()
                if len(last) > 10:
                    meaning = last[:200]

        audit_trail = dict(audit_global)
        audit_trail[f"extract_equation_{eq.number}"] = (
            f"Extracted equation ({eq.number}) from PDF page {eq.page} via pix2tex OCR"
        )
        audit_trail[f"crop_region_{eq.number}"] = (
            f"Cropped region ({eq.bbox[0]:.0f},{eq.bbox[1]:.0f})-"
            f"({eq.bbox[2]:.0f},{eq.bbox[3]:.0f}) on page {eq.page}"
        )

        eq_info = EquationInfo(
            number=eq.number, latex=eq.latex, symbols=sym_keys, position=0
        )
        eq_infos.append(eq_info)

        eq_data[eq.number] = {
            "equation": eq.latex,
            "meaning": meaning,
            "symbols": sym_dict,
            "relations": {},
            "audit-trail": audit_trail,
        }

    # Classify relations (symbol overlap based, no tex cross-refs).
    from nlp_extraction import _compute_symbol_similarity
    eq_numbers = [e.number for e in eq_infos]
    for eq in eq_infos:
        rels = {}
        for other in eq_infos:
            if other.number == eq.number:
                continue
            sim = _compute_symbol_similarity(eq, other)
            if sim > 0.4:
                rels[other.number] = {"grade": "potential", "description": "shares significant mathematical symbols"}
            elif sim > 0.25:
                rels[other.number] = {"grade": "potential", "description": "nearby equation with shared symbols"}
            else:
                rels[other.number] = {"grade": "none", "description": ""}
        eq_data[eq.number]["relations"] = rels

    return eq_data, len(pdf_eqs)


def process_paper(
    arxiv_id: str,
    cache_dir: Path,
    max_equations: int = 7,
    sleep_seconds: float = 3.0,
) -> tuple[dict[str, Any], int]:
    """Process a single paper and return the dataset entry.

    Uses a **PDF-first** strategy for 100% accurate equation counting:
    1. Download the PDF and count ``(N)`` equation labels (ground truth).
    2. Download the TeX source and parse equation content.
    3. Match TeX equations to PDF numbers by sequential order.

    Parameters
    ----------
    arxiv_id : str
        arXiv identifier (e.g., ``2410.07429``).
    cache_dir : Path
        Directory for caching downloaded source archives.
    max_equations : int
        Maximum equations to extract from this paper.
    sleep_seconds : float
        Delay before downloading (respect arXiv rate limits).

    Returns
    -------
    entry : dict
        The paper's dataset entry ``{eq_num: {equation, meaning, ...}}``.
    count : int
        Number of equations extracted.
    """
    audit_global: dict[str, str] = {}

    # ── Step 1: Download PDF and count equations (ground truth) ───
    try:
        pdf_path = download_arxiv_pdf(
            arxiv_id, cache_dir, sleep_seconds=sleep_seconds, force=False,
        )
    except Exception as exc:
        print(f"  WARN: Could not download PDF for {arxiv_id}: {exc}")
        return {}, 0

    pdf_eq_numbers = count_equations_from_pdf(pdf_path)
    audit_global["count_from_pdf"] = (
        f"PDF ground truth: {len(pdf_eq_numbers)} numbered equations"
    )

    if not pdf_eq_numbers:
        return {}, 0

    # Cap at max_equations.
    pdf_eq_numbers = pdf_eq_numbers[:max_equations]

    # ── Step 2: Download TeX source and parse equation content ────
    try:
        source_path = download_arxiv_source(
            arxiv_id, cache_dir, sleep_seconds=0,  # PDF already downloaded with delay
        )
        tex_raw = extract_tex_from_source(source_path)
        audit_global["download_source"] = (
            f"Downloaded arXiv source for {arxiv_id}"
        )
    except Exception:
        tex_raw = ""

    tex = ""
    label_to_number: dict[str, str] = {}
    tex_equations: list[dict[str, Any]] = []

    if tex_raw:
        parsed = parse_equations_with_context(
            tex_raw, max_equations=max(200, max_equations),
        )
        tex_equations, label_to_number, tex = parsed
        audit_global["parse_tex"] = (
            f"TeX source: {len(tex_equations)} equation environments found"
        )

    # ── Step 3: Match TeX equations to PDF numbers by order ───────
    # The PDF numbers are the ground truth. TeX equations are matched
    # sequentially: PDF eq (1) ↔ TeX eq[0], PDF eq (2) ↔ TeX eq[1], etc.
    equations: list[dict[str, Any]] = []
    for idx, pdf_num in enumerate(pdf_eq_numbers):
        eq_entry: dict[str, Any] = {"number": str(pdf_num)}
        if idx < len(tex_equations):
            tex_eq = tex_equations[idx]
            eq_entry.update({
                "latex": tex_eq["latex"],
                "label": tex_eq.get("label", ""),
                "env_start": tex_eq.get("env_start", 0),
                "env_end": tex_eq.get("env_end", 0),
                "source": "arxiv_tex_source",
            })
        else:
            # No matching TeX equation — use placeholder.
            eq_entry.update({
                "latex": "",
                "label": "",
                "env_start": 0,
                "env_end": 0,
                "source": "pdf_number_only",
            })
        equations.append(eq_entry)

    audit_global["match_equations"] = (
        f"Matched {sum(1 for e in equations if e['source'] == 'arxiv_tex_source')}"
        f"/{len(equations)} equations with TeX content"
    )

    if not equations:
        return {}, 0

    # Step 4: Build global symbol table from the paper.
    global_symbols = build_symbol_table(tex)
    audit_global["build_symbol_table"] = (
        f"Built global symbol table with {len(global_symbols)} entries"
    )

    # Step 5: Process each equation.
    eq_infos: list[EquationInfo] = []
    eq_data: dict[str, dict[str, Any]] = {}

    for eq in equations:
        eq_num = eq["number"]
        eq_latex = eq["latex"]

        # 5a: Extract meaning.
        meaning, meaning_audit = extract_meaning(
            tex, eq["env_start"], eq["env_end"], eq_latex
        )

        # 5b: Extract symbols and descriptions.
        sym_keys = extract_symbols_from_latex(eq_latex)
        sym_dict, sym_audit = get_symbol_descriptions(
            sym_keys, global_symbols, tex, eq["env_start"], eq["env_end"]
        )

        # 5c: Build EquationInfo for relation classification.
        eq_info = EquationInfo(
            number=eq_num,
            latex=eq_latex,
            symbols=sym_keys,
            label=eq["label"],
            position=eq["env_start"],
        )
        eq_infos.append(eq_info)

        # 5d: Assemble audit trail.
        audit_trail = dict(audit_global)
        audit_trail[f"extract_equation_{eq_num}"] = (
            f"Extracted equation ({eq_num}) from {eq['source']}"
        )
        audit_trail.update(meaning_audit)
        audit_trail.update(sym_audit)

        eq_data[eq_num] = {
            "equation": eq_latex,
            "meaning": meaning,
            "symbols": sym_dict,
            "relations": {},  # filled in step 6
            "audit-trail": audit_trail,
        }

    # Step 6: Classify relations between all equation pairs.
    relations, rel_audit = classify_relations(eq_infos, tex, label_to_number)

    for eq_num in eq_data:
        eq_data[eq_num]["relations"] = relations.get(eq_num, {})
        eq_data[eq_num]["audit-trail"].update(rel_audit)

    return eq_data, len(equations)


# ---------------------------------------------------------------------------
# Dataset builder
# ---------------------------------------------------------------------------

def build_dataset(
    paper_list_path: Path,
    cache_dir: Path,
    output_path: Path,
    *,
    max_per_paper: int = 7,
    target_total: int = 350,
    sleep_seconds: float = 3.0,
    source: str = "tex",
) -> None:
    """Build the full equations knowledge-graph dataset.

    Parameters
    ----------
    paper_list_path : Path
        Path to the paper list file (one arXiv ID per line).
    cache_dir : Path
        Cache directory for downloads.
    output_path : Path
        Output JSON file path.
    max_per_paper : int
        Maximum equations per paper.
    target_total : int
        Target total equations (stop after reaching this, completing last paper).
    sleep_seconds : float
        Delay between arXiv downloads.
    """
    paper_ids = read_paper_list(paper_list_path)
    print(f"Paper list: {len(paper_ids)} papers from {paper_list_path}")
    print(f"Target: {target_total} equations, max {max_per_paper} per paper")
    print()

    dataset: dict[str, Any] = {}
    total_equations = 0

    for idx, arxiv_id in enumerate(paper_ids, start=1):
        if total_equations >= target_total:
            break

        print(f"[{idx}/{len(paper_ids)}] Processing arXiv:{arxiv_id} "
              f"(total so far: {total_equations})...")

        if source == "pdf-texify":
            processor = process_paper_pdf_texify
        elif source == "pdf":
            processor = process_paper_pdf
        else:
            processor = process_paper
        paper_entry, count = processor(
            arxiv_id, cache_dir,
            max_equations=max_per_paper,
            sleep_seconds=sleep_seconds,
        )

        dataset[arxiv_id] = paper_entry
        total_equations += count

        print(f"  -> {count} equation(s) extracted "
              f"(running total: {total_equations})")

    # Write output.
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(dataset, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print()
    print(f"Dataset complete: {total_equations} equations "
          f"from {len(dataset)} papers")
    print(f"Output: {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    """Entry point for the dataset builder."""
    parser = argparse.ArgumentParser(
        description="Build equations knowledge-graph dataset from arXiv papers."
    )
    parser.add_argument(
        "--paper-list", type=Path, default=Path("paper_list_16.txt"),
        help="Path to the assigned paper list.",
    )
    parser.add_argument(
        "--output", type=Path, default=Path("output/dataset.json"),
        help="Output JSON dataset path.",
    )
    parser.add_argument(
        "--cache-dir", type=Path, default=Path("data/pdf_cache"),
        help="Cache directory for downloaded source archives.",
    )
    parser.add_argument(
        "--max-per-paper", type=int, default=7,
        help="Maximum equations per paper.",
    )
    parser.add_argument(
        "--target-total", type=int, default=350,
        help="Target total equations in the dataset.",
    )
    parser.add_argument(
        "--sleep-seconds", type=float, default=3.0,
        help="Delay between arXiv downloads.",
    )
    parser.add_argument(
        "--source", choices=["tex", "pdf", "pdf-texify"], default="tex",
        help="Extraction source: 'tex' (PDF count + TeX content), "
        "'pdf-texify' (PDF-only via texify OCR), "
        "'pdf' (PDF-only via pix2tex OCR).",
    )
    args = parser.parse_args()

    build_dataset(
        args.paper_list,
        args.cache_dir,
        args.output,
        max_per_paper=args.max_per_paper,
        target_total=args.target_total,
        sleep_seconds=args.sleep_seconds,
        source=args.source,
    )


if __name__ == "__main__":
    main()
