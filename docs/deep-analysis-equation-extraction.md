# Deep Analysis: PDF Math Equation Extraction Pipeline (v2)

**Date**: 2026-06-19
**Target PDF**: `2410.07429v2.pdf` — "Foundation of statistical mechanics under even more experimentally realistic conditions"
**Constraint**: No LLM / no cloud API — local libraries and code only

---

## 1. The Core Problem

We need to extract numbered display equations from research paper PDFs and produce:
```json
{
  "equation": "\\sum_n d_n(0^+) e^{-iE_n t} |E_n\\rangle",   // LaTeX code
  "number": "1",                                                  // equation label
  "mathsSymbol": ["∑", "⟩"]                                      // Unicode math symbols
}
```

**Why this is hard**: PDFs are a *rendering format*, not a *semantic format*. A PDF stores "draw glyph X at position (x,y)" — it has no concept of "this is equation (1)". Reconstructing structured LaTeX from rendered glyphs is fundamentally a reverse-engineering problem.

---

## 2. What We Tried & What Happened

### 2.1 Docling WITH formula enrichment
- **Result**: Process ran 40+ minutes on a 9-page paper, never finished
- **Why**: Downloads and runs a deep learning model (LayoutLM + formula recognition) on every page. For a math-heavy physics paper, this is extremely CPU-intensive
- **Verdict**: Produces good LaTeX when it works, but unusably slow for development/iteration

### 2.2 Docling WITHOUT formula enrichment
- **Result**: Completed fast (~30 sec), but ALL equations replaced with `<!-- formula-not-decoded -->`
- **Why**: Without the ML formula model, Docling can't parse math regions at all
- **Verdict**: Useless for equation extraction

### 2.3 PyMuPDF raw text extraction (`get_text()`)
- **Result**: Gets equation text as Unicode characters, NOT LaTeX
- **Example**: `|Ψ(t)⟩ = Σ_n d_n(0+)e^{-iE_n t}|E_n⟩` instead of `\sum_n d_n(0^+) e^{-iE_n t} |E_n\rangle`
- **Why**: The PDF text layer stores the *rendered* Unicode characters, not the source LaTeX
- **Verdict**: Can detect WHERE equations are, but can't give us LaTeX code

### 2.4 PyMuPDF font-based analysis (`get_text("dict")`)
- **Result**: VERY promising! Can identify math regions precisely by font:
  - `CMMI10` = Computer Modern Math Italic (variables: E, A, d, t, ρ)
  - `CMSY10` = Computer Modern Math Symbols (|, ⟩, ⟨, ≡, ≤, −)
  - `CMEX10` = Computer Modern Math Extensions (∑, ∫ — large operators)
  - `CMR10` = Computer Modern Roman (text, numbers, parentheses)
- **Can detect**: Equation regions, equation numbers `(1)`, `(2)` at right margin, inline vs display math
- **Verdict**: Excellent for DETECTION, but still gives Unicode text, not LaTeX

---

## 3. All Possible Approaches (Ranked)

### Approach A: PyMuPDF Detection + pix2tex LaTeX OCR (RECOMMENDED)

```
PDF Page → [PyMuPDF] → Detect equation regions by font/coordinates
                      → Crop equation as image
                      → [pix2tex/LaTeX-OCR] → LaTeX string
                      → Extract number from "(N)" text
                      → Extract symbols from LaTeX
                      → JSON output
```

**How it works**:
1. **PyMuPDF** scans each page using `get_text("dict")` to find equation regions:
   - Look for standalone `(N)` pattern at right margin (x > 80% page width)
   - Group nearby spans with math fonts (CMMI*, CMSY*, CMEX*)
   - Determine bounding box of the equation region
2. **Crop** the equation region as a high-res image using `page.get_pixmap(clip=rect)`
3. **pix2tex** (LaTeX-OCR) converts the cropped image to LaTeX code
4. Our existing `extract_math_symbols()` extracts symbols from the LaTeX

**Pros**:
- Fast: PyMuPDF detection is instant; pix2tex is ~1-2 sec per equation
- Produces ACTUAL LaTeX code (not Unicode approximation)
- Works on ANY PDF (not just arXiv papers)
- Fully local — no cloud API calls
- pix2tex is a specialized OCR model, not an LLM

**Cons**:
- Requires `pix2tex` package (~500MB model download on first run)
- pix2tex accuracy ~90-95% on clean equations (occasional errors on complex ones)
- Needs equation region detection logic (but font analysis makes this reliable)

