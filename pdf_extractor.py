"""PDF-only equation extraction using PyMuPDF + texify.

Detects equation regions in PDF pages via font analysis, crops them
as images, and converts to LaTeX using the texify OCR model (~88% accuracy).

No LLM or prompting is used — texify is a specialized math-OCR model.
"""
from __future__ import annotations

import io
import re
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF

# Lazily loaded texify model.
_texify_model = None
_texify_processor = None


def _load_texify():
    """Load the texify model and processor (once)."""
    global _texify_model, _texify_processor
    if _texify_model is None:
        from texify.model.model import load_model
        from texify.model.processor import load_processor
        _texify_model = load_model()
        _texify_processor = load_processor()
    return _texify_model, _texify_processor


def _find_equation_regions(page: fitz.Page, eq_numbers: list[dict]) -> list[dict]:
    """Find bounding boxes of equation content for each equation number.

    Parameters
    ----------
    page : fitz.Page
        The PDF page.
    eq_numbers : list[dict]
        Equation number info dicts with keys: num, x0, y0, x1, y1.

    Returns
    -------
    list[dict]
        Each dict has: num (int), bbox (fitz.Rect), eq_num_info (dict).
    """
    blocks = page.get_text("dict")["blocks"]
    page_w = page.rect.width
    mid_x = page_w / 2
    results = []

    for eq_info in eq_numbers:
        eq_y = (eq_info["y0"] + eq_info["y1"]) / 2
        col_start = mid_x if eq_info["x0"] > mid_x else 0
        col_end = page_w if eq_info["x0"] > mid_x else mid_x

        # Find all text spans with math fonts near this y-coordinate.
        math_bboxes = []
        for block in blocks:
            if "lines" not in block:
                continue
            bx0, by0, bx1, by1 = block["bbox"]
            if bx0 < col_start - 10 or bx1 > col_end + 10:
                continue
            by_mid = (by0 + by1) / 2
            if abs(by_mid - eq_y) > 35:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    font = span.get("font", "")
                    if any(font.startswith(p) for p in ("CM", "LM", "STIX", "Math")):
                        math_bboxes.append(span["bbox"])
                    elif span["text"].strip():
                        # Also include non-math spans at the same line
                        ly = (span["bbox"][1] + span["bbox"][3]) / 2
                        if abs(ly - eq_y) < 20:
                            math_bboxes.append(span["bbox"])

        if not math_bboxes:
            continue

        x0 = min(b[0] for b in math_bboxes) - 5
        y0 = min(b[1] for b in math_bboxes) - 8
        x1 = min(max(b[2] for b in math_bboxes) + 5, eq_info["x0"] - 3)
        y1 = max(b[3] for b in math_bboxes) + 8

        if x1 - x0 < 15 or y1 - y0 < 8:
            continue

        results.append({
            "num": eq_info["num"],
            "bbox": fitz.Rect(x0, y0, x1, y1),
            "eq_num_info": eq_info,
        })

    return results


def _crop_and_pad(page: fitz.Page, rect: fitz.Rect, zoom: int = 5):
    """Crop a region from a page as a PIL Image with white padding.

    Parameters
    ----------
    page : fitz.Page
        The PDF page.
    rect : fitz.Rect
        Region to crop.
    zoom : int
        Zoom factor for resolution.

    Returns
    -------
    PIL.Image.Image
        Cropped and padded image.
    """
    from PIL import Image

    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    padded = Image.new("RGB", (img.width + 40, img.height + 40), "white")
    padded.paste(img, (20, 20))
    return padded


def _get_context(page: fitz.Page, eq_y: float, col_start: float, col_end: float) -> tuple[str, str]:
    """Get text before and after an equation for context."""
    blocks = page.get_text("dict")["blocks"]
    before_parts = []
    after_parts = []

    for block in blocks:
        if "lines" not in block:
            continue
        bx0, by0, bx1, by1 = block["bbox"]
        if bx0 < col_start - 10 or bx1 > col_end + 10:
            continue
        text = ""
        for line in block["lines"]:
            for span in line["spans"]:
                text += span["text"]
        if not text.strip():
            continue
        by_mid = (by0 + by1) / 2
        if by_mid < eq_y - 15:
            before_parts.append((by0, text))
        elif by_mid > eq_y + 15:
            after_parts.append((by0, text))

    before_parts.sort(key=lambda x: x[0])
    after_parts.sort(key=lambda x: x[0])
    before = " ".join(t for _, t in before_parts[-2:])[:400] if before_parts else ""
    after = " ".join(t for _, t in after_parts[:2])[:400] if after_parts else ""
    return before, after


