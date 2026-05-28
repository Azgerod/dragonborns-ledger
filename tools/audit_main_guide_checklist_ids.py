#!/usr/bin/env python3
"""Audit checklist-row representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-002. It compares every
coverage-matrix row against the player-facing guide and the internal guide
coverage ledger, then writes a reviewable CSV with representation status and
the next cross-cutting action.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MATRIX_CSV = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"
GUIDE_COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVES_CSV = REPO_ROOT / "data" / "objectives" / "objectives.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-checklist-id-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

GENERIC_ENTRY_MATCHES = {
    "armor",
    "black book",
    "boots",
    "bow",
    "dagger",
    "damage health",
    "damage magicka",
    "damage stamina",
    "fishing",
    "gauntlets",
    "helmet",
    "hunting bow",
    "sword",
    "thief",
}

MAPPING_ACTIONS = {
    "Branch-route prototype": "defer_to_TB-035-COV-003_branch_audit",
    "Option-list note": "defer_to_TB-035-COV-004_option_default_audit",
    "Explicit exclusion": "defer_to_TB-035-COV-005_exclusion_audit",
    "Appendix-only checklist": "defer_to_TB-035-COV-006_appendix_to_guide_audit",
}


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    lowered = ascii_value.lower()
    compact = re.sub(r"[^a-z0-9]+", " ", lowered).strip()
    return re.sub(r"\s+", " ", compact)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def expand_checklist_refs(raw_value: str, valid_ids: set[str]) -> list[str]:
    raw_value = raw_value.strip()
    if not raw_value:
        return []

    ids: set[str] = set()
    for match in CHECKLIST_RANGE_RE.finditer(raw_value):
        prefix, start_raw, end_raw = match.groups()
        start, end = int(start_raw), int(end_raw)
        if start <= end:
            for number in range(start, end + 1):
                checklist_id = f"{prefix}{number:04d}"
                if checklist_id in valid_ids:
                    ids.add(checklist_id)

    for checklist_id in CHECKLIST_ID_RE.findall(raw_value):
        if checklist_id in valid_ids:
            ids.add(checklist_id)

    return sorted(ids)


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


def guide_contains_entry(guide_normalized: str, checklist_entry: str) -> bool:
    normalized_entry = normalize(checklist_entry.replace("*", ""))
    if len(normalized_entry) < 4 or normalized_entry in GENERIC_ENTRY_MATCHES:
        return False
    pattern = rf"(?<![a-z0-9]){re.escape(normalized_entry)}(?![a-z0-9])"
    return re.search(pattern, guide_normalized) is not None


def joined(values: set[str], limit: int = 6) -> str:
    clean_values = sorted(value for value in values if value)
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def recommended_action_for(mapping_type: str, audit_status: str) -> str:
    if audit_status in {
        "covered_by_internal_checklist_coverage",
        "covered_by_mapped_objective_internal_coverage",
    }:
        return "none"

    if mapping_type in MAPPING_ACTIONS:
        return MAPPING_ACTIONS[mapping_type]

    if audit_status == "guide_entry_match_missing_internal_coverage":
        return "confirm_entry_match_and_add_internal_coverage_row"

    return "targeted_guide_or_coverage_repair"


def main() -> int:
    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}

    objective_rows = read_csv(OBJECTIVES_CSV)
    objective_ids = {row["objective_id"] for row in objective_rows}

    guide_text = MAIN_GUIDE.read_text(encoding="utf-8")
    guide_normalized = normalize(guide_text)

    coverage_by_checklist_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    coverage_by_objective_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(GUIDE_COVERAGE_CSV):
        raw_id = row.get("objective_id", "")
        for checklist_id in expand_checklist_refs(raw_id, checklist_ids):
            coverage_by_checklist_id[checklist_id].append(row)
        for objective_id in expand_objective_refs(raw_id, objective_ids):
            coverage_by_objective_id[objective_id].append(row)

    output_rows: list[dict[str, str]] = []
    status_counts: Counter[str] = Counter()
    action_counts: Counter[str] = Counter()

    for matrix_row in matrix_rows:
        checklist_id = matrix_row["checklist_id"]
        objective_id = matrix_row.get("objective_id", "")
        checklist_coverage_rows = coverage_by_checklist_id.get(checklist_id, [])
        objective_coverage_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []

        guide_checklist_id_match = checklist_id in guide_text
        guide_objective_id_match = bool(objective_id and objective_id in guide_text)
        guide_entry_match = guide_contains_entry(guide_normalized, matrix_row["checklist_entry"])

        combined_coverage_rows = checklist_coverage_rows or objective_coverage_rows
        coverage_statuses = {row.get("coverage_status", "") for row in combined_coverage_rows}
        completion_statuses = {row.get("completion_status", "") for row in combined_coverage_rows}
        guide_locations = {row.get("player_facing_location", "") for row in combined_coverage_rows}

        if checklist_coverage_rows:
            audit_status = "covered_by_internal_checklist_coverage"
        elif objective_coverage_rows:
            audit_status = "covered_by_mapped_objective_internal_coverage"
        elif guide_checklist_id_match:
            audit_status = "guide_explicit_checklist_id_missing_internal_coverage"
        elif guide_objective_id_match:
            audit_status = "guide_explicit_objective_id_missing_internal_coverage"
        elif guide_entry_match:
            audit_status = "guide_entry_match_missing_internal_coverage"
        else:
            audit_status = "not_found_in_guide_or_internal_coverage"

        recommended_action = recommended_action_for(matrix_row["mapping_type"], audit_status)
        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        notes = ""
        if audit_status == "guide_entry_match_missing_internal_coverage":
            notes = "Entry-name matches are mechanical and need human confirmation."
        elif recommended_action.startswith("defer_to_"):
            notes = "Rows in this mapping bucket are handled by the named focused cross-cutting audit."

        output_rows.append(
            {
                "checklist_id": checklist_id,
                "checklist_tab": matrix_row["checklist_tab"],
                "checklist_entry": matrix_row["checklist_entry"],
                "category": matrix_row["category"],
                "mapping_type": matrix_row["mapping_type"],
                "coverage_matrix_status": matrix_row["status"],
                "objective_id": objective_id,
                "matched_objective_name": matrix_row.get("matched_objective_name", ""),
                "guide_literal_checklist_id_match": "Y" if guide_checklist_id_match else "N",
                "guide_mapped_objective_id_match": "Y" if guide_objective_id_match else "N",
                "guide_entry_match": "Y" if guide_entry_match else "N",
                "internal_checklist_coverage_row_count": str(len(checklist_coverage_rows)),
                "internal_objective_coverage_row_count": str(len(objective_coverage_rows)),
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "recommended_action": recommended_action,
                "notes": notes,
            }
        )

    fieldnames = [
        "checklist_id",
        "checklist_tab",
        "checklist_entry",
        "category",
        "mapping_type",
        "coverage_matrix_status",
        "objective_id",
        "matched_objective_name",
        "guide_literal_checklist_id_match",
        "guide_mapped_objective_id_match",
        "guide_entry_match",
        "internal_checklist_coverage_row_count",
        "internal_objective_coverage_row_count",
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

    print(f"Wrote {len(output_rows)} checklist audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
