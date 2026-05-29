#!/usr/bin/env python3
"""Audit trophy, leveled-reward, and cell-entry constraints for TB-039."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
COVERAGE_LEDGER = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVE_STATUS = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-final-status.csv"
OBJECTIVE_CONSTRAINTS = REPO_ROOT / "data" / "route-planning" / "objective-constraints.csv"
OUTPUT_AUDIT = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-trophy-leveled-cell-audit.csv"
OUTPUT_SUMMARY = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-trophy-leveled-cell-summary.csv"

SOURCE_AREAS = {
    "data/constraints/trophy-dependencies.md": "trophy_dependency",
    "data/constraints/leveled-unique-items.md": "leveled_item",
    "data/constraints/cell-entry-locks.md": "cell_entry",
}

REVIEW_ACTIONS = {
    "trophy_dependency": "review_trophy_route",
    "leveled_item": "review_leveled_reward_gate",
    "cell_entry": "review_cell_entry_gate",
    "trophy_setup": "review_trophy_setup",
}

GLOBAL_SETUP_RULES = [
    {
        "audit_area": "trophy_setup",
        "constraint_id": "TB039-SETUP-001",
        "row_label": "PS4 SE/AE trophy set",
        "route_protection": "Use a PS4 Special Edition / Anniversary Edition run and preserve PlayStation trophies.",
        "required_terms": ("ps4", "playstation trophies"),
    },
    {
        "audit_area": "trophy_setup",
        "constraint_id": "TB039-SETUP-002",
        "row_label": "Trophy-safe content setup",
        "route_protection": "Install only the base game, official DLC, and official AE Creation Club bundle; forbid mods and non-AE Creations.",
        "required_terms": ("do not install mods", "non-ae creations"),
    },
    {
        "audit_area": "trophy_setup",
        "constraint_id": "TB039-SETUP-003",
        "row_label": "Mod-contaminated save recovery",
        "route_protection": "Prevent the contaminated-save state by starting from a clean trophy-safe setup and forbidding content changes mid-run.",
        "required_terms": ("do not add or remove content mid-run", "trophies preserved"),
    },
    {
        "audit_area": "trophy_setup",
        "constraint_id": "TB039-SETUP-004",
        "row_label": "PS4 trophy-pop fallback",
        "route_protection": "Use rotating manual saves and named hard saves before risky trophy, reward, or branch windows.",
        "required_terms": ("rotating manual save", "hard save"),
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def coverage_by_objective(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    output: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        objective_id = row.get("objective_id", "")
        if objective_id:
            output.setdefault(objective_id, []).append(row)
    return output


def coverage_text(rows: list[dict[str, str]]) -> str:
    return " ".join(
        " ".join(
            row.get(field, "")
            for field in (
                "coverage_status",
                "player_facing_cue",
                "player_facing_location",
                "completion_status",
                "notes",
            )
        )
        for row in rows
    )


def explicit_route_resolution(final_row: dict[str, str], coverage_rows: list[dict[str, str]]) -> bool:
    text = " ".join(
        [
            final_row.get("final_coverage_status", ""),
            final_row.get("coverage_statuses", ""),
            final_row.get("completion_statuses", ""),
            coverage_text(coverage_rows),
        ]
    ).lower()
    return "unresolved" in final_row.get("final_coverage_status", "") or "needs route resolution" in text or "needs_route_resolution" in text


def area_status(
    area: str,
    final_row: dict[str, str],
    coverage_rows: list[dict[str, str]],
) -> tuple[str, str, str]:
    final_status = final_row.get("final_coverage_status", "")
    if final_status == "placed_in_main_guide":
        return "pass_constraint_accounted_in_main_guide", "none", "Objective is represented in the current main guide coverage ledger."
    if final_status == "branch_handled":
        return "pass_branch_handled", "none", "Objective is represented by branch-first/reload guide handling."
    if final_status == "option_default_handled":
        return "pass_option_default_handled", "none", "Objective is represented by route default or option-list handling."
    if final_status == "excluded":
        return "pass_scope_exclusion", "none", "Objective has an explicit route-scope exclusion."
    if explicit_route_resolution(final_row, coverage_rows):
        return (
            "pass_existing_route_resolution",
            "none_existing_route_resolution",
            "Constraint row remains visible through explicit NEEDS ROUTE RESOLUTION coverage.",
        )
    return (
        f"needs_{area}_review",
        REVIEW_ACTIONS[area],
        "Constraint row lacks placed, branch, option/default, exclusion, or explicit route-resolution coverage.",
    )


def setup_rows(guide_text: str) -> list[dict[str, str]]:
    output = []
    for rule in GLOBAL_SETUP_RULES:
        missing_terms = [term for term in rule["required_terms"] if term not in guide_text]
        if missing_terms:
            status = "needs_trophy_setup_review"
            action = REVIEW_ACTIONS["trophy_setup"]
            evidence = "Missing setup terms: " + ", ".join(missing_terms)
        else:
            status = "pass_setup_rule_in_guide"
            action = "none"
            evidence = "Setup section contains the required trophy-safety baseline terms."
        output.append(
            {
                "audit_area": rule["audit_area"],
                "constraint_id": rule["constraint_id"],
                "constraint_source_file": "data/constraints/trophy-dependencies.md",
                "source_section": "Setup and Global Trophy Safety",
                "row_label": rule["row_label"],
                "constraint_type": "trophy_setup",
                "objective_id": "",
                "objective_name": "",
                "severity": "hard_gate",
                "final_coverage_status": "",
                "guide_locations": "Setup and Save Baseline",
                "route_protection": rule["route_protection"],
                "audit_status": status,
                "recommended_action": action,
                "evidence": evidence,
                "notes": "TB-039 setup check derived from the trophy dependency table and current guide setup prose.",
            }
        )
    return output


def constraint_rows() -> list[dict[str, str]]:
    final_by_id = {row["objective_id"]: row for row in read_csv(OBJECTIVE_STATUS)}
    coverage_by_id = coverage_by_objective(read_csv(COVERAGE_LEDGER))
    rows = []

    for row in read_csv(OBJECTIVE_CONSTRAINTS):
        source_file = row["constraint_source_file"]
        if source_file not in SOURCE_AREAS:
            continue
        if row["source_section"] == "Queue Disposition":
            continue

        area = SOURCE_AREAS[source_file]
        objective_id = row["objective_id"]
        final_row = final_by_id.get(objective_id, {})
        coverage_rows = coverage_by_id.get(objective_id, [])
        status, action, evidence = area_status(area, final_row, coverage_rows)
        rows.append(
            {
                "audit_area": area,
                "constraint_id": row["constraint_id"],
                "constraint_source_file": source_file,
                "source_section": row["source_section"],
                "row_label": row["row_label"],
                "constraint_type": row["constraint_type"],
                "objective_id": objective_id,
                "objective_name": row["objective_name"],
                "severity": row["severity"],
                "final_coverage_status": final_row.get("final_coverage_status", "missing_objective_final_status"),
                "guide_locations": final_row.get("guide_locations", ""),
                "route_protection": row["routing_rule"],
                "audit_status": status,
                "recommended_action": action,
                "evidence": evidence,
                "notes": (
                    f"Source notes: {row['source_notes']}. "
                    "TB-039 uses existing sourced constraint rows and current guide/coverage state; no broad gameplay research performed."
                ),
            }
        )
    return rows


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    areas = sorted({row["audit_area"] for row in rows})
    for area in areas:
        area_rows = [row for row in rows if row["audit_area"] == area]
        output.append({"metric": f"{area}:rows", "count": str(len(area_rows)), "notes": "Generated TB-039 audit rows."})
        for status, count in sorted(Counter(row["audit_status"] for row in area_rows).items()):
            output.append({"metric": f"{area}:status:{status}", "count": str(count), "notes": "Audit-status distribution."})
        for action, count in sorted(Counter(row["recommended_action"] for row in area_rows).items()):
            output.append({"metric": f"{area}:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    output.append({"metric": "all:rows", "count": str(len(rows)), "notes": "Generated TB-039 audit rows."})
    for action, count in sorted(Counter(row["recommended_action"] for row in rows).items()):
        output.append({"metric": f"all:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    return output


def main() -> int:
    guide_text = MAIN_GUIDE.read_text(encoding="utf-8").lower()
    rows = setup_rows(guide_text) + constraint_rows()
    fieldnames = [
        "audit_area",
        "constraint_id",
        "constraint_source_file",
        "source_section",
        "row_label",
        "constraint_type",
        "objective_id",
        "objective_name",
        "severity",
        "final_coverage_status",
        "guide_locations",
        "route_protection",
        "audit_status",
        "recommended_action",
        "evidence",
        "notes",
    ]
    write_csv(OUTPUT_AUDIT, fieldnames, rows)
    write_csv(OUTPUT_SUMMARY, ["metric", "count", "notes"], summary_rows(rows))
    actions = Counter(row["recommended_action"] for row in rows)
    print(f"Wrote {OUTPUT_AUDIT.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUTPUT_SUMMARY.relative_to(REPO_ROOT)}")
    print(", ".join(f"{key}: {actions[key]}" for key in sorted(actions)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
