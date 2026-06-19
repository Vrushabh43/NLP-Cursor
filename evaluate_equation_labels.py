"""Evaluate extracted equation labels against a reference annotation file.

This script is intentionally evaluation-only. It compares equation labels, not
equation LaTeX, meanings, symbols, or relations. Do not import it from the
extractor or use the reference file as extraction input.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_reference_labels(path: Path) -> dict[str, set[str]]:
    """Load paper -> equation-labels from an LLM-assisted reference file."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    papers = payload.get("papers", payload)
    return {
        arxiv_id: set(equations)
        for arxiv_id, equations in papers.items()
        if isinstance(equations, dict)
    }


def load_prediction_labels(path: Path) -> dict[str, set[str]]:
    """Load paper -> equation-labels from the pipeline output JSON."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        arxiv_id: set(equations)
        for arxiv_id, equations in payload.items()
        if isinstance(equations, dict)
    }


def build_label_report(
    reference: dict[str, set[str]],
    prediction: dict[str, set[str]],
) -> dict[str, Any]:
    """Build precision/recall-style metrics using labels only."""

    paper_ids = sorted(set(reference) | set(prediction))
    papers: dict[str, Any] = {}
    total_reference = 0
    total_predicted = 0
    total_matched = 0

    for arxiv_id in paper_ids:
        reference_labels = reference.get(arxiv_id, set())
        predicted_labels = prediction.get(arxiv_id, set())
        matched = reference_labels & predicted_labels
        missing = reference_labels - predicted_labels
        extra = predicted_labels - reference_labels

        total_reference += len(reference_labels)
        total_predicted += len(predicted_labels)
        total_matched += len(matched)

        papers[arxiv_id] = {
            "reference_count": len(reference_labels),
            "predicted_count": len(predicted_labels),
            "matched_count": len(matched),
            "missing_count": len(missing),
            "extra_count": len(extra),
            "matched_labels": sorted(matched),
            "missing_labels": sorted(missing),
            "extra_labels": sorted(extra),
        }

    precision = total_matched / total_predicted if total_predicted else 0.0
    recall = total_matched / total_reference if total_reference else 0.0
    return {
        "evaluation_type": "equation_label_only",
        "warning": (
            "Reference annotations are for evaluation and pattern learning only; "
            "they are not used by the extractor."
        ),
        "summary": {
            "paper_count": len(paper_ids),
            "reference_label_count": total_reference,
            "predicted_label_count": total_predicted,
            "matched_label_count": total_matched,
            "label_precision": round(precision, 4),
            "label_recall": round(recall, 4),
        },
        "papers": papers,
    }


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description="Evaluate extracted equation labels only.")
    parser.add_argument("--reference", type=Path, default=Path("annotation.json"))
    parser.add_argument(
        "--prediction",
        type=Path,
        default=Path("output/pdf/equations_pdf_pdf_only_server.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/pdf/equation_label_evaluation.json"),
    )
    return parser.parse_args()


def main() -> None:
    """Run label-only evaluation."""

    args = parse_args()
    report = build_label_report(
        load_reference_labels(args.reference),
        load_prediction_labels(args.prediction),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = report["summary"]
    print(
        "label evaluation: "
        f"matched={summary['matched_label_count']} "
        f"reference={summary['reference_label_count']} "
        f"predicted={summary['predicted_label_count']} "
        f"precision={summary['label_precision']} "
        f"recall={summary['label_recall']}"
    )


if __name__ == "__main__":
    main()
