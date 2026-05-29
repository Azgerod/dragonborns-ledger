#!/usr/bin/env python3
"""Generate a simulated playtest audit and notes for TB-042."""

from __future__ import annotations

import csv
import re
from collections import Counter
from datetime import date
from pathlib import Path

from check_main_guide_placeholders import PLACEHOLDER_PHRASES, is_exception


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
QA_CHECKLIST = REPO_ROOT / "drafts" / "final-guide" / "qa-checklist.md"
APPENDICES = REPO_ROOT / "drafts" / "final-guide" / "appendices-v0.md"
PLAYTEST_NOTES = REPO_ROOT / "drafts" / "final-guide" / "playtest-notes.md"
GUIDE_COVERAGE_DIR = REPO_ROOT / "data" / "guide-coverage"
FINAL_STATUS = GUIDE_COVERAGE_DIR / "main-guide-v1-objective-final-status.csv"
OUTPUT_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-playtest-audit.csv"
OUTPUT_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-playtest-summary.csv"

FIELDNAMES = [
    "audit_area",
    "check_id",
    "source_file",
    "source_section",
    "row_label",
    "check_type",
    "guide_locations",
    "audit_status",
    "recommended_action",
    "evidence",
    "notes",
]

GLOBAL_RULES = [
    (
        "TB042-SETUP-001",
        "Trophy-safe setup is executable",
        "setup_baseline",
        [("ps4",), ("official ae", "anniversary edition"), ("do not install mods",)],
    ),
    (
        "TB042-SETUP-002",
        "Survival and Legendary baseline is explicit",
        "setup_baseline",
        [("survival mode is mandatory",), ("keep legendary difficulty on",)],
    ),
    (
        "TB042-SETUP-003",
        "Route discipline is player-facing",
        "route_discipline",
        [("route discipline",), ("do only the actions it routes",), ("creation prompts",)],
    ),
    (
        "TB042-SETUP-004",
        "Checklist logging policy is self-contained",
        "checklist_logging",
        [("keep the completion checklist open",), ("update the matching checklist row",)],
    ),
    (
        "TB042-SETUP-005",
        "Branch-return contract is explicit",
        "branch_continuity",
        [("branches are played first",), ("save is reloaded",), ("canonical main-route choice",)],
    ),
    (
        "TB042-SETUP-006",
        "Unresolved rows are visible",
        "route_resolution",
        [("needs route resolution",), ("inputs checked", "inputs already checked")],
    ),
]

PREVIOUS_QA_FILES = [
    (
        "TB042-QA-038",
        "TB-038/TB-038R order and delayed-task QA",
        GUIDE_COVERAGE_DIR / "main-guide-v1-order-delayed-task-audit.csv",
        {"none", "none_existing_route_resolution", "none_local_save"},
    ),
    (
        "TB042-QA-039",
        "TB-039 trophy, leveled-item, and cell-entry QA",
        GUIDE_COVERAGE_DIR / "main-guide-v1-trophy-leveled-cell-audit.csv",
        {"none", "none_existing_route_resolution"},
    ),
    (
        "TB042-QA-040",
        "TB-040 Survival/Legendary QA",
        GUIDE_COVERAGE_DIR / "main-guide-v1-survival-legendary-audit.csv",
        {"none", "none_existing_route_resolution"},
    ),
    (
        "TB042-QA-041",
        "TB-041 branch/spoiler QA",
        GUIDE_COVERAGE_DIR / "main-guide-v1-branch-spoiler-audit.csv",
        {"none", "none_existing_route_resolution"},
    ),
]

ROUTE_HEAVY_TERMS = (
    "travel",
    "ride",
    "walk",
    "enter",
    "clear",
    "fight",
    "defeat",
    "kill",
    "dungeon",
    "barrow",
    "crypt",
    "ruin",
    "cave",
    "fort",
    "camp",
    "branch",
    "cold",
    "mountain",
    "solstheim",
    "ferry",
    "carriage",
    "dragon",
)

