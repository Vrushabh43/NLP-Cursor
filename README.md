# PDF Math Equation Extractor

A Python pipeline that extracts numbered mathematical equations from arXiv research papers and outputs structured JSON with LaTeX code, equation numbers, and detected math symbols. **No LLM or cloud API required** -- runs entirely locally using open-source libraries.

---

## Table of Contents

1. [What It Does](#what-it-does)
2. [How It Works (Step by Step)](#how-it-works-step-by-step)
3. [Project Structure](#project-structure)
4. [Setup & Installation](#setup--installation)
5. [Usage](#usage)
6. [Output Format](#output-format)
7. [Web UI](#web-ui)
8. [Architecture Deep Dive](#architecture-deep-dive)
9. [Approaches Explored](#approaches-explored)
10. [Known Limitations](#known-limitations)

---

## What It Does

Given an arXiv paper URL or ID, this tool:

1. Downloads the LaTeX source from arXiv
2. Parses all numbered equation environments (`equation`, `align`, `multline`, `gather`, etc.)
3. Extracts the raw LaTeX code for each equation
4. Detects Unicode math symbols present in each equation
5. Outputs a clean JSON file with `{equation, number, mathsSymbol}` for every equation

### Example Output

```json
[
  {
    "equation": "|\\Psi(t)\\rangle = \\sum_{n} d_{n}(0^{+}) e^{-i E_{n}t}|E_n\\rangle,",
    "number": "1",
    "mathsSymbol": ["Psi", "sum", "rangle"]
  },
  {
    "equation": "\\overline{\\Delta A(t)^2} \\leq \\frac{||A||^2}{d_{eff}},",
    "number": "2",
    "mathsSymbol": ["Delta", "leq"]
  }
]
```

---

## How It Works (Step by Step)

### Step 1: Problem Analysis

We needed to extract math equations from PDF research papers. The challenge: PDFs are a **rendering format** (draw glyph X at pixel Y), not a semantic format. They have zero concept of "this is equation (1) in LaTeX."

### Step 2: Approaches Evaluated

We researched and tested 5 different approaches:

| Approach | How | Result |
|----------|-----|--------|
| **Docling + formula enrichment** | PDF -> ML model -> Markdown -> regex | 40+ minutes, too slow |
| **Docling without enrichment** | PDF -> Markdown | All equations become `<!-- formula-not-decoded -->` |
| **PyMuPDF text extraction** | PDF -> Unicode text | Gets text but NOT LaTeX (`sum` instead of `\sum`) |
| **PyMuPDF font analysis** | PDF -> font-tagged spans | Can DETECT equation regions via CM* fonts, but no LaTeX |
| **arXiv LaTeX source** | Download .tex -> parse environments | Perfect LaTeX in <2 seconds |

### Step 3: Chosen Approach -- arXiv .tex Source Parsing

Since arXiv papers have their original LaTeX source available for download, we bypass the PDF entirely:

```
arXiv ID --> Download .tar.gz source --> Extract .tex file
         --> Parse equation environments --> Extract LaTeX + numbers
         --> Detect math symbols --> JSON output
```

This gives us **100% accurate LaTeX** (it IS the original source code) in under 2 seconds.

### Step 4: LaTeX Environment Parsing

The parser handles all standard numbered equation environments:

**Single-number environments** (one number per block):
- `\begin{equation}...\end{equation}` -- standard display equation
- `\begin{multline}...\end{multline}` -- multi-line, single number

**Multi-row environments** (one number per `\\` row):
- `\begin{align}...\end{align}` -- aligned equations, each row numbered
- `\begin{gather}...\end{gather}` -- gathered equations, each row numbered
- `\begin{eqnarray}...\end{eqnarray}` -- legacy aligned equations
- `\begin{flalign}...\end{flalign}` -- full-width aligned
- `\begin{alignat}...\end{alignat}` -- custom-spaced aligned

Rows with `\nonumber` or `\notag` are correctly skipped.

**Appendix handling**: After `\appendix`, equation numbers reset per section and get letter prefixes (A1, A2, ..., B1, B2, ..., etc.).

### Step 5: Math Symbol Extraction

Each equation's LaTeX string is scanned with a **triple-pass** approach:

1. **Unicode character scan** -- find characters like `sum`, `int`, `leq`, `psi` etc. directly present in the string
2. **LaTeX command mapping** -- map `\sum` to `sum`, `\int` to `int`, `\leq` to `leq`, `\alpha` to `alpha`, etc. (90+ mappings)
3. **pylatexenc fallback** -- convert the full LaTeX string to text and scan for additional symbols

### Step 6: Web UI

A Flask server + HTML frontend provides a browser-based interface:
- Paste any arXiv URL or ID
- Click Extract
- View rendered equations (via MathJax) with equation numbers and symbols
- Switch to JSON tab to see/copy the raw output

---

## Project Structure

```
NLP-Cursor/
  pdf_equation_pipeline.py   # Core extraction engine (all logic)
  server.py                  # Flask web server for the UI
  viewer.html                # Browser frontend (MathJax rendering)
  requirements.txt           # Python dependencies
  paper_list_16.txt          # List of arXiv paper IDs (assignment)
  data/pdf_cache/            # Cached downloaded PDFs and source archives
  output/                    # Generated JSON output files
  docs/
    deep-analysis-equation-extraction.md  # Research & design analysis
```

### Key Files Explained

**`pdf_equation_pipeline.py`** (core engine):
- `download_arxiv_source()` -- downloads `.tar.gz` LaTeX source from arXiv
- `extract_tex_from_source()` -- extracts `.tex` file from tar.gz/gzip/bare archives
- `parse_equations_from_tex()` -- parses all equation environments with correct numbering
- `extract_math_symbols()` -- triple-pass symbol detection (Unicode + LaTeX commands + pylatexenc)
- `format_simple_json()` -- formats output as `{equation, number, mathsSymbol}`
- Also retains the original Docling-based pipeline as a fallback (`--source docling`)

**`server.py`** (web backend):
- `/` -- serves the HTML viewer
- `/extract` (POST) -- accepts `{"url": "..."}`, returns JSON with extracted equations

**`viewer.html`** (web frontend):
- Input bar for arXiv URL/ID
- "Equations" tab with MathJax-rendered equations, numbers, and symbol badges
- "JSON Preview" tab with raw JSON output

---

## Setup & Installation

### Prerequisites

- Python 3.9+
- macOS / Linux

### Install

```bash
# 1. Clone the repository
git clone <repo-url>
cd NLP-Cursor

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install pymupdf pylatexenc flask

# Optional: install docling for PDF-based fallback (heavy, ~1GB)
# pip install docling
```

### Dependencies

| Library | Purpose | Required? |
|---------|---------|-----------|
| `pymupdf` | PDF text/font extraction (for analysis) | For PDF analysis |
| `pylatexenc` | LaTeX <-> Unicode conversion for symbol extraction | Yes |
| `flask` | Web server for the browser UI | For UI only |
| `docling` | PDF -> Markdown conversion (alternative approach) | Optional fallback |

---

## Usage

### Command Line

```bash
# Activate virtual environment
source .venv/bin/activate

# Extract from an arXiv paper by ID (auto-downloads source)
python pdf_equation_pipeline.py \
  --pdf-path "2410.07429v2.pdf" \
  --source tex \
  --output output/equations.json \
  --max-equations 200

# Extract from paper list by number
python pdf_equation_pipeline.py \
  --paper-number 9 \
  --source tex \
  --output output/equations.json

# Use Docling fallback (slow, needs docling installed)
python pdf_equation_pipeline.py \
  --paper-number 9 \
  --source docling \
  --output output/equations.json \
  --enable-ocr
```

### CLI Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--pdf-path` | None | Path to local PDF (arXiv ID auto-detected from filename) |
| `--paper-number` | None | 1-based index into `paper_list_16.txt` |
| `--source` | `tex` | Extraction strategy: `tex` (fast, arXiv source) or `docling` (slow, any PDF) |
| `--output` | `output/pdf/equations_pdf.json` | Output JSON file path |
| `--output-format` | `simple` | `simple` for `{equation,number,mathsSymbol}` or `professor` for full schema |
| `--max-equations` | `7` | Maximum equations to extract |
| `--cache-dir` | `data/pdf_cache` | Cache directory for downloads |

### Web UI

```bash
source .venv/bin/activate
python server.py
# Open http://127.0.0.1:5001 in your browser
```

Then paste any arXiv URL or ID (e.g., `https://arxiv.org/abs/2410.07429` or just `2410.07427`) and click **Extract**.

---

## Output Format

### Simple Format (`--output-format simple`)

```json
[
  {
    "equation": "\\overline{\\Delta A(t)^2} \\leq \\frac{||A||^2}{d_{eff}},",
    "number": "2",
    "mathsSymbol": ["Delta", "leq"]
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| `equation` | string | Raw LaTeX source code of the equation |
| `number` | string | Equation label as it appears in the paper (e.g., "1", "A3", "C12") |
| `mathsSymbol` | string[] | Sorted list of unique Unicode math symbols detected |

### Professor Format (`--output-format professor`)

Nested by arXiv ID with additional fields: `meaning`, `symbols`, `relations`, `audit-trail`.

---

## Architecture Deep Dive

### Extraction Pipeline Flow

```
Input: arXiv URL/ID
          |
          v
[download_arxiv_source()]
  - GET https://arxiv.org/e-print/{id}
  - Save .tar.gz to data/pdf_cache/
          |
          v
[extract_tex_from_source()]
  - Try tar.gz extraction
  - Fallback: plain gzip
  - Fallback: bare .tex file
  - Pick largest .tex file as main document
          |
          v
[parse_equations_from_tex()]
  - Strip LaTeX comments (% ...)
  - Find \appendix and \section positions
  - Regex-match all equation environments
  - Single-number envs: 1 equation per block
  - Multi-row envs: split by \\, skip \nonumber rows
  - Auto-number: main body (1,2,3...) + appendix (A1,A2,...,B1,...)
          |
          v
[extract_math_symbols()]  (per equation)
  - Pass 1: Unicode char scan (60+ chars)
  - Pass 2: LaTeX command map (90+ commands)
  - Pass 3: pylatexenc conversion fallback
          |
          v
[format_simple_json()]
  - Map to {equation, number, mathsSymbol}
          |
          v
Output: JSON file
```

### Symbol Detection Dictionaries

**Unicode Math Symbols** (60+ characters):
- Operators: `sum`, `int`, `prod`, `partial`, `nabla`, `sqrt`
- Relations: `leq`, `geq`, `equiv`, `neq`, `approx`
- Greek: `alpha` through `omega`, `Gamma` through `Omega`
- Special: `infty`, `dagger`, `langle`, `rangle`, `hbar`

**LaTeX Command Mappings** (90+ commands):
- `\sum` -> `sum`, `\int` -> `int`, `\leq` -> `leq`
- `\alpha` -> `alpha`, `\beta` -> `beta`, `\psi` -> `psi`
- `\rightarrow` -> `->`, `\infty` -> `infty`, `\nabla` -> `nabla`

---

## Approaches Explored

During development, we researched and tested multiple approaches. Full analysis is in [`docs/deep-analysis-equation-extraction.md`](docs/deep-analysis-equation-extraction.md).

### Why Not Direct PDF Parsing?

We tested several PDF-based approaches and found fundamental limitations:

1. **PDF text layer loses structure**: Fractions become `a/b`, superscripts flatten, matrices collapse
2. **No LaTeX in PDFs**: The text layer stores rendered Unicode glyphs, not LaTeX commands
3. **Formula detection is unreliable**: While PyMuPDF font analysis (CMMI10, CMSY10 fonts) can detect WHERE equations are, it cannot reconstruct the LaTeX

### Why arXiv Source?

- arXiv papers are written in LaTeX and the source is publicly available
- Downloading the `.tex` file gives us the **exact original LaTeX** -- no reconstruction needed
- Parsing equation environments with regex is fast, reliable, and deterministic
- The entire pipeline runs in under 2 seconds per paper

### Alternative for Non-arXiv PDFs

For PDFs without LaTeX source, we recommend:
- **pix2tex** (LaTeX-OCR): Crop equation regions from the PDF as images, then use pix2tex's Vision Transformer to convert images to LaTeX
- **Nougat** (Meta): Full-page PDF-to-LaTeX conversion using neural OCR

These approaches are implemented in the codebase as future extensions.

---

## Known Limitations

1. **arXiv-only**: The `tex` source strategy requires arXiv papers with available LaTeX source. Non-arXiv PDFs need the Docling fallback or pix2tex (not yet integrated).

2. **Custom LaTeX macros**: Papers using `\newcommand` or `\def` for custom math macros will have those macros in the output LaTeX (unexpanded). This doesn't affect rendering but may affect downstream processing.

3. **Starred environments**: `equation*`, `align*` etc. are intentionally excluded since they produce unnumbered equations in LaTeX.

4. **Subequations**: Papers using `\begin{subequations}` with labels like (1a), (1b) are not yet handled -- they will be numbered sequentially instead of with sub-labels.

5. **Symbol detection coverage**: The symbol dictionaries cover 90+ common LaTeX commands. Rare or custom symbols may not be detected. The pylatexenc fallback catches most edge cases.

---

## Test Results

| Paper | Equations Found | Time |
|-------|----------------|------|
| `2410.07429` (Quantum physics, 9 pages) | 76 (22 main + 54 appendix) | ~2 sec |
| `2410.07427` (Machine learning, 30+ pages) | 104 (40 equation + 64 align rows) | ~2 sec |

---

## Credits

- **pylatexenc** -- LaTeX to Unicode conversion
- **PyMuPDF** -- PDF analysis and font detection
- **MathJax** -- Browser-based LaTeX rendering in the web UI
- **Flask** -- Lightweight web server
- **arXiv** -- Open access to research paper LaTeX sources