**Libraries**: `pymupdf` (already installed), `pix2tex` (new), `pylatexenc` (already installed)

**Effort**: Medium (~150-200 lines of new code)

---

### Approach B: arXiv LaTeX Source Download + .tex Parsing

```
arXiv ID → Download .tar.gz source → Extract .tex file
         → Parse equation environments (equation, align, gather)
         → Extract LaTeX + equation numbers
         → JSON output
```

**How it works**:
1. Download source from `https://arxiv.org/e-print/{arxiv_id}` (confirmed available as `.tar.gz`)
2. Extract `.tex` file(s) from the archive
3. Parse LaTeX source using regex or `TexSoup` to find equation environments:
   - `\begin{equation}...\end{equation}`
   - `\begin{align}...\end{align}`
   - `$$...$$` display math with `\tag{}`
4. Extract the LaTeX content and equation numbers

**Pros**:
- **Perfect LaTeX** — this IS the original source code
- Extremely fast (just text parsing, no ML)
- Zero ambiguity in equation detection
- No additional ML dependencies

**Cons**:
- **Only works for arXiv papers** with available source
- Custom LaTeX macros (`\newcommand`) need expansion
- Multi-file LaTeX projects need flattening
- Not generalizable to arbitrary PDFs

**Libraries**: `tarfile` (stdlib), `TexSoup` or regex (new)

**Effort**: Low-Medium (~100-150 lines)

---

### Approach C: PyMuPDF Text + Unicode→LaTeX Reverse Mapping

```
PDF Page → [PyMuPDF dict mode] → Extract equation text spans
         → Group by y-coordinate → Reconstruct equation text
         → [pylatexenc] → Map Unicode chars back to LaTeX commands
         → JSON output
```

**How it works**:
1. PyMuPDF extracts all text spans with font info and coordinates
2. Identify equation regions (font-based detection as described above)
3. Concatenate spans in reading order to get Unicode equation text
4. Use `pylatexenc` `unicode_to_latex()` to reverse-map: `∑` → `\sum`, `≤` → `\leq`

**Pros**:
- No additional dependencies (pymupdf + pylatexenc already installed)
- Very fast
- No ML model needed

**Cons**:
- **LOSES STRUCTURAL INFORMATION**: fractions, superscripts/subscripts, matrices are flattened
  - `\frac{||A||^2}{d_{eff}}` becomes `||A||^2 / d_eff` (lost fraction structure)
  - `e^{-iE_n t}` may appear as `e−iEnt` (lost superscript grouping)
- The LaTeX produced is an APPROXIMATION, not the original
- Complex equations (piecewise, matrices, aligned) will be poorly reconstructed

**Libraries**: `pymupdf`, `pylatexenc` (both already installed)

**Effort**: Medium (~120-150 lines)

---

### Approach D: Nougat (Meta's Neural PDF Parser)

```
PDF → [Nougat model] → Full Markdown with LaTeX equations
    → Parse equation blocks → JSON output
```

**How it works**:
- Nougat is a vision-encoder-decoder model that converts entire PDF pages to Markdown
- Equations appear as LaTeX within `\[...\]` or `$$...$$` blocks

**Pros**:
- Produces excellent LaTeX for academic papers
- Handles the entire page including context

**Cons**:
- **Very slow** (~30-60 sec per page, similar problem as Docling)
- Large model (~1.5GB download)
- GPU recommended (CPU-only is very slow)
- Overkill — we only need equations, not full page text

**Libraries**: `nougat-ocr` (new, heavy)

**Effort**: Low (Nougat does most work), but slow runtime

---

### Approach E: Docling with formula enrichment (current pipeline)

Already analyzed above. Works but takes 40+ minutes.

---

## 4. Comparison Matrix

| Criteria | A: PyMuPDF+pix2tex | B: arXiv Source | C: Unicode Reverse | D: Nougat |
|----------|:--:|:--:|:--:|:--:|
| **LaTeX Quality** | High (90-95%) | Perfect (100%) | Low (60-70%) | High (90%+) |
| **Speed (per page)** | ~3-5 sec | <1 sec | <1 sec | 30-60 sec |
| **Works on any PDF** | Yes | arXiv only | Yes | Yes |
| **New dependencies** | pix2tex (~500MB) | TexSoup (tiny) | None | nougat (~1.5GB) |
| **Handles fractions** | Yes | Yes | No | Yes |
| **Handles superscripts** | Yes | Yes | Partial | Yes |
| **Equation detection** | Font-based (reliable) | Env-based (perfect) | Font-based | Auto |
| **No ML/model needed** | No (uses ViT) | Yes | Yes | No |

