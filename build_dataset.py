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
    _strip_tex_comments,
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

    # Only parse equations in the main body:
    #   - After \begin{document} (skip preamble macros)
    #   - Before \appendix (skip supplementary/appendix equations like S1, A1)
    # The assignment specifies equations "noted by a number in brackets (e.g. '(1)')"
    # — only main-body numbered equations are relevant.
    doc_start = re.search(r"\\begin\{document\}", tex)
    if doc_start:
        tex = tex[doc_start.end():]

    appendix_match = re.search(r"\\appendix\b", tex)
    if appendix_match:
        tex = tex[:appendix_match.start()]

    # Equation counter — main body only (appendix already truncated).
    eq_count = 0

    def _next_number(pos: int) -> str:
        nonlocal eq_count
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
            rows = re.split(r"\\\\", content)
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

def process_paper(
    arxiv_id: str,
    cache_dir: Path,
    max_equations: int = 7,
    sleep_seconds: float = 3.0,
) -> tuple[dict[str, Any], int]:
    """Process a single paper and return the dataset entry.

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

    # Step 1: Download source.
    try:
        source_path = download_arxiv_source(
            arxiv_id, cache_dir, sleep_seconds=sleep_seconds
        )
        audit_global["download_source"] = (
            f"Downloaded arXiv source for {arxiv_id} to {source_path.name}"
        )
    except Exception as exc:
        print(f"  WARN: Could not download source for {arxiv_id}: {exc}")
        return {}, 0

    # Step 2: Extract .tex content.
    try:
        tex_raw = extract_tex_from_source(source_path)
        audit_global["extract_tex"] = (
            f"Extracted .tex file ({len(tex_raw)} chars)"
        )
    except Exception as exc:
        print(f"  WARN: Could not extract .tex for {arxiv_id}: {exc}")
        return {}, 0

    # Step 3: Parse equations with context.
    equations, label_to_number, tex = parse_equations_with_context(
        tex_raw, max_equations=max_equations
    )
    audit_global["parse_equations"] = (
        f"Found {len(equations)} enumerated equation(s)"
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

        paper_entry, count = process_paper(
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
    args = parser.parse_args()

    build_dataset(
        args.paper_list,
        args.cache_dir,
        args.output,
        max_per_paper=args.max_per_paper,
        target_total=args.target_total,
        sleep_seconds=args.sleep_seconds,
    )


if __name__ == "__main__":
    main()
