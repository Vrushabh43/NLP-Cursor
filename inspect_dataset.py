"""Inspect and validate the equations dataset interactively.

Usage
-----
    # Show summary
    python inspect_dataset.py

    # Show specific paper
    python inspect_dataset.py --paper 2506.17199

    # Show specific equation
    python inspect_dataset.py --paper 2506.17199 --eq 1

    # Validate dataset against assignment requirements
    python inspect_dataset.py --validate
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_dataset(path: Path) -> dict:
    """Load the dataset JSON file."""
    return json.loads(path.read_text(encoding="utf-8"))


def show_summary(data: dict) -> None:
    """Print a summary of the dataset."""
    total_eqs = sum(len(v) for v in data.values())
    papers_with = sum(1 for v in data.values() if v)
    papers_empty = sum(1 for v in data.values() if not v)

    meanings = sum(1 for eqs in data.values() for eq in eqs.values()
                   if len(eq.get("meaning", "")) > 10)
    total_syms = sum(len(eq.get("symbols", {}))
                     for eqs in data.values() for eq in eqs.values())
    syms_desc = sum(1 for eqs in data.values() for eq in eqs.values()
                    for v in eq.get("symbols", {}).values() if v)
    strong = sum(1 for eqs in data.values() for eq in eqs.values()
                 for r in eq.get("relations", {}).values()
                 if r.get("grade") == "strong")
    potential = sum(1 for eqs in data.values() for eq in eqs.values()
                    for r in eq.get("relations", {}).values()
                    if r.get("grade") == "potential")

    print("=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)
    print(f"Papers total:                {len(data)}")
    print(f"  With equations:            {papers_with}")
    print(f"  Empty:                     {papers_empty}")
    print(f"Total equations:             {total_eqs}")
    print(f"Meanings filled (>10 chars): {meanings}/{total_eqs} ({pct(meanings, total_eqs)})")
    print(f"Symbols total:               {total_syms}")
    print(f"  With descriptions:         {syms_desc}/{total_syms} ({pct(syms_desc, total_syms)})")
    print(f"Relations - strong:          {strong}")
    print(f"Relations - potential:        {potential}")
    print()

    print("PAPERS:")
    for i, (arxiv_id, eqs) in enumerate(data.items(), 1):
        count = len(eqs)
        marker = "  " if count > 0 else "  [empty]"
        print(f"  {i:3d}. arXiv:{arxiv_id} — {count} equations{marker}")


def show_paper(data: dict, arxiv_id: str) -> None:
    """Print all equations for a specific paper."""
    eqs = data.get(arxiv_id, {})
    if not eqs:
        print(f"No equations found for arXiv:{arxiv_id}")
        return

    print(f"\narXiv:{arxiv_id} — {len(eqs)} equations\n")
    for eq_num, eq in eqs.items():
        print(f"--- Equation ({eq_num}) ---")
        print(f"  LaTeX:    {eq['equation'][:100]}{'...' if len(eq['equation']) > 100 else ''}")
        print(f"  Meaning:  {eq['meaning'][:100]}")

        syms = eq.get("symbols", {})
        if syms:
            print(f"  Symbols:")
            for k, v in syms.items():
                print(f"    {k}: {v or '(no description)'}")

        rels = eq.get("relations", {})
        strong_rels = {k: v for k, v in rels.items() if v["grade"] == "strong"}
        pot_rels = {k: v for k, v in rels.items() if v["grade"] == "potential"}
        none_count = len(rels) - len(strong_rels) - len(pot_rels)
        print(f"  Relations: {len(strong_rels)} strong, {len(pot_rels)} potential, {none_count} none")
        for k, v in strong_rels.items():
            print(f"    -> ({k}): STRONG — {v['description']}")
        for k, v in pot_rels.items():
            print(f"    -> ({k}): POTENTIAL — {v['description']}")

        trail = eq.get("audit-trail", {})
        print(f"  Audit trail: {len(trail)} entries")
        print()


def show_equation(data: dict, arxiv_id: str, eq_num: str) -> None:
    """Print full details of a single equation."""
    eqs = data.get(arxiv_id, {})
    eq = eqs.get(eq_num)
    if not eq:
        print(f"Equation ({eq_num}) not found in arXiv:{arxiv_id}")
        return

    print(f"\narXiv:{arxiv_id} — Equation ({eq_num})\n")
    print(json.dumps(eq, indent=2, ensure_ascii=False))


def validate(data: dict) -> None:
    """Validate dataset against assignment requirements."""
    print("=" * 60)
    print("VALIDATION REPORT")
    print("=" * 60)
    total_eqs = sum(len(v) for v in data.values())
    errors = 0

    # Check 1: 350-356 equations
    if 350 <= total_eqs <= 356:
        print(f"[PASS] Total equations: {total_eqs} (target: 350-356)")
    elif total_eqs >= 350:
        print(f"[WARN] Total equations: {total_eqs} (slightly above 356)")
    else:
        print(f"[FAIL] Total equations: {total_eqs} (below 350)")
        errors += 1

    # Check 2: Max 7 per paper
    over_7 = [(k, len(v)) for k, v in data.items() if len(v) > 7]
    if not over_7:
        print(f"[PASS] Max 7 equations per paper")
    else:
        print(f"[FAIL] Papers with >7 equations: {over_7}")
        errors += 1

    # Check 3: Required fields
    missing_fields = []
    for arxiv_id, eqs in data.items():
        for eq_num, eq in eqs.items():
            for field in ["equation", "meaning", "symbols", "relations", "audit-trail"]:
                if field not in eq:
                    missing_fields.append(f"{arxiv_id}/{eq_num}/{field}")
    if not missing_fields:
        print(f"[PASS] All required fields present in all equations")
    else:
        print(f"[FAIL] Missing fields: {missing_fields[:5]}...")
        errors += 1

    # Check 4: Relations have all other equations
    bad_relations = []
    for arxiv_id, eqs in data.items():
        eq_nums = set(eqs.keys())
        for eq_num, eq in eqs.items():
            expected = eq_nums - {eq_num}
            actual = set(eq.get("relations", {}).keys())
            if expected != actual:
                bad_relations.append(f"{arxiv_id}/{eq_num}")
    if not bad_relations:
        print(f"[PASS] All equations have relations to all other equations in their paper")
    else:
        print(f"[FAIL] Incomplete relations: {bad_relations[:5]}...")
        errors += 1

    # Check 5: Relations have grade + description
    bad_grades = []
    for arxiv_id, eqs in data.items():
        for eq_num, eq in eqs.items():
            for other_num, rel in eq.get("relations", {}).items():
                if "grade" not in rel or "description" not in rel:
                    bad_grades.append(f"{arxiv_id}/{eq_num}->{other_num}")
                elif rel["grade"] not in ("none", "strong", "potential"):
                    bad_grades.append(f"{arxiv_id}/{eq_num}->{other_num}: bad grade '{rel['grade']}'")
    if not bad_grades:
        print(f"[PASS] All relations have valid grade and description")
    else:
        print(f"[FAIL] Bad relation entries: {bad_grades[:5]}...")
        errors += 1

    # Check 6: Audit trail exists
    no_trail = [f"{aid}/{en}" for aid, eqs in data.items()
                for en, eq in eqs.items() if not eq.get("audit-trail")]
    if not no_trail:
        print(f"[PASS] All equations have audit trails")
    else:
        print(f"[FAIL] Missing audit trails: {no_trail[:5]}...")
        errors += 1

    print()
    if errors == 0:
        print("ALL CHECKS PASSED")
    else:
        print(f"{errors} CHECK(S) FAILED")


def pct(a: int, b: int) -> str:
    return f"{100 * a / b:.0f}%" if b > 0 else "N/A"


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect the equations dataset.")
    parser.add_argument("--dataset", type=Path, default=Path("output/dataset.json"))
    parser.add_argument("--paper", type=str, default=None, help="Show a specific paper")
    parser.add_argument("--eq", type=str, default=None, help="Show a specific equation (requires --paper)")
    parser.add_argument("--validate", action="store_true", help="Run validation checks")
    args = parser.parse_args()

    data = load_dataset(args.dataset)

    if args.validate:
        validate(data)
    elif args.paper and args.eq:
        show_equation(data, args.paper, args.eq)
    elif args.paper:
        show_paper(data, args.paper)
    else:
        show_summary(data)


if __name__ == "__main__":
    main()
