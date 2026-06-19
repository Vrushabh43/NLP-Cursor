"""Deterministic PDF equation extraction for arXiv papers.

This script targets PDF-only papers from the NLP project paper list. It downloads
one arXiv PDF, converts it locally with Docling, extracts enumerated display
equations, and writes the result in the JSON shape required by the assignment.
No external LLM or prompting API is used.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARXIV_PDF_URL = "https://arxiv.org/pdf/{arxiv_id}"
ARXIV_SOURCE_URL = "https://arxiv.org/e-print/{arxiv_id}"
DEFAULT_USER_AGENT = "NLP-Cursor-equation-extractor/0.1 (student project; respectful single-paper requests)"
EQUATION_NUMBER_RE = re.compile(
    r"(?<![\w.])\(\s*([A-Za-z]?\s*\d+(?:\.\d+)?\s*[a-z]?)\s*\)\s*$"
)
TAG_RE = re.compile(r"\\tag\{([^{}]+)\}")
SPACED_NUMBER_RE = re.compile(r"\(\s*([A-Za-z]?\s*\d+(?:\.\d+)?\s*[a-z]?)\s*\)")
LATEX_LABEL_RE = re.compile(
    r"(?:\\quad|,|\\\s+)\s*"
    r"(?:\\left\s*)?\(\s*([A-Za-z]?\s*\d+(?:\.\d+)?\s*[a-z]?)\s*"
    r"(?:\\right\s*)?\)"
)
MATH_SIGNAL_RE = re.compile(
    r"(\\[A-Za-z]+|[=+\-*/^_<>]|[∑∫√≤≥≠≈∞∂∇α-ωΑ-Ω]|"
    r"\b(?:psi|phi|rho|sigma|lambda|omega|theta|hat|ket|bra)\b)"
)

# ---------------------------------------------------------------------------
# Math symbol extraction dictionaries
# ---------------------------------------------------------------------------

UNICODE_MATH_SYMBOLS: set[str] = {
    # Operators
    "∑", "∫", "∏", "∂", "∇", "√",
    # Relations
    "≤", "≥", "≡", "≠", "≈", "≪", "≫", "∝", "∼",
    # Arrows
    "→", "←", "↔", "⇒", "⇐", "⇔",
    # Greek lowercase
    "α", "β", "γ", "δ", "ε", "ζ", "η", "θ",
    "ι", "κ", "λ", "μ", "ν", "ξ", "π", "ρ",
    "σ", "τ", "υ", "φ", "χ", "ψ", "ω",
    # Greek uppercase
    "Γ", "Δ", "Θ", "Λ", "Ξ", "Π", "Σ", "Φ", "Ψ", "Ω",
    # Special
    "∞", "†", "‡", "⟨", "⟩", "ℏ", "ℓ",
}

LATEX_CMD_TO_SYMBOL: dict[str, str] = {
    # Operators
    r"\sum": "∑", r"\int": "∫", r"\prod": "∏",
    r"\partial": "∂", r"\nabla": "∇", r"\sqrt": "√",
    r"\oint": "∮",
    # Relations
    r"\leq": "≤", r"\le": "≤", r"\geq": "≥", r"\ge": "≥",
    r"\equiv": "≡", r"\neq": "≠", r"\approx": "≈",
    r"\ll": "≪", r"\gg": "≫", r"\propto": "∝", r"\sim": "∼",
    # Arrows
    r"\to": "→", r"\rightarrow": "→", r"\leftarrow": "←",
    r"\leftrightarrow": "↔", r"\Rightarrow": "⇒",
    r"\Leftarrow": "⇐", r"\Leftrightarrow": "⇔",
    # Greek lowercase
    r"\alpha": "α", r"\beta": "β", r"\gamma": "γ",
    r"\delta": "δ", r"\epsilon": "ε", r"\varepsilon": "ε",
    r"\zeta": "ζ", r"\eta": "η", r"\theta": "θ",
    r"\vartheta": "θ", r"\iota": "ι", r"\kappa": "κ",
    r"\lambda": "λ", r"\mu": "μ", r"\nu": "ν",
    r"\xi": "ξ", r"\pi": "π", r"\rho": "ρ",
    r"\sigma": "σ", r"\tau": "τ", r"\upsilon": "υ",
    r"\phi": "φ", r"\varphi": "φ", r"\chi": "χ",
    r"\psi": "ψ", r"\omega": "ω",
    # Greek uppercase
    r"\Gamma": "Γ", r"\Delta": "Δ", r"\Theta": "Θ",
    r"\Lambda": "Λ", r"\Xi": "Ξ", r"\Pi": "Π",
    r"\Sigma": "Σ", r"\Phi": "Φ", r"\Psi": "Ψ", r"\Omega": "Ω",
    # Special
    r"\infty": "∞", r"\dagger": "†", r"\ddagger": "‡",
    r"\langle": "⟨", r"\rangle": "⟩", r"\hbar": "ℏ", r"\ell": "ℓ",
    r"\forall": "∀", r"\exists": "∃", r"\in": "∈",
    r"\subset": "⊂", r"\supset": "⊃", r"\cup": "∪", r"\cap": "∩",
    r"\pm": "±", r"\mp": "∓", r"\times": "×", r"\cdot": "·",
    r"\otimes": "⊗", r"\oplus": "⊕",
}

# Pre-compiled pattern to find LaTeX commands in a string.
_LATEX_CMD_RE = re.compile(r"\\[A-Za-z]+")


def extract_math_symbols(latex: str) -> list[str]:
    """Extract unique math symbols from a LaTeX equation string.

    Uses a triple-pass approach:
      1. Direct Unicode character scan
      2. LaTeX command → symbol mapping
      3. pylatexenc fallback for remaining commands
    """
    symbols: set[str] = set()

    # Pass 1: Unicode characters already present in the string.
    for char in latex:
        if char in UNICODE_MATH_SYMBOLS:
            symbols.add(char)

    # Pass 2: Map known LaTeX commands to Unicode symbols.
    for match in _LATEX_CMD_RE.finditer(latex):
        cmd = match.group()
        if cmd in LATEX_CMD_TO_SYMBOL:
            symbols.add(LATEX_CMD_TO_SYMBOL[cmd])

    # Pass 3: pylatexenc conversion for commands not in our dictionary.
    try:
        from pylatexenc.latex2text import LatexNodes2Text
        converted = LatexNodes2Text().latex_to_text(latex)
        for char in converted:
            if char in UNICODE_MATH_SYMBOLS:
                symbols.add(char)
    except Exception:
        pass  # pylatexenc unavailable or parse error — passes 1+2 suffice

    return sorted(symbols)


@dataclass(frozen=True)
class EquationCandidate:
    """A single enumerated equation found in the converted document."""

    number: str
    latex: str
    source: str
    line_start: int
    line_end: int
    context: str


def read_paper_list(path: Path) -> list[str]:
    """Read arXiv IDs from a Moodle paper list.

    Parameters
    ----------
    path:
        Text file containing entries such as ``arXiv:2409.18913``.

    Returns
    -------
    list[str]
        Normalized arXiv IDs in the original order.
    """

    paper_ids: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        paper_ids.append(line.removeprefix("arXiv:").strip())
    return paper_ids


def select_arxiv_id(paper_ids: list[str], paper_number: int) -> str:
    """Return the 1-based paper-list entry requested on the command line."""

    if paper_number < 1 or paper_number > len(paper_ids):
        raise ValueError(f"paper number must be between 1 and {len(paper_ids)}")
    return paper_ids[paper_number - 1]


def download_arxiv_pdf(
    arxiv_id: str,
    cache_dir: Path,
    *,
    sleep_seconds: float,
    force: bool,
) -> Path:
    """Download one arXiv PDF with a respectful user agent and cache it."""

    cache_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = cache_dir / f"{arxiv_id.replace('/', '_')}.pdf"
    if pdf_path.exists() and not force:
        return pdf_path

    if sleep_seconds > 0:
        time.sleep(sleep_seconds)

    request = urllib.request.Request(
        ARXIV_PDF_URL.format(arxiv_id=arxiv_id),
        headers={"User-Agent": DEFAULT_USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            content_type = response.headers.get("Content-Type", "")
            payload = response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"failed to download PDF for arXiv:{arxiv_id}: {exc}") from exc

    if b"%PDF" not in payload[:1024]:
        raise RuntimeError(
            f"download for arXiv:{arxiv_id} did not look like a PDF "
            f"(content-type={content_type!r})"
        )
    pdf_path.write_bytes(payload)
    return pdf_path


def download_arxiv_source(
    arxiv_id: str,
    cache_dir: Path,
    *,
    sleep_seconds: float,
) -> Path:
    """Download the arXiv LaTeX source archive for a paper."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    source_path = cache_dir / f"{arxiv_id.replace('/', '_')}_source.tar.gz"
    if source_path.exists():
        return source_path

    if sleep_seconds > 0:
        time.sleep(sleep_seconds)

    request = urllib.request.Request(
        ARXIV_SOURCE_URL.format(arxiv_id=arxiv_id),
        headers={"User-Agent": DEFAULT_USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            payload = response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"failed to download source for arXiv:{arxiv_id}: {exc}") from exc

    source_path.write_bytes(payload)
    return source_path


def extract_tex_from_source(source_path: Path) -> str:
    """Extract the main .tex content from an arXiv source archive.

    Handles tar.gz archives, plain gzip, and bare .tex files.
    """
    import gzip
    import io
    import tarfile

    raw = source_path.read_bytes()

    # Try tar.gz first.
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tar:
            tex_files = [m for m in tar.getmembers() if m.name.endswith(".tex")]
            if not tex_files:
                raise RuntimeError("No .tex files found in archive")
            main_tex = max(tex_files, key=lambda m: m.size)
            extracted = tar.extractfile(main_tex)
            if extracted is None:
                raise RuntimeError(f"Could not read {main_tex.name} from archive")
            return extracted.read().decode("utf-8", errors="replace")
    except tarfile.TarError:
        pass

    # Try plain gzip (single .tex file).
    try:
        return gzip.decompress(raw).decode("utf-8", errors="replace")
    except gzip.BadGzipFile:
        pass

    # Maybe it's a bare .tex file.
    return raw.decode("utf-8", errors="replace")


def _strip_tex_comments(tex: str) -> str:
    """Remove LaTeX line comments while preserving escaped percent signs."""
    return re.sub(r"(?<!\\)%.*$", "", tex, flags=re.MULTILINE)


# Matches numbered equation environments (not starred variants like equation*).
_NUMBERED_ENV_RE = re.compile(
    r"\\begin\{(equation|multline|align|gather|eqnarray|flalign|alignat)\}"
    r"(.*?)"
    r"\\end\{\1\}",
    re.DOTALL,
)

# Environments where each \\ row gets its own equation number.
_MULTI_ROW_ENVS = {"align", "gather", "eqnarray", "flalign", "alignat"}

# Single-number environments (one number for the whole block).
_SINGLE_NUM_ENVS = {"equation", "multline"}


def _clean_latex(raw: str) -> str:
    """Remove \\label{...} and normalize whitespace in a LaTeX string."""
    cleaned = re.sub(r"\\label\{[^}]*\}", "", raw).strip()
    return re.sub(r"\s+", " ", cleaned).strip()


def parse_equations_from_tex(tex_content: str) -> list[EquationCandidate]:
    """Parse all numbered equation environments from LaTeX source.

    Handles both main-body and appendix numbering (A1, B1, ...).
    Multi-row environments (align, gather, eqnarray) are split into
    individual rows — each row becomes a separate numbered equation
    unless it contains ``\\nonumber`` or ``\\notag``.
    """
    tex = _strip_tex_comments(tex_content)

    # Locate structural markers.
    appendix_match = re.search(r"\\appendix\b", tex)
    appendix_pos = appendix_match.start() if appendix_match else len(tex) + 1

    # Find section boundaries after \appendix.
    appendix_sections: list[int] = []
    if appendix_match:
        for m in re.finditer(r"\\section\b", tex):
            if m.start() > appendix_pos:
                appendix_sections.append(m.start())

    # --- Equation counter state ---
    main_eq_count = 0
    current_appendix_section = -1
    section_eq_count = 0
    candidates: list[EquationCandidate] = []

    def _next_number(pos: int) -> str:
        """Advance the equation counter and return the next number string."""
        nonlocal main_eq_count, current_appendix_section, section_eq_count

        if pos < appendix_pos:
            main_eq_count += 1
            return str(main_eq_count)

        new_section = 0
        for i, sec_pos in enumerate(appendix_sections):
            if pos > sec_pos:
                new_section = i
        if new_section != current_appendix_section:
            current_appendix_section = new_section
            section_eq_count = 0
        section_eq_count += 1
        section_letter = chr(ord("A") + current_appendix_section)
        return f"{section_letter}{section_eq_count}"

    for match in _NUMBERED_ENV_RE.finditer(tex):
        env_name = match.group(1)
        content = match.group(2)
        pos = match.start()
        line_start = tex[:pos].count("\n") + 1
        line_end = tex[: match.end()].count("\n") + 1

        if env_name in _SINGLE_NUM_ENVS:
            # One equation number for the entire block.
            latex = _clean_latex(content)
            if latex:
                candidates.append(
                    EquationCandidate(
                        number=_next_number(pos),
                        latex=latex,
                        source="arxiv_tex_source",
                        line_start=line_start,
                        line_end=line_end,
                        context="",
                    )
                )
        else:
            # Multi-row: split by \\ and emit one equation per numbered row.
            rows = re.split(r"\\\\", content)
            for row in rows:
                row_stripped = row.strip()
                if not row_stripped:
                    continue
                # Skip rows explicitly marked as unnumbered.
                if r"\nonumber" in row_stripped or r"\notag" in row_stripped:
                    continue
                latex = _clean_latex(row_stripped)
                if latex:
                    candidates.append(
                        EquationCandidate(
                            number=_next_number(pos),
                            latex=latex,
                            source="arxiv_tex_source",
                            line_start=line_start,
                            line_end=line_end,
                            context="",
                        )
                    )

    return candidates


def make_docling_converter(*, enable_ocr: bool) -> Any:
    """Create a Docling PDF converter with formula enrichment when available."""

    try:
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import DocumentConverter, PdfFormatOption
    except ImportError as exc:
        raise RuntimeError(
            "Docling is required for the PDF pipeline. Install dependencies with "
            "`python -m pip install -r requirements.txt`."
        ) from exc

    pipeline_options = PdfPipelineOptions()
    # arXiv papers are normally born-digital PDFs with a text layer. OCR adds
    # substantial CPU/RAM cost and can fail on modest machines, so keep it off
    # unless the caller explicitly requests it for a scanned PDF.
    if hasattr(pipeline_options, "do_ocr"):
        pipeline_options.do_ocr = enable_ocr
    if hasattr(pipeline_options, "ocr_batch_size"):
        pipeline_options.ocr_batch_size = 1
    for image_flag in ("generate_page_images", "generate_picture_images", "generate_table_images"):
        if hasattr(pipeline_options, image_flag):
            setattr(pipeline_options, image_flag, False)
    if hasattr(pipeline_options, "do_formula_enrichment"):
        pipeline_options.do_formula_enrichment = True

    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )


