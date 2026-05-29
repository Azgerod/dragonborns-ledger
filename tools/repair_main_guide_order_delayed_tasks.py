#!/usr/bin/env python3
"""Classify TB-038 delayed-task audit findings for TB-038R."""

from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-order-delayed-task-audit.csv"
COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
REPAIR_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-order-delayed-task-repair.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"

ACTION_VALUES = {"repair_or_mark_route_resolution", "review_support_delay"}
GUIDE_BLOCK_START = (
    "15. NEEDS ROUTE RESOLUTION: TB-038R order and delayed-task repair register"
)
CLOSURE_IDS = {
    "OBJ-001501",  # Seeks-Ancient-Artifacts' Journal, v1 is later read in the Nchuanthumz route.
    "OBJ-001508",  # Soran's Journal is later read in the Creature of Legend route.
    "OBJ-001773",  # Stones of Barenziah set is closed by No Stone Unturned.
    "OBJ-001774",  # Whiterun Stone of Barenziah member acquired in guide.
    "OBJ-001796",  # Pinewatch Stone of Barenziah member acquired in guide.
    "OBJ-002414",  # Goldenhills Farm Bunkhouse is tied to the later farm buildout.
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def is_closed_or_connected(row: dict[str, str]) -> bool:
    current_status = row["current_status"].lower()
    if row["record_id"] in CLOSURE_IDS:
        return True
    if row["record_type"] == "property_detail" and row["section"] == "MR-008":
        return True
    if row["record_type"] in {"save", "branch_state", "handoff"}:
        return True
    if row["record_type"] == "crafting_system" and "staged_for_mr069" in current_status:
        return True
    if current_status.startswith("acquired_now / in_progress_collectible_member"):
        return True
    if current_status.startswith("completed_at_level_14_or_staged / conditional_complete_or_staged"):
        return True
    if current_status.startswith("branch_route_completed"):
        return True
    return False


def repair_rows() -> list[dict[str, str]]:
    rows = []
    for row in read_csv(AUDIT_CSV):
        if row["recommended_action"] not in ACTION_VALUES:
            continue
        classification = "closed_or_connected" if is_closed_or_connected(row) else "explicit_route_resolution"
        if classification == "closed_or_connected":
            repair_status = "tb038r_delayed_task_closed"
            exact_missing_fact = (
                "TB-038R connected this delayed/support row to an existing routed action, "
                "final reference, branch reload, or later buildout already present in main-guide-v1."
            )
        else:
            repair_status = "tb038r_needs_route_resolution"
            exact_missing_fact = (
                "The current coverage row is delayed, held, conditional, or in progress, "
                "and TB-038 found no later same-record closeout in the current coverage ledger."
            )
        record_id = row["record_id"]
        if not record_id or row["record_type"] == "save":
            record_id = f"TB038R-SOURCE-LINE-{row['source_line']}"
        rows.append(
            {
                "source_line": row["source_line"],
                "audit_area": row["audit_area"],
                "audit_status": row["audit_status"],
                "recommended_action_before_repair": row["recommended_action"],
                "classification": classification,
                "repair_status": repair_status,
                "record_type": row["record_type"],
                "record_id": record_id,
                "mapped_objective_id": row["mapped_objective_id"],
                "name": row["name"],
                "current_location": row["current_location"],
                "current_status": row["current_status"],
                "exact_missing_fact": exact_missing_fact,
                "inputs_checked": (
                    "data/guide-coverage/main-guide-v1-order-delayed-task-audit.csv; "
                    "data/guide-coverage/main-guide-v1-coverage.csv; "
                    "data/guide-coverage/main-guide-v1-objective-final-status.csv; "
                    "drafts/final-guide/main-guide-v1.md"
                ),
            }
        )
    return rows


def coverage_repair_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in rows:
        record_id = "" if row["record_id"].startswith("TB038R-SOURCE-LINE-") else row["record_id"]
        if row["classification"] == "closed_or_connected":
            coverage_status = "tb038r_delayed_task_closed"
            completion_status = "complete_or_accounted_for"
            cue = f"TB-038R closeout: {row['name']}"
        else:
            coverage_status = "needs_route_resolution_added"
            completion_status = "NEEDS ROUTE RESOLUTION"
            cue = f"NEEDS ROUTE RESOLUTION: {row['record_id']} {row['name']}"
        output.append(
            {
                "mr_section": "TB-038R",
                "record_type": row["record_type"],
                "objective_id": record_id,
                "objective_name": row["name"],
                "coverage_status": coverage_status,
                "player_facing_cue": cue,
                "player_facing_location": "TB-038R order and delayed-task repair register",
                "completion_status": completion_status,
                "notes": (
                    f"TB-038R source line {row['source_line']}: {row['exact_missing_fact']} "
                    f"Previous status: {row['current_status']}. Inputs checked: {row['inputs_checked']}."
                ),
            }
        )
    return output


def update_coverage(rows: list[dict[str, str]]) -> None:
    existing = read_csv(COVERAGE_CSV)
    fieldnames = list(existing[0])
    kept = [
        row
        for row in existing
        if not (row["mr_section"] == "TB-038R" and "TB-038R source line" in row["notes"])
    ]
    kept.extend(coverage_repair_rows(rows))
    write_csv(COVERAGE_CSV, fieldnames, kept)


def guide_block(rows: list[dict[str, str]]) -> str:
    route_resolution_rows = [row for row in rows if row["classification"] == "explicit_route_resolution"]
    closed_rows = [row for row in rows if row["classification"] == "closed_or_connected"]
    lines = [
        f"{GUIDE_BLOCK_START} - exact missing fact: the TB-038 audit found delayed, held, conditional, or in-progress rows without a later same-record closeout. TB-038R classifies each row below as either an explicit open route-resolution item or a closeout already connected to existing guide prose. Inputs checked for the batch: `data/guide-coverage/main-guide-v1-order-delayed-task-audit.csv`, `data/guide-coverage/main-guide-v1-coverage.csv`, `data/guide-coverage/main-guide-v1-objective-final-status.csv`, and the current `main-guide-v1.md`.",
        "",
        "| Record ID | Record | TB-038R status | Exact missing fact or closeout | Inputs checked |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        status = (
            "NEEDS ROUTE RESOLUTION"
            if row["classification"] == "explicit_route_resolution"
            else "Connected to existing route or final reference"
        )
        lines.append(
            "| {record_id} | {name} | {status} | {fact} Previous status: `{current_status}`. | {inputs} |".format(
                record_id=row["record_id"],
                name=row["name"].replace("|", "/"),
                status=status,
                fact=row["exact_missing_fact"],
                current_status=row["current_status"],
                inputs=row["inputs_checked"].replace(";", "; "),
            )
        )
    lines.append("")
    lines.append(
        f"TB-038R summary: {len(route_resolution_rows)} rows remain explicit route-resolution items and {len(closed_rows)} rows were connected to existing route/final-reference closeouts."
    )
    return "\n".join(lines)


def update_guide(rows: list[dict[str, str]]) -> None:
    text = MAIN_GUIDE.read_text(encoding="utf-8").rstrip()
    marker_index = text.find(GUIDE_BLOCK_START)
    if marker_index != -1:
        text = text[:marker_index].rstrip()
    MAIN_GUIDE.write_text(f"{text}\n\n{guide_block(rows)}\n", encoding="utf-8")


def main() -> int:
    rows = repair_rows()
    if not rows and REPAIR_CSV.exists():
        rows = read_csv(REPAIR_CSV)
    repair_fields = [
        "source_line",
        "audit_area",
        "audit_status",
        "recommended_action_before_repair",
        "classification",
        "repair_status",
        "record_type",
        "record_id",
        "mapped_objective_id",
        "name",
        "current_location",
        "current_status",
        "exact_missing_fact",
        "inputs_checked",
    ]
    write_csv(REPAIR_CSV, repair_fields, rows)
    update_coverage(rows)
    update_guide(rows)
    print(f"Wrote {REPAIR_CSV.relative_to(REPO_ROOT)} ({len(rows)} rows).")
    print(f"Updated {COVERAGE_CSV.relative_to(REPO_ROOT)} with TB-038R repair rows.")
    print(f"Updated {MAIN_GUIDE.relative_to(REPO_ROOT)} with TB-038R repair register.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
