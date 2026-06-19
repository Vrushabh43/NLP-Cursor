#!/usr/bin/env bash
set -euo pipefail

PYTHON_EXE="${PYTHON_EXE:-.venv/bin/python}"
OUTPUT_JSON="${OUTPUT_JSON:-output/pdf/equations_pdf_pdf_only_server.json}"
REPORT_JSON="${REPORT_JSON:-output/pdf/equations_pdf_pdf_only_server_report.json}"
MARKDOWN_DIR="${MARKDOWN_DIR:-output/pdf/docling_markdown_server}"

# PDF-only papers identified in the first 70 entries of paper_list_16.txt.
PDF_ONLY_PAPERS=(9 19 27 37 40 41 47 53 54 55 57 58 59 67 69)

mkdir -p "$(dirname "${OUTPUT_JSON}")" "$(dirname "${REPORT_JSON}")" "${MARKDOWN_DIR}"
rm -f "${OUTPUT_JSON}" "${REPORT_JSON}"

for PAPER_NUMBER in "${PDF_ONLY_PAPERS[@]}"; do
  echo "Processing paper ${PAPER_NUMBER} ..."
  "${PYTHON_EXE}" pdf_equation_pipeline.py \
    --paper-number "${PAPER_NUMBER}" \
    --sleep-seconds 3 \
    --output "${OUTPUT_JSON}" \
    --report-output "${REPORT_JSON}" \
    --merge \
    --save-docling-markdown "${MARKDOWN_DIR}/paper_${PAPER_NUMBER}_docling.md"
done

echo
echo "Done."
echo "Dataset: ${OUTPUT_JSON}"
echo "QA report: ${REPORT_JSON}"