def convert_pdf_with_docling(pdf_path: Path, *, enable_ocr: bool) -> tuple[str, dict[str, Any]]:
    """Convert the PDF to Markdown and keep compact conversion metadata."""

    converter = make_docling_converter(enable_ocr=enable_ocr)
    result = converter.convert(str(pdf_path))
    document = result.document
    markdown = document.export_to_markdown()
    metadata = {
        "status": str(getattr(result, "status", "unknown")),
        "converter": "docling",
        "ocr_enabled": enable_ocr,
        "markdown_chars": len(markdown),
    }
    return markdown, metadata


def normalize_latex(text: str) -> str:
    """Clean Docling Markdown math into a compact LaTeX-like equation string."""

    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:math|latex)?", "", cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    cleaned = cleaned.removeprefix("$$").removesuffix("$$").strip()
    cleaned = cleaned.removeprefix(r"\[").removesuffix(r"\]").strip()
    cleaned = TAG_RE.sub("", cleaned).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def extract_number_from_text(text: str, *, allow_embedded_label: bool = False) -> str | None:
    """Extract an equation number from ``\\tag{...}`` or a trailing ``(...)``."""

    candidate_text = text.strip()
    candidate_text = candidate_text.removesuffix("$$").removesuffix(r"\]").removesuffix("```").strip()
    tag_match = TAG_RE.search(candidate_text)
    if tag_match:
        return re.sub(r"\s+", "", tag_match.group(1).strip())
    trailing_match = EQUATION_NUMBER_RE.search(candidate_text)
    if trailing_match:
        return re.sub(r"\s+", "", trailing_match.group(1).strip())

    if not allow_embedded_label:
        return None

    for match in reversed(list(LATEX_LABEL_RE.finditer(candidate_text))):
        preceding = candidate_text[max(0, match.start() - 8) : match.start()]
        if "^" not in preceding:
            return re.sub(r"\s+", "", match.group(1).strip())

    # Docling sometimes places the visible equation label inside a wrapper such
    # as ``} \end{array}``. Treat only late labels as enumeration labels so
    # constructs like ``P^{(1)}`` near the start of a formula are ignored.
    for match in reversed(list(SPACED_NUMBER_RE.finditer(candidate_text))):
        preceding = candidate_text[max(0, match.start() - 8) : match.start()]
        is_superscript = "^" in preceding
        is_late_label = match.start() > int(len(candidate_text) * 0.65)
        if is_late_label and not is_superscript:
            return re.sub(r"\s+", "", match.group(1).strip())
    return None