---

## 5. RECOMMENDATION: Hybrid A+B

**Best strategy: Use Approach B for arXiv papers, fall back to Approach A for other PDFs.**

```
Input PDF
  ├── Is arXiv paper? (check filename/metadata)
  │   ├── YES → Approach B: Download .tex source, parse equations (FAST + PERFECT)
  │   └── NO  → Approach A: PyMuPDF detection + pix2tex OCR (FAST + HIGH QUALITY)
  └── Output: JSON with {equation, number, mathsSymbol}
```

### For Your Immediate Case (2410.07429v2.pdf):
- This IS an arXiv paper → Use **Approach B** for perfect LaTeX
- Result in seconds, not minutes

### For General Use:
- Fall back to **Approach A** (pix2tex) for non-arXiv PDFs
- pix2tex is a local ViT model — NOT an LLM, no cloud calls

---

## 6. Implementation Plan for Recommended Approach

### Phase 1: arXiv Source Extraction (Approach B)
1. Add function to download arXiv source tar.gz
2. Extract .tex file from archive
3. Parse equation environments with regex:
   - `\begin{equation}...\end{equation}`
   - `\begin{align}...\end{align}`
   - `\begin{gather}...\end{gather}`
   - `\begin{eqnarray}...\end{eqnarray}`
4. Extract equation numbers from `\label{}` + `\tag{}`
5. Handle `\newcommand` macro expansion (basic)
6. Output JSON in desired format

### Phase 2: pix2tex Fallback (Approach A)
1. Add PyMuPDF equation region detection (font-based)
2. Crop equation regions as images
3. Run pix2tex on each cropped image
4. Extract equation numbers from text near the region
5. Output JSON

### Phase 3: Integration
1. Auto-detect if PDF is arXiv (from filename or metadata)
2. Route to Phase 1 or Phase 2 accordingly
3. Apply existing `extract_math_symbols()` to all results

---

## 7. Key Insight from Font Analysis

Our PyMuPDF font analysis of page 1 revealed the **exact structure** of equation (1):

```
y=398.7  CMSY10  |           ← opening ket bracket
y=398.9  CMR10   Ψ(          ← Psi and parenthesis
y=398.9  CMMI10  t           ← variable t
y=398.9  CMR10   )           ← closing paren
y=398.7  CMSY10  ⟩           ← closing ket
y=398.9  CMR10   =           ← equals
y=396.6  CMEX10  ∑ (as glyph)← summation (large operator)
y=412.7  CMMI7   n           ← subscript n
y=398.9  CMMI10  d           ← variable d
y=402.7  CMMI7   n           ← subscript n
y=398.9  CMR10   (0          ← opening paren + zero
y=397.1  CMR7    +           ← superscript +
y=398.9  CMR10   )           ← closing paren
y=398.9  CMMI10  e           ← exponential
y=397.0  CMSY7   −           ← superscript minus
y=397.1  CMMI7   iE          ← superscript iE
y=399.6  CMMI5   n           ← sub-subscript n
y=397.1  CMMI7   t           ← superscript t
y=398.7  CMSY10  |           ← opening ket
y=398.9  CMMI10  E           ← E
y=402.7  CMMI7   n           ← subscript n
y=398.7  CMSY10  ⟩           ← closing ket
y=398.9  CMMI10  ,           ← comma
y=398.9  CMR10   (1)         ← EQUATION NUMBER
```

This font data is GOLD for equation detection:
- **CMEX10** presence = display equation (large operators)
- **Subscript fonts** (CMMI7, CMMI5, CMR7 at different y) = structured math
- **`(N)` with CMR10** at right margin = equation number

---

## 8. Sources & References

- [PyMuPDF equation detection discussion](https://github.com/pymupdf/PyMuPDF/discussions/763)
- [pix2tex / LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) — ViT-based equation image → LaTeX
- [Nougat by Meta](https://github.com/facebookresearch/nougat) — full PDF → Markdown+LaTeX
- [latex-in-arxiv](https://github.com/allofphysicsgraph/latex-in-arxiv) — extract LaTeX math from arXiv sources
- [paper2tex](https://github.com/mrpositron/paper2tex) — ScanSSD + pix2tex pipeline
- [paperpipe](https://hummat.github.io/paperpipe/) — extract equations from research papers
- [Benchmarking Document Parsers on Math Formula Extraction](https://arxiv.org/pdf/2512.09874)
