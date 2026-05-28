#!/usr/bin/env python3
"""Audit previous appendix-only checklist-row representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-006. It checks every
Appendix-only checklist row from the checklist coverage matrix and confirms
that each row is represented in the self-contained guide plus internal guide
coverage.
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
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-appendix-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

APPENDIX_COVERAGE_TERMS = (
    "appendix",
    "reference",
    "service",
    "represented",
    "promoted",
    "placed",
    "complete",
    "staged",
    "redistributed",
    "route-resolution",
    "route resolution",
)

SHORT_NAME_ALLOWLIST = {"lod"}


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


def name_variants(value: str) -> set[str]:
    clean = value.replace("*", "").strip()
    variants = {clean}
    variants.add(re.sub(r"\([^)]*\)", "", clean).strip())
    variants.add(clean.replace("The ", "", 1).strip())
    return {variant for variant in variants if variant}


def guide_contains_name(guide_normalized: str, name: str) -> bool:
    for variant in name_variants(name):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4 and normalized_name not in SHORT_NAME_ALLOWLIST:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        if re.search(pattern, guide_normalized):
            return True
    return False


def split_source_refs(raw_value: str) -> list[str]:
    return [part.strip() for part in raw_value.split("|") if part.strip()]


def source_note_status(source_refs: list[str]) -> tuple[str, str]:
    if not source_refs:
        return ("no_refs", "")

    missing = [ref for ref in source_refs if not (SOURCE_NOTES_DIR / ref).exists()]
    if missing:
        return ("missing_refs", " | ".join(missing))
    return ("all_found", "")


def rows_have_appendix_coverage_signal(rows: list[dict[str, str]]) -> bool:
    blob = normalize(
        " ".join(
            " ".join(
                row.get(key, "")
                for key in (
                    "record_type",
                    "objective_name",
                    "coverage_status",
                    "player_facing_cue",
                    "player_facing_location",
                    "completion_status",
                    "notes",
                )
            )
            for row in rows
        )
    )
    return any(term in blob for term in APPENDIX_COVERAGE_TERMS)


def joined(values: set[str] | list[str], limit: int = 6) -> str:
    clean_values = sorted({value for value in values if value})
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def audit_status_for(
    exact_rows: list[dict[str, str]],
    mapped_objective_rows: list[dict[str, str]],
    guide_name_match: bool,
) -> tuple[str, str, str]:
    if exact_rows and guide_name_match and rows_have_appendix_coverage_signal(exact_rows):
        return ("appendix_row_covered", "none", "")

    if exact_rows and not guide_name_match:
        return (
            "internal_appendix_coverage_missing_guide_name",
            "add_player_facing_reference_name",
            "Exact checklist coverage exists, but the guide does not name this previous appendix-only row.",
        )

    if exact_rows:
        return (
            "internal_appendix_coverage_missing_signal",
            "add_internal_checklist_appendix_signal",
            "Exact checklist coverage exists, but it does not state the guide/reference treatment clearly.",
        )

    if mapped_objective_rows and guide_name_match and rows_have_appendix_coverage_signal(mapped_objective_rows):
        return ("appendix_row_covered_by_mapped_objective", "none", "")

    if mapped_objective_rows and guide_name_match:
        return (
            "mapped_objective_missing_appendix_signal",
            "add_internal_checklist_appendix_row",
            "Mapped objective coverage exists, but this checklist row needs exact guide-reference coverage.",
        )

    if guide_name_match:
        return (
            "guide_reference_missing_internal_coverage",
            "add_internal_checklist_appendix_row",
            "Guide names this previous appendix-only row; add exact internal checklist coverage.",
        )

    return (
        "appendix_row_missing_from_guide_and_coverage",
        "add_player_facing_reference_and_internal_coverage",
        "Add a self-contained guide reference plus exact internal checklist coverage.",
    )


def main() -> int:
    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    appendix_rows = [row for row in matrix_rows if row.get("mapping_type") == "Appendix-only checklist"]

    objective_ids = {row["objective_id"] for row in read_csv(OBJECTIVES_CSV)}

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

    for appendix_row in appendix_rows:
        checklist_id = appendix_row["checklist_id"]
        objective_id = appendix_row.get("objective_id", "")
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        source_refs = split_source_refs(appendix_row.get("source_note_refs", ""))
        source_status, missing_source_refs = source_note_status(source_refs)
        guide_name_match = guide_contains_name(guide_normalized, appendix_row["checklist_entry"])

        audit_status, recommended_action, notes = audit_status_for(
            exact_rows,
            mapped_objective_rows,
            guide_name_match,
        )

        combined_rows = exact_rows or mapped_objective_rows
        coverage_statuses = {row.get("coverage_status", "") for row in combined_rows}
        completion_statuses = {row.get("completion_status", "") for row in combined_rows}
        guide_locations = {row.get("player_facing_location", "") for row in combined_rows}

        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        output_rows.append(
            {
                "checklist_id": checklist_id,
                "checklist_tab": appendix_row["checklist_tab"],
                "checklist_entry": appendix_row["checklist_entry"],
                "category": appendix_row["category"],
                "objective_id": objective_id,
                "matched_objective_name": appendix_row.get("matched_objective_name", ""),
                "coverage_matrix_guide_location": appendix_row.get("guide_location", ""),
                "raw_group": appendix_row.get("raw_group", ""),
                "raw_detail": appendix_row.get("raw_detail", ""),
                "source_note_refs": " | ".join(source_refs),
                "source_note_status": source_status,
                "missing_source_refs": missing_source_refs,
                "guide_name_match": "Y" if guide_name_match else "N",
                "internal_checklist_coverage_row_count": str(len(exact_rows)),
                "internal_objective_coverage_row_count": str(len(mapped_objective_rows)),
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
        "objective_id",
        "matched_objective_name",
        "coverage_matrix_guide_location",
        "raw_group",
        "raw_detail",
        "source_note_refs",
        "source_note_status",
        "missing_source_refs",
        "guide_name_match",
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

    print(f"Wrote {len(output_rows)} appendix-only audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
