"""Deterministic PDF equation extraction for arXiv papers.

This script targets PDF-only papers from the NLP project paper list. It downloads
one arXiv PDF, converts it locally with Docling, extracts enumerated display
equations, and writes the result in the JSON shape required by the assignment.
No external LLM or prompting API is used.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import time
import tempfile
import unicodedata
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARXIV_PDF_URL = "https://arxiv.org/pdf/{arxiv_id}"
DEFAULT_USER_AGENT = "NLP-Cursor-equation-extractor/0.1 (student project; respectful single-paper requests)"
DEFAULT_MODEL_CACHE_DIR = Path(".cache/model_cache")
EQUATION_NUMBER_RE = re.compile(
    r"(?<![\w.])\(\s*([A-Za-z]?\s*\d+(?:\.\d+)?\s*[a-z]?)\s*\)\s*$"
)
TAG_RE = re.compile(r"\\tag\{([^{}]+)\}")
SPACED_NUMBER_RE = re.compile(r"\(\s*([A-Za-z]?\s*\d+(?:\.\d+)?\s*[a-z]?)\s*\)")
PROSE_EQUATION_REFERENCE_RE = re.compile(r"\b[Ee]q\.?\s*\(?\s*([1-9]\d*(?:\.\d+)?[a-z]?)\s*\)?")
PAREN_DECIMAL_EQUATION_REFERENCE_RE = re.compile(r"\(\s*([1-9]\d?\.\d{1,3})\s*\)")
LATEX_LABEL_RE = re.compile(
    r"(?:\\quad|,|\\\s+)\s*"
    r"(?:\\left\s*)?\(\s*([A-Za-z]?\s*\d+(?:\.\d+)?\s*[a-z]?)\s*"
    r"(?:\\right\s*)?\)"
)
MATH_SIGNAL_RE = re.compile(
    r"(\\[A-Za-z]+|[=+\-*/^_<>]|[∑∫√≤≥≠≈∞∂∇α-ωΑ-Ω]|"
    r"\b(?:psi|phi|rho|sigma|lambda|omega|theta|hat|ket|bra)\b)"
)
STRONG_EQUATION_SIGNAL_RE = re.compile(
    r"(=|:=|\\(?:frac|sum|int|prod|lim|begin\{(?:array|matrix|pmatrix|bmatrix)|"
    r"le|ge|neq|approx|in|to|rightarrow|leftarrow)\b|[≤≥≠≈∑∫∏→←]|"
    r"\b(?:lim|arg\s*min|arg\s*max)\b)"
)
PROSE_STOP_RE = re.compile(
    r"\b(?:according|ancilla|figure|implementation|resulting|controlled|respectively|"
    r"where|describes|represents|shown|given|using|between|register)\b",
    re.IGNORECASE,
)
PDF_LABEL_LINE_RE = re.compile(r"^\s*\(\s*([1-9]\d*(?:\.\d+)?[a-z]?)\s*\)\s*$")
PDF_TRAILING_LABEL_RE = re.compile(r"\(\s*([1-9]\d*(?:\.\d+)?[a-z]?)\s*\)\s*$")
LATEX_COMMAND_SPACING_RE = re.compile(r"\\([A-Za-z]+)\s+(?=\{)")
GREEK_TO_LATEX = {
    "α": r"\alpha",
    "β": r"\beta",
    "γ": r"\gamma",
    "δ": r"\delta",
    "ε": r"\varepsilon",
    "κ": r"\kappa",
    "λ": r"\lambda",
    "π": r"\pi",
    "ω": r"\omega",
    "ℏ": r"\hbar",
    "∆": r"\Delta",
    "∗": r"^*",
    "⟨": r"\langle ",
    "⟩": r" \rangle",
    "−": "-",
    "·": r"\cdot",
    "√": r"\sqrt",
    "Σ": r"\sum",
    "∑": r"\sum",
}


@dataclass(frozen=True)
class EquationCandidate:
    """A single enumerated equation found in the converted document."""

    number: str
    latex: str
    raw_latex: str
    source: str
    confidence: str
    warnings: list[str]
    line_start: int
    line_end: int
    context: str
    source_location: str


@dataclass(frozen=True)
class PdfTextLine:
    """One text-layer line extracted from a PDF page."""

    text: str
    page: int
    page_line: int
    global_line: int


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


def is_writable_directory(path: Path) -> bool:
    """Return whether a directory can be created and written by this process."""

    try:
        path.mkdir(parents=True, exist_ok=True)
        probe = path / ".write_test"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink(missing_ok=True)
    except OSError:
        return False
    return True


def configure_writable_model_cache(cache_dir: Path = DEFAULT_MODEL_CACHE_DIR) -> None:
    """Force Docling/Hugging Face model downloads into a writable local cache."""

    cache_root = cache_dir.resolve()
    huggingface_home = cache_root / "huggingface"
    huggingface_hub = huggingface_home / "hub"
    transformers_cache = cache_root / "transformers"
    xdg_cache = cache_root / "xdg"

    def set_if_unwritable(env_name: str, path: Path) -> None:
        current = os.environ.get(env_name)
        if current and is_writable_directory(Path(current)):
            return
        path.mkdir(parents=True, exist_ok=True)
        os.environ[env_name] = str(path)

    set_if_unwritable("HF_HOME", huggingface_home)
    set_if_unwritable("HF_HUB_CACHE", huggingface_hub)
    set_if_unwritable("HUGGINGFACE_HUB_CACHE", huggingface_hub)
    set_if_unwritable("TRANSFORMERS_CACHE", transformers_cache)
    set_if_unwritable("XDG_CACHE_HOME", xdg_cache)
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")


def pdf_page_count(pdf_path: Path) -> int | None:
    """Return PDF page count when PyMuPDF is available."""

    try:
        import fitz
    except ImportError:
        return None

    try:
        with fitz.open(pdf_path) as document:
            return document.page_count
    except Exception:
        return None


def configure_docling_device(
    pdf_path: Path,
    *,
    policy: str,
    gpu_max_pages: int,
    gpu_max_mb: float,
) -> dict[str, Any]:
    """Choose CPU/GPU before Docling imports heavy model dependencies."""

    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    pages = pdf_page_count(pdf_path)
    reason = "requested_gpu"
    selected_device = "gpu"

    if policy == "cpu":
        selected_device = "cpu"
        reason = "requested_cpu"
    elif policy == "auto":
        too_many_pages = pages is not None and pages > gpu_max_pages
        too_large = size_mb > gpu_max_mb
        if too_many_pages or too_large:
            selected_device = "cpu"
            reason_parts = []
            if too_many_pages:
                reason_parts.append(f"pages>{gpu_max_pages}")
            if too_large:
                reason_parts.append(f"size_mb>{gpu_max_mb:g}")
            reason = "auto_cpu_" + "_".join(reason_parts)
        else:
            reason = "auto_gpu_small_pdf"
    elif policy != "gpu":
        raise ValueError(f"unsupported device policy: {policy}")

    if selected_device == "cpu":
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
    elif os.environ.get("CUDA_VISIBLE_DEVICES") == "":
        reason = f"{reason}_but_cuda_hidden_by_environment"

    print(
        "Docling device policy: "
        f"policy={policy}, selected={selected_device}, pages={pages}, "
        f"size_mb={size_mb:.2f}, reason={reason}"
    )
    return {
        "device_policy": policy,
        "selected_device": selected_device,
        "device_reason": reason,
        "pdf_pages": pages,
        "pdf_size_mb": round(size_mb, 2),
        "gpu_max_pages": gpu_max_pages,
        "gpu_max_mb": gpu_max_mb,
    }


def make_docling_converter(*, enable_ocr: bool) -> Any:
    """Create a Docling PDF converter with formula enrichment when available."""

    configure_writable_model_cache()
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
        trailing_label_and_layout_re = re.compile(
            rf"(?:\\qquad|\\quad|,\s*|\s{{2,}})\s*(?:\\left\s*)?\(\s*{spaced_number}\s*"
            rf"(?:\\right\s*)?\).*$"
        )
        candidate_text = trailing_label_and_layout_re.sub("", candidate_text).strip()
        embedded_label_re = re.compile(
            rf"(?:\\quad|,|\\\s+)?\s*(?:\\left\s*)?\(\s*{spaced_number}\s*"
            rf"(?:\\right\s*)?\)\s*(?:\\quad)?\s*"
            rf"(?=(?:\s*\}})?\s*\\end\{{array\}}|(?:\s*\\\s*){{4,}}|\s*$)"
        )
        candidate_text = embedded_label_re.sub("", candidate_text).strip()
        candidate_text = re.sub(r"(?:\\\s*){4,}$", "", candidate_text).strip()
    return (candidate_text + suffix).strip()


def normalize_equation_for_output(text: str) -> str:
    """Apply conservative LaTeX cleanup without changing equation meaning."""

    normalized = unicodedata.normalize("NFKC", text).strip()
    normalized = strip_equation_number(normalized)
    normalized = re.sub(
        r"^\\begin\{array\}\s*\{[^{}]*\}\s*(.*?)\s*\\end\{array\}$",
        r"\1",
        normalized,
    ).strip()
    normalized = re.sub(r"^\{\s*(?:[A-Za-z]\s+){1,}[A-Za-z]\s*\}\s*&\s*", "", normalized).strip()
    normalized = re.sub(r"\\mathbf\s*\{\s*i\s*\}", r"\\mathrm{i}", normalized)
    normalized = re.sub(r"\\mathbf\s+i\b", r"\\mathrm{i}", normalized)
    normalized = re.sub(r"(?:\\quad|\\qquad|\\,|\\;|\\:|\s)+$", "", normalized).strip()
    normalized = re.sub(r"(?:\\\s*){2,}$", "", normalized).strip()
    normalized = re.sub(r"(?<!\\)[,.]\s*$", "", normalized).strip()
    normalized = re.sub(r"\\frac\s*\{\s*([^{}]+?)\s*\}\s*\{\s*([^{}]+?)\s*\}", r"\\frac{\1}{\2}", normalized)
    normalized = re.sub(r"\{\s*([^{}]+?)\s*\}", lambda match: "{" + match.group(1).strip() + "}", normalized)
    normalized = re.sub(r"_\s*\{\s*([^{}]+?)\s*\}", r"_{\1}", normalized)
    normalized = re.sub(r"\^\s*\{\s*([^{}]+?)\s*\}", r"^{\1}", normalized)
    normalized = re.sub(r"\s+([_^])", r"\1", normalized)
    normalized = re.sub(r"([_^])\s+", r"\1", normalized)
    normalized = LATEX_COMMAND_SPACING_RE.sub(r"\\\1", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    normalized = re.sub(r"(?:\\quad|\\qquad|\\,|\\;|\\:|\\\s*)+$", "", normalized).strip()
    return normalized


def confidence_for_source(source: str) -> str:
    """Assign confidence based on the extraction source."""

    if source in {"docling_markdown_math_block", "docling_page_retry_math_block"}:
        return "high"
    if source.startswith("pix2text_markdown_"):
        return "medium"
    if source in {"docling_markdown_numbered_line", "docling_markdown_neighbor_reference"}:
        return "medium"
    return "low"


def quality_warnings(source: str, equation: str, raw_latex: str) -> list[str]:
    """Create short QA warnings for audit and validation reports."""

    warnings: list[str] = []
    if source == "docling_page_retry_math_block":
        warnings.append("page_retry_replaced_fallback")
    if source.startswith("pix2text_markdown_"):
        warnings.append("pix2text_fallback_replaced_pymupdf")
    if source in {"docling_markdown_neighbor_reference", "pix2text_markdown_neighbor_reference"}:
        warnings.append("label_inferred_from_nearby_prose")
    if source == "pymupdf_text_fallback":
        warnings.append("fallback_only_needs_review")
        warnings.append("pymupdf_text_is_recall_signal_not_trusted_latex")
    if re.search(r"\b(?:where|Megahertz|cients|coeffi|respectively|Fig)\b", equation, re.IGNORECASE):
        warnings.append("possible_prose_contamination")
    if re.search(r"\b(?:X\s+[a-z]|ħ\(|\d+i\\beta|\\kappaT LS|\\sqrt\\[A-Za-z])", equation):
        warnings.append("possible_pdf_text_degradation")
    if r"\begin{array}" in raw_latex or re.search(r"^\s*\{\s*(?:[A-Za-z]\s+){1,}[A-Za-z]\s*\}\s*&", raw_latex):
        warnings.append("needs_artifact_cleanup")
    if raw_latex != equation:
        warnings.append("normalized_from_raw")
    return warnings


def label_quality_warnings(number: str) -> list[str]:
    """Warn about labels that may be appendix/supplement or false positives."""

    warnings: list[str] = []
    if number == "0":
        warnings.append("suspicious_zero_equation_label")
    if re.match(r"[A-Za-z]\d+", number):
        warnings.append("appendix_or_supplement_label")
    if re.match(r"\d+[A-Za-z]+", number):
        warnings.append("suspicious_alphanumeric_equation_label")
    return warnings


def is_main_equation_label(number: str) -> bool:
    """Return whether a label should count as a main-paper equation label."""

    return bool(re.fullmatch(r"[1-9]\d*(?:\.\d+)?", number))


def apply_label_scope(equations: list[EquationCandidate], label_scope: str) -> list[EquationCandidate]:
    """Filter equations according to a generic label-scope policy."""

    if label_scope == "all":
        return equations
    if label_scope == "main":
        return [candidate for candidate in equations if is_main_equation_label(candidate.number)]
    raise ValueError(f"unsupported label scope: {label_scope}")


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
                raw_latex = strip_equation_number(normalize_latex(raw_block), number)
                latex = normalize_equation_for_output(raw_latex)
                if latex:
                    source = "docling_markdown_math_block"
                    candidates.append(
                        EquationCandidate(
                            number=number,
                            latex=latex,
                            raw_latex=raw_latex,
                            source=source,
                            confidence=confidence_for_source(source),
                            warnings=quality_warnings(source, latex, raw_latex),
                            line_start=start + 1,
                            line_end=end + 1,
                            context=window_context(lines, start, end),
                            source_location=f"Docling Markdown lines {start + 1}-{end + 1}",
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
            raw_latex = strip_equation_number(normalize_latex(raw_block), number)
            latex = normalize_equation_for_output(raw_latex)
            if latex:
                source = "docling_markdown_math_block"
                candidates.append(
                    EquationCandidate(
                        number=number,
                        latex=latex,
                        raw_latex=raw_latex,
                        source=source,
                        confidence=confidence_for_source(source),
                        warnings=quality_warnings(source, latex, raw_latex),
                        line_start=start + 1,
                        line_end=end + 1,
                        context=window_context(lines, start, end),
                        source_location=f"Docling Markdown lines {start + 1}-{end + 1}",
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
            raw_latex = normalize_latex(equation_text)
            latex = normalize_equation_for_output(raw_latex)
            source = "docling_markdown_numbered_line"
            candidates.append(
                EquationCandidate(
                    number=number,
                    latex=latex,
                    raw_latex=raw_latex,
                    source=source,
                    confidence=confidence_for_source(source),
                    warnings=quality_warnings(source, latex, raw_latex),
                    line_start=start + 1,
                    line_end=index + 1,
                    context=window_context(lines, start, index),
                    source_location=f"Docling Markdown lines {start + 1}-{index + 1}",
                )
            )
    return candidates


def nearest_prose_equation_reference(lines: list[str], start: int, end: int, radius: int = 4) -> str | None:
    """Find an equation number referenced near an unnumbered Docling math block."""

    search_indices: list[int] = []
    for offset in range(1, radius + 1):
        search_indices.append(end + offset)
    for offset in range(1, radius + 1):
        search_indices.append(start - offset)

    for index in search_indices:
        if index < 0 or index >= len(lines):
            continue
        line = lines[index].strip()
        if not line or line.startswith("$$"):
            continue
        references = PROSE_EQUATION_REFERENCE_RE.findall(line)
        if len(references) == 1:
            return re.sub(r"\s+", "", references[0])
        decimal_references = PAREN_DECIMAL_EQUATION_REFERENCE_RE.findall(line)
        if len(decimal_references) == 1:
            return re.sub(r"\s+", "", decimal_references[0])
    return None


def extract_unnumbered_math_blocks_with_neighbor_references(markdown: str) -> list[EquationCandidate]:
    """Label Docling math blocks when the equation number is only in nearby prose.

    Some PDFs render the display equation without a visible ``(N)`` marker but
    mention it immediately afterwards as ``Eq. N``. This extractor keeps the
    Docling formula text and marks the label inference in the audit trail.
    """

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
        else:
            index += 1
            while index < len(lines):
                block_lines.append(lines[index])
                stripped = lines[index].strip()
                if stripped.endswith("$$") or stripped.endswith(r"\]") or stripped == "```":
                    break
                index += 1
            end = index

        raw_block = "\n".join(block_lines)
        if extract_number_from_text(raw_block, allow_embedded_label=True) is None:
            number = nearest_prose_equation_reference(lines, start, end)
            raw_latex = normalize_latex(raw_block)
            if number is not None and MATH_SIGNAL_RE.search(raw_latex):
                latex = normalize_equation_for_output(raw_latex)
                source = "docling_markdown_neighbor_reference"
                candidates.append(
                    EquationCandidate(
                        number=number,
                        latex=latex,
                        raw_latex=raw_latex,
                        source=source,
                        confidence=confidence_for_source(source),
                        warnings=quality_warnings(source, latex, raw_latex),
                        line_start=start + 1,
                        line_end=end + 1,
                        context=window_context(lines, start, end),
                        source_location=(
                            f"Docling Markdown lines {start + 1}-{end + 1}; "
                            f"label inferred from nearby Eq. {number} reference"
                        ),
                    )
                )
        index += 1
    return candidates


def unicode_math_to_latexish(text: str) -> str:
    """Convert common PDF text-layer math glyphs into LaTeX-like text.

    The fallback is intentionally approximate: its main purpose is recall when
    Docling misses later pages. The raw fallback text is preserved in the audit
    trail so these approximations remain reviewable.
    """

    converted = unicodedata.normalize("NFKC", text)
    for glyph, latex in GREEK_TO_LATEX.items():
        converted = converted.replace(glyph, latex)
    converted = converted.replace("ˆ", r"\hat ")
    converted = converted.replace("˙", r"\dot ")
    converted = converted.replace("∂", r"\partial ")
    converted = converted.replace("∇", r"\nabla ")
    converted = converted.replace("≤", r"\le ")
    converted = converted.replace("≥", r"\ge ")
    converted = converted.replace("≠", r"\ne ")
    converted = converted.replace("≈", r"\approx ")
    converted = converted.replace("∞", r"\infty ")
    converted = re.sub(r"\s+", " ", converted).strip()
    return converted


def extract_pdf_text_lines(pdf_path: Path) -> list[PdfTextLine]:
    """Extract page-aware text lines with PyMuPDF for low-memory fallback."""

    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError(
            "PyMuPDF is required for the PDF fallback. Install dependencies with "
            "`python -m pip install -r requirements.txt`."
        ) from exc

    text_lines: list[PdfTextLine] = []
    global_line = 0
    with fitz.open(pdf_path) as document:
        for page_index, page in enumerate(document, start=1):
            for page_line, line in enumerate(page.get_text("text").splitlines(), start=1):
                global_line += 1
                text_lines.append(
                    PdfTextLine(
                        text=line.strip(),
                        page=page_index,
                        page_line=page_line,
                        global_line=global_line,
                    )
                )
    return text_lines


def pdf_label_from_line(line: str, *, page_line: int) -> tuple[str | None, bool]:
    """Return a possible equation label and whether the label is isolated."""

    stripped = line.strip()
    isolated = PDF_LABEL_LINE_RE.match(stripped)
    if isolated:
        return isolated.group(1), True
    trailing = PDF_TRAILING_LABEL_RE.search(stripped)
    if trailing and MATH_SIGNAL_RE.search(stripped):
        return trailing.group(1), False
    return None, False


def is_likely_pdf_math_fragment(line: str) -> bool:
    """Heuristic for keeping nearby PDF text-layer lines as equation fragments."""

    stripped = line.strip()
    if not stripped:
        return False
    if re.search(r"\b(?:Eq|Fig|where|giving|respectively|represents|describes)\b", stripped, re.IGNORECASE):
        return False
    if re.search(r"\[\d+(?:,\s*\d+)*\]", stripped):
        return False
    if len(stripped) > 160 and not MATH_SIGNAL_RE.search(stripped):
        return False
    prose_words = len(re.findall(r"\b[a-zA-Z]{4,}\b", stripped))
    math_marks = len(re.findall(r"[=+\-*/^_()|⟨⟩∑∫√≤≥≠≈∞∂∇α-ωΑ-Ω]", stripped))
    strong_math_marks = len(re.findall(r"[=+*/^_|⟨⟩∑∫√≤≥≠≈∞∂∇α-ωΑ-Ω]", stripped))
    if prose_words > 3 and strong_math_marks == 0:
        return False
    if MATH_SIGNAL_RE.search(stripped) and (math_marks >= 2 or prose_words <= 6):
        return True
    return bool(re.fullmatch(r"[\w\s\\{}()[\].,|+\-*/^_=<>⟨⟩∑∫√≤≥≠≈∞∂∇α-ωΑ-Ω]+", stripped) and math_marks >= 3)


def is_short_pdf_equation_continuation(line: str) -> bool:
    """Return whether a short PDF line can continue a split equation."""

    stripped = line.strip()
    if not stripped or len(stripped) > 35:
        return False
    if re.search(r"\b(?:Eq|Fig|where|giving|respectively|represents|describes)\b", stripped, re.IGNORECASE):
        return False
    prose_words = len(re.findall(r"\b[a-zA-Z]{4,}\b", stripped))
    return prose_words <= 1 and bool(re.search(r"[\w\d|()[\]{}+\-*/^_=<>⟨⟩α-ωΑ-Ω]", stripped))


def pdf_fallback_candidate_warnings(text: str) -> list[str]:
    """Return generic fallback-quality warnings for a collected PDF text candidate."""

    stripped = text.strip()
    warnings: list[str] = []
    prose_words = len(re.findall(r"\b[a-zA-Z]{4,}\b", stripped))
    strong_signal = bool(STRONG_EQUATION_SIGNAL_RE.search(stripped))
    if prose_words > 8:
        warnings.append("fallback_candidate_has_many_prose_words")
    if not strong_signal:
        warnings.append("fallback_candidate_has_weak_equation_structure")
    if PROSE_STOP_RE.search(stripped) and prose_words > 4:
        warnings.append("fallback_candidate_contains_prose_cue")
    return warnings


def is_usable_pdf_fallback_candidate(text: str, *, strict: bool) -> bool:
    """Decide whether a PDF text-layer candidate is usable as a fallback equation."""

    stripped = text.strip()
    if not stripped or not MATH_SIGNAL_RE.search(stripped):
        return False

    warnings = pdf_fallback_candidate_warnings(stripped)
    if strict and warnings:
        return False

    prose_words = len(re.findall(r"\b[a-zA-Z]{4,}\b", stripped))
    strong_signal = bool(STRONG_EQUATION_SIGNAL_RE.search(stripped))
    math_marks = len(re.findall(r"[=+\-*/^_<>|⟨⟩∑∫√≤≥≠≈∞∂∇α-ωΑ-Ω]", stripped))
    if prose_words > 12 and not strong_signal:
        return False
    if PROSE_STOP_RE.search(stripped) and prose_words > 8 and math_marks < 4:
        return False
    return True


def collect_pdf_equation_window(lines: list[PdfTextLine], label_index: int, isolated_label: bool) -> tuple[str, int, int]:
    """Collect a high-recall equation window around a PDF text-layer label."""

    current = lines[label_index].text
    start = label_index
    current_without_label = PDF_TRAILING_LABEL_RE.sub("", current).strip()
    fragments: list[str] = [] if isolated_label else [current_without_label]
    for index in range(label_index - 1, max(-1, label_index - 16), -1):
        candidate = lines[index].text
        previous_label = PDF_TRAILING_LABEL_RE.search(candidate) or PDF_LABEL_LINE_RE.match(candidate)
        if fragments and previous_label:
            break
        is_math_fragment = is_likely_pdf_math_fragment(candidate)
        is_continuation = bool(fragments) and is_short_pdf_equation_continuation(candidate)
        if not is_math_fragment and not is_continuation:
            if fragments:
                break
            continue
        fragments.insert(0, candidate)
        start = index

    end = label_index
    if not fragments and label_index > 0:
        fragments.append(lines[label_index - 1].text)
        start = label_index - 1
    return " ".join(fragment for fragment in fragments if fragment), start, end


def extract_from_pdf_text(pdf_path: Path, max_equations: int, *, strict: bool = False) -> list[EquationCandidate]:
    """Extract missing numbered equations from the PDF text layer.

    This fallback favors recall over perfect LaTeX. It is used to avoid missing
    equations when Docling returns partial output because of local memory limits.
    """

    lines = extract_pdf_text_lines(pdf_path)
    candidates: list[EquationCandidate] = []
    for index, line in enumerate(lines):
        number, isolated_label = pdf_label_from_line(line.text, page_line=line.page_line)
        if number is None:
            continue

        raw_text, start, end = collect_pdf_equation_window(lines, index, isolated_label)
        if not is_usable_pdf_fallback_candidate(raw_text, strict=strict):
            continue

        raw_text = re.sub(r"\(\s*" + re.escape(number) + r"\s*\)\s*$", "", raw_text).strip()
        raw_latex = unicode_math_to_latexish(raw_text)
        latex = normalize_equation_for_output(raw_latex)
        if not latex:
            continue

        source = "pymupdf_text_fallback"
        context_start = max(0, start - 2)
        context_end = min(len(lines), end + 3)
        context = " ".join(item.text for item in lines[context_start:context_end])[:500]
        candidates.append(
            EquationCandidate(
                number=number,
                latex=latex,
                raw_latex=raw_latex,
                source=source,
                confidence=confidence_for_source(source),
                warnings=quality_warnings(source, latex, raw_latex) + pdf_fallback_candidate_warnings(raw_text),
                line_start=lines[start].global_line,
                line_end=lines[end].global_line,
                context=context,
                source_location=(
                    f"PDF page {line.page}, text lines "
                    f"{lines[start].page_line}-{lines[end].page_line}"
                ),
            )
        )
        if len(candidates) >= max_equations:
            break
    return candidates


def page_number_from_location(source_location: str) -> int | None:
    """Parse a 1-based PDF page number from a candidate source location."""

    match = re.search(r"PDF page\s+(\d+)", source_location)
    if not match:
        return None
    return int(match.group(1))


def create_single_page_pdf(source_pdf: Path, page_number: int, output_dir: Path) -> Path:
    """Create a single-page PDF for page-targeted Docling retry."""

    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError(
            "PyMuPDF is required for page retry. Install dependencies with "
            "`python -m pip install -r requirements.txt`."
        ) from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    page_pdf = output_dir / f"{source_pdf.stem}_page_{page_number}.pdf"
    if page_pdf.exists():
        return page_pdf

    with fitz.open(source_pdf) as source_document:
        if page_number < 1 or page_number > source_document.page_count:
            raise ValueError(f"page {page_number} is outside {source_pdf}")
        with fitz.open() as page_document:
            page_document.insert_pdf(source_document, from_page=page_number - 1, to_page=page_number - 1)
            page_document.save(page_pdf)
    return page_pdf


def with_page_retry_source(candidate: EquationCandidate) -> EquationCandidate:
    """Return a Docling page-retry candidate with updated source metadata."""

    source = "docling_page_retry_math_block"
    return EquationCandidate(
        number=candidate.number,
        latex=candidate.latex,
        raw_latex=candidate.raw_latex,
        source=source,
        confidence=confidence_for_source(source),
        warnings=quality_warnings(source, candidate.latex, candidate.raw_latex),
        line_start=candidate.line_start,
        line_end=candidate.line_end,
        context=candidate.context,
        source_location=f"Page retry from {candidate.source_location}",
    )


def with_pix2text_source(candidate: EquationCandidate) -> EquationCandidate:
    """Return a Pix2Text fallback candidate with updated source metadata."""

    source_map = {
        "docling_markdown_math_block": "pix2text_markdown_math_block",
        "docling_markdown_numbered_line": "pix2text_markdown_numbered_line",
        "docling_markdown_neighbor_reference": "pix2text_markdown_neighbor_reference",
    }
    source = source_map.get(candidate.source, "pix2text_markdown_math_block")
    return EquationCandidate(
        number=candidate.number,
        latex=candidate.latex,
        raw_latex=candidate.raw_latex,
        source=source,
        confidence=confidence_for_source(source),
        warnings=quality_warnings(source, candidate.latex, candidate.raw_latex),
        line_start=candidate.line_start,
        line_end=candidate.line_end,
        context=candidate.context,
        source_location=f"Pix2Text fallback from {candidate.source_location}",
    )


def fallback_pages_for_pix2text(
    equations: list[EquationCandidate],
    *,
    max_pages: int,
) -> list[int]:
    """Select PDF pages worth retrying with Pix2Text."""

    pages = []
    seen = set()
    for candidate in equations:
        if candidate.source != "pymupdf_text_fallback":
            continue
        page_number = page_number_from_location(candidate.source_location)
        if page_number is None or page_number in seen:
            continue
        seen.add(page_number)
        pages.append(page_number)
        if len(pages) >= max_pages:
            break
    return pages


def read_markdown_files(markdown_dir: Path) -> str:
    """Read all Markdown files from an output directory in stable order."""

    markdown_parts = []
    for markdown_file in sorted(markdown_dir.rglob("*.md")):
        markdown_parts.append(markdown_file.read_text(encoding="utf-8", errors="ignore"))
    return "\n\n".join(markdown_parts)


def pix2text_cache_path(pdf_path: Path, pages: list[int], cache_dir: Path) -> Path:
    """Build a cache path for Pix2Text Markdown output."""

    page_key = "all" if not pages else "_".join(str(page) for page in pages)
    return cache_dir / f"{pdf_path.stem}_pages_{page_key}.md"


def convert_pdf_pages_with_pix2text(
    pdf_path: Path,
    pages: list[int],
    *,
    cache_dir: Path,
) -> tuple[str, dict[str, Any]]:
    """Convert selected PDF pages to Markdown with local Pix2Text."""

    cache_dir.mkdir(parents=True, exist_ok=True)
    markdown_cache = pix2text_cache_path(pdf_path, pages, cache_dir)
    if markdown_cache.exists():
        markdown = markdown_cache.read_text(encoding="utf-8", errors="ignore")
        return markdown, {
            "status": "cached_pix2text_markdown",
            "converter": "pix2text",
            "pages": pages,
            "markdown_chars": len(markdown),
            "cached_markdown": str(markdown_cache),
        }

    try:
        from pix2text import Pix2Text
    except ImportError as exc:
        raise RuntimeError(
            "Pix2Text fallback requested but pix2text is not installed. "
            "Install it with `python -m pip install pix2text`."
        ) from exc

    zero_based_pages = [page - 1 for page in pages if page > 0] or None
    output_root = cache_dir / f"{pdf_path.stem}_pix2text_work"
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="pix2text_", dir=str(output_root)) as temporary_dir:
        temporary_path = Path(temporary_dir)
        p2t = Pix2Text.from_config()
        document = p2t.recognize_pdf(str(pdf_path), page_numbers=zero_based_pages)

        markdown = ""
        if isinstance(document, str):
            markdown = document
        elif hasattr(document, "to_markdown"):
            result = document.to_markdown(str(temporary_path))
            if isinstance(result, str) and "\n" in result:
                markdown = result
            elif isinstance(result, str) and Path(result).exists():
                result_path = Path(result)
                markdown = result_path.read_text(encoding="utf-8", errors="ignore")
            else:
                markdown = read_markdown_files(temporary_path)
        else:
            markdown = str(document)

    markdown_cache.write_text(markdown, encoding="utf-8")
    return markdown, {
        "status": "ConversionStatus.SUCCESS",
        "converter": "pix2text",
        "pages": pages,
        "markdown_chars": len(markdown),
        "cached_markdown": str(markdown_cache),
    }


def retry_fallback_equations_with_pix2text_pages(
    pdf_path: Path,
    equations: list[EquationCandidate],
    *,
    cache_dir: Path,
    max_pages: int,
    max_equations: int,
) -> list[EquationCandidate]:
    """Replace weak PyMuPDF fallback equations with Pix2Text Markdown equations."""

    pages = fallback_pages_for_pix2text(equations, max_pages=max_pages)
    if not pages:
        return equations

    try:
        pix2text_markdown, metadata = convert_pdf_pages_with_pix2text(
            pdf_path,
            pages,
            cache_dir=cache_dir,
        )
    except Exception as exc:
        print(f"Pix2Text fallback failed for {pdf_path.name}: {exc}")
        return equations

    pix2text_candidates = [
        with_pix2text_source(candidate)
        for candidate in extract_equations(
            pix2text_markdown,
            max_equations=max_equations,
            use_pdf_fallback=False,
        )
    ]
    if not pix2text_candidates:
        print(f"Pix2Text fallback found no equations for {pdf_path.name}; pages={pages}")
        return equations

    replacements = {candidate.number: candidate for candidate in pix2text_candidates}
    existing_numbers = {candidate.number for candidate in equations}
    improved: list[EquationCandidate] = []
    replaced = 0
    for candidate in equations:
        if candidate.source == "pymupdf_text_fallback" and candidate.number in replacements:
            improved.append(replacements[candidate.number])
            replaced += 1
        else:
            improved.append(candidate)

    additions = [
        candidate
        for candidate in pix2text_candidates
        if candidate.number not in existing_numbers
    ]
    if additions:
        improved.extend(additions)
    print(
        f"Pix2Text fallback for {pdf_path.name}: pages={metadata['pages']}, "
        f"candidates={len(pix2text_candidates)}, replaced={replaced}, added={len(additions)}"
    )
    return deduplicate_candidates(improved, max_equations)


def retry_fallback_equations_with_docling_pages(
    pdf_path: Path,
    equations: list[EquationCandidate],
    *,
    enable_ocr: bool,
    retry_dir: Path,
) -> list[EquationCandidate]:
    """Try to replace fallback-only equations with Docling output from single pages."""

    fallback_pages = sorted(
        {
            page_number
            for candidate in equations
            if candidate.source == "pymupdf_text_fallback"
            for page_number in [page_number_from_location(candidate.source_location)]
            if page_number is not None
        }
    )
    if not fallback_pages:
        return equations

    replacements: dict[str, EquationCandidate] = {}
    for page_number in fallback_pages:
        try:
            page_pdf = create_single_page_pdf(pdf_path, page_number, retry_dir)
            page_markdown, _metadata = convert_pdf_with_docling(page_pdf, enable_ocr=enable_ocr)
            page_candidates = extract_equations(
                page_markdown,
                max_equations=20,
                use_pdf_fallback=False,
            )
        except Exception as exc:
            print(f"Page retry failed for {pdf_path.name} page {page_number}: {exc}")
            continue

        for candidate in page_candidates:
            replacements[candidate.number] = with_page_retry_source(candidate)

    if not replacements:
        return equations

    improved: list[EquationCandidate] = []
    for candidate in equations:
        if candidate.source == "pymupdf_text_fallback" and candidate.number in replacements:
            improved.append(replacements[candidate.number])
        else:
            improved.append(candidate)
    return improved


def equation_number_sort_key(number: str) -> tuple[int, int, str]:
    """Sort common equation labels in document order."""

    decimal_match = re.fullmatch(r"(\d+)\.(\d+)", number)
    if decimal_match:
        major, minor = decimal_match.groups()
        return 0, int(major), f"{int(minor):06d}"
    match = re.match(r"([A-Za-z]?)(\d+)(.*)", number)
    if match:
        prefix, numeric, suffix = match.groups()
        prefix_rank = 1 if prefix else 0
        return prefix_rank, int(numeric), suffix
    return 2, 10**9, number


def deduplicate_candidates(candidates: list[EquationCandidate], limit: int) -> list[EquationCandidate]:
    """Keep first occurrence of each equation number while preserving order."""

    selected_by_number: dict[str, EquationCandidate] = {}
    seen: set[str] = set()
    for candidate in candidates:
        if candidate.number in seen:
            continue
        seen.add(candidate.number)
        selected_by_number[candidate.number] = candidate
    selected = sorted(selected_by_number.values(), key=lambda candidate: equation_number_sort_key(candidate.number))
    return selected[:limit]


def extract_equations(
    markdown: str,
    max_equations: int,
    *,
    pdf_path: Path | None = None,
    use_pdf_fallback: bool = True,
    strict_pdf_fallback: bool = False,
) -> list[EquationCandidate]:
    """Run the deterministic equation candidate extractors."""

    candidates = extract_from_math_blocks(markdown)
    candidates.extend(extract_from_numbered_lines(markdown))
    candidates.extend(extract_unnumbered_math_blocks_with_neighbor_references(markdown))
    if use_pdf_fallback and pdf_path is not None:
        candidates.extend(extract_from_pdf_text(pdf_path, max_equations, strict=strict_pdf_fallback))
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
                "extraction_confidence": candidate.confidence,
                "quality_warnings": candidate.warnings + label_quality_warnings(candidate.number),
                "equation_location": candidate.source_location,
                "equation_raw": candidate.raw_latex,
                "normalize_equation": (
                    "Applied conservative cleanup for LaTeX spacing, trailing layout markers, "
                    "and visible equation labels."
                ),
                "context_window": candidate.context,
            },
        }
    return {arxiv_id: paper_entry}


def build_validation_report(
    arxiv_id: str,
    equations: list[EquationCandidate],
    conversion_metadata: dict[str, Any],
) -> dict[str, Any]:
    """Build a compact QA report for manual accuracy review."""

    actionable_warnings = {
        candidate.number: [
            warning for warning in candidate.warnings + label_quality_warnings(candidate.number)
            if warning != "normalized_from_raw"
        ]
        for candidate in equations
    }
    confidence_counts = Counter(candidate.confidence for candidate in equations)
    source_counts = Counter(candidate.source for candidate in equations)
    clean_labels = [
        candidate.number
        for candidate in equations
        if candidate.confidence in {"high", "medium"} and not actionable_warnings.get(candidate.number)
    ]
    main_equation_labels = [
        candidate.number
        for candidate in equations
        if is_main_equation_label(candidate.number)
    ]
    return {
        arxiv_id: {
            "equation_count": len(equations),
            "equation_labels": [candidate.number for candidate in equations],
            "main_equation_count": len(main_equation_labels),
            "main_equation_labels": main_equation_labels,
            "clean_labels": clean_labels,
            "docling_status": conversion_metadata.get("status", "unknown"),
            "confidence_counts": dict(sorted(confidence_counts.items())),
            "source_counts": dict(sorted(source_counts.items())),
            "sources": {
                candidate.number: candidate.source
                for candidate in equations
            },
            "confidence": {
                candidate.number: candidate.confidence
                for candidate in equations
            },
            "quality_warnings": {
                candidate.number: candidate.warnings + label_quality_warnings(candidate.number)
                for candidate in equations
                if candidate.warnings or label_quality_warnings(candidate.number)
            },
            "suspicious_labels": [
                candidate.number
                for candidate in equations
                if label_quality_warnings(candidate.number)
            ],
            "fallback_only_labels": [
                candidate.number
                for candidate in equations
                if candidate.source == "pymupdf_text_fallback"
            ],
            "needs_review": [
                candidate.number
                for candidate in equations
                if candidate.confidence == "low" or actionable_warnings.get(candidate.number)
            ],
            "review_summary": {
                "fallback_only_count": sum(
                    1 for candidate in equations if candidate.source == "pymupdf_text_fallback"
                ),
                "suspicious_label_count": sum(
                    1 for candidate in equations if label_quality_warnings(candidate.number)
                ),
                "artifact_cleanup_count": sum(
                    1 for warnings in actionable_warnings.values()
                    if "needs_artifact_cleanup" in warnings
                ),
            },
        }
    }


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
        "--paper-list",
        type=Path,
        default=Path("paper_list_16.txt"),
        help="Path to the assigned Moodle paper list.",
    )
    parser.add_argument(
        "--paper-number",
        type=int,
        required=True,
        help="1-based paper number from the paper list, e.g. 9 for the ninth entry.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/pdf/equations_pdf.json"),
        help="Professor-shaped output JSON path.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=None,
        help="Optional compact QA report JSON path.",
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
        default=200,
        help="Maximum relevant enumerated equations to keep for this paper.",
    )
    parser.add_argument(
        "--label-scope",
        choices=("all", "main"),
        default="all",
        help=(
            "Equation label policy: 'all' keeps every extracted enumerated label; "
            "'main' keeps only normal main-paper numeric labels such as 1, 2, 3."
        ),
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
        "--docling-markdown-input",
        type=Path,
        default=None,
        help="Optional cached Docling Markdown input. Skips Docling PDF conversion when the file exists.",
    )
    parser.add_argument(
        "--enable-ocr",
        action="store_true",
        help="Enable OCR for scanned PDFs. Leave off for normal arXiv text-layer PDFs.",
    )
    parser.add_argument(
        "--device-policy",
        choices=("auto", "cpu", "gpu"),
        default="auto",
        help="Docling device policy: auto uses GPU for small PDFs and CPU for larger PDFs.",
    )
    parser.add_argument(
        "--gpu-max-pages",
        type=int,
        default=10,
        help="In --device-policy auto, use GPU only when page count is at or below this value.",
    )
    parser.add_argument(
        "--gpu-max-mb",
        type=float,
        default=20.0,
        help="In --device-policy auto, use GPU only when PDF size is at or below this value.",
    )
    parser.add_argument(
        "--disable-pdf-fallback",
        action="store_true",
        help="Disable PyMuPDF text-layer fallback extraction.",
    )
    parser.add_argument(
        "--strict-pdf-fallback",
        action="store_true",
        help="Reject PDF text fallback candidates that look prose-heavy or structurally weak.",
    )
    parser.add_argument(
        "--enable-pix2text-fallback",
        action="store_true",
        help="Use local Pix2Text on pages where PyMuPDF found low-confidence fallback labels.",
    )
    parser.add_argument(
        "--pix2text-cache-dir",
        type=Path,
        default=Path("data/pix2text_cache"),
        help="Directory for cached Pix2Text Markdown fallback output.",
    )
    parser.add_argument(
        "--pix2text-max-pages",
        type=int,
        default=8,
        help="Maximum fallback pages per paper to send to Pix2Text.",
    )
    parser.add_argument(
        "--disable-page-retry",
        action="store_true",
        help="Disable page-level Docling retry for PyMuPDF fallback equations.",
    )
    parser.add_argument(
        "--page-retry-dir",
        type=Path,
        default=Path("data/page_retry_cache"),
        help="Directory for cached single-page PDFs used by Docling page retry.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the single-paper PDF equation extraction pipeline."""

    args = parse_args()
    paper_ids = read_paper_list(args.paper_list)
    arxiv_id = select_arxiv_id(paper_ids, args.paper_number)
    cached_markdown_available = (
        args.docling_markdown_input is not None and args.docling_markdown_input.exists()
    )
    needs_pdf = (
        not cached_markdown_available
        or not args.disable_pdf_fallback
        or not args.disable_page_retry
        or args.enable_pix2text_fallback
    )
    pdf_path = (
        download_arxiv_pdf(
            arxiv_id,
            args.cache_dir,
            sleep_seconds=args.sleep_seconds,
            force=args.force_download,
        )
        if needs_pdf
        else None
    )
    if cached_markdown_available:
        markdown = args.docling_markdown_input.read_text(encoding="utf-8")
        conversion_metadata = {
            "status": "cached_docling_markdown",
            "converter": "docling",
            "ocr_enabled": args.enable_ocr,
            "markdown_chars": len(markdown),
            "cached_markdown": str(args.docling_markdown_input),
        }
    else:
        if args.docling_markdown_input is not None:
            print(f"Cached Markdown not found at {args.docling_markdown_input}; running Docling.")
        if pdf_path is None:
            raise RuntimeError("PDF path is required when cached Markdown is unavailable.")
        device_metadata = configure_docling_device(
            pdf_path,
            policy=args.device_policy,
            gpu_max_pages=args.gpu_max_pages,
            gpu_max_mb=args.gpu_max_mb,
        )
        try:
            markdown, conversion_metadata = convert_pdf_with_docling(pdf_path, enable_ocr=args.enable_ocr)
            conversion_metadata.update(device_metadata)
        except Exception as exc:
            markdown = ""
            conversion_metadata = {
                "status": f"docling_failed:{type(exc).__name__}",
                "converter": "docling",
                "ocr_enabled": args.enable_ocr,
                "markdown_chars": 0,
                "error": str(exc),
                **device_metadata,
            }
            print(f"Docling failed for arXiv:{arxiv_id}; continuing with PDF text fallback: {exc}")
    if args.save_docling_markdown is not None:
        args.save_docling_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.save_docling_markdown.write_text(markdown, encoding="utf-8")

    equations = extract_equations(
        markdown,
        args.max_equations,
        pdf_path=pdf_path,
        use_pdf_fallback=not args.disable_pdf_fallback and pdf_path is not None,
        strict_pdf_fallback=args.strict_pdf_fallback,
    )
    if args.enable_pix2text_fallback and pdf_path is not None:
        equations = retry_fallback_equations_with_pix2text_pages(
            pdf_path,
            equations,
            cache_dir=args.pix2text_cache_dir,
            max_pages=args.pix2text_max_pages,
            max_equations=args.max_equations,
        )
    if not args.disable_page_retry and pdf_path is not None:
        equations = retry_fallback_equations_with_docling_pages(
            pdf_path,
            equations,
            enable_ocr=args.enable_ocr,
            retry_dir=args.page_retry_dir,
        )
    equations = apply_label_scope(equations, args.label_scope)
    dataset_entry = build_dataset_entry(arxiv_id, equations, conversion_metadata)
    write_json(args.output, dataset_entry, merge=args.merge)
    if args.report_output is not None:
        report_entry = build_validation_report(arxiv_id, equations, conversion_metadata)
        write_json(args.report_output, report_entry, merge=args.merge)
    print(
        f"arXiv:{arxiv_id}: extracted {len(equations)} enumerated equation(s) "
        f"to {args.output}"
    )


if __name__ == "__main__":
    main()