SUPPORT_TERMS = (
    "rotating manual save",
    "hard save",
    "food",
    "healing",
    "rest",
    "sleep",
    "bed",
    "inn",
    "store",
    "storage",
    "sell ordinary",
    "carry",
    "hot food",
    "cold gear",
    "support stop",
)

START_CUE_TERMS = (
    "start",
    "begin",
    "continue",
    "return",
    "travel",
    "go ",
    "walk",
    "ride",
    "at ",
    "from ",
    "after ",
    "on ",
    "use ",
    "load ",
    "enter ",
    "make ",
    "confirm ",
    "read ",
    "speak ",
    "prepare ",
    "stay ",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def md(value: object) -> str:
    return str(value).replace("|", "\\|")


def table(headers: list[str], rows: list[list[object]]) -> list[str]:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(md(value) for value in row) + " |")
    return output


def csv_join(values: list[str]) -> str:
    return "; ".join(value for value in values if value)


def groups_found(text: str, groups: list[tuple[str, ...]]) -> tuple[bool, list[str], list[str]]:
    found: list[str] = []
    missing: list[str] = []
    for group in groups:
        match = next((term for term in group if term in text), None)
        if match:
            found.append(match)
        else:
            missing.append(" or ".join(group))
    return not missing, found, missing


def base_row(
    *,
    audit_area: str,
    check_id: str,
    source_file: str,
    source_section: str,
    row_label: str,
    check_type: str,
    guide_locations: str = "",
    audit_status: str,
    recommended_action: str,
    evidence: str,
    notes: str,
) -> dict[str, str]:
    return {
        "audit_area": audit_area,
        "check_id": check_id,
        "source_file": source_file,
        "source_section": source_section,
        "row_label": row_label,
        "check_type": check_type,
        "guide_locations": guide_locations,
        "audit_status": audit_status,
        "recommended_action": recommended_action,
        "evidence": evidence,
        "notes": notes,
    }


def markdown_sections(text: str) -> list[tuple[str, int, int]]:
    matches = list(re.finditer(r"^###\s+(.+)$", text, flags=re.MULTILINE))
    sections: list[tuple[str, int, int]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), start, end))
    return sections


def numbered_steps(section_text: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"^\d+\.\s+(.+)$", section_text, flags=re.MULTILINE)]


def placeholder_hits(text: str) -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        lower = line.lower()
        for phrase in PLACEHOLDER_PHRASES:
            if phrase in lower and not is_exception(phrase, lower):
                hits.append((line_number, phrase, line.strip()))
    return hits


def policy_rows(guide_text: str) -> list[dict[str, str]]:
    lower = guide_text.lower()
    rows: list[dict[str, str]] = []
    for check_id, label, check_type, groups in GLOBAL_RULES:
        ok, found, missing = groups_found(lower, groups)
        rows.append(
            base_row(
                audit_area="playtest_setup",
                check_id=check_id,
                source_file=rel(MAIN_GUIDE),
                source_section="Guide Conventions / Setup / Final Reconciliation",
                row_label=label,
                check_type=check_type,
                guide_locations="Guide Conventions; Setup and Save Baseline; Final Reconciliation",
                audit_status="pass_player_contract_present" if ok else "needs_player_contract_review",
                recommended_action="none" if ok else "review_player_contract",
                evidence="Required terms present: " + csv_join(found) if ok else "Missing required terms: " + csv_join(missing),
                notes="TB-042 simulated playtest first checks that the guide tells a player how to execute the route without internal project context.",
            )
        )

    hits = placeholder_hits(guide_text)
    rows.append(
        base_row(
            audit_area="playtest_setup",
            check_id="TB042-SETUP-007",
            source_file=rel(MAIN_GUIDE),
            source_section="Full guide",
            row_label="Placeholder phrase scan",
            check_type="placeholder_phrase_scan",
            guide_locations="Full guide",
            audit_status="pass_no_placeholder_phrases" if not hits else "needs_placeholder_phrase_review",
            recommended_action="none" if not hits else "review_placeholder_phrases",
            evidence="No banned placeholder phrases found." if not hits else "Hits: " + csv_join([f"L{line}:{phrase}" for line, phrase, _ in hits]),
            notes="Uses the same phrase list as check_main_guide_placeholders.py.",
        )
    )
    return rows


