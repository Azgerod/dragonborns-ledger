#!/usr/bin/env python3
"""Summarize final main-guide-v1 coverage buckets for TB-035-COV-013."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OBJECTIVES_CSV = REPO_ROOT / "data" / "objectives" / "objectives.csv"
GUIDE_COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVE_AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-id-audit.csv"
CHECKLIST_AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-checklist-id-audit.csv"
OUTPUT_SUMMARY_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-final-coverage-summary.csv"
OUTPUT_DETAIL_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-final-status.csv"

AUDIT_CSVS = [
    OBJECTIVE_AUDIT_CSV,
    CHECKLIST_AUDIT_CSV,
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-branch-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-option-default-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-exclusion-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-appendix-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-location-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-book-document-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-collectible-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-crafting-progression-audit.csv",
    REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-radiant-counter-audit.csv",
]

OBJECTIVE_REF_RE = re.compile(r"\bOBJ-(\d{6})(?:\s*(?:-|through)\s*(?:OBJ-)?(\d{6}))?\b", re.IGNORECASE)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def objective_refs(value: str) -> list[str]:
    refs: list[str] = []
    for match in OBJECTIVE_REF_RE.finditer(value or ""):
        start = int(match.group(1))
        end = int(match.group(2) or match.group(1))
        if end < start:
            start, end = end, start
        refs.extend(f"OBJ-{number:06d}" for number in range(start, end + 1))
    return refs


def row_text(rows: list[dict[str, str]]) -> str:
    return " ".join(" ".join(value or "" for value in row.values()) for row in rows).lower()


def status_values(rows: list[dict[str, str]], field: str) -> str:
    values = sorted({(row.get(field) or "").strip() for row in rows if (row.get(field) or "").strip()})
    return " | ".join(values)


def has_unresolved(rows: list[dict[str, str]]) -> bool:
    text = row_text(rows)
    return (
        "needs route resolution" in text
        or "needs_route_resolution" in text
        or any((row.get("completion_status") or "").strip() == "NEEDS ROUTE RESOLUTION" for row in rows)
    )


def has_explicit_exclusion(objective: dict[str, str], rows: list[dict[str, str]]) -> bool:
    if objective["route_placement"] == "excluded":
        return True
    for row in rows:
        coverage_status = (row.get("coverage_status") or "").lower()
        completion_status = (row.get("completion_status") or "").lower()
        if "exclusion" in coverage_status or "excluded" in coverage_status:
            return True
        if "excluded" in completion_status:
            return True
    return False


def classify_objective(objective: dict[str, str], coverage_rows: list[dict[str, str]]) -> str:
    # Keep this priority conservative: unresolved rows remain visible even if
    # their canonical route placement is branch or appendix.
    if has_unresolved(coverage_rows):
        return "unresolved"
    if has_explicit_exclusion(objective, coverage_rows):
        return "excluded"
    if objective["route_placement"] == "branch_route":
        return "branch_handled"
    if objective["route_placement"] == "option_list":
        return "option_default_handled"
    return "placed_in_main_guide"


def audit_summary(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    rows = read_csv(path)
    recommended_actions = Counter(row.get("recommended_action", "") or "" for row in rows)
    audit_statuses = Counter(row.get("audit_status", "") or "" for row in rows)
    summary_rows = [
        {
            "summary_group": "audit_artifact",
            "metric": f"{path.name}:rows",
            "count": str(len(rows)),
            "notes": f"Generated audit artifact rows in {path.relative_to(REPO_ROOT)}.",
        }
    ]
    for action, count in sorted(recommended_actions.items()):
        metric = action or "blank_recommended_action"
        summary_rows.append(
            {
                "summary_group": "audit_recommended_action",
                "metric": f"{path.name}:{metric}",
                "count": str(count),
                "notes": "Recommended-action distribution from generated audit artifact.",
            }
        )
    for status, count in sorted(audit_statuses.items()):
        metric = status or "blank_audit_status"
        summary_rows.append(
            {
                "summary_group": "audit_status",
                "metric": f"{path.name}:{metric}",
                "count": str(count),
                "notes": "Audit-status distribution from generated audit artifact.",
            }
        )
    return summary_rows


def cross_cutting_ledger_summaries(coverage_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summary_rows = []
    for row in coverage_rows:
        mr_section = row.get("mr_section", "")
        if not mr_section.startswith("COV-") or row.get("record_type") != "summary":
            continue
        summary_rows.append(
            {
                "summary_group": "coverage_ledger_summary",
                "metric": f"{mr_section}:{row.get('objective_name', '')}",
                "count": "1",
                "notes": row.get("notes", ""),
            }
        )
    return summary_rows


def main() -> None:
    objectives = read_csv(OBJECTIVES_CSV)
    coverage_rows = read_csv(GUIDE_COVERAGE_CSV)

    coverage_by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in coverage_rows:
        for objective_id in objective_refs(row.get("objective_id", "")):
            coverage_by_objective[objective_id].append(row)

    detail_rows: list[dict[str, str]] = []
    status_counts: Counter[str] = Counter()
    route_placement_counts: Counter[str] = Counter()
    unresolved_by_category: Counter[str] = Counter()
    unresolved_by_subcategory: Counter[str] = Counter()

    for objective in objectives:
        objective_id = objective["objective_id"]
        rows = coverage_by_objective.get(objective_id, [])
        final_status = classify_objective(objective, rows)
        status_counts[final_status] += 1
        route_placement_counts[objective["route_placement"]] += 1
        if final_status == "unresolved":
            unresolved_by_category[objective["category"]] += 1
            unresolved_by_subcategory[f"{objective['category']}:{objective['subcategory']}"] += 1
        detail_rows.append(
            {
                "objective_id": objective_id,
                "objective_name": objective["objective_name"],
                "category": objective["category"],
                "subcategory": objective["subcategory"],
                "route_placement": objective["route_placement"],
                "final_coverage_status": final_status,
                "internal_coverage_row_count": str(len(rows)),
                "coverage_statuses": status_values(rows, "coverage_status"),
                "completion_statuses": status_values(rows, "completion_status"),
                "guide_locations": status_values(rows, "player_facing_location"),
            }
        )

    summary_rows: list[dict[str, str]] = [
        {
            "summary_group": "objective_final_status",
            "metric": "objective_rows_processed",
            "count": str(len(objectives)),
            "notes": "All rows from data/objectives/objectives.csv were classified.",
        },
        {
            "summary_group": "objective_final_status",
            "metric": "placed_in_main_guide",
            "count": str(status_counts["placed_in_main_guide"]),
            "notes": "Non-branch, non-option, non-excluded, non-unresolved objective rows represented in the self-contained guide or promoted guide reference surfaces.",
        },
        {
            "summary_group": "objective_final_status",
            "metric": "branch_handled",
            "count": str(status_counts["branch_handled"]),
            "notes": "Canonical branch_route objective rows handled by branch-first/reload guide blocks after unresolved rows are counted separately.",
        },
        {
            "summary_group": "objective_final_status",
            "metric": "option_default_handled",
            "count": str(status_counts["option_default_handled"]),
            "notes": "Canonical option_list objective rows represented by route defaults and option/default guide surfaces.",
        },
        {
            "summary_group": "objective_final_status",
            "metric": "excluded",
            "count": str(status_counts["excluded"]),
            "notes": "Objective rows with canonical excluded placement or explicit guide/coverage exclusion after unresolved rows are counted separately.",
        },
        {
            "summary_group": "objective_final_status",
            "metric": "unresolved",
            "count": str(status_counts["unresolved"]),
            "notes": "Objective rows with explicit NEEDS ROUTE RESOLUTION coverage, including unresolved branch or appendix rows.",
        },
        {
            "summary_group": "objective_final_status",
            "metric": "total_classified_objective_rows",
            "count": str(sum(status_counts.values())),
            "notes": "Should equal objective_rows_processed.",
        },
    ]

    for route_placement, count in sorted(route_placement_counts.items()):
        summary_rows.append(
            {
                "summary_group": "objective_route_placement_raw",
                "metric": route_placement,
                "count": str(count),
                "notes": "Raw route_placement count from data/objectives/objectives.csv before final-status priority rules.",
            }
        )

    for category, count in sorted(unresolved_by_category.items()):
        summary_rows.append(
            {
                "summary_group": "unresolved_by_category",
                "metric": category,
                "count": str(count),
                "notes": "Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage.",
            }
        )

    for subcategory, count in sorted(unresolved_by_subcategory.items()):
        summary_rows.append(
            {
                "summary_group": "unresolved_by_subcategory",
                "metric": subcategory,
                "count": str(count),
                "notes": "Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage.",
            }
        )

    for audit_csv in AUDIT_CSVS:
        summary_rows.extend(audit_summary(audit_csv))
    summary_rows.extend(cross_cutting_ledger_summaries(coverage_rows))

    with OUTPUT_DETAIL_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(detail_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(detail_rows)

    with OUTPUT_SUMMARY_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["summary_group", "metric", "count", "notes"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Wrote {OUTPUT_SUMMARY_CSV.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUTPUT_DETAIL_CSV.relative_to(REPO_ROOT)}")
    print(
        "Objective final status: "
        + ", ".join(f"{key}={status_counts[key]}" for key in sorted(status_counts))
    )


if __name__ == "__main__":
    main()
