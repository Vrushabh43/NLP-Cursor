#!/bin/bash
# One-command setup and run for the Equations Knowledge Graph project.
# Usage: bash run.sh

set -e

echo "=========================================="
echo "  Equations Knowledge Graph - Setup & Run"
echo "=========================================="
echo ""

# 1. Create virtual environment if not exists
if [ ! -d ".venv" ]; then
    echo "[1/5] Creating virtual environment..."
    python3 -m venv .venv
else
    echo "[1/5] Virtual environment exists."
fi

# 2. Activate and install dependencies
echo "[2/5] Installing dependencies..."
source .venv/bin/activate
pip install --quiet pymupdf pylatexenc flask

# 3. Build dataset (350+ equations)
if [ ! -f "output/dataset.json" ]; then
    echo "[3/5] Building dataset (this takes ~5 minutes)..."
    python build_dataset.py
else
    echo "[3/5] Dataset already exists ($(python -c "import json; print(sum(len(v) for v in json.load(open('output/dataset.json')).values()))") equations)."
fi

# 4. Validate
echo "[4/5] Validating dataset..."
python inspect_dataset.py --validate

# 5. Start web UI
echo ""
echo "[5/5] Starting web server..."
echo "=========================================="
echo "  Open http://127.0.0.1:5001 in browser"
echo "=========================================="
echo ""
python server.py
