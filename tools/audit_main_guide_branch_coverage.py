#!/usr/bin/env python3
"""Audit branch-row representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-003. It checks every
Branch-route prototype checklist row plus every branch_route objective row
against the player-facing guide, the internal guide coverage ledger, and the
branch prototype drafts.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MATRIX_CSV = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"
OBJECTIVES_CSV = REPO_ROOT / "data" / "objectives" / "objectives.csv"
OBJECTIVE_ROUTE_INDEX_CSV = REPO_ROOT / "data" / "route-planning" / "objective-route-index.csv"
GUIDE_COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
BRANCH_ROUTES_DIR = REPO_ROOT / "drafts" / "branch-routes"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-branch-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)
BRANCH_CODE_RE = re.compile(r"BR-\d{3}[A-Z]?")

BRANCH_HARD_SAVE_ALIASES = {
    "BR-001": ["HS-CW-BEFORE-FACTION-OATH"],
    "BR-002": ["HS-DG-BLOODLINE"],
    "BR-003": ["HS-DB-ABANDONED-SHACK"],
    "BR-004": ["HS-MQ-PAARTHURNAX"],
    "BR-005": ["HS-TROPHY-MASTER-CRIMINAL"],
    "BR-006": ["HS-DRAGONBORN-THIRSK-CHOICE"],
    "BR-007": ["HS-AE-GHOSTS-TEMPLE", "HS-AE-GHOSTS-PROPAGANDA"],
    "BR-008A": ["HS-AE-BITTERCUP-ALTAR"],
    "BR-008B": ["HS-AE-BITTERCUP-ALTAR"],
    "BR-009": ["HS-DAEDRIC-BLACK-STAR"],
    "BR-010": ["HS-DAEDRIC-CLAVICUS"],
    "BR-011": ["HS-DAEDRIC-HIRCINE-GROTTO"],
    "BR-015": ["HS-AETHERIUM-FORGE"],
}

OBJECTIVE_BRANCH_OVERRIDES = {
    "OBJ-002777": "BR-005 Master Criminal Trophy",
}

MAIN_CONTINUITY_BRANCH_RESOLVED_OBJECTIVES = {"OBJ-002785", "OBJ-002786"}
MAIN_CONTINUITY_BRANCH_RESOLVED_CHECKLISTS = {"CHK-QUESTS-0055", "CHK-QUESTS-0057"}

BRANCH_SIGNAL_TERMS = (
    "branch",
    "reload",
    "reloaded",
    "hard save",
    "complete_in_mr043",
    "main continuity",
)

ROUTE_RESOLUTION_TERMS = (
    "needs_route_resolution",
    "needs route resolution",
)


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


def name_variants(value: str) -> list[str]:
    variants = {value.strip()}
    if ":" in value:
        variants.add(value.split(":", 1)[1].strip())
    variants.add(re.sub(r"\([^)]*\)", "", value).strip())
    return [variant for variant in variants if variant]


def guide_contains_name(guide_normalized: str, name: str) -> bool:
    for variant in name_variants(name):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        if re.search(pattern, guide_normalized):
            return True
    return False


def joined(values: set[str] | list[str], limit: int = 6) -> str:
    clean_values = sorted({value for value in values if value})
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def branch_code(branch_name: str) -> str:
    match = BRANCH_CODE_RE.search(branch_name)
    return match.group(0) if match else ""


def hard_save_aliases_for(branch_name: str) -> list[str]:
    return BRANCH_HARD_SAVE_ALIASES.get(branch_code(branch_name), [])


def has_hard_save_match(guide_text: str, aliases: list[str]) -> bool:
    return any(alias in guide_text for alias in aliases)


def has_reload_near_hard_save(guide_text: str, aliases: list[str]) -> bool:
    lowered = guide_text.lower()
    for alias in aliases:
        start = 0
        while True:
            index = guide_text.find(alias, start)
            if index == -1:
                break
            window = lowered[max(0, index - 1500) : index + 1500]
            if "reload" in window:
                return True
            start = index + len(alias)
    return False


def row_blob(row: dict[str, str]) -> str:
    return " ".join(row.get(key, "") for key in row).lower()


def rows_have_term(rows: list[dict[str, str]], terms: tuple[str, ...]) -> bool:
    blob = " ".join(row_blob(row) for row in rows)
    return any(term in blob for term in terms)


def rows_have_branch_signal(rows: list[dict[str, str]]) -> bool:
    return rows_have_term(rows, BRANCH_SIGNAL_TERMS)


def rows_have_route_resolution(rows: list[dict[str, str]]) -> bool:
    return rows_have_term(rows, ROUTE_RESOLUTION_TERMS)


def rows_have_conditional_not_applicable(rows: list[dict[str, str]]) -> bool:
    blob = " ".join(row_blob(row) for row in rows)
    return "conditional_not_routed" in blob or "not_applicable_no_treaty_branch" in blob


def rows_resolve_by_main_continuity(record_id: str, objective_id: str, rows: list[dict[str, str]]) -> bool:
    if objective_id not in MAIN_CONTINUITY_BRANCH_RESOLVED_OBJECTIVES and record_id not in MAIN_CONTINUITY_BRANCH_RESOLVED_CHECKLISTS:
        return False
    blob = " ".join(row_blob(row) for row in rows)
    return "complete_in_mr043" in blob or ("placed_in_guide" in blob and "complete" in blob)


def infer_branch_name(objective: dict[str, str], objective_to_branch: dict[str, str]) -> str:
    objective_id = objective["objective_id"]
    if objective_id in objective_to_branch:
        return objective_to_branch[objective_id]
    if objective_id in OBJECTIVE_BRANCH_OVERRIDES:
        return OBJECTIVE_BRANCH_OVERRIDES[objective_id]

    subcategory = objective.get("subcategory", "")
    objective_name = objective.get("objective_name", "")

    if subcategory == "civil_war_stormcloak":
        return "BR-001 Stormcloak Civil War"
    if subcategory.startswith("volkihar_branch"):
        return "BR-002 Volkihar"
    if subcategory == "dark_brotherhood_branch":
        return "BR-003 Destroy the Dark Brotherhood"
    if subcategory in {"optional_main_quest", "blades_branch_quest", "blades_branch_radiant"}:
        return "BR-004 Paarthurnax / Blades"
    if subcategory == "dragonborn_thirsk_side_quest":
        return "BR-006 Thirsk Riekling"
    if objective_name == "The Pit":
        return "BR-008A Bittercup Power"
    if objective_name == "Artifact: Azura's Star":
        return "BR-009 Azura's Star"
    if objective_name == "Artifact: The Rueful Axe":
        return "BR-010 Rueful Axe"
    if objective_name == "Artifact: Savior's Hide":
        return "BR-011 Savior's Hide"
    if objective_name in {"Artifact: Aetherial Shield", "Artifact: Aetherial Staff"}:
        return "BR-015 Aetherium Forge rewards"
    if objective_name in {
        "Unique Item: Amulet of Bats",
        "Unique Item: Amulet of The Gargoyle",
        "Unique Item: Ring of The Beast",
        "Unique Item: Ring of the Erudite",
    }:
        return "BR-002 Volkihar"

    return ""


def prototype_refs_for(prototype_text_by_file: dict[str, str], record_id: str, objective_id: str, name: str) -> list[str]:
    refs: list[str] = []
    normalized_variants = [normalize(variant) for variant in name_variants(name)]
    for file_name, text in prototype_text_by_file.items():
        normalized_text = normalize(text)
        if record_id and record_id in text:
            refs.append(file_name)
            continue
        if objective_id and objective_id in text:
            refs.append(file_name)
            continue
        if any(variant and re.search(rf"(?<![a-z0-9]){re.escape(variant)}(?![a-z0-9])", normalized_text) for variant in normalized_variants):
            refs.append(file_name)
    return refs


def audit_status_for(
    audit_source: str,
    record_id: str,
    objective_id: str,
    checklist_rows: list[dict[str, str]],
    objective_rows: list[dict[str, str]],
    guide_hard_save_match: bool,
    guide_reload_match: bool,
    prototype_match: bool,
) -> tuple[str, str, str]:
    exact_rows = checklist_rows if audit_source == "branch_checklist" else objective_rows
    combined_rows = exact_rows or objective_rows

    if audit_source == "branch_checklist" and not checklist_rows and rows_have_route_resolution(objective_rows):
        return (
            "branch_checklist_missing_route_resolution_row",
            "add_internal_checklist_route_resolution_row",
            "Mapped objective already has a route-resolution note; add checklist-specific internal coverage for this branch row.",
        )

    if rows_have_route_resolution(combined_rows):
        return (
            f"{audit_source}_route_resolution_recorded",
            "none_existing_route_resolution",
            "Existing internal coverage keeps the missing branch facts explicit instead of hiding them.",
        )

    if rows_have_conditional_not_applicable(combined_rows):
        return (
            f"{audit_source}_conditionally_not_applicable",
            "none",
            "Conditional Stormcloak treaty-only branch row is represented as not applicable for the no-treaty route.",
        )

    if rows_resolve_by_main_continuity(record_id, objective_id, combined_rows):
        return (
            f"{audit_source}_resolved_by_main_continuity",
            "none",
            "Blades checklist branch row is already completed on main continuity before the Paarthurnax lockout.",
        )

    if exact_rows and rows_have_branch_signal(exact_rows):
        return (f"{audit_source}_covered", "none", "")

    if audit_source == "branch_checklist" and objective_rows and rows_have_branch_signal(objective_rows):
        return (
            "branch_checklist_mapped_objective_missing_checklist_row",
            "add_internal_checklist_branch_row",
            "Mapped objective has branch coverage, but the checklist row needs checklist-specific internal coverage.",
        )

    if guide_hard_save_match and guide_reload_match and prototype_match:
        return (
            f"{audit_source}_guide_branch_block_missing_internal_coverage",
            "add_internal_branch_coverage_row",
            "Guide and prototype show a branch/reload block, but the coverage ledger lacks an exact branch coverage row.",
        )

    return (
        f"{audit_source}_gap",
        "targeted_branch_guide_or_coverage_repair",
        "No adequate branch/reload representation found in internal coverage.",
    )


def main() -> int:
    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    branch_checklist_rows = [row for row in matrix_rows if row.get("mapping_type") == "Branch-route prototype"]

    objectives = read_csv(OBJECTIVES_CSV)
    objective_by_id = {row["objective_id"]: row for row in objectives}
    objective_ids = set(objective_by_id)

    route_index_objective_ids = set()
    if OBJECTIVE_ROUTE_INDEX_CSV.exists():
        route_index_objective_ids = {
            row["objective_id"]
            for row in read_csv(OBJECTIVE_ROUTE_INDEX_CSV)
            if row.get("route_placement") == "branch_route"
        }
    branch_objective_ids = {
        row["objective_id"] for row in objectives if row.get("route_placement") == "branch_route"
    } | route_index_objective_ids

    objective_to_branch: dict[str, str] = {}
    for row in branch_checklist_rows:
        objective_id = row.get("objective_id", "")
        if objective_id and objective_id not in objective_to_branch:
            objective_to_branch[objective_id] = row.get("branch_name", "")

    guide_text = MAIN_GUIDE.read_text(encoding="utf-8")
    guide_normalized = normalize(guide_text)

    prototype_text_by_file = {
        path.name: path.read_text(encoding="utf-8")
        for path in sorted(BRANCH_ROUTES_DIR.glob("*.md"))
    }

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

    def add_output_row(
        audit_source: str,
        record_id: str,
        checklist_id: str,
        objective_id: str,
        name: str,
        category: str,
        route_placement_or_mapping_type: str,
        branch_name: str,
    ) -> None:
        checklist_rows = coverage_by_checklist_id.get(checklist_id, []) if checklist_id else []
        objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        combined_rows = checklist_rows or objective_rows

        hard_save_aliases = hard_save_aliases_for(branch_name)
        guide_name_match = guide_contains_name(guide_normalized, name)
        guide_hard_save_match = has_hard_save_match(guide_text, hard_save_aliases)
        guide_reload_match = has_reload_near_hard_save(guide_text, hard_save_aliases)
        prototype_refs = prototype_refs_for(prototype_text_by_file, record_id, objective_id, name)
        prototype_match = bool(prototype_refs)

        audit_status, recommended_action, status_note = audit_status_for(
            audit_source,
            record_id,
            objective_id,
            checklist_rows,
            objective_rows,
            guide_hard_save_match,
            guide_reload_match,
            prototype_match,
        )

        coverage_statuses = {row.get("coverage_status", "") for row in combined_rows}
        completion_statuses = {row.get("completion_status", "") for row in combined_rows}
        guide_locations = {row.get("player_facing_location", "") for row in combined_rows}

        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        output_rows.append(
            {
                "audit_source": audit_source,
                "record_id": record_id,
                "checklist_id": checklist_id,
                "objective_id": objective_id,
                "name": name,
                "category": category,
                "route_placement_or_mapping_type": route_placement_or_mapping_type,
                "branch_name": branch_name,
                "expected_hard_save_aliases": joined(hard_save_aliases),
                "internal_checklist_coverage_row_count": str(len(checklist_rows)),
                "internal_objective_coverage_row_count": str(len(objective_rows)),
                "guide_name_match": "Y" if guide_name_match else "N",
                "guide_branch_hard_save_match": "Y" if guide_hard_save_match else "N",
                "guide_branch_reload_match": "Y" if guide_reload_match else "N",
                "prototype_reference_match": "Y" if prototype_match else "N",
                "prototype_reference_files": joined(prototype_refs),
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "recommended_action": recommended_action,
                "notes": status_note,
            }
        )

    for row in branch_checklist_rows:
        add_output_row(
            audit_source="branch_checklist",
            record_id=row["checklist_id"],
            checklist_id=row["checklist_id"],
            objective_id=row.get("objective_id", ""),
            name=row["checklist_entry"],
            category=row["category"],
            route_placement_or_mapping_type=row["mapping_type"],
            branch_name=row.get("branch_name", ""),
        )

    for objective_id in sorted(branch_objective_ids):
        objective = objective_by_id[objective_id]
        add_output_row(
            audit_source="branch_objective",
            record_id=objective_id,
            checklist_id="",
            objective_id=objective_id,
            name=objective["objective_name"],
            category=objective["category"],
            route_placement_or_mapping_type=objective["route_placement"],
            branch_name=infer_branch_name(objective, objective_to_branch),
        )

    fieldnames = [
        "audit_source",
        "record_id",
        "checklist_id",
        "objective_id",
        "name",
        "category",
        "route_placement_or_mapping_type",
        "branch_name",
        "expected_hard_save_aliases",
        "internal_checklist_coverage_row_count",
        "internal_objective_coverage_row_count",
        "guide_name_match",
        "guide_branch_hard_save_match",
        "guide_branch_reload_match",
        "prototype_reference_match",
        "prototype_reference_files",
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

    print(f"Wrote {len(output_rows)} branch audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