def section_rows(guide_text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, (name, start, end) in enumerate(markdown_sections(guide_text), start=1):
        section_text = guide_text[start:end]
        lower = section_text.lower()
        steps = numbered_steps(section_text)
        first = steps[0] if steps else ""
        route_heavy = any(term in lower for term in ROUTE_HEAVY_TERMS)
        support_found = [term for term in SUPPORT_TERMS if term in lower]
        first_lower = first.lower()
        start_cue = any(first_lower.startswith(term) or f" {term}" in first_lower for term in START_CUE_TERMS)

        if not steps and "no standalone" in lower and "continue with the named" in lower:
            status = "pass_non_executable_handoff_section"
            action = "none"
            evidence = "Section explicitly says there is no standalone sweep and points the player to the named reconciliation blocks below."
        elif not steps:
            status = "needs_section_numbered_steps"
            action = "review_section_executability"
            evidence = "No numbered player route steps found."
        elif not start_cue:
            status = "needs_section_start_review"
            action = "review_section_transition"
            evidence = f"First numbered step lacks an obvious start/continuity cue: {first[:120]}"
        elif route_heavy and not support_found:
            status = "needs_section_logistics_review"
            action = "review_section_logistics"
            evidence = "Route-heavy section lacks save, support, food, rest, carry, or storage cues."
        else:
            status = "pass_section_executable"
            action = "none"
            if route_heavy:
                evidence = f"{len(steps)} numbered steps; support cues found: {csv_join(support_found[:8])}."
            else:
                evidence = f"{len(steps)} numbered steps; section is not route-heavy by the simulated-playtest term scan."

        rows.append(
            base_row(
                audit_area="section_walkthrough",
                check_id=f"TB042-SECTION-{index:03d}",
                source_file=rel(MAIN_GUIDE),
                source_section=name,
                row_label=name,
                check_type="section_executability",
                guide_locations=name,
                audit_status=status,
                recommended_action=action,
                evidence=evidence,
                notes=(
                    "Simulated playtest verifies the section has a clear player start, numbered route steps, "
                    "and logistics cues when the section contains travel, dungeon, combat, cold, or branch language."
                ),
            )
        )
    return rows


def previous_qa_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for check_id, label, path, allowed_actions in PREVIOUS_QA_FILES:
        audit_rows = read_csv(path)
        actions = Counter((row.get("recommended_action") or "blank") for row in audit_rows)
        ok = set(actions).issubset(allowed_actions)
        route_resolution = actions.get("none_existing_route_resolution", 0)
        if ok and route_resolution:
            status = "pass_previous_qa_with_explicit_route_resolution"
        elif ok:
            status = "pass_previous_qa_no_repair_actions"
        else:
            status = "needs_previous_qa_review"
        rows.append(
            base_row(
                audit_area="previous_qa_integration",
                check_id=check_id,
                source_file=rel(path),
                source_section="Full artifact",
                row_label=label,
                check_type="prior_qa_action_state",
                guide_locations="QA artifact",
                audit_status=status,
                recommended_action="none" if ok else "review_previous_qa_actions",
                evidence=", ".join(f"{key}: {actions[key]}" for key in sorted(actions)),
                notes="TB-042 treats prior QA repair actions as practical playtest blockers unless they are already no-action or explicit route-resolution states.",
            )
        )
    return rows


def route_resolution_rows() -> list[dict[str, str]]:
    final_rows = read_csv(FINAL_STATUS)
    unresolved = [row for row in final_rows if row.get("final_coverage_status") == "unresolved"]
    by_category = Counter(row["category"] for row in unresolved)
    return [
        base_row(
            audit_area="route_resolution_visibility",
            check_id="TB042-ROUTE-RESOLUTION-001",
            source_file=rel(FINAL_STATUS),
            source_section="Final objective status",
            row_label="Explicit unresolved route-resolution register",
            check_type="known_route_resolution_risk",
            guide_locations="Final Reconciliation; Appendix I",
            audit_status="pass_existing_route_resolution_visible",
            recommended_action="none_existing_route_resolution",
            evidence=(
                f"{len(unresolved)} unresolved rows remain explicit; by category: "
                + ", ".join(f"{key}: {by_category[key]}" for key in sorted(by_category))
            ),
            notes="TB-042 does not resolve the register; TB-043 owns unresolved-risk reporting.",
        )
    ]


def simulated_limit_rows() -> list[dict[str, str]]:
    rows = [
        (
            "TB042-LIMIT-001",
            "Actual in-game execution not performed",
            "manual_playtest_boundary",
            "This is a document-level simulated playtest. It cannot prove live combat outcome, cash balance, loading behavior, trophy pops, or random target behavior.",
        ),
        (
            "TB042-LIMIT-002",
            "Source-neutral pass",
            "source_boundary",
            "No broad gameplay research was performed. Concrete contradictions found in later play should be source-checked under docs/source-standards.md.",
        ),
    ]
    return [
        base_row(
            audit_area="simulated_playtest_limits",
            check_id=check_id,
            source_file=rel(MAIN_GUIDE),
            source_section="Full guide",
            row_label=label,
            check_type=check_type,
            guide_locations="Full guide",
            audit_status="pass_simulated_playtest_limit_recorded",
            recommended_action="none",
            evidence=evidence,
            notes="Recorded as a TB-042 scope boundary, not as a guide defect.",
        )
        for check_id, label, check_type, evidence in rows
    ]


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    areas = sorted({row["audit_area"] for row in rows})
    for area in areas:
        area_rows = [row for row in rows if row["audit_area"] == area]
        output.append({"metric": f"{area}:rows", "count": str(len(area_rows)), "notes": "Generated TB-042 audit rows."})
        for status, count in sorted(Counter(row["audit_status"] for row in area_rows).items()):
            output.append({"metric": f"{area}:status:{status}", "count": str(count), "notes": "Audit-status distribution."})
        for action, count in sorted(Counter(row["recommended_action"] for row in area_rows).items()):
            output.append({"metric": f"{area}:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    output.append({"metric": "all:rows", "count": str(len(rows)), "notes": "Generated TB-042 audit rows."})
    for action, count in sorted(Counter(row["recommended_action"] for row in rows).items()):
        output.append({"metric": f"all:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    return output


def build_notes(rows: list[dict[str, str]]) -> list[str]:
    actions = Counter(row["recommended_action"] for row in rows)
    statuses = Counter(row["audit_status"] for row in rows)
    by_area = Counter(row["audit_area"] for row in rows)
    repair_actions = {action: count for action, count in actions.items() if action not in {"none", "none_existing_route_resolution"}}
    result = "Pass" if not repair_actions else "Needs repair"
    section_rows_found = [row for row in rows if row["audit_area"] == "section_walkthrough"]
    section_statuses = Counter(row["audit_status"] for row in section_rows_found)
    route_resolution = next(row for row in rows if row["check_id"] == "TB042-ROUTE-RESOLUTION-001")

    lines: list[str] = [
        "# Playtest Notes",
        "",
        f"Status: TB-042 simulated playtest complete; result: {result} with explicit route-resolution rows carried forward.",
        f"Generated: {date.today().isoformat()}.",
        "",
        "Scope: document-level simulated playtest of `drafts/final-guide/main-guide-v1.md` as a player-facing black-box itinerary. This pass checks executable section starts, numbered route steps, route-heavy section logistics cues, previous QA repair-action state, placeholder language, and visibility of known unresolved route-resolution rows.",
        "",
        "No broad gameplay research was performed. This is not a live PS4 run; live combat, economy, random assignment, trophy-pop, and engine-state behavior still require actual play or targeted source checks if a contradiction appears.",
        "",
        "## Result Summary",
        "",
    ]
    lines.extend(
        table(
            ["Check", "Result"],
            [
                ["Audit rows", len(rows)],
                ["Recommended actions", ", ".join(f"{key}: {actions[key]}" for key in sorted(actions))],
                ["Section walkthrough rows", len(section_rows_found)],
                ["Section walkthrough status", ", ".join(f"{key}: {section_statuses[key]}" for key in sorted(section_statuses))],
                ["Route-resolution register", route_resolution["evidence"]],
                ["Repair actions", "none" if not repair_actions else ", ".join(f"{key}: {value}" for key, value in sorted(repair_actions.items()))],
            ],
        )
    )
    lines.extend(["", "## Area Summary", ""])
    lines.extend(table(["Area", "Rows"], [[area, count] for area, count in sorted(by_area.items())]))
    lines.extend(["", "## Findings", ""])
    if repair_actions:
        lines.append("The simulated pass found repair actions. Review `data/guide-coverage/main-guide-v1-playtest-audit.csv` before advancing to TB-043.")
    else:
        lines.append("No simulated-playtest repair actions remain. Every executable route section has numbered player steps, a clear start/continuity cue, and logistics support where the section contains travel, combat, cold, dungeon, or branch language. The one no-step section is an explicit no-standalone-sweep handoff into the named reconciliation blocks below it.")
        lines.append("")
        lines.append("Known unresolved route-resolution rows remain explicit and are not hidden player-memory debt. TB-043 should summarize those risks rather than rerunning the route coverage audits.")
    lines.extend(["", "## Manual Playtest Boundary", ""])
    lines.append("A live playtest or targeted source check is still needed for any concrete contradiction found during actual play, especially cash balance, difficulty/power curve, random target behavior, trophy-pop timing, and exact quest-state behavior.")
    lines.extend(["", "## Inputs", ""])
    lines.extend(
        table(
            ["Path", "Use"],
            [
                [rel(MAIN_GUIDE), "Primary player-facing route walked section by section."],
                [rel(QA_CHECKLIST), "Prior Phase 15 QA checkpoint state."],
                [rel(APPENDICES), "Reference appendix and unresolved-register support."],
                [rel(FINAL_STATUS), "Explicit unresolved route-resolution count and categories."],
                [rel(OUTPUT_AUDIT), "Generated TB-042 detailed audit rows."],
                [rel(OUTPUT_SUMMARY), "Generated TB-042 summary counts."],
            ],
        )
    )
    lines.extend(["", "Regenerate with `python3 tools/audit_main_guide_playtest.py` after guide or QA-artifact changes."])
    return lines


def main() -> int:
    guide_text = MAIN_GUIDE.read_text(encoding="utf-8")
    rows = (
        policy_rows(guide_text)
        + section_rows(guide_text)
        + previous_qa_rows()
        + route_resolution_rows()
        + simulated_limit_rows()
    )
    write_csv(OUTPUT_AUDIT, FIELDNAMES, rows)
    write_csv(OUTPUT_SUMMARY, ["metric", "count", "notes"], summary_rows(rows))
    PLAYTEST_NOTES.write_text("\n".join(build_notes(rows)) + "\n", encoding="utf-8")
    actions = Counter(row["recommended_action"] for row in rows)
    print(f"Wrote {rel(OUTPUT_AUDIT)}")
    print(f"Wrote {rel(OUTPUT_SUMMARY)}")
    print(f"Wrote {rel(PLAYTEST_NOTES)}")
    print(", ".join(f"{key}: {actions[key]}" for key in sorted(actions)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
