#!/usr/bin/env python3
"""Audit branch handling and spoiler discipline for TB-041."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
BRANCH_README = REPO_ROOT / "drafts" / "branch-routes" / "README.md"
GUIDE_COVERAGE_DIR = REPO_ROOT / "data" / "guide-coverage"
BRANCH_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-branch-audit.csv"
OUTPUT_AUDIT = GUIDE_COVERAGE_DIR / "main-guide-v1-branch-spoiler-audit.csv"
OUTPUT_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-branch-spoiler-summary.csv"

FIELDNAMES = [
    "audit_area",
    "check_id",
    "source_file",
    "source_section",
    "row_label",
    "check_type",
    "branch_id",
    "hard_save",
    "guide_locations",
    "audit_status",
    "recommended_action",
    "evidence",
    "notes",
]

BRANCH_REQUIRED_TREATMENTS = (
    "full branch route",
    "compact branch route",
    "reward branch",
    "trophy branch",
    "two compact",
)

SPOILER_PHRASES = (
    "spoiler",
    "plot twist",
    "backstory",
    "lore explanation",
    "reveals that",
    "turns out",
    "secretly",
)

BRANCH_CUE_RE = re.compile(r"\bbranch route(?:\s*:|\s+from\b|\s+first\b)", re.IGNORECASE)

POLICY_RULES = [
    (
        "TB041-POLICY-001",
        "Named hard-save convention",
        "branch_policy",
        [("named saves are written as",), ("hard save: hs-name",)],
    ),
    (
        "TB041-POLICY-002",
        "Branch-first reload policy",
        "branch_policy",
        [("branches are played first",), ("save is reloaded",), ("canonical main-route choice",)],
    ),
    (
        "TB041-POLICY-003",
        "Branch checklist state policy",
        "branch_policy",
        [("branch checklist rows",), ("branch-experienced",), ("final main-save world state",)],
    ),
    (
        "TB041-POLICY-004",
        "Final branch-state reconciliation",
        "branch_reconciliation",
        [("final reconciliation",), ("relevant named branch save",), ("final continuity state",)],
    ),
]


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


def csv_join(values: list[str]) -> str:
    return "; ".join(value for value in values if value)


def clean_cell(value: str) -> str:
    value = re.sub(r"`([^`]*)`", r"\1", value)
    return re.sub(r"\s+", " ", value).strip().rstrip(".")


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
    branch_id: str = "",
    hard_save: str = "",
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
        "branch_id": branch_id,
        "hard_save": hard_save,
        "guide_locations": guide_locations,
        "audit_status": audit_status,
        "recommended_action": recommended_action,
        "evidence": evidence,
        "notes": notes,
    }


def parse_branch_matrix() -> list[dict[str, str]]:
    text = BRANCH_README.read_text(encoding="utf-8")
    rows: list[dict[str, str]] = []
    headers: list[str] = []
    in_matrix = False

    for line in text.splitlines():
        if line.startswith("| ID | Decision point |"):
            headers = [clean_cell(cell).lower().replace(" ", "_").replace("-", "_") for cell in line.strip("|").split("|")]
            in_matrix = True
            continue
        if not in_matrix:
            continue
        if not line.startswith("| "):
            break
        raw_cells = [cell.strip() for cell in line.strip("|").split("|")]
        if raw_cells and set("".join(raw_cells)) <= {"-", ":", " "}:
            continue
        if len(raw_cells) != len(headers):
            continue
        rows.append(dict(zip(headers, [clean_cell(cell) for cell in raw_cells])))

    return rows


def markdown_sections(text: str) -> list[tuple[str, int, int]]:
    matches = list(re.finditer(r"^(#{2,3})\s+(.+)$", text, flags=re.MULTILINE))
    sections: list[tuple[str, int, int]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((clean_cell(match.group(2)), start, end))
    return sections


def section_name_for_index(sections: list[tuple[str, int, int]], index: int) -> str:
    for name, start, end in sections:
        if start <= index < end:
            return name
    return "Document preface"


def section_text_for_index(text: str, sections: list[tuple[str, int, int]], index: int) -> tuple[str, str]:
    for name, start, end in sections:
        if start <= index < end:
            return name, text[start:end]
    return "Document preface", text[: index + 1]


def locations_for_term(text: str, sections: list[tuple[str, int, int]], term: str) -> str:
    names: list[str] = []
    for match in re.finditer(re.escape(term), text):
        name = section_name_for_index(sections, match.start())
        if name not in names:
            names.append(name)
    return csv_join(names)


def hard_save_alias(value: str) -> str:
    match = re.search(r"HS-[A-Z0-9-]+", value)
    return match.group(0) if match else clean_cell(value)


def branch_id(value: str) -> str:
    match = re.search(r"BR-\d{3}", value)
    return match.group(0) if match else ""


def route_resolution_branch_ids(branch_audit_rows: list[dict[str, str]]) -> set[str]:
    output: set[str] = set()
    for row in branch_audit_rows:
        if row.get("recommended_action") == "none_existing_route_resolution":
            code = branch_id(row.get("branch_name", ""))
            if code:
                output.add(code)
    return output


def reload_near_alias(text: str, alias: str, radius: int = 2200) -> bool:
    if not alias:
        return False
    for match in re.finditer(re.escape(alias), text):
        start = max(0, match.start() - radius)
        end = min(len(text), match.end() + radius)
        if "reload" in text[start:end].lower():
            return True
    return False


def treatment_requires_branch(treatment: str) -> bool:
    lower = treatment.lower()
    return any(marker in lower for marker in BRANCH_REQUIRED_TREATMENTS)


def policy_rows(guide_text: str) -> list[dict[str, str]]:
    lower = guide_text.lower()
    rows: list[dict[str, str]] = []
    for check_id, label, check_type, groups in POLICY_RULES:
        ok, found, missing = groups_found(lower, groups)
        rows.append(
            base_row(
                audit_area="branch_policy_setup",
                check_id=check_id,
                source_file=rel(MAIN_GUIDE),
                source_section="Guide Conventions / Final Reconciliation",
                row_label=label,
                check_type=check_type,
                guide_locations="Guide Conventions; Final Reconciliation",
                audit_status="pass_policy_rule_present" if ok else "needs_branch_policy_review",
                recommended_action="none" if ok else "review_branch_policy_text",
                evidence=(
                    "Required terms present: " + csv_join(found)
                    if ok
                    else "Missing required terms: " + csv_join(missing)
                ),
                notes="TB-041 checks the player-facing branch contract before auditing individual branch rows.",
            )
        )
    return rows


def decision_matrix_rows(
    guide_text: str,
    sections: list[tuple[str, int, int]],
    route_resolution_ids: set[str],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in parse_branch_matrix():
        code = row["id"]
        alias = hard_save_alias(row["hard_save"])
        treatment = row["treatment"]
        locations = locations_for_term(guide_text, sections, alias)
        present = alias in guide_text
        reload_present = reload_near_alias(guide_text, alias)
        required = treatment_requires_branch(treatment)
        main_resolved = "main-route resolved" in treatment.lower()

        if required:
            if present and reload_present:
                status = "pass_branch_save_reload_present"
                action = "none"
                evidence = f"{alias} appears in guide branch handling with a nearby reload cue."
            elif code in route_resolution_ids:
                status = "pass_existing_route_resolution"
                action = "none_existing_route_resolution"
                evidence = f"{code} is explicitly retained as an existing route-resolution row in the branch audit."
            elif present:
                status = "needs_branch_reload_review"
                action = "review_branch_reload_cue"
                evidence = f"{alias} appears in the guide, but no nearby reload cue was found."
            else:
                status = "needs_branch_save_review"
                action = "review_branch_hard_save"
                evidence = f"{alias} was not found in the guide and no explicit route-resolution branch row was found."
        elif main_resolved:
            if present and code == "BR-018" and reload_present:
                status = "pass_main_resolved_optional_branch_save"
                action = "none"
                evidence = f"{alias} appears with an optional branch-and-reload handling for the compact Ralis outcome."
            elif present:
                status = "pass_main_route_resolved_no_full_branch"
                action = "none"
                evidence = f"{alias} appears in main-route-resolved handling; no full branch is required by the matrix."
            elif code in route_resolution_ids:
                status = "pass_existing_route_resolution"
                action = "none_existing_route_resolution"
                evidence = f"{code} is explicitly retained as an existing route-resolution row in the branch audit."
            else:
                status = "needs_main_resolved_branch_review"
                action = "review_main_resolved_branch_state"
                evidence = f"{alias} was not found in the guide for a main-route-resolved decision."
        else:
            status = "pass_non_branch_treatment"
            action = "none"
            evidence = f"Treatment is {treatment}; no branch-save audit required."

        rows.append(
            base_row(
                audit_area="branch_decision_matrix",
                check_id=f"TB041-MATRIX-{code}",
                source_file=rel(BRANCH_README),
                source_section="Branch Decision Matrix",
                row_label=row["decision_point"],
                check_type=treatment,
                branch_id=code,
                hard_save=alias,
                guide_locations=locations,
                audit_status=status,
                recommended_action=action,
                evidence=evidence,
                notes=f"Canonical main continuity: {row['canonical_main_continuity']}. Matrix notes: {row['notes']}",
            )
        )
    return rows


def existing_branch_audit_rows(rows_in: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source_row in rows_in:
        action = source_row.get("recommended_action", "")
        if action == "none":
            status = "pass_existing_branch_audit_row"
            recommended = "none"
        elif action == "none_existing_route_resolution":
            status = "pass_existing_route_resolution"
            recommended = "none_existing_route_resolution"
        else:
            status = "needs_existing_branch_audit_review"
            recommended = action or "review_branch_coverage"

        rows.append(
            base_row(
                audit_area="existing_branch_audit",
                check_id=f"TB041-EXISTING-{source_row['record_id']}",
                source_file=rel(BRANCH_AUDIT),
                source_section=source_row.get("branch_name", ""),
                row_label=source_row.get("name", ""),
                check_type=source_row.get("audit_source", ""),
                branch_id=branch_id(source_row.get("branch_name", "")),
                hard_save=source_row.get("expected_hard_save_aliases", ""),
                guide_locations=source_row.get("guide_locations", ""),
                audit_status=status,
                recommended_action=recommended,
                evidence=(
                    f"Existing branch audit status {source_row.get('audit_status', '')}; "
                    f"coverage {source_row.get('coverage_statuses', '')}; completion {source_row.get('completion_statuses', '')}."
                ),
                notes=source_row.get("notes", ""),
            )
        )
    return rows


def guide_branch_cue_rows(guide_text: str, sections: list[tuple[str, int, int]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    running_index = 0
    for line_number, line in enumerate(guide_text.splitlines(), start=1):
        line_start = guide_text.find(line, running_index)
        running_index = line_start + len(line)
        if not BRANCH_CUE_RE.search(line):
            continue

        section_name, section_text = section_text_for_index(guide_text, sections, line_start)
        section_lower = section_text.lower()
        line_lower = line.lower()
        hard_saves = sorted(set(re.findall(r"HS-[A-Z0-9-]+", section_text)))
        has_save_cue = (
            "hard save" in section_lower
            or "rotating manual save" in line_lower
            or bool(re.search(r"HS-[A-Z0-9-]+", line))
        )
        has_reload_cue = "reload" in section_lower or "reload" in line_lower

        if has_save_cue and has_reload_cue:
            status = "pass_branch_cue_has_save_and_reload"
            action = "none"
            evidence = "Branch cue appears in a section with explicit save and reload instructions."
        elif has_save_cue:
            status = "needs_branch_reload_review"
            action = "review_branch_reload_cue"
            evidence = "Branch cue appears with a save cue, but no reload cue was found in the section."
        else:
            status = "needs_branch_save_review"
            action = "review_branch_hard_save"
            evidence = "Branch cue lacks a nearby hard-save or manual-save cue."

        rows.append(
            base_row(
                audit_area="guide_branch_cues",
                check_id=f"TB041-GUIDE-L{line_number:04d}",
                source_file=rel(MAIN_GUIDE),
                source_section=section_name,
                row_label=line.strip()[:120],
                check_type="guide_branch_route_cue",
                hard_save=csv_join(hard_saves),
                guide_locations=section_name,
                audit_status=status,
                recommended_action=action,
                evidence=evidence,
                notes="TB-041 guide-local scan checks branch-route prose for continuity protection cues; it does not add gameplay facts.",
            )
        )
    return rows


def spoiler_rows(guide_text: str) -> list[dict[str, str]]:
    hits: list[str] = []
    for line_number, line in enumerate(guide_text.splitlines(), start=1):
        lower = line.lower()
        for phrase in SPOILER_PHRASES:
            if phrase in lower:
                hits.append(f"L{line_number}:{phrase}:{line.strip()[:90]}")

    rows = [
        base_row(
            audit_area="spoiler_discipline",
            check_id="TB041-SPOILER-001",
            source_file=rel(MAIN_GUIDE),
            source_section="Full guide",
            row_label="Narrative-spoiler phrase scan",
            check_type="spoiler_phrase_scan",
            guide_locations="Full guide",
            audit_status="pass_spoiler_phrase_scan" if not hits else "needs_spoiler_language_review",
            recommended_action="none" if not hits else "review_spoiler_language",
            evidence="No curated spoiler phrases found." if not hits else "Hits: " + csv_join(hits),
            notes="The scan avoids broad terms such as lore, secret, and plot because the guide uses those mechanically.",
        )
    ]

    lower = guide_text.lower()
    branch_route_count = lower.count("branch route")
    reload_count = lower.count("reload")
    branch_experienced_count = lower.count("branch-experienced")
    mechanical_ok = branch_route_count > 0 and reload_count > 0 and branch_experienced_count > 0
    rows.append(
        base_row(
            audit_area="spoiler_discipline",
            check_id="TB041-SPOILER-002",
            source_file=rel(MAIN_GUIDE),
            source_section="Full guide",
            row_label="Mechanical branch language",
            check_type="branch_language_scan",
            guide_locations="Full guide",
            audit_status="pass_mechanical_branch_language_present" if mechanical_ok else "needs_branch_language_review",
            recommended_action="none" if mechanical_ok else "review_branch_language",
            evidence=(
                f"branch route: {branch_route_count}; reload: {reload_count}; "
                f"branch-experienced: {branch_experienced_count}."
            ),
            notes="TB-041 checks that branch prose is framed as player-facing route mechanics rather than hidden coverage accounting.",
        )
    )
    return rows


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    areas = sorted({row["audit_area"] for row in rows})
    for area in areas:
        area_rows = [row for row in rows if row["audit_area"] == area]
        output.append({"metric": f"{area}:rows", "count": str(len(area_rows)), "notes": "Generated TB-041 audit rows."})
        for status, count in sorted(Counter(row["audit_status"] for row in area_rows).items()):
            output.append({"metric": f"{area}:status:{status}", "count": str(count), "notes": "Audit-status distribution."})
        for action, count in sorted(Counter(row["recommended_action"] for row in area_rows).items()):
            output.append({"metric": f"{area}:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    output.append({"metric": "all:rows", "count": str(len(rows)), "notes": "Generated TB-041 audit rows."})
    for action, count in sorted(Counter(row["recommended_action"] for row in rows).items()):
        output.append({"metric": f"all:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    return output


def main() -> int:
    guide_text = MAIN_GUIDE.read_text(encoding="utf-8")
    sections = markdown_sections(guide_text)
    branch_audit_rows = read_csv(BRANCH_AUDIT)
    route_resolution_ids = route_resolution_branch_ids(branch_audit_rows)
    rows = (
        policy_rows(guide_text)
        + decision_matrix_rows(guide_text, sections, route_resolution_ids)
        + existing_branch_audit_rows(branch_audit_rows)
        + guide_branch_cue_rows(guide_text, sections)
        + spoiler_rows(guide_text)
    )
    write_csv(OUTPUT_AUDIT, FIELDNAMES, rows)
    write_csv(OUTPUT_SUMMARY, ["metric", "count", "notes"], summary_rows(rows))
    actions = Counter(row["recommended_action"] for row in rows)
    print(f"Wrote {rel(OUTPUT_AUDIT)}")
    print(f"Wrote {rel(OUTPUT_SUMMARY)}")
    print(", ".join(f"{key}: {actions[key]}" for key in sorted(actions)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