def extract_equations_pdf_only(
    pdf_path: Path | str,
    max_equations: int = 7,
) -> list[dict[str, Any]]:
    """Extract numbered equations from a PDF using PyMuPDF + texify.

    Parameters
    ----------
    pdf_path : Path or str
        Path to the PDF file.
    max_equations : int
        Maximum equations to extract.

    Returns
    -------
    list[dict]
        Each dict has: number, latex, page, context_before, context_after.
    """
    from pdf_equation_pipeline import count_equations_from_pdf

    # Step 1: Get ground-truth equation numbers from PDF.
    eq_num_list = count_equations_from_pdf(Path(pdf_path))
    if not eq_num_list:
        return []
    eq_num_list = eq_num_list[:max_equations]

    # Step 2: Load texify model.
    model, processor = _load_texify()

    # Step 3: For each page, find equation regions and OCR them.
    doc = fitz.open(str(pdf_path))
    page_w = doc[0].rect.width
    mid_x = page_w / 2

    # Build a map: equation_number → (page_idx, eq_num_word_info).
    # Sort occurrences by x-position descending so the rightmost (actual
    # equation label) comes first, not in-text references like "Eq. (1)".
    eq_page_map: dict[int, list[tuple[int, dict]]] = {}
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        words = page.get_text("words")
        for w in words:
            x0, y0, x1, y1, text = w[0], w[1], w[2], w[3], w[4]
            m = re.match(r"^\((\d+)([a-z])?\)$", text.strip())
            if m and x0 > page_w * 0.35:
                num = int(m.group(1))
                if num > 999:
                    continue
                info = {"num": num, "x0": x0, "y0": y0, "x1": x1, "y1": y1}
                eq_page_map.setdefault(num, []).append((page_idx, info))

    # Sort each number's occurrences: rightmost x first (actual labels are flush-right)
    for num in eq_page_map:
        eq_page_map[num].sort(key=lambda t: t[1]["x0"], reverse=True)

    results: list[dict[str, Any]] = []
    images_to_ocr: list[tuple[int, Any]] = []  # (index, PIL image)

    for eq_num in eq_num_list:
        if eq_num not in eq_page_map:
            # Number not found in word scan — add placeholder
            results.append({
                "number": str(eq_num),
                "latex": "",
                "page": 0,
                "context_before": "",
                "context_after": "",
            })
            continue

        # Use the first occurrence (actual equation label, not a reference)
        page_idx, eq_info = eq_page_map[eq_num][0]
        page = doc[page_idx]

        # Crop equation region: area to the LEFT of the equation number.
        # Use a simple but robust approach — take the full column width,
        # vertically centered on the equation number, with some expansion.
        eq_y = (eq_info["y0"] + eq_info["y1"]) / 2
        col_start = mid_x if eq_info["x0"] > mid_x else page.rect.x0 + 20
        crop_rect = fitz.Rect(
            col_start,
            eq_info["y0"] - 20,   # extend 20pt above
            eq_info["x0"] - 3,    # stop before number
            eq_info["y1"] + 20,   # extend 20pt below
        )
        # Clamp to page bounds
        crop_rect = crop_rect & page.rect
        if crop_rect.width < 15 or crop_rect.height < 10:
            results.append({
                "number": str(eq_num),
                "latex": "",
                "page": page_idx + 1,
                "context_before": "",
                "context_after": "",
            })
            continue

        img = _crop_and_pad(page, crop_rect)

        # Get context
        eq_y = (eq_info["y0"] + eq_info["y1"]) / 2
        col_start = mid_x if eq_info["x0"] > mid_x else 0
        col_end = page_w if eq_info["x0"] > mid_x else mid_x
        before, after = _get_context(page, eq_y, col_start, col_end)

        idx = len(results)
        results.append({
            "number": str(eq_num),
            "latex": "",  # filled by batch OCR below
            "page": page_idx + 1,
            "context_before": before,
            "context_after": after,
        })
        images_to_ocr.append((idx, img))

    doc.close()

    # Step 4: Batch OCR all equation images with texify.
    if images_to_ocr:
        from texify.inference import batch_inference

        images = [img for _, img in images_to_ocr]
        # Process in batches of 8 to avoid memory issues
        batch_size = 8
        all_latex = []
        for i in range(0, len(images), batch_size):
            batch = images[i:i + batch_size]
            batch_results = batch_inference(batch, model, processor)
            all_latex.extend(batch_results)

        for (idx, _), latex in zip(images_to_ocr, all_latex):
            # Clean texify output
            latex = latex.strip()
            latex = re.sub(r"^\$\$\s*", "", latex)
            latex = re.sub(r"\s*\$\$$", "", latex)
            latex = re.sub(r"^\$\s*", "", latex)
            latex = re.sub(r"\s*\$$", "", latex)
            results[idx]["latex"] = latex.strip()

    return results
