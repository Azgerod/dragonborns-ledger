#!/usr/bin/env python3
"""Validate the generated checklist coverage matrix.

This is a structural contract check for the TB-030/TB-031 checklist
coverage matrix. It does not decide gameplay scope; rows that still need
source/objective/support-table readiness work must be explicit, typed, and
carried forward by status.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MATRIX = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"

REQUIRED_COLUMNS = [
    "checklist_id",
    "checklist_tab",
    "checklist_entry",
    "category",
    "mapping_type",
    "guide_location",
    "branch_name",
    "exclusion_reason",
    "source_note_refs",
    "status",
    "notes",
    "objective_id",
    "matched_objective_name",
    "route_block",
    "disposition",
    "prototype_status",
    "deferred_to",
    "match_status",
    "match_source",
    "raw_sheet_row",
    "raw_cell",
    "raw_group",
    "raw_status",
    "raw_detail",
]

KNOWN_CHECKLIST_TABS = {
    "Quests",
    "Enchanting Effects",
    "Spells",
    "Dragon Shouts",
    "Locations",
    "Merchants",
    "Unique Gear",
    "Books",
    "Collectible Items",
    "Recruitable Followers",
    "Learned Alchemy Effects",
    "Perks",
}

ALLOWED_MAPPING_TYPES = {
    "Main-route prototype block",
    "Branch-route prototype",
    "Option-list note",
    "Appendix-only checklist",
    "Explicit exclusion",
    "Source-readiness hold",
}

ALLOWED_STATUS_VALUES = {
    "mapped_to_route_prototype",
    "mapped_to_branch_prototype",
    "mapped_to_option_list",
    "mapped_to_appendix",
    "excluded_with_justification",
    "source_readiness_required",
}

EXPECTED_STATUS_BY_MAPPING_TYPE = {
    "Main-route prototype block": {"mapped_to_route_prototype"},
    "Branch-route prototype": {"mapped_to_branch_prototype"},
    "Option-list note": {"mapped_to_option_list"},
    "Appendix-only checklist": {"mapped_to_appendix"},
    "Explicit exclusion": {"excluded_with_justification"},
    "Source-readiness hold": {"source_readiness_required"},
}

ALLOWED_MATCH_STATUSES = {"matched", "support_table_only", "unmatched"}

CHECKLIST_ID_RE = re.compile(r"^CHK-[A-Z0-9-]+-\d{4}$")
EXCEL_CELL_RE = re.compile(r"^[A-Z]+[1-9][0-9]*$")
OBJECTIVE_ID_RE = re.compile(r"^OBJ-\d{6}$")
ROUTE_BLOCK_RE = re.compile(r"^G(?:0[0-9]|1[0-4])$")
SOURCE_NOTE_RE = re.compile(r"^SN-\d{6}(?:-[A-Za-z0-9_.-]+\.md)?$")


def value(row: dict[str, str], column: str) -> str:
    return (row.get(column) or "").strip()


def is_blank(row: dict[str, str], column: str) -> bool:
    return value(row, column) == ""


def tab_slug(tab: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "-", tab.upper()).strip("-")


def split_pipe_refs(raw_value: str) -> list[str]:
    if not raw_value.strip():
        return []
    return [part.strip() for part in raw_value.split("|") if part.strip()]


def add_error(errors: list[str], line_number: int, checklist_id: str, message: str) -> None:
    row_label = checklist_id or "<blank checklist_id>"
    errors.append(f"line {line_number} {row_label}: {message}")


def validate_row(
    row: dict[str, str],
    line_number: int,
    seen_checklist_ids: set[str],
    errors: list[str],
) -> None:
    checklist_id = value(row, "checklist_id")
    checklist_tab = value(row, "checklist_tab")
    mapping_type = value(row, "mapping_type")
    status = value(row, "status")
    match_status = value(row, "match_status")
    objective_id = value(row, "objective_id")
    source_note_refs = value(row, "source_note_refs")

    for column in [
        "checklist_id",
        "checklist_tab",
        "checklist_entry",
        "category",
        "mapping_type",
        "status",
        "notes",
        "raw_sheet_row",
        "raw_cell",
        "raw_status",
    ]:
        if is_blank(row, column):
            add_error(errors, line_number, checklist_id, f"{column} is required")

    if checklist_id:
        if checklist_id in seen_checklist_ids:
            add_error(errors, line_number, checklist_id, "duplicate checklist_id")
        seen_checklist_ids.add(checklist_id)

        if not CHECKLIST_ID_RE.match(checklist_id):
            add_error(errors, line_number, checklist_id, "checklist_id has invalid format")
        elif checklist_tab:
            expected_prefix = f"CHK-{tab_slug(checklist_tab)}-"
            if not checklist_id.startswith(expected_prefix):
                add_error(
                    errors,
                    line_number,
                    checklist_id,
                    f"checklist_id prefix does not match checklist_tab {checklist_tab!r}",
                )

    if checklist_tab and checklist_tab not in KNOWN_CHECKLIST_TABS:
        add_error(errors, line_number, checklist_id, f"unknown checklist_tab {checklist_tab!r}")

    if mapping_type not in ALLOWED_MAPPING_TYPES:
        add_error(errors, line_number, checklist_id, f"unknown mapping_type {mapping_type!r}")

    if status not in ALLOWED_STATUS_VALUES:
        add_error(errors, line_number, checklist_id, f"unknown status {status!r}")
    elif mapping_type in EXPECTED_STATUS_BY_MAPPING_TYPE:
        expected_statuses = EXPECTED_STATUS_BY_MAPPING_TYPE[mapping_type]
        if status not in expected_statuses:
            add_error(
                errors,
                line_number,
                checklist_id,
                f"status {status!r} is inconsistent with mapping_type {mapping_type!r}",
            )

    if match_status not in ALLOWED_MATCH_STATUSES:
        add_error(errors, line_number, checklist_id, f"unknown match_status {match_status!r}")

    raw_sheet_row = value(row, "raw_sheet_row")
    if raw_sheet_row and (not raw_sheet_row.isdigit() or int(raw_sheet_row) < 1):
        add_error(errors, line_number, checklist_id, "raw_sheet_row must be a positive integer")

    raw_cell = value(row, "raw_cell")
    if raw_cell and not EXCEL_CELL_RE.match(raw_cell):
        add_error(errors, line_number, checklist_id, f"raw_cell has invalid format {raw_cell!r}")

    if objective_id and not OBJECTIVE_ID_RE.match(objective_id):
        add_error(errors, line_number, checklist_id, f"objective_id has invalid format {objective_id!r}")

    route_block = value(row, "route_block")
    if route_block and not ROUTE_BLOCK_RE.match(route_block):
        add_error(errors, line_number, checklist_id, f"route_block has invalid format {route_block!r}")

    for source_ref in split_pipe_refs(source_note_refs):
        if not SOURCE_NOTE_RE.match(source_ref):
            add_error(errors, line_number, checklist_id, f"source_note_ref has invalid format {source_ref!r}")

    guide_location = value(row, "guide_location")
    if not guide_location:
        add_error(errors, line_number, checklist_id, f"{status} rows require guide_location")

    branch_name = value(row, "branch_name")
    if status == "mapped_to_branch_prototype":
        if not branch_name:
            add_error(errors, line_number, checklist_id, "branch prototype rows require branch_name")
    elif branch_name:
        add_error(errors, line_number, checklist_id, f"{status} rows must not have branch_name")

    exclusion_reason = value(row, "exclusion_reason")
    if status == "excluded_with_justification":
        if guide_location != "excluded":
            add_error(errors, line_number, checklist_id, "excluded rows must use guide_location=excluded")
        if not exclusion_reason:
            add_error(errors, line_number, checklist_id, "excluded rows require exclusion_reason")
    elif exclusion_reason:
        add_error(errors, line_number, checklist_id, f"{status} rows must not have exclusion_reason")

    matched_objective_name = value(row, "matched_objective_name")
    match_source = value(row, "match_source")
    if match_status == "matched":
        if not objective_id:
            add_error(errors, line_number, checklist_id, "matched rows require objective_id")
        if not matched_objective_name:
            add_error(errors, line_number, checklist_id, "matched rows require matched_objective_name")
        if not source_note_refs:
            add_error(errors, line_number, checklist_id, "matched rows require source_note_refs")
        if not match_source:
            add_error(errors, line_number, checklist_id, "matched rows require match_source")
    elif match_status == "support_table_only":
        if objective_id or matched_objective_name:
            add_error(errors, line_number, checklist_id, "support_table_only rows must not have objective fields")
        if not match_source:
            add_error(errors, line_number, checklist_id, "support_table_only rows require match_source")
    elif match_status == "unmatched":
        add_error(errors, line_number, checklist_id, "unmatched rows are not allowed after TB-031B")
        for column in ["objective_id", "matched_objective_name", "source_note_refs", "match_source"]:
            if not is_blank(row, column):
                add_error(errors, line_number, checklist_id, f"unmatched rows must not have {column}")

    if status == "source_readiness_required":
        if match_status != "support_table_only":
            add_error(errors, line_number, checklist_id, "source-readiness rows must be support_table_only")
        if not source_note_refs:
            add_error(errors, line_number, checklist_id, "source-readiness rows require source_note_refs")
        if not match_source:
            add_error(errors, line_number, checklist_id, "source-readiness rows require match_source")


def validate_matrix() -> list[str]:
    errors: list[str] = []
    seen_checklist_ids: set[str] = set()

    if not COVERAGE_MATRIX.exists():
        return [f"missing coverage matrix: {COVERAGE_MATRIX}"]

    with COVERAGE_MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing = [column for column in REQUIRED_COLUMNS if column not in columns]
        if missing:
            return ["coverage matrix is missing required columns: " + ", ".join(missing)]

        rows = []
        for line_number, row in enumerate(reader, start=2):
            rows.append(row)
            validate_row(row, line_number, seen_checklist_ids, errors)

    if not rows:
        errors.append("coverage matrix is empty")
        return errors

    return errors


def main() -> int:
    errors = validate_matrix()
    if errors:
        print("Coverage matrix validation failed:", file=sys.stderr)
        for error in errors[:100]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 100:
            print(f"- ... {len(errors) - 100} additional errors", file=sys.stderr)
        return 1

    print("Coverage matrix structure OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
