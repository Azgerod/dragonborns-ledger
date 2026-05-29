#!/usr/bin/env python3
"""Audit main-guide-v1 order and delayed-task closure for TB-038."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
COVERAGE_LEDGER = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVE_FINAL_STATUS = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-final-status.csv"
CHECKLIST_AUDIT = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-checklist-id-audit.csv"
HARD_SAVE_REGISTER = REPO_ROOT / "data" / "constraints" / "quest-conflicts-hard-saves.md"
OUTPUT_AUDIT = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-order-delayed-task-audit.csv"
OUTPUT_SUMMARY = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-order-delayed-task-summary.csv"
REPAIR_REGISTER = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-order-delayed-task-repair.csv"

SAVE_RE = re.compile(r"\bHS-[A-Z0-9-]+\b")
SECTION_RE = re.compile(r"^###\s+(.*)")
DELAY_TERMS = (
    "staged",
    "held",
    "hold",
    "later",
    "wait",
    "not_completed_here",
    "not_started_here",
    "not_acquired_here",
    "not_read_here",
    "deferred",
    "park",
    "gated",
    "in_progress",
)
BRANCH_MARKER_RE = re.compile(
    r"\b(branch route|branch continuity|trophy branch only|BRANCH ROUTE)\b"
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def repair_identity_from_register(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    record_type = row.get("record_type", "")
    record_id = row.get("record_id", "")
    if record_type == "save" or record_id.startswith("TB038R-SOURCE-LINE-"):
        record_id = ""
    return (
        record_type,
        record_id,
        row.get("name", ""),
        row.get("current_location", ""),
        row.get("current_status", ""),
    )


def repair_identity_from_coverage(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    record_type = row.get("record_type", "")
    record_id = "" if record_type == "save" else row.get("objective_id", "")
    return (
        record_type,
        record_id,
        row.get("objective_name", ""),
        row.get("player_facing_location", ""),
        f"{row.get('coverage_status', '')} / {row.get('completion_status', '')}",
    )


def read_repair_register() -> tuple[dict[str, dict[str, str]], dict[tuple[str, str, str, str, str], dict[str, str]]]:
    if not REPAIR_REGISTER.exists():
        return {}, {}
    by_source_line = {}
    by_identity = {}
    for row in read_csv(REPAIR_REGISTER):
        if row.get("source_line"):
            by_source_line[row["source_line"]] = row
        by_identity[repair_identity_from_register(row)] = row
    return by_source_line, by_identity


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def row_text(row: dict[str, str]) -> str:
    return " ".join(
        row.get(field, "")
        for field in ("coverage_status", "completion_status", "notes", "player_facing_cue")
    ).lower()


def is_delayed(row: dict[str, str]) -> bool:
    if row.get("record_type") in {"summary", "audit"}:
        return False
    text = row_text(row)
    return any(term in text for term in DELAY_TERMS)


def is_route_resolution(row: dict[str, str]) -> bool:
    text = row_text(row)
    return "needs route resolution" in text or "needs_route_resolution" in text


def is_closure(row: dict[str, str]) -> bool:
    completion = row.get("completion_status", "").lower()
    coverage = row.get("coverage_status", "").lower()
    if is_route_resolution(row):
        return True
    if completion.startswith(("not_", "staged", "in_progress", "partial")):
        return False
    if completion.startswith(
        (
            "complete",
            "completed",
            "branch_complete",
            "route_default_complete",
            "already_complete",
            "service_available",
            "guide_reference_represented",
            "option",
            "excluded",
            "created",
        )
    ):
        return True
    if coverage.startswith(
        (
            "placed_in_guide",
            "completed_now",
            "acquired_now",
            "read_in_guide",
            "branch_placed",
            "explicit_exclusion",
            "appendix_reference_promoted",
            "retrospectively_confirmed_complete",
            "retrospectively_confirmed_read",
            "route_source_named_or_already_routed",
        )
    ) and not completion.startswith(("staged", "in_progress", "not_")):
        return True
    return False


def expand_save_ranges(line: str) -> set[str]:
    saves = set(SAVE_RE.findall(line))
    if " through " not in line or len(saves) < 2:
        return saves

    ordered = SAVE_RE.findall(line)
    for first, second in zip(ordered, ordered[1:]):
        first_match = re.match(r"^(.*?)(\d+)$", first)
        second_match = re.match(r"^(.*?)(\d+)$", second)
        if not first_match or not second_match:
            continue
        first_prefix, first_number = first_match.groups()
        second_prefix, second_number = second_match.groups()
        if first_prefix != second_prefix:
            continue
        start = int(first_number)
        end = int(second_number)
        if start > end or end - start > 50:
            continue
        width = max(len(first_number), len(second_number))
        for number in range(start, end + 1):
            saves.add(f"{first_prefix}{number:0{width}d}")
    return saves


def guide_lines() -> list[dict[str, object]]:
    current_section = ""
    lines = []
    for line_number, line in enumerate(MAIN_GUIDE.read_text(encoding="utf-8").splitlines(), start=1):
        match = SECTION_RE.match(line)
        if match:
            current_section = match.group(1).strip()
        lines.append(
            {
                "line_number": line_number,
                "section": current_section,
                "text": line,
                "saves": set(SAVE_RE.findall(line)) - {"HS-NAME"},
            }
        )
    return lines


def hard_save_rows(lines: list[dict[str, object]]) -> list[dict[str, str]]:
    guide_saves = set().union(*(line["saves"] for line in lines)) if lines else set()
    save_creation_lines: dict[str, list[dict[str, object]]] = defaultdict(list)
    for line in lines:
        if "HARD SAVE" not in str(line["text"]):
            continue
        for save in line["saves"]:
            save_creation_lines[save].append(line)

    register_lines = HARD_SAVE_REGISTER.read_text(encoding="utf-8").splitlines()
    register_saves: dict[str, int] = {}
    for line_number, line in enumerate(register_lines, start=1):
        for save in expand_save_ranges(line):
            register_saves.setdefault(save, line_number)

    rows: list[dict[str, str]] = []
    for save in sorted(register_saves):
        if save in guide_saves:
            status = "pass_register_save_present_in_guide"
            action = "none"
            note = "Registered hard save appears in main-guide-v1.md."
        elif save == "HS-DAEDRIC-BLACK-STAR" and "OBJ-001612" in MAIN_GUIDE.read_text(encoding="utf-8"):
            status = "known_route_resolution_missing_guide_save"
            action = "none_existing_route_resolution"
            note = "Azura's Star branch save is still owned by the explicit OBJ-001612 route-resolution row."
        else:
            status = "missing_registered_save_in_guide"
            action = "repair_hard_save_placement"
            note = "Registered hard save does not appear in main-guide-v1.md."
        rows.append(
            audit_row(
                "hard_save_register",
                status,
                action,
                str(register_saves[save]),
                "",
                "hard_save",
                save,
                "",
                save,
                "",
                "",
                "",
                note,
            )
        )

    for save in sorted(guide_saves - set(register_saves)):
        creation_lines = save_creation_lines.get(save, [])
        if creation_lines:
            first = creation_lines[0]
            status = "guide_local_hard_save_has_creation_cue"
            action = "none_local_save"
            note = "Guide-created local hard save has an explicit creation cue; it is not part of the central constraint register."
            line_number = str(first["line_number"])
            section = str(first["section"])
            current_location = section
        else:
            status = "guide_save_reference_without_creation_cue"
            action = "review_save_creation"
            note = "Guide references this save but no explicit HARD SAVE creation line was found."
            line_number = ""
            section = ""
            current_location = ""
        rows.append(
            audit_row(
                "hard_save_register",
                status,
                action,
                line_number,
                section,
                "hard_save",
                save,
                "",
                save,
                current_location,
                "",
                "",
                note,
            )
        )
    return rows


def branch_reload_rows(lines: list[dict[str, object]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    section_indexes: dict[str, list[int]] = defaultdict(list)
    for index, line in enumerate(lines):
        section_indexes[str(line["section"])].append(index)

    for index, line in enumerate(lines):
        text = str(line["text"])
        if not re.match(r"^\d+\.", text.strip()):
            continue
        if not BRANCH_MARKER_RE.search(text):
            continue
        section = str(line["section"])
        indexes = section_indexes[section]
        before = [i for i in indexes if i <= index]
        after = [i for i in indexes if i >= index]
        prior_saves: list[str] = []
        for before_index in before:
            prior_saves.extend(sorted(lines[before_index]["saves"]))
        save = prior_saves[-1] if prior_saves else ""
        reload_lines = [
            lines[after_index]
            for after_index in after
            if "reload" in str(lines[after_index]["text"]).lower()
            and (not save or save in str(lines[after_index]["text"]) or "hard save" in str(lines[after_index]["text"]).lower())
        ]
        if reload_lines:
            status = "pass_branch_reload_cue_found"
            action = "none"
            closeout = f"line {reload_lines[0]['line_number']}"
            note = "Branch marker has a same-section reload cue after the branch instruction."
        else:
            status = "branch_reload_cue_not_found"
            action = "repair_branch_reload_cue"
            closeout = ""
            note = "Branch marker did not have a same-section reload cue after it."
        rows.append(
            audit_row(
                "branch_reload",
                status,
                action,
                str(line["line_number"]),
                section,
                "guide_line",
                save,
                "",
                text.strip(),
                section,
                "branch marker",
                closeout,
                note,
            )
        )
    return rows


def delayed_rows() -> list[dict[str, str]]:
    coverage_rows = read_csv(COVERAGE_LEDGER)
    repair_register_by_source_line, repair_register_by_identity = read_repair_register()
    final_status = {
        row["objective_id"]: row["final_coverage_status"]
        for row in read_csv(OBJECTIVE_FINAL_STATUS)
    }
    checklist_to_objective = {
        row["checklist_id"]: row.get("objective_id", "")
        for row in read_csv(CHECKLIST_AUDIT)
    }

    rows_by_id: dict[str, list[tuple[int, dict[str, str]]]] = defaultdict(list)
    for index, row in enumerate(coverage_rows):
        record_id = row.get("objective_id", "")
        if record_id:
            rows_by_id[record_id].append((index, row))

    rows: list[dict[str, str]] = []
    for index, row in enumerate(coverage_rows):
        if not is_delayed(row):
            continue
        source_line = str(index + 2)
        repair_entry = repair_register_by_source_line.get(source_line) or repair_register_by_identity.get(
            repair_identity_from_coverage(row)
        )
        if repair_entry:
            if repair_entry.get("classification") == "explicit_route_resolution":
                status = "pass_tb038r_explicit_route_resolution"
                action = "none_existing_route_resolution"
                note = "TB-038R repair register records this delayed/support row as an explicit route-resolution item."
            else:
                status = "pass_tb038r_closed_or_connected"
                action = "none"
                note = "TB-038R repair register connects this delayed/support row to an existing guide route or final reference."
            rows.append(
                audit_row(
                    "delayed_coverage",
                    status,
                    action,
                    source_line,
                    row.get("mr_section", ""),
                    row.get("record_type", ""),
                    row.get("objective_id", ""),
                    "",
                    row.get("objective_name", ""),
                    row.get("player_facing_location", ""),
                    f"{row.get('coverage_status', '')} / {row.get('completion_status', '')}",
                    repair_entry.get("repair_status", "TB-038R repair register"),
                    note,
                )
            )
            continue
        record_id = row.get("objective_id", "")
        mapped_objective_id = checklist_to_objective.get(record_id, "") if record_id.startswith("CHK-") else ""
        if not record_id and is_closure(row):
            rows.append(
                audit_row(
                    "delayed_coverage",
                    "pass_self_closing_support_row",
                    "none",
                    source_line,
                    row.get("mr_section", ""),
                    row.get("record_type", ""),
                    "",
                    "",
                    row.get("objective_name", ""),
                    row.get("player_facing_location", ""),
                    f"{row.get('coverage_status', '')} / {row.get('completion_status', '')}",
                    "self-closing support row",
                    "Delayed wording appears in this support row, but the same row records the closing state.",
                )
            )
            continue
        candidate_ids = [value for value in (record_id, mapped_objective_id) if value]

        later_closures = []
        later_same_record_rows = []
        any_closures = []
        route_resolution = False
        for candidate_id in candidate_ids:
            for other_index, other_row in rows_by_id.get(candidate_id, []):
                if is_route_resolution(other_row):
                    route_resolution = True
                if other_index > index:
                    later_same_record_rows.append(other_row)
                if is_closure(other_row):
                    any_closures.append(other_row)
                    if other_index > index:
                        later_closures.append(other_row)

        candidate_final_status = final_status.get(record_id) or final_status.get(mapped_objective_id, "")
        if later_closures:
            status = "pass_closed_by_later_same_record"
            action = "none"
            closeout = closeout_summary(later_closures)
            note = "A later coverage row for this record closes the staged or held state."
        elif route_resolution or candidate_final_status == "unresolved":
            status = "pass_explicit_route_resolution"
            action = "none_existing_route_resolution"
            closeout = "explicit route-resolution row"
            note = "The delayed state remains open only as an explicit route-resolution risk."
        elif any_closures:
            status = "pass_closed_elsewhere_same_record"
            action = "none"
            closeout = closeout_summary(any_closures)
            note = "The same record has a closure row elsewhere in the coverage ledger."
        elif later_same_record_rows:
            status = "pass_progress_continues_later_same_record"
            action = "none"
            closeout = closeout_summary(later_same_record_rows)
            note = "The record is still open here, but a later row continues the same delayed task before final closeout review."
        elif candidate_final_status in {"excluded", "option_default_handled", "branch_handled"}:
            status = f"pass_final_status_{candidate_final_status}"
            action = "none"
            closeout = candidate_final_status
            note = "Final objective status accounts for this delayed state."
        elif record_id.startswith("OBJ-"):
            status = "needs_delayed_task_repair"
            action = "repair_or_mark_route_resolution"
            closeout = ""
            note = "Objective row is delayed or held but has no same-record closeout or explicit route-resolution status."
        else:
            status = "needs_support_delay_review"
            action = "review_support_delay"
            closeout = ""
            note = "Support/checklist row is delayed or held but no same-record closeout was found by this audit."

        rows.append(
            audit_row(
                "delayed_coverage",
                status,
                action,
                source_line,
                row.get("mr_section", ""),
                row.get("record_type", ""),
                record_id,
                mapped_objective_id,
                row.get("objective_name", ""),
                row.get("player_facing_location", ""),
                f"{row.get('coverage_status', '')} / {row.get('completion_status', '')}",
                closeout,
                note,
            )
        )
    return rows


def closeout_summary(rows: list[dict[str, str]]) -> str:
    parts = []
    for row in rows[:3]:
        parts.append(
            f"{row.get('mr_section', '')}: {row.get('coverage_status', '')} / {row.get('completion_status', '')}"
        )
    if len(rows) > 3:
        parts.append(f"+{len(rows) - 3} more")
    return "; ".join(parts)


def audit_row(
    audit_area: str,
    audit_status: str,
    recommended_action: str,
    source_line: str,
    section: str,
    record_type: str,
    record_id: str,
    mapped_objective_id: str,
    name: str,
    current_location: str,
    current_status: str,
    closeout_status: str,
    notes: str,
) -> dict[str, str]:
    return {
        "audit_area": audit_area,
        "audit_status": audit_status,
        "recommended_action": recommended_action,
        "source_line": source_line,
        "section": section,
        "record_type": record_type,
        "record_id": record_id,
        "mapped_objective_id": mapped_objective_id,
        "name": name,
        "current_location": current_location,
        "current_status": current_status,
        "closeout_status": closeout_status,
        "notes": notes,
    }


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summary: list[dict[str, str]] = []
    by_area = Counter(row["audit_area"] for row in rows)
    by_status = Counter((row["audit_area"], row["audit_status"]) for row in rows)
    by_action = Counter((row["audit_area"], row["recommended_action"]) for row in rows)

    for area, count in sorted(by_area.items()):
        summary.append({"metric": f"{area}:rows", "count": str(count), "notes": "Generated audit rows."})
    for (area, status), count in sorted(by_status.items()):
        summary.append(
            {
                "metric": f"{area}:status:{status}",
                "count": str(count),
                "notes": "Audit-status distribution.",
            }
        )
    for (area, action), count in sorted(by_action.items()):
        summary.append(
            {
                "metric": f"{area}:recommended_action:{action}",
                "count": str(count),
                "notes": "Recommended-action distribution.",
            }
        )
    return summary


def main() -> int:
    lines = guide_lines()
    rows = []
    rows.extend(hard_save_rows(lines))
    rows.extend(branch_reload_rows(lines))
    rows.extend(delayed_rows())

    fieldnames = [
        "audit_area",
        "audit_status",
        "recommended_action",
        "source_line",
        "section",
        "record_type",
        "record_id",
        "mapped_objective_id",
        "name",
        "current_location",
        "current_status",
        "closeout_status",
        "notes",
    ]
    write_csv(OUTPUT_AUDIT, fieldnames, rows)
    write_csv(OUTPUT_SUMMARY, ["metric", "count", "notes"], summary_rows(rows))

    action_counts = Counter(row["recommended_action"] for row in rows)
    print(f"Wrote {OUTPUT_AUDIT.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUTPUT_SUMMARY.relative_to(REPO_ROOT)}")
    print(", ".join(f"{action}: {count}" for action, count in sorted(action_counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