def strip_equation_number(text: str, number: str | None = None) -> str:
    """Remove a visible equation number marker from an equation candidate."""

    suffix = ""
    candidate_text = text.strip()
    for delimiter in ("$$", r"\]", "```"):
        if candidate_text.endswith(delimiter):
            candidate_text = candidate_text[: -len(delimiter)].strip()
            suffix = delimiter
            break
    candidate_text = EQUATION_NUMBER_RE.sub("", candidate_text).strip()
    if number is not None:
        spaced_number = r"\s*".join(re.escape(character) for character in number)
        embedded_label_re = re.compile(
            rf"(?:\\quad|,|\\\s+)?\s*(?:\\left\s*)?\(\s*{spaced_number}\s*"
            rf"(?:\\right\s*)?\)\s*(?:\\quad)?\s*"
            rf"(?=(?:\s*\}})?\s*\\end\{{array\}}|(?:\s*\\\s*){{4,}}|\s*$)"
        )
        candidate_text = embedded_label_re.sub("", candidate_text).strip()
        candidate_text = re.sub(r"(?:\\\s*){4,}$", "", candidate_text).strip()
    return (candidate_text + suffix).strip()


def window_context(lines: list[str], start: int, end: int, radius: int = 2) -> str:
    """Return a short neighboring text window for audit and later QA."""

    left = max(0, start - radius)
    right = min(len(lines), end + radius + 1)
    context_lines = [line.strip() for line in lines[left:right] if line.strip()]
    return " ".join(context_lines)[:500]


