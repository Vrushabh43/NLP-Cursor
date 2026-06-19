#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_PATH="${VENV_PATH:-.venv}"

echo "Creating virtual environment at ${VENV_PATH} ..."
"${PYTHON_BIN}" -m venv "${VENV_PATH}"

PYTHON_EXE="${VENV_PATH}/bin/python"
echo "Upgrading pip ..."
"${PYTHON_EXE}" -m pip install --upgrade pip

echo "Installing project dependencies ..."
"${PYTHON_EXE}" -m pip install -r requirements.txt

echo
echo "Environment is ready."
echo "Activate it with:"
echo "  source ${VENV_PATH}/bin/activate"
echo
echo "Example:"
echo "  ${PYTHON_EXE} pdf_equation_pipeline.py --paper-number 19 --output output/pdf/equations_pdf_server.json --report-output output/pdf/equations_pdf_server_report.json"
