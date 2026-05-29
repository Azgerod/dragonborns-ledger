#!/usr/bin/env python3
"""Build the TB-036 appendices-v0 draft from current guide artifacts."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT = REPO_ROOT / "drafts" / "final-guide" / "appendices-v0.md"
HARD_SAVE_MD = REPO_ROOT / "data" / "constraints" / "quest-conflicts-hard-saves.md"
FINAL_SUMMARY_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-final-coverage-summary.csv"
OBJECTIVE_STATUS_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-final-status.csv"
BRANCH_AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-branch-audit.csv"
OPTION_AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-option-default-audit.csv"
EXCLUSION_AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-exclusion-audit.csv"
APPENDIX_AUDIT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-appendix-audit.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def compact(value: str, max_len: int = 180) -> str:
    text = re.sub(r"\s+", " ", value or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def md(value: str, max_len: int = 180) -> str:
    text = compact(value, max_len=max_len)
    return text.replace("|", "\\|")


def table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(md(value) for value in row) + " |")
    return lines


def guide_heading_rows() -> list[list[str]]:
    rows: list[list[str]] = []
    with MAIN_GUIDE.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if line.startswith("## ") and not line.startswith("### "):
                rows.append([str(line_no), "Part", line.removeprefix("## ").strip()])
            elif line.startswith("### "):
                rows.append([str(line_no), "Section", line.removeprefix("### ").strip()])
    return rows


def hard_save_rows() -> list[list[str]]:
    rows: list[list[str]] = []
    in_table = False
    with HARD_SAVE_MD.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("## TB-032 Hard-Save Placement Register"):
                in_table = True
                continue
            if in_table and line.startswith("## "):
                break
            if not in_table or not line.startswith("| "):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if not cells or cells[0] in {"Hard-save name", "---"}:
                continue
            rows.append(cells[:4])
    return rows


def summary_rows(summary: list[dict[str, str]], group: str) -> list[list[str]]:
    return [[row["metric"], row["count"], row["notes"]] for row in summary if row["summary_group"] == group]


def audit_artifact_rows(summary: list[dict[str, str]]) -> list[list[str]]:
    artifacts: dict[str, dict[str, str]] = defaultdict(dict)
    for row in summary:
        metric = row["metric"]
        if row["summary_group"] == "audit_artifact":
            artifact = metric.removesuffix(":rows")
            artifacts[artifact]["rows"] = row["count"]
        elif row["summary_group"] == "audit_recommended_action":
            artifact, action = metric.split(":", 1)
            artifacts[artifact][action] = row["count"]
    ordered = []
    for artifact in sorted(artifacts):
        data = artifacts[artifact]
        actions = ", ".join(
            f"{action}: {count}" for action, count in sorted(data.items()) if action != "rows"
        )
        ordered.append([artifact, data.get("rows", ""), actions])
    return ordered


def branch_rows() -> list[list[str]]:
    rows = []
    for row in read_csv(BRANCH_AUDIT_CSV):
        record_id = row["checklist_id"] or row["objective_id"] or row["record_id"]
        rows.append(
            [
                row["audit_source"],
                record_id,
                row["name"],
                row["branch_name"],
                row["expected_hard_save_aliases"],
                row["guide_locations"],
                row["audit_status"],
            ]
        )
    return rows


def option_rows() -> list[list[str]]:
    rows = []
    for row in read_csv(OPTION_AUDIT_CSV):
        rows.append(
            [
                row["checklist_id"],
                row["checklist_entry"],
                row["category"],
                row["support_option_types"] or row["matched_objective_name"],
                row["guide_locations"],
                row["audit_status"],
            ]
        )
    return rows


def exclusion_summary_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    by_category = Counter(row["category"] or "uncategorized" for row in rows)
    return [[category, str(count)] for category, count in sorted(by_category.items())]


def notable_exclusion_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    notable = []
    for row in rows:
        if row["category"] == "general_book" and not row["objective_id"]:
            continue
        notable.append(
            [
                row["checklist_id"],
                row["checklist_entry"],
                row["category"],
                row["objective_id"],
                row["exclusion_reason"],
                row["guide_locations"],
            ]
        )
    return notable


def appendix_audit_rows() -> list[list[str]]:
    rows = []
    for row in read_csv(APPENDIX_AUDIT_CSV):
        rows.append(
            [
                row["checklist_id"],
                row["checklist_entry"],
                row["category"],
                row["raw_group"],
                row["guide_locations"],
                row["audit_status"],
            ]
        )
    return rows


def unresolved_rows(objective_status: list[dict[str, str]]) -> list[list[str]]:
    rows = []
    for row in objective_status:
        if row["final_coverage_status"] != "unresolved":
            continue
        rows.append(
            [
                row["objective_id"],
                row["objective_name"],
                row["category"],
                row["subcategory"],
                row["route_placement"],
                row["guide_locations"],
            ]
        )
    return rows


def status_count_rows(objective_status: list[dict[str, str]], status: str) -> list[list[str]]:
    rows = []
    for row in objective_status:
        if row["final_coverage_status"] != status:
            continue
        rows.append(
            [
                row["objective_id"],
                row["objective_name"],
                row["category"],
                row["subcategory"],
                row["route_placement"],
                row["guide_locations"],
            ]
        )
    return rows


def main() -> None:
    summary = read_csv(FINAL_SUMMARY_CSV)
    objective_status = read_csv(OBJECTIVE_STATUS_CSV)
    exclusion_rows = read_csv(EXCLUSION_AUDIT_CSV)

    lines: list[str] = [
        "# Appendices v0",
        "",
        "Status: TB-036 draft generated from current guide and coverage artifacts.",
        "",
        "These appendices are reference and verification material for `main-guide-v1.md`. The main guide remains the execution source. If a table here exposes a missing route instruction, fix the guide and coverage tracker rather than treating this appendix as the only instruction.",
        "",
        "## Appendix A - Coverage Snapshot",
        "",
        "Final objective status totals:",
        "",
    ]
    lines.extend(table(["Metric", "Count", "Notes"], summary_rows(summary, "objective_final_status")))
    lines.extend(["", "Raw objective route-placement counts before final-status priority rules:", ""])
    lines.extend(table(["Route placement", "Count", "Notes"], summary_rows(summary, "objective_route_placement_raw")))
    lines.extend(["", "Generated audit artifacts:", ""])
    lines.extend(table(["Artifact", "Rows", "Recommended-action counts"], audit_artifact_rows(summary)))

    lines.extend(["", "## Appendix B - Guide Section Index", ""])
    lines.extend(table(["Line", "Level", "Heading"], guide_heading_rows()))

    lines.extend(["", "## Appendix C - Named Hard-Save Reference", ""])
    lines.append("This table mirrors the current hard-save register for quick review. The guide route still controls when each save is made and reloaded.")
    lines.extend([""])
    lines.extend(table(["Hard-save name", "Place immediately before", "Main continuity after branch/audit", "Warning-layer note"], hard_save_rows()))

    lines.extend(["", "## Appendix D - Branch Reference", ""])
    lines.append("Branch rows are branch-experienced unless the guide states they resolve on main continuity before the branch lockout.")
    lines.extend([""])
    lines.extend(table(["Source", "Row ID", "Name", "Branch", "Hard save", "Guide location", "Audit status"], branch_rows()))

    lines.extend(["", "## Appendix E - Option and Default Reference", ""])
    lines.append("These rows summarize option-list/default coverage. They do not require the player to branch isolated preference choices.")
    lines.extend([""])
    lines.extend(table(["Checklist ID", "Entry", "Category", "Option type or objective", "Guide location", "Audit status"], option_rows()))

    lines.extend(["", "## Appendix F - Exclusion Reference", ""])
    lines.append("The exclusion audit covers all explicit exclusions. Broad regular-book exclusions are summarized here; non-book or objective-linked exclusions are listed below.")
    lines.extend(["", "Exclusion audit rows by category:", ""])
    lines.extend(table(["Category", "Rows"], exclusion_summary_rows(exclusion_rows)))
    lines.extend(["", "Notable non-book or objective-linked exclusions:", ""])
    lines.extend(table(["Checklist ID", "Entry", "Category", "Objective ID", "Reason", "Guide location"], notable_exclusion_rows(exclusion_rows)))

    lines.extend(["", "## Appendix G - Previous Appendix-Only Rows", ""])
    lines.append("These are checklist rows that used to be appendix-only. TB-035-COV-006 verified they are represented in `main-guide-v1.md`; this table is a reviewer index.")
    lines.extend([""])
    lines.extend(table(["Checklist ID", "Entry", "Category", "Raw group", "Guide location", "Audit status"], appendix_audit_rows()))

    lines.extend(["", "## Appendix H - Objective-Level Exclusions", ""])
    lines.append("These are objective rows classified as excluded by the final coverage summary.")
    lines.extend([""])
    lines.extend(table(["Objective ID", "Objective", "Category", "Subcategory", "Route placement", "Guide location"], status_count_rows(objective_status, "excluded")))

    lines.extend(["", "## Appendix I - Unresolved Route-Resolution Register", ""])
    lines.append("These 248 objective rows have explicit `NEEDS ROUTE RESOLUTION` coverage. They are not silent appendix-only coverage; the guide and coverage tracker carry the missing-fact notes.")
    lines.extend(["", "Unresolved rows by category:", ""])
    lines.extend(table(["Category", "Count", "Notes"], summary_rows(summary, "unresolved_by_category")))
    lines.extend(["", "Unresolved rows by subcategory:", ""])
    lines.extend(table(["Subcategory", "Count", "Notes"], summary_rows(summary, "unresolved_by_subcategory")))
    lines.extend(["", "Full unresolved objective index:", ""])
    lines.extend(table(["Objective ID", "Objective", "Category", "Subcategory", "Route placement", "Guide location"], unresolved_rows(objective_status)))

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
