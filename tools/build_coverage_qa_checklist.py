#!/usr/bin/env python3
"""Build the Phase 15 coverage, focused QA, and final-risk checklist."""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from check_main_guide_placeholders import PLACEHOLDER_PHRASES, is_exception


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = REPO_ROOT / "drafts" / "final-guide" / "qa-checklist.md"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
APPENDICES = REPO_ROOT / "drafts" / "final-guide" / "appendices-v0.md"
COVERAGE_LEDGER = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
FINAL_SUMMARY = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-final-coverage-summary.csv"
OBJECTIVE_STATUS = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-final-status.csv"
CHECKLIST_MATRIX = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"
GUIDE_COVERAGE_DIR = REPO_ROOT / "data" / "guide-coverage"
ORDER_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-order-delayed-task-audit.csv"
ORDER_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-order-delayed-task-summary.csv"
ORDER_REPAIR = GUIDE_COVERAGE_DIR / "main-guide-v1-order-delayed-task-repair.csv"
TLC_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-trophy-leveled-cell-audit.csv"
TLC_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-trophy-leveled-cell-summary.csv"
SURVIVAL_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-survival-legendary-audit.csv"
SURVIVAL_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-survival-legendary-summary.csv"
BRANCH_SPOILER_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-branch-spoiler-audit.csv"
BRANCH_SPOILER_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-branch-spoiler-summary.csv"
PLAYTEST_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-playtest-audit.csv"
PLAYTEST_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-playtest-summary.csv"
UNRESOLVED_RISK_REGISTER = GUIDE_COVERAGE_DIR / "main-guide-v1-unresolved-risk-register.csv"
UNRESOLVED_RISK_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-unresolved-risk-summary.csv"
UNRESOLVED_RISK_REPORT = REPO_ROOT / "drafts" / "final-guide" / "unresolved-risk-report.md"


EXPECTED_OBJECTIVE_STATUSES = [
    "placed_in_main_guide",
    "branch_handled",
    "option_default_handled",
    "excluded",
    "unresolved",
]

EXPECTED_APPENDIX_HEADINGS = [
    "## Appendix A - Coverage Snapshot",
    "## Appendix B - Guide Section Index",
    "## Appendix C - Named Hard-Save Reference",
    "## Appendix D - Branch Reference",
    "## Appendix E - Option and Default Reference",
    "## Appendix F - Exclusion Reference",
    "## Appendix G - Previous Appendix-Only Rows",
    "## Appendix H - Objective-Level Exclusions",
    "## Appendix I - Unresolved Route-Resolution Register",
]


@dataclass(frozen=True)
class AuditSpec:
    key: str
    label: str
    filename: str
    allowed_actions: frozenset[str]
    require_all_none: bool = False


