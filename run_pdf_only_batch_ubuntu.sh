#!/usr/bin/env bash
set -euo pipefail

PYTHON_EXE="${PYTHON_EXE:-.venv/bin/python}"
OUTPUT_JSON="${OUTPUT_JSON:-output/pdf/equations_pdf_pdf_only_server.json}"
REPORT_JSON="${REPORT_JSON:-output/pdf/equations_pdf_pdf_only_server_report.json}"
MARKDOWN_DIR="${MARKDOWN_DIR:-output/pdf/docling_markdown_server}"
MODEL_CACHE_DIR="${MODEL_CACHE_DIR:-.cache/model_cache}"
FORCE_CPU="${FORCE_CPU:-}"
DEVICE_POLICY="${DEVICE_POLICY:-auto}"
GPU_MAX_PAGES="${GPU_MAX_PAGES:-10}"
GPU_MAX_MB="${GPU_MAX_MB:-20}"
LABEL_SCOPE="${LABEL_SCOPE:-all}"
REUSE_MARKDOWN="${REUSE_MARKDOWN:-0}"
MAX_EQUATIONS="${MAX_EQUATIONS:-200}"
PAGE_RETRY="${PAGE_RETRY:-0}"
STRICT_PDF_FALLBACK="${STRICT_PDF_FALLBACK:-1}"

export HF_HOME="${PWD}/${MODEL_CACHE_DIR}/huggingface"
export HF_HUB_CACHE="${HF_HOME}/hub"
export HUGGINGFACE_HUB_CACHE="${HF_HOME}/hub"
export TRANSFORMERS_CACHE="${PWD}/${MODEL_CACHE_DIR}/transformers"
export XDG_CACHE_HOME="${PWD}/${MODEL_CACHE_DIR}/xdg"
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
if [[ "${FORCE_CPU}" == "1" ]]; then
  DEVICE_POLICY="cpu"
  echo "FORCE_CPU=1: using CPU device policy."
elif [[ "${FORCE_CPU}" == "0" ]]; then
  DEVICE_POLICY="gpu"
  echo "FORCE_CPU=0: using GPU device policy."
fi
mkdir -p "${HF_HOME}" "${HF_HUB_CACHE}" "${TRANSFORMERS_CACHE}" "${XDG_CACHE_HOME}"
echo "Docling device policy: ${DEVICE_POLICY} (GPU thresholds: pages<=${GPU_MAX_PAGES}, size<=${GPU_MAX_MB}MB)"

# PDF-only papers identified in the first 70 entries of paper_list_16.txt.
if [[ -n "${PDF_ONLY_PAPERS_OVERRIDE:-}" ]]; then
  read -r -a PDF_ONLY_PAPERS <<< "${PDF_ONLY_PAPERS_OVERRIDE}"
else
  PDF_ONLY_PAPERS=(9 19 27 37 40 41 47 53 54 55 57 58 59 67 69)
fi

mkdir -p "$(dirname "${OUTPUT_JSON}")" "$(dirname "${REPORT_JSON}")" "${MARKDOWN_DIR}"
rm -f "${OUTPUT_JSON}" "${REPORT_JSON}"

for PAPER_NUMBER in "${PDF_ONLY_PAPERS[@]}"; do
  echo "Processing paper ${PAPER_NUMBER} ..."
  MARKDOWN_FILE="${MARKDOWN_DIR}/paper_${PAPER_NUMBER}_docling.md"
  EXTRA_ARGS=()
  if [[ "${PAGE_RETRY}" != "1" ]]; then
    EXTRA_ARGS+=(--disable-page-retry)
  fi
  if [[ "${STRICT_PDF_FALLBACK}" == "1" ]]; then
    EXTRA_ARGS+=(--strict-pdf-fallback)
  fi
  if [[ "${REUSE_MARKDOWN}" == "1" && -s "${MARKDOWN_FILE}" ]]; then
    echo "Reusing cached Docling Markdown: ${MARKDOWN_FILE}"
    EXTRA_ARGS+=(--docling-markdown-input "${MARKDOWN_FILE}")
  fi
  "${PYTHON_EXE}" pdf_equation_pipeline.py \
    --paper-number "${PAPER_NUMBER}" \
    --max-equations "${MAX_EQUATIONS}" \
    --device-policy "${DEVICE_POLICY}" \
    --gpu-max-pages "${GPU_MAX_PAGES}" \
    --gpu-max-mb "${GPU_MAX_MB}" \
    --sleep-seconds 3 \
    --output "${OUTPUT_JSON}" \
    --report-output "${REPORT_JSON}" \
    --merge \
    --label-scope "${LABEL_SCOPE}" \
    --save-docling-markdown "${MARKDOWN_FILE}" \
    "${EXTRA_ARGS[@]}"
done

echo
echo "Done."
echo "Dataset: ${OUTPUT_JSON}"
echo "QA report: ${REPORT_JSON}"