def extract_from_math_blocks(markdown: str) -> list[EquationCandidate]:
    """Extract numbered equations from display math blocks in Docling Markdown."""

    lines = markdown.splitlines()
    candidates: list[EquationCandidate] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        starts_block = line.startswith("$$") or line.startswith(r"\[") or line.startswith("```math")
        if not starts_block:
            index += 1
            continue

        start = index
        block_lines = [lines[index]]
        if line.endswith("$$") or line.endswith(r"\]"):
            end = index
            raw_block = "\n".join(block_lines)
            number = extract_number_from_text(raw_block, allow_embedded_label=True)
            if number is not None:
                latex = strip_equation_number(normalize_latex(raw_block), number)
                if latex:
                    candidates.append(
                        EquationCandidate(
                            number=number,
                            latex=latex,
                            source="docling_markdown_math_block",
                            line_start=start + 1,
                            line_end=end + 1,
                            context=window_context(lines, start, end),
                        )
                    )
            index += 1
            continue

        index += 1
        while index < len(lines):
            block_lines.append(lines[index])
            stripped = lines[index].strip()
            if stripped.endswith("$$") or stripped.endswith(r"\]") or stripped == "```":
                break
            index += 1

        end = index
        raw_block = "\n".join(block_lines)
        number = extract_number_from_text(raw_block, allow_embedded_label=True)
        if number is None:
            for neighbor in (end + 1, start - 1):
                if 0 <= neighbor < len(lines):
                    number = extract_number_from_text(lines[neighbor])
                    if number is not None:
                        break

        if number is not None:
            latex = strip_equation_number(normalize_latex(raw_block), number)
            if latex:
                candidates.append(
                    EquationCandidate(
                        number=number,
                        latex=latex,
                        source="docling_markdown_math_block",
                        line_start=start + 1,
                        line_end=end + 1,
                        context=window_context(lines, start, end),
                    )
                )
        index += 1
    return candidates


