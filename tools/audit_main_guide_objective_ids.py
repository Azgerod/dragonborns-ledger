#!/usr/bin/env python3
"""Audit objective-ID representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-001. It compares every
objective row against the player-facing guide and the internal guide coverage
ledger, then writes a reviewable CSV with the representation status and next
action.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OBJECTIVES_CSV = REPO_ROOT / "data" / "objectives" / "objectives.csv"
GUIDE_COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-id-audit.csv"

OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

GENERIC_NAME_MATCHES = {
    "black book",
    "thief",
    "fishing",
    "hendraheim",
    "myrwatch",
}


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    lowered = ascii_value.lower()
    compact = re.sub(r"[^a-z0-9]+", " ", lowered).strip()
    return re.sub(r"\s+", " ", compact)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def expand_objective_refs(raw_value: str, valid_ids: set[str]) -> list[str]:
    raw_value = raw_value.strip()
    if not raw_value:
        return []

    ids = OBJECTIVE_ID_RE.findall(raw_value)
    if len(ids) == 2 and OBJECTIVE_RANGE_RE.search(raw_value):
        start, end = (int(ids[0][-6:]), int(ids[1][-6:]))
        if start <= end:
            return [f"OBJ-{number:06d}" for number in range(start, end + 1) if f"OBJ-{number:06d}" in valid_ids]

    return [objective_id for objective_id in ids if objective_id in valid_ids]


def guide_contains_name(guide_normalized: str, objective_name: str) -> bool:
    normalized_name = normalize(objective_name)
    if len(normalized_name) < 4 or normalized_name in GENERIC_NAME_MATCHES:
        return False
    pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
    return re.search(pattern, guide_normalized) is not None


def joined(values: set[str], limit: int = 6) -> str:
    clean_values = sorted(value for value in values if value)
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def main() -> int:
    objectives = read_csv(OBJECTIVES_CSV)
    objective_by_id = {row["objective_id"]: row for row in objectives}
    valid_ids = set(objective_by_id)

    guide_text = MAIN_GUIDE.read_text(encoding="utf-8")
    guide_normalized = normalize(guide_text)

    coverage_by_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(GUIDE_COVERAGE_CSV):
        for objective_id in expand_objective_refs(row.get("objective_id", ""), valid_ids):
            coverage_by_id[objective_id].append(row)

    output_rows: list[dict[str, str]] = []
    status_counts: Counter[str] = Counter()
    action_counts: Counter[str] = Counter()

    for objective in objectives:
        objective_id = objective["objective_id"]
        coverage_rows = coverage_by_id.get(objective_id, [])
        guide_id_match = objective_id in guide_text
        guide_name_match = guide_contains_name(guide_normalized, objective["objective_name"])

        coverage_statuses = {row.get("coverage_status", "") for row in coverage_rows}
        completion_statuses = {row.get("completion_status", "") for row in coverage_rows}
        guide_locations = {row.get("player_facing_location", "") for row in coverage_rows}

        if coverage_rows:
            audit_status = "covered_by_internal_coverage"
            recommended_action = "none"
        elif guide_id_match:
            audit_status = "guide_explicit_id_missing_internal_coverage"
            recommended_action = "add_internal_coverage_row"
        elif guide_name_match:
            audit_status = "guide_name_match_missing_internal_coverage"
            recommended_action = "confirm_name_match_and_add_internal_coverage_row"
        else:
            audit_status = "not_found_in_guide_or_internal_coverage"
            recommended_action = "targeted_guide_or_coverage_repair"

        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        output_rows.append(
            {
                "objective_id": objective_id,
                "objective_name": objective["objective_name"],
                "category": objective["category"],
                "subcategory": objective["subcategory"],
                "route_placement": objective["route_placement"],
                "guide_literal_id_match": "Y" if guide_id_match else "N",
                "guide_name_match": "Y" if guide_name_match else "N",
                "internal_coverage_row_count": str(len(coverage_rows)),
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "recommended_action": recommended_action,
                "notes": (
                    "Name matches are mechanical and need human confirmation."
                    if audit_status == "guide_name_match_missing_internal_coverage"
                    else ""
                ),
            }
        )

    fieldnames = [
        "objective_id",
        "objective_name",
        "category",
        "subcategory",
        "route_placement",
        "guide_literal_id_match",
        "guide_name_match",
        "internal_coverage_row_count",
        "audit_status",
        "coverage_statuses",
        "completion_statuses",
        "guide_locations",
        "recommended_action",
        "notes",
    ]

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} objective audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