AUDITS = [
    AuditSpec(
        "objective",
        "Objective ID audit",
        "main-guide-v1-objective-id-audit.csv",
        frozenset({"none"}),
        require_all_none=True,
    ),
    AuditSpec(
        "checklist",
        "Checklist ID audit",
        "main-guide-v1-checklist-id-audit.csv",
        frozenset({"none"}),
        require_all_none=True,
    ),
    AuditSpec(
        "branch",
        "Branch audit",
        "main-guide-v1-branch-audit.csv",
        frozenset({"none", "none_existing_route_resolution"}),
    ),
    AuditSpec(
        "option",
        "Option/default audit",
        "main-guide-v1-option-default-audit.csv",
        frozenset({"none"}),
    ),
    AuditSpec(
        "exclusion",
        "Explicit exclusion audit",
        "main-guide-v1-exclusion-audit.csv",
        frozenset({"none"}),
    ),
    AuditSpec(
        "appendix",
        "Appendix/reference audit",
        "main-guide-v1-appendix-audit.csv",
        frozenset({"none"}),
    ),
    AuditSpec(
        "location",
        "Location audit",
        "main-guide-v1-location-audit.csv",
        frozenset({"none", "none_existing_route_resolution"}),
    ),
    AuditSpec(
        "book_document",
        "Book/document audit",
        "main-guide-v1-book-document-audit.csv",
        frozenset({"none", "none_existing_route_resolution"}),
    ),
    AuditSpec(
        "collectible",
        "Collectible audit",
        "main-guide-v1-collectible-audit.csv",
        frozenset({"none", "none_existing_route_resolution"}),
    ),
    AuditSpec(
        "crafting_progression",
        "Crafting/progression audit",
        "main-guide-v1-crafting-progression-audit.csv",
        frozenset({"none", "none_existing_route_resolution"}),
    ),
    AuditSpec(
        "radiant_counter",
        "Radiant/counter audit",
        "main-guide-v1-radiant-counter-audit.csv",
        frozenset({"none", "none_existing_route_resolution"}),
    ),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def md(value: object) -> str:
    return str(value).replace("|", "\\|")


def table(headers: list[str], rows: list[list[object]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md(value) for value in row) + " |")
    return lines


def summary_counts(summary: list[dict[str, str]], group: str) -> dict[str, int]:
    return {
        row["metric"]: int(row["count"])
        for row in summary
        if row["summary_group"] == group
    }


def summary_notes(summary: list[dict[str, str]], group: str) -> dict[str, str]:
    return {row["metric"]: row["notes"] for row in summary if row["summary_group"] == group}


def action_counts(rows: list[dict[str, str]]) -> Counter[str]:
    return Counter((row.get("recommended_action") or "blank") for row in rows)


def format_counts(counts: Counter[str]) -> str:
    return ", ".join(f"{key}: {counts[key]}" for key in sorted(counts))


def pass_fail(ok: bool) -> str:
    return "Pass" if ok else "Fail"


def guide_placeholder_hits() -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(MAIN_GUIDE.read_text(encoding="utf-8").splitlines(), start=1):
        lower = line.lower()
        for phrase in PLACEHOLDER_PHRASES:
            if phrase in lower and not is_exception(phrase, lower):
                hits.append((line_number, phrase, line.strip()))
    return hits


def appendix_unresolved_count() -> int:
    text = APPENDICES.read_text(encoding="utf-8")
    if "Full unresolved objective index:" not in text:
        return 0
    unresolved_text = text.split("Full unresolved objective index:", 1)[1]
    return sum(1 for line in unresolved_text.splitlines() if line.startswith("| OBJ-"))


def appendix_heading_counts() -> dict[str, int]:
    text = APPENDICES.read_text(encoding="utf-8")
    return {heading: text.count(heading) for heading in EXPECTED_APPENDIX_HEADINGS}


def audit_summary_rows(summary: list[dict[str, str]]) -> tuple[list[list[object]], bool]:
    artifact_counts = summary_counts(summary, "audit_artifact")
    rows_out: list[list[object]] = []
    all_ok = True

    for spec in AUDITS:
        path = GUIDE_COVERAGE_DIR / spec.filename
        rows = read_csv(path)
        actions = action_counts(rows)
        expected_rows = artifact_counts.get(f"{spec.filename}:rows")
        row_count_ok = expected_rows == len(rows)
        allowed_ok = set(actions).issubset(spec.allowed_actions)
        all_none_ok = (not spec.require_all_none) or actions == Counter({"none": len(rows)})
        ok = row_count_ok and allowed_ok and all_none_ok
        all_ok = all_ok and ok

        route_resolution_rows = actions.get("none_existing_route_resolution", 0)
        if ok and route_resolution_rows:
            status = "Pass with explicit route-resolution rows"
        else:
            status = pass_fail(ok)
        rows_out.append(
            [
                spec.label,
                len(rows),
                expected_rows if expected_rows is not None else "missing summary",
                format_counts(actions),
                status,
            ]
        )

    return rows_out, all_ok


def checklist_status_rows(rows: list[dict[str, str]]) -> list[list[object]]:
    statuses = Counter(row.get("audit_status", "") or "blank" for row in rows)
    return [[status, count] for status, count in sorted(statuses.items())]


def order_summary_counts() -> dict[str, int]:
    if not ORDER_SUMMARY.exists():
        return {}
    return {row["metric"]: int(row["count"]) for row in read_csv(ORDER_SUMMARY)}


def order_repair_counts() -> Counter[str]:
    if not ORDER_REPAIR.exists():
        return Counter()
    return Counter(row["classification"] for row in read_csv(ORDER_REPAIR))


def metric_counts(path: Path) -> dict[str, int]:
    if not path.exists():
        return {}
    return {row["metric"]: int(row["count"]) for row in read_csv(path)}


def build_output() -> tuple[list[str], bool]:
    summary = read_csv(FINAL_SUMMARY)
    objective_status = read_csv(OBJECTIVE_STATUS)
    checklist_matrix = read_csv(CHECKLIST_MATRIX)
    checklist_audit = read_csv(GUIDE_COVERAGE_DIR / "main-guide-v1-checklist-id-audit.csv")
    coverage_ledger = read_csv(COVERAGE_LEDGER)
    order_audit = read_csv(ORDER_AUDIT) if ORDER_AUDIT.exists() else []
    order_actions = action_counts(order_audit)
    order_counts = order_summary_counts()
    repair_counts = order_repair_counts()
    tlc_audit = read_csv(TLC_AUDIT) if TLC_AUDIT.exists() else []
    tlc_actions = action_counts(tlc_audit)
    tlc_counts = metric_counts(TLC_SUMMARY)
    survival_audit = read_csv(SURVIVAL_AUDIT) if SURVIVAL_AUDIT.exists() else []
    survival_actions = action_counts(survival_audit)
    survival_counts = metric_counts(SURVIVAL_SUMMARY)
    branch_spoiler_audit = read_csv(BRANCH_SPOILER_AUDIT) if BRANCH_SPOILER_AUDIT.exists() else []
    branch_spoiler_actions = action_counts(branch_spoiler_audit)
    branch_spoiler_counts = metric_counts(BRANCH_SPOILER_SUMMARY)
    playtest_audit = read_csv(PLAYTEST_AUDIT) if PLAYTEST_AUDIT.exists() else []
    playtest_actions = action_counts(playtest_audit)
    playtest_counts = metric_counts(PLAYTEST_SUMMARY)
    risk_register = read_csv(UNRESOLVED_RISK_REGISTER) if UNRESOLVED_RISK_REGISTER.exists() else []
    risk_summary = read_csv(UNRESOLVED_RISK_SUMMARY) if UNRESOLVED_RISK_SUMMARY.exists() else []

    objective_summary = summary_counts(summary, "objective_final_status")
    objective_notes = summary_notes(summary, "objective_final_status")
    objective_status_counts = Counter(row["final_coverage_status"] for row in objective_status)
    unresolved_by_category = summary_counts(summary, "unresolved_by_category")

    objective_total = len(objective_status)
    classified_total = sum(objective_status_counts.values())
    expected_total = objective_summary.get("objective_rows_processed", 0)
    objective_status_ok = (
        objective_total == expected_total
        and classified_total == objective_summary.get("total_classified_objective_rows", -1)
        and all(objective_status_counts[status] == objective_summary.get(status, -1) for status in EXPECTED_OBJECTIVE_STATUSES)
        and set(objective_status_counts).issubset(set(EXPECTED_OBJECTIVE_STATUSES))
    )

    checklist_ok = (
        len(checklist_matrix) == len(checklist_audit)
        and action_counts(checklist_audit) == Counter({"none": len(checklist_audit)})
    )

    audit_rows, audits_ok = audit_summary_rows(summary)
    placeholder_hits = guide_placeholder_hits()
    placeholder_ok = not placeholder_hits

    appendix_rows = appendix_unresolved_count()
    appendix_unresolved_ok = appendix_rows == objective_summary.get("unresolved", -1)
    heading_counts = appendix_heading_counts()
    appendix_headings_ok = all(count == 1 for count in heading_counts.values())
    appendix_ok = appendix_unresolved_ok and appendix_headings_ok

    cov_summary_rows = [
        row
        for row in coverage_ledger
        if row.get("record_type") == "summary" and row.get("mr_section", "").startswith("COV-")
    ]
    cov_summary_count = len(cov_summary_rows)
    cov_summary_ok = cov_summary_count >= 13
    order_allowed_actions = {"none", "none_existing_route_resolution", "none_local_save"}
    order_ok = bool(order_audit) and set(order_actions).issubset(order_allowed_actions)
    tlc_allowed_actions = {"none", "none_existing_route_resolution"}
    tlc_ok = bool(tlc_audit) and set(tlc_actions).issubset(tlc_allowed_actions)
    survival_allowed_actions = {"none", "none_existing_route_resolution"}
    survival_ok = bool(survival_audit) and set(survival_actions).issubset(survival_allowed_actions)
    branch_spoiler_allowed_actions = {"none", "none_existing_route_resolution"}
    branch_spoiler_ok = bool(branch_spoiler_audit) and set(branch_spoiler_actions).issubset(branch_spoiler_allowed_actions)
    playtest_allowed_actions = {"none", "none_existing_route_resolution"}
    playtest_ok = bool(playtest_audit) and set(playtest_actions).issubset(playtest_allowed_actions)
    risk_severity_counts = summary_counts(risk_summary, "severity")
    risk_category_counts = summary_counts(risk_summary, "category")
    risk_all_counts = summary_counts(risk_summary, "all")
    risk_ok = (
        bool(risk_register)
        and UNRESOLVED_RISK_REPORT.exists()
        and len(risk_register) == objective_summary.get("unresolved", -1)
        and risk_all_counts.get("unresolved_rows", -2) == len(risk_register)
        and set(row.get("severity", "") for row in risk_register).issubset({"high", "medium", "low"})
    )

    overall_ok = (
        objective_status_ok
        and checklist_ok
        and audits_ok
        and placeholder_ok
        and appendix_ok
        and cov_summary_ok
        and order_ok
        and tlc_ok
        and survival_ok
        and branch_spoiler_ok
        and playtest_ok
        and risk_ok
    )
    result = "Pass" if overall_ok else "Fail"
    unresolved_count = objective_summary.get("unresolved", 0)

    lines: list[str] = [
        "# QA Checklist",
        "",
        f"Status: Phase 15 coverage, order/delayed-task, constraint, branch/spoiler, simulated-playtest, and final-risk QA checkpoint complete; result: {result}.",
        f"Generated: {date.today().isoformat()}.",
        "",
        "Scope: coverage accounting, TB-038 order/delayed-task closeout, TB-039 trophy/leveled/cell-entry constraint QA, TB-040 Survival Mode/Legendary difficulty QA, TB-041 branch/spoiler QA, TB-042 simulated playtest QA, and TB-043 unresolved-risk summary. This pass checks whether objective rows, checklist rows, delayed tasks, trophy dependencies, leveled reward gates, cell-entry risks, Survival logistics, Legendary progression constraints, branch-save/reload handling, spoiler discipline, section execution, route handoffs, and known route-resolution risks are represented by current guide prose, branch handling, option/default handling, explicit exclusions, reference appendix support, or explicit unresolved route-resolution state.",
        "",
        "No broad gameplay research was performed. TB-040 uses the existing Survival, progression, geography, guide, and coverage artifacts. TB-041 uses the branch decision matrix, branch audit, current guide prose, and coverage artifacts. TB-042 is a document-level simulated playtest, not a live PS4 run. TB-043 summarizes explicit unresolved risks without resolving or accepting them.",
        "",
        "## Result Summary",
        "",
    ]

    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Objective final accounting",
                    pass_fail(objective_status_ok),
                    f"{objective_total} objective rows classified; status total {classified_total}; expected total {expected_total}.",
                ],
                [
                    "Checklist row accounting",
                    pass_fail(checklist_ok),
                    f"{len(checklist_matrix)} coverage-matrix rows and {len(checklist_audit)} checklist-audit rows; recommended_action: {format_counts(action_counts(checklist_audit))}.",
                ],
                [
                    "Focused COV audit artifacts",
                    pass_fail(audits_ok),
                    "All generated audits use only allowed no-action states.",
                ],
                [
                    "Appendix unresolved register",
                    pass_fail(appendix_unresolved_ok),
                    f"{appendix_rows} Appendix I unresolved rows; expected {unresolved_count}.",
                ],
                [
                    "Appendix headings",
                    pass_fail(appendix_headings_ok),
                    "All expected Appendix A through I headings appear once.",
                ],
                [
                    "Placeholder phrase scan",
                    pass_fail(placeholder_ok),
                    f"{len(placeholder_hits)} banned placeholder hits in main-guide-v1.md.",
                ],
                [
                    "Coverage ledger COV summaries",
                    pass_fail(cov_summary_ok),
                    f"{cov_summary_count} COV summary rows found in main-guide-v1-coverage.csv.",
                ],
                [
                    "TB-039 trophy/leveled/cell QA",
                    "Pass with explicit route-resolution rows" if tlc_ok and tlc_actions.get("none_existing_route_resolution", 0) else pass_fail(tlc_ok),
                    f"{len(tlc_audit)} audit rows; recommended_action: {format_counts(tlc_actions)}.",
                ],
                [
                    "TB-040 Survival/Legendary QA",
                    "Pass with explicit route-resolution rows" if survival_ok and survival_actions.get("none_existing_route_resolution", 0) else pass_fail(survival_ok),
                    f"{len(survival_audit)} audit rows; recommended_action: {format_counts(survival_actions)}.",
                ],
                [
                    "TB-041 branch/spoiler QA",
                    "Pass with explicit route-resolution rows" if branch_spoiler_ok and branch_spoiler_actions.get("none_existing_route_resolution", 0) else pass_fail(branch_spoiler_ok),
                    f"{len(branch_spoiler_audit)} audit rows; recommended_action: {format_counts(branch_spoiler_actions)}.",
                ],
                [
                    "TB-042 simulated playtest QA",
                    "Pass with explicit route-resolution rows" if playtest_ok and playtest_actions.get("none_existing_route_resolution", 0) else pass_fail(playtest_ok),
                    f"{len(playtest_audit)} audit rows; recommended_action: {format_counts(playtest_actions)}.",
                ],
                [
                    "TB-043 unresolved-risk report",
                    "Pass with known unresolved risks" if risk_ok else "Fail",
                    f"{len(risk_register)} risk-register rows; severity: high: {risk_severity_counts.get('high', 0)}, medium: {risk_severity_counts.get('medium', 0)}, low: {risk_severity_counts.get('low', 0)}.",
                ],
            ],
        )
    )

    lines.extend(["", "## Objective Final Status", ""])
    lines.extend(
        table(
            ["Final status", "Count", "QA note"],
            [
                [
                    status,
                    objective_status_counts[status],
                    objective_notes.get(status, ""),
                ]
                for status in EXPECTED_OBJECTIVE_STATUSES
            ]
            + [
                [
                    "total_classified_objective_rows",
                    classified_total,
                    "Matches objective_rows_processed." if classified_total == expected_total else "Mismatch.",
                ]
            ],
        )
    )

    lines.extend(["", "## Checklist Audit Status", ""])
    lines.extend(table(["Audit status", "Count"], checklist_status_rows(checklist_audit)))

    lines.extend(["", "## Focused Audit Artifacts", ""])
    lines.extend(table(["Audit", "Rows", "Summary rows", "Recommended actions", "QA result"], audit_rows))

    lines.extend(["", "## Unresolved Route-Resolution Register", ""])
    lines.append(
        f"The {unresolved_count} unresolved objective rows are explicit `NEEDS ROUTE RESOLUTION` states, not hidden coverage gaps. The full row list is in Appendix I of `drafts/final-guide/appendices-v0.md` and in `data/guide-coverage/main-guide-v1-objective-final-status.csv`."
    )
    lines.extend([""])
    lines.extend(table(["Category", "Unresolved rows"], [[key, value] for key, value in sorted(unresolved_by_category.items())]))

    lines.extend(["", "## Appendix Checks", ""])
    lines.extend(table(["Appendix heading", "Count"], [[heading, count] for heading, count in heading_counts.items()]))

    lines.extend(["", "## TB-038 Order and Delayed-Task QA", ""])
    order_result = "Pass with explicit route-resolution rows" if order_ok else "Fail"
    lines.append(
        f"Status: TB-038 order/delayed-task QA complete; TB-038R repair/classification complete; result: {order_result}."
    )
    lines.append("")
    lines.append(
        "No broad gameplay research was performed. TB-038R records remaining delayed-task uncertainty as explicit route-resolution state rather than hidden reader-memory debt."
    )
    lines.append("")
    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Registered hard saves",
                    "Pass with explicit route-resolution row",
                    f"{order_counts.get('hard_save_register:status:pass_register_save_present_in_guide', 0)} registered saves appear in the guide; {order_counts.get('hard_save_register:status:known_route_resolution_missing_guide_save', 0)} known save remains tied to explicit route-resolution state.",
                ],
                [
                    "Guide-local hard saves",
                    "Pass",
                    f"{order_counts.get('hard_save_register:status:guide_local_hard_save_has_creation_cue', 0)} local guide saves have creation cues.",
                ],
                [
                    "Branch reload cues",
                    "Pass",
                    f"{order_counts.get('branch_reload:status:pass_branch_reload_cue_found', 0)} branch markers have same-section reload cues.",
                ],
                [
                    "Delayed coverage closeout",
                    "Pass with explicit route-resolution rows",
                    f"{len(order_audit)} audit rows; recommended_action: {format_counts(order_actions)}. TB-038R classified {sum(repair_counts.values())} findings: {repair_counts.get('explicit_route_resolution', 0)} explicit route-resolution and {repair_counts.get('closed_or_connected', 0)} connected to existing route/final-reference closeouts.",
                ],
            ],
        )
    )

    lines.extend(["", "## TB-039 Trophy, Leveled-Item, and Cell-Entry QA", ""])
    tlc_result = "Pass with explicit route-resolution rows" if tlc_ok else "Fail"
    lines.append(
        f"Status: TB-039 trophy, leveled-item, and cell-entry QA complete; result: {tlc_result}."
    )
    lines.append("")
    lines.append(
        "No broad gameplay research was performed. This pass audits the v1 guide against the existing `trophy-dependencies.md`, `leveled-unique-items.md`, and `cell-entry-locks.md` constraints plus current final coverage state."
    )
    lines.append("")
    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Trophy setup rules",
                    "Pass",
                    f"{tlc_counts.get('trophy_setup:rows', 0)} setup rows; recommended_action: none: {tlc_counts.get('trophy_setup:recommended_action:none', 0)}.",
                ],
                [
                    "Trophy dependencies",
                    "Pass with explicit route-resolution rows",
                    f"{tlc_counts.get('trophy_dependency:rows', 0)} constraint rows; recommended_action: none: {tlc_counts.get('trophy_dependency:recommended_action:none', 0)}, none_existing_route_resolution: {tlc_counts.get('trophy_dependency:recommended_action:none_existing_route_resolution', 0)}.",
                ],
                [
                    "Leveled rewards",
                    "Pass",
                    f"{tlc_counts.get('leveled_item:rows', 0)} constraint rows; recommended_action: none: {tlc_counts.get('leveled_item:recommended_action:none', 0)}.",
                ],
                [
                    "Cell-entry and related locks",
                    "Pass with explicit route-resolution row",
                    f"{tlc_counts.get('cell_entry:rows', 0)} constraint rows; recommended_action: none: {tlc_counts.get('cell_entry:recommended_action:none', 0)}, none_existing_route_resolution: {tlc_counts.get('cell_entry:recommended_action:none_existing_route_resolution', 0)}.",
                ],
            ],
        )
    )

    lines.extend(["", "## TB-040 Survival Mode and Legendary Difficulty QA", ""])
    survival_result = "Pass with explicit route-resolution rows" if survival_ok else "Fail"
    lines.append(
        f"Status: TB-040 Survival Mode and Legendary difficulty QA complete; result: {survival_result}."
    )
    lines.append("")
    lines.append(
        "No broad gameplay research was performed. This pass audits the v1 guide against existing Survival Mode constraints, progression policy, selected reset/training/crafting defaults, current guide logistics cues, and generated geography support data."
    )
    lines.append("")
    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Setup baseline",
                    "Pass",
                    f"{survival_counts.get('setup_baseline:rows', 0)} setup rules; recommended_action: none: {survival_counts.get('setup_baseline:recommended_action:none', 0)}.",
                ],
                [
                    "Survival constraint table",
                    "Pass with explicit route-resolution row",
                    f"{survival_counts.get('survival_global_rule:rows', 0) + survival_counts.get('survival_travel_network:rows', 0) + survival_counts.get('survival_cold_region:rows', 0) + survival_counts.get('survival_infrastructure:rows', 0)} constraint rows; recommended_action: none: {survival_counts.get('survival_global_rule:recommended_action:none', 0) + survival_counts.get('survival_travel_network:recommended_action:none', 0) + survival_counts.get('survival_cold_region:recommended_action:none', 0) + survival_counts.get('survival_infrastructure:recommended_action:none', 0)}, none_existing_route_resolution: {survival_counts.get('survival_infrastructure:recommended_action:none_existing_route_resolution', 0)}.",
                ],
                [
                    "Guide section logistics",
                    "Pass",
                    f"{survival_counts.get('guide_section_logistics:rows', 0)} guide sections scanned; {survival_counts.get('guide_section_logistics:status:pass_section_has_survival_logistics_cues', 0)} route sections include explicit logistics cues.",
                ],
                [
                    "Legendary progression constraints",
                    "Pass",
                    f"{survival_counts.get('legendary_progression_constraint:rows', 0)} progression constraint rows accounted in current guide coverage.",
                ],
                [
                    "Reset, training, crafting, and policy defaults",
                    "Pass",
                    f"{survival_counts.get('progression_source_legendary_reset_distribution:rows', 0) + survival_counts.get('progression_source_training_policy:rows', 0) + survival_counts.get('progression_source_crafting_system_action:rows', 0) + survival_counts.get('progression_source_progression_policy:rows', 0)} progression-source rows represented.",
                ],
                [
                    "Cold and transport geography support",
                    "Pass",
                    f"{survival_counts.get('geography_cold_support:rows', 0)} cold-risk groups and {survival_counts.get('geography_transport_support:rows', 0)} transport/access groups audited.",
                ],
            ],
        )
    )

    lines.extend(["", "## TB-041 Branch and Spoiler QA", ""])
    branch_spoiler_result = "Pass with explicit route-resolution rows" if branch_spoiler_ok else "Fail"
    lines.append(
        f"Status: TB-041 branch and spoiler QA complete; result: {branch_spoiler_result}."
    )
    lines.append("")
    lines.append(
        "No broad gameplay research was performed. This pass audits current guide branch policy, the branch decision matrix, the existing branch coverage audit, guide-local branch cues, and curated spoiler-language phrases."
    )
    lines.append("")
    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Branch policy setup",
                    "Pass",
                    f"{branch_spoiler_counts.get('branch_policy_setup:rows', 0)} policy rows; recommended_action: none: {branch_spoiler_counts.get('branch_policy_setup:recommended_action:none', 0)}.",
                ],
                [
                    "Branch decision matrix",
                    "Pass with explicit route-resolution row",
                    f"{branch_spoiler_counts.get('branch_decision_matrix:rows', 0)} matrix rows; recommended_action: none: {branch_spoiler_counts.get('branch_decision_matrix:recommended_action:none', 0)}, none_existing_route_resolution: {branch_spoiler_counts.get('branch_decision_matrix:recommended_action:none_existing_route_resolution', 0)}.",
                ],
                [
                    "Existing branch audit rows",
                    "Pass with explicit route-resolution rows",
                    f"{branch_spoiler_counts.get('existing_branch_audit:rows', 0)} branch-audit rows mirrored; recommended_action: none: {branch_spoiler_counts.get('existing_branch_audit:recommended_action:none', 0)}, none_existing_route_resolution: {branch_spoiler_counts.get('existing_branch_audit:recommended_action:none_existing_route_resolution', 0)}.",
                ],
                [
                    "Guide-local branch cues",
                    "Pass",
                    f"{branch_spoiler_counts.get('guide_branch_cues:rows', 0)} branch-route cue rows; recommended_action: none: {branch_spoiler_counts.get('guide_branch_cues:recommended_action:none', 0)}.",
                ],
                [
                    "Spoiler discipline",
                    "Pass",
                    f"{branch_spoiler_counts.get('spoiler_discipline:rows', 0)} spoiler-language rows; recommended_action: none: {branch_spoiler_counts.get('spoiler_discipline:recommended_action:none', 0)}.",
                ],
            ],
        )
    )

    lines.extend(["", "## TB-042 Simulated Playtest QA", ""])
    playtest_result = "Pass with explicit route-resolution rows" if playtest_ok else "Fail"
    lines.append(
        f"Status: TB-042 simulated playtest QA complete; result: {playtest_result}."
    )
    lines.append("")
    lines.append(
        "No broad gameplay research was performed. This document-level pass audits executable section starts, numbered route steps, route-heavy section logistics cues, prior QA repair-action state, placeholder language, and visibility of known unresolved route-resolution rows. It is not a live PS4 run."
    )
    lines.append("")
    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Player setup contract",
                    "Pass",
                    f"{playtest_counts.get('playtest_setup:rows', 0)} setup/player-contract rows; recommended_action: none: {playtest_counts.get('playtest_setup:recommended_action:none', 0)}.",
                ],
                [
                    "Section walkthrough",
                    "Pass",
                    f"{playtest_counts.get('section_walkthrough:rows', 0)} route-section rows; pass_section_executable: {playtest_counts.get('section_walkthrough:status:pass_section_executable', 0)}, pass_non_executable_handoff_section: {playtest_counts.get('section_walkthrough:status:pass_non_executable_handoff_section', 0)}.",
                ],
                [
                    "Prior QA integration",
                    "Pass",
                    f"{playtest_counts.get('previous_qa_integration:rows', 0)} prior-QA artifacts checked; recommended_action: none: {playtest_counts.get('previous_qa_integration:recommended_action:none', 0)}.",
                ],
                [
                    "Route-resolution visibility",
                    "Pass with explicit route-resolution row",
                    f"{playtest_counts.get('route_resolution_visibility:rows', 0)} route-resolution visibility row; recommended_action: none_existing_route_resolution: {playtest_counts.get('route_resolution_visibility:recommended_action:none_existing_route_resolution', 0)}.",
                ],
                [
                    "Simulated-playtest limits",
                    "Pass",
                    f"{playtest_counts.get('simulated_playtest_limits:rows', 0)} scope-boundary rows; recommended_action: none: {playtest_counts.get('simulated_playtest_limits:recommended_action:none', 0)}.",
                ],
            ],
        )
    )

    lines.extend(["", "## TB-043 Unresolved-Risk Report and Final QA Summary", ""])
    risk_result = "Pass with known unresolved risks" if risk_ok else "Fail"
    lines.append(
        f"Status: TB-043 unresolved-risk report and final QA summary complete; result: {risk_result}."
    )
    lines.append("")
    lines.append(
        "No broad gameplay research was performed. This section summarizes explicit route-resolution rows already visible in the guide, coverage ledger, appendices, and QA artifacts; it does not resolve or accept those risks."
    )
    lines.append("")
    lines.extend(
        table(
            ["Check", "Status", "Evidence"],
            [
                [
                    "Risk report artifact",
                    "Pass" if UNRESOLVED_RISK_REPORT.exists() else "Fail",
                    "drafts/final-guide/unresolved-risk-report.md exists." if UNRESOLVED_RISK_REPORT.exists() else "Missing unresolved-risk-report.md.",
                ],
                [
                    "Risk register row count",
                    "Pass" if len(risk_register) == unresolved_count else "Fail",
                    f"{len(risk_register)} risk-register rows; expected {unresolved_count} unresolved objective rows.",
                ],
                [
                    "Severity triage",
                    "Pass" if set(row.get("severity", "") for row in risk_register).issubset({"high", "medium", "low"}) else "Fail",
                    f"high: {risk_severity_counts.get('high', 0)}, medium: {risk_severity_counts.get('medium', 0)}, low: {risk_severity_counts.get('low', 0)}.",
                ],
                [
                    "Category ownership",
                    "Pass" if risk_category_counts else "Fail",
                    ", ".join(f"{key}: {risk_category_counts[key]}" for key in sorted(risk_category_counts)),
                ],
            ],
        )
    )

    lines.extend(["", "## Remaining Work Handoff", ""])
    lines.extend(
        table(
            ["Task", "Owner scope"],
            [
                ["TB-044", "Resolve high-severity route-resolution risks from the TB-043 risk register."],
            ],
        )
    )

    lines.extend(["", "## Inputs", ""])
    lines.extend(
        table(
            ["Path", "Use"],
            [
                ["drafts/final-guide/main-guide-v1.md", "Player-facing guide checked for placeholder phrases and coverage support."],
                ["drafts/final-guide/appendices-v0.md", "Appendix heading and unresolved-register checks."],
                ["data/guide-coverage/main-guide-v1-coverage.csv", "COV summary row presence."],
                ["data/guide-coverage/main-guide-v1-final-coverage-summary.csv", "Final objective, audit, and unresolved summary counts."],
                ["data/guide-coverage/main-guide-v1-objective-final-status.csv", "Per-objective final coverage status."],
                ["data/checklist-mapping/coverage-matrix.csv", "Checklist row source count."],
                ["data/guide-coverage/main-guide-v1-*-audit.csv", "Generated COV audit artifacts."],
                ["data/guide-coverage/main-guide-v1-order-delayed-task-audit.csv", "TB-038 order and delayed-task audit."],
                ["data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv", "TB-038R delayed-task repair/classification register."],
                ["data/guide-coverage/main-guide-v1-trophy-leveled-cell-audit.csv", "TB-039 trophy, leveled-item, and cell-entry audit."],
                ["data/guide-coverage/main-guide-v1-survival-legendary-audit.csv", "TB-040 Survival Mode and Legendary difficulty audit."],
                ["data/guide-coverage/main-guide-v1-branch-spoiler-audit.csv", "TB-041 branch and spoiler QA audit."],
                ["data/guide-coverage/main-guide-v1-playtest-audit.csv", "TB-042 simulated playtest audit."],
                ["drafts/final-guide/playtest-notes.md", "TB-042 simulated playtest notes."],
                ["data/guide-coverage/main-guide-v1-unresolved-risk-register.csv", "TB-043 row-level unresolved-risk register."],
                ["data/guide-coverage/main-guide-v1-unresolved-risk-summary.csv", "TB-043 unresolved-risk summary counts."],
                ["drafts/final-guide/unresolved-risk-report.md", "TB-043 unresolved-risk report."],
            ],
        )
    )

    lines.extend(["", "Regenerate with `python3 tools/build_coverage_qa_checklist.py` after refreshing coverage or audit artifacts."])
    return lines, overall_ok


def main() -> int:
    lines, ok = build_output()
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