def extract_from_numbered_lines(markdown: str) -> list[EquationCandidate]:
    """Fallback extraction for Docling text lines ending in equation numbers."""

    lines = markdown.splitlines()
    candidates: list[EquationCandidate] = []
    for index, line in enumerate(lines):
        stripped = line.strip()
        if len(stripped) > 500:
            continue
        number = extract_number_from_text(stripped)
        if number is None:
            continue

        equation_text = strip_equation_number(stripped, number)
        start = index
        if not MATH_SIGNAL_RE.search(equation_text) and index > 0:
            previous = lines[index - 1].strip()
            if MATH_SIGNAL_RE.search(previous):
                equation_text = previous
                start = index - 1

        if MATH_SIGNAL_RE.search(equation_text):
            candidates.append(
                EquationCandidate(
                    number=number,
                    latex=normalize_latex(equation_text),
                    source="docling_markdown_numbered_line",
                    line_start=start + 1,
                    line_end=index + 1,
                    context=window_context(lines, start, index),
                )
            )
    return candidates


def deduplicate_candidates(candidates: list[EquationCandidate], limit: int) -> list[EquationCandidate]:
    """Keep first occurrence of each equation number while preserving order."""

    selected: list[EquationCandidate] = []
    seen: set[str] = set()
    for candidate in candidates:
        if candidate.number in seen:
            continue
        seen.add(candidate.number)
        selected.append(candidate)
        if len(selected) >= limit:
            break
    return selected


