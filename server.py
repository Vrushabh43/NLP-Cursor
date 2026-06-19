"""Simple Flask server for the equation extraction UI."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


@app.route("/")
def index():
    return send_from_directory(".", "viewer.html")


@app.route("/extract", methods=["POST"])
def extract():
    body = request.get_json(force=True)
    url = body.get("url", "").strip()

    # Parse arXiv ID from URL or raw ID.
    arxiv_id = None
    m = re.search(r"(\d{4}\.\d{4,5})", url)
    if m:
        arxiv_id = m.group(1)
    if not arxiv_id:
        return jsonify({"error": "Could not parse arXiv ID from input"}), 400

    out_path = OUTPUT_DIR / f"{arxiv_id}_equations.json"

    # Run the pipeline.
    result = subprocess.run(
        [
            sys.executable, "pdf_equation_pipeline.py",
            "--pdf-path", f"dummy_{arxiv_id}.pdf",  # triggers arxiv_id detection
            "--source", "tex",
            "--output", str(out_path),
            "--max-equations", "200",
            "--output-format", "simple",
        ],
        capture_output=True, text=True, timeout=60,
    )

    # The --pdf-path with dummy won't work for ID detection. Use direct API instead.
    # Fallback: call extraction functions directly.
    try:
        sys.path.insert(0, ".")
        from pdf_equation_pipeline import (
            download_arxiv_source,
            extract_math_symbols,
            extract_tex_from_source,
            format_simple_json,
            parse_equations_from_tex,
        )

        source_path = download_arxiv_source(
            arxiv_id, Path("data/pdf_cache"), sleep_seconds=1
        )
        tex = extract_tex_from_source(source_path)
        equations = parse_equations_from_tex(tex)
        payload = format_simple_json(equations)
        out_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return jsonify({"arxiv_id": arxiv_id, "count": len(payload), "equations": payload})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
