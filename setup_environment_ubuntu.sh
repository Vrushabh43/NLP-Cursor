#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_PATH="${VENV_PATH:-.venv}"
MODEL_CACHE_DIR="${MODEL_CACHE_DIR:-.cache/model_cache}"
FORCE_CPU="${FORCE_CPU:-1}"

export HF_HOME="${PWD}/${MODEL_CACHE_DIR}/huggingface"
export HF_HUB_CACHE="${HF_HOME}/hub"
export HUGGINGFACE_HUB_CACHE="${HF_HOME}/hub"
export TRANSFORMERS_CACHE="${PWD}/${MODEL_CACHE_DIR}/transformers"
export XDG_CACHE_HOME="${PWD}/${MODEL_CACHE_DIR}/xdg"
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
if [[ "${FORCE_CPU}" == "1" ]]; then
  export CUDA_VISIBLE_DEVICES=""
fi
mkdir -p "${HF_HOME}" "${HF_HUB_CACHE}" "${TRANSFORMERS_CACHE}" "${XDG_CACHE_HOME}"

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
echo
echo "Batch run defaults to FORCE_CPU=1 to avoid small-GPU CUDA OOM."
echo "To try GPU anyway:"
echo "  FORCE_CPU=0 bash run_pdf_only_batch_ubuntu.sh"