def extract_equations(markdown: str, max_equations: int) -> list[EquationCandidate]:
    """Run the deterministic equation candidate extractors."""

    candidates = extract_from_math_blocks(markdown)
    candidates.extend(extract_from_numbered_lines(markdown))
    return deduplicate_candidates(candidates, max_equations)


def build_relations(equation_numbers: list[str], current_number: str) -> dict[str, dict[str, str]]:
    """Create graph-ready placeholder relations for all other paper equations."""

    return {
        other_number: {"grade": "none", "description": ""}
        for other_number in equation_numbers
        if other_number != current_number
    }


def build_dataset_entry(
    arxiv_id: str,
    equations: list[EquationCandidate],
    conversion_metadata: dict[str, Any],
) -> dict[str, Any]:
    """Build the professor-required JSON shape for one paper."""

    equation_numbers = [candidate.number for candidate in equations]
    paper_entry: dict[str, Any] = {}
    for rank, candidate in enumerate(equations, start=1):
        paper_entry[candidate.number] = {
            "equation": candidate.latex,
            "meaning": "",
            "symbols": {},
            "relations": build_relations(equation_numbers, candidate.number),
            "audit-trail": {
                "download_pdf": f"Used arXiv PDF for arXiv:{arxiv_id}",
                "convert_with_docling": (
                    f"Converted PDF locally with Docling; status={conversion_metadata['status']}"
                ),
                "extract_enumerated_equations": (
                    f"Selected equation {rank}/{len(equations)} from {candidate.source}"
                ),
                "equation_location": (
                    f"Docling Markdown lines {candidate.line_start}-{candidate.line_end}"
                ),
                "context_window": candidate.context,
            },
        }
    return {arxiv_id: paper_entry}


def format_simple_json(equations: list[EquationCandidate]) -> list[dict[str, Any]]:
    """Format equations into the simple ``{equation, number, mathsSymbol}`` schema."""
    return [
        {
            "equation": eq.latex,
            "number": eq.number,
            "mathsSymbol": extract_math_symbols(eq.latex),
        }
        for eq in equations
    ]


