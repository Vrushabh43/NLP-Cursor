"""Flask server for the equation extraction UI and dataset browser."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

sys.path.insert(0, ".")

app = Flask(__name__)
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


@app.route("/")
def index():
    return send_from_directory(".", "viewer.html")


@app.route("/extract", methods=["POST"])
def extract():
    """Extract equations from a single arXiv paper (full format)."""
    body = request.get_json(force=True)
    url = body.get("url", "").strip()

    m = re.search(r"(\d{4}\.\d{4,5})", url)
    if not m:
        return jsonify({"error": "Could not parse arXiv ID from input"}), 400
    arxiv_id = m.group(1)

    try:
        from build_dataset import process_paper
        entry, count = process_paper(
            arxiv_id, Path("data/pdf_cache"), max_equations=7, sleep_seconds=1
        )
        return jsonify({"arxiv_id": arxiv_id, "count": count, "equations": entry})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/dataset", methods=["GET"])
def dataset():
    """Serve the full pre-built dataset summary."""
    dataset_path = OUTPUT_DIR / "dataset.json"
    if not dataset_path.exists():
        return jsonify({"error": "Dataset not built yet. Run build_dataset.py first."}), 404
    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    summary = []
    for arxiv_id, eqs in data.items():
        summary.append({"arxiv_id": arxiv_id, "count": len(eqs)})
    total = sum(len(v) for v in data.values())
    return jsonify({"papers": len(data), "total_equations": total, "summary": summary})


@app.route("/dataset/<arxiv_id>", methods=["GET"])
def dataset_paper(arxiv_id):
    """Serve full equations for a paper from the pre-built dataset."""
    dataset_path = OUTPUT_DIR / "dataset.json"
    if not dataset_path.exists():
        return jsonify({"error": "Dataset not built yet."}), 404
    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    if arxiv_id not in data:
        return jsonify({"error": f"Paper {arxiv_id} not in dataset"}), 404
    return jsonify({"arxiv_id": arxiv_id, "count": len(data[arxiv_id]), "equations": data[arxiv_id]})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