def write_json(path: Path, payload: dict[str, Any], *, merge: bool) -> None:
    """Write or merge a paper-level dataset JSON file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    if merge and path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        existing.update(payload)
        payload = existing
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Extract enumerated equations from one arXiv PDF using Docling."
    )
    parser.add_argument(
        "--pdf-path",
        type=Path,
        default=None,
        help="Path to a local PDF file. When provided, skips arXiv download.",
    )
    parser.add_argument(
        "--paper-list",
        type=Path,
        default=Path("paper_list_16.txt"),
        help="Path to the assigned Moodle paper list.",
    )
    parser.add_argument(
        "--paper-number",
        type=int,
        default=None,
        help="1-based paper number from the paper list, e.g. 9 for the ninth entry.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/pdf/equations_pdf.json"),
        help="Professor-shaped output JSON path.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("data/pdf_cache"),
        help="Directory for cached downloaded PDFs.",
    )
    parser.add_argument(
        "--max-equations",
        type=int,
        default=7,
        help="Maximum relevant enumerated equations to keep for this paper.",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=3.0,
        help="Delay before downloading a missing PDF from arXiv.",
    )
    parser.add_argument(
        "--force-download",
        action="store_true",
        help="Re-download the PDF even when it already exists in the cache.",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge this paper into an existing output JSON instead of replacing it.",
    )
    parser.add_argument(
        "--save-docling-markdown",
        type=Path,
        default=None,
        help="Optional path for saving Docling Markdown for manual audit.",
    )
    parser.add_argument(
        "--enable-ocr",
        action="store_true",
        help="Enable OCR for scanned PDFs. Leave off for normal arXiv text-layer PDFs.",
    )
    parser.add_argument(
        "--output-format",
        choices=["professor", "simple"],
        default="simple",
        help="Output JSON format: 'simple' for {equation,number,mathsSymbol} or 'professor' for full schema.",
    )
    parser.add_argument(
        "--source",
        choices=["tex", "docling"],
        default="tex",
        help="Extraction strategy: 'tex' downloads arXiv LaTeX source (fast, perfect); "
        "'docling' converts PDF with Docling (slow, needs formula enrichment).",
    )
    return parser.parse_args()


def main() -> None:
    """Run the single-paper PDF equation extraction pipeline."""

    args = parse_args()

    # Resolve arXiv ID and/or PDF path.
    arxiv_id: str | None = None
    if args.pdf_path is not None:
        pdf_path = args.pdf_path
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")
        # Try to detect arXiv ID from filename (e.g., "2410.07429v2.pdf").
        stem = pdf_path.stem
        if re.match(r"\d{4}\.\d{4,5}(v\d+)?$", stem):
            arxiv_id = re.sub(r"v\d+$", "", stem)
    elif args.paper_number is not None:
        paper_ids = read_paper_list(args.paper_list)
        arxiv_id = select_arxiv_id(paper_ids, args.paper_number)
    else:
        raise SystemExit("Either --pdf-path or --paper-number is required.")

    identifier = arxiv_id or (args.pdf_path.stem if args.pdf_path else "unknown")

    # --- Source strategy: tex (arXiv LaTeX source) or docling ---
    if args.source == "tex":
        if arxiv_id is None:
            raise SystemExit(
                "The 'tex' source strategy requires an arXiv ID. "
                "Either use --paper-number or pass an arXiv-named PDF with --pdf-path."
            )
        source_path = download_arxiv_source(
            arxiv_id, args.cache_dir, sleep_seconds=args.sleep_seconds
        )
        tex_content = extract_tex_from_source(source_path)
        equations = parse_equations_from_tex(tex_content)
        if args.max_equations < len(equations):
            equations = equations[: args.max_equations]
    else:
        # Docling path (original behavior).
        if args.pdf_path is not None:
            pdf_path = args.pdf_path
        else:
            pdf_path = download_arxiv_pdf(
                arxiv_id,
                args.cache_dir,
                sleep_seconds=args.sleep_seconds,
                force=args.force_download,
            )
        markdown, conversion_metadata = convert_pdf_with_docling(
            pdf_path, enable_ocr=args.enable_ocr
        )
        if args.save_docling_markdown is not None:
            args.save_docling_markdown.parent.mkdir(parents=True, exist_ok=True)
            args.save_docling_markdown.write_text(markdown, encoding="utf-8")
        equations = extract_equations(markdown, args.max_equations)

    # --- Output ---
    if args.output_format == "simple":
        payload = format_simple_json(equations)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    else:
        if args.source != "docling":
            conversion_metadata = {"status": "success", "converter": "arxiv_tex_source"}
        dataset_entry = build_dataset_entry(identifier, equations, conversion_metadata)
        write_json(args.output, dataset_entry, merge=args.merge)

    print(
        f"{identifier}: extracted {len(equations)} enumerated equation(s) "
        f"to {args.output}"
    )


if __name__ == "__main__":
    main()
