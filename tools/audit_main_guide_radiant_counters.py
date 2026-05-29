#!/usr/bin/env python3
"""Audit radiant and counter representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-011. It checks radiant,
trophy/counter, Fishing, and work-action objectives plus mapped checklist rows
against the player-facing guide and the internal guide coverage ledger.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MATRIX_CSV = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"
GUIDE_COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVES_CSV = REPO_ROOT / "data" / "objectives" / "objectives.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-radiant-counter-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

RADIANT_COUNTER_SUBCATEGORIES = {
    "angi_archery_practice",
    "blades_branch_radiant",
    "bounty_quest_type",
    "companions_finite_set",
    "companions_post_quest",
    "companions_radiant",
    "companions_radiant_windowed",
    "companions_representative_set",
    "companions_required_gate",
    "college_repeatable",
    "dark_brotherhood_radiant",
    "dawnguard_faction_finite",
    "dawnguard_faction_radiant",
    "dragonborn_skaal_misc_radiant",
    "fishing_special_catch_member",
    "fishing_species_member",
    "fishing_species_set",
    "hearthfire_property_defense",
    "no_journal_activity_radiant",
    "no_journal_brawl_radiant",
    "no_journal_favor_radiant",
    "thieves_guild_job_type",
    "thieves_guild_restoration",
    "volkihar_branch_other",
    "volkihar_branch_radiant",
    "word_wall_radiant",
}

TARGET_TERMS = (
    "assigned target",
    "boss chest",
    "business",
    "city",
    "client",
    "directly to",
    "dungeon",
    "giver",
    "hold",
    "house",
    "job marker",
    "lair",
    "location",
    "marked",
    "marker",
    "named",
    "settlement",
    "strongbox",
    "target",
)
ASSIGNMENT_TERMS = (
    "accept only",
    "actual",
    "ask",
    "assigned",
    "assignment",
    "assignment log",
    "client",
    "filler",
    "job",
    "offer",
    "random",
    "radiant",
    "reload the pre request save",
    "representative",
    "requesting",
)
COUNTER_TERMS = (
    "0 of",
    "1 of",
    "2 of",
    "3 of",
    "4 of",
    "5 of",
    "10 of",
    "20 of",
    "25 jobs",
    "35 jobs",
    "45 jobs",
    "50",
    "55 jobs",
    "75 jobs",
    "100",
    "125",
    "counter",
    "general stats",
    "milestone",
    "progress",
    "record",
    "tracking",
    "trophy",
    "verify",
)
BOUNDARY_TERMS = (
    "all three",
    "at least",
    "available once",
    "before",
    "complete exactly",
    "direct out and back",
    "do not",
    "eligible",
    "exactly",
    "one completed",
    "one representative",
    "reject",
    "stop",
    "stop taking",
    "total",
    "until",
)
FISHING_TERMS = (
    "active quest state",
    "biome",
    "catch",
    "fish",
    "fishery",
    "fishing",
    "ingredient preservation",
    "rod",
    "species",
    "spot",
    "time",
    "weather",
)
WORK_TERMS = (
    "archery practice",
    "barehanded",
    "beggar",
    "brawl",
    "chop",
    "crop",
    "drunk",
    "favor",
    "firewood",
    "gather",
    "gift of charity",
    "mine",
    "ore",
    "sell",
    "wheat",
    "wood",
)
TROPHY_TERMS = (
    "general stats",
    "hard save",
    "pop",
    "record",
    "reload",
    "trophy",
    "verify",
)
NO_REROLL_TERMS = (
    "actual assigned",
    "actual target",
    "do not chase",
    "do not restart",
    "do not route unrelated",
    "no save rerolling",
    "not restart",
    "record the actual",
)
HOLD_TERMS = (
    "deferred",
    "held",
    "if ",
    "in progress",
    "later",
    "not completed",
    "not routed",
    "pending",
    "staged",
    "wait",
)
ROUTE_RESOLUTION_TERMS = ("needs route resolution", "route-resolution", "route resolution", "unresolved")
EXCLUSION_TERMS = ("excluded", "exclusion", "not required", "outside required")
BRANCH_TERMS = ("branch", "branch route", "branch_complete", "reloaded", "reload")

COMPLETED_COVERAGE_TERMS = (
    "already_represented",
    "branch_complete",
    "complete",
    "completed",
    "confirmed",
    "counter_completed",
    "counter_progressed",
    "placed",
    "progressed",
    "represented",
    "retrospectively_placed",
)

NAME_ALIASES = {
    "fight fight representative brawl": "Fight! Fight!",
    "quest all beggars have representative favor": "Quest all Beggars Have",
    "quest all drunks have representative favor": "Quest all Drunks Have",
    "thieves guild city influence and side job counter": "Delvin/Vex side-job counter",
}


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


def strip_prefix(value: str) -> str:
    cleaned = value.replace("*", "").replace("\u200e", "").strip()
    cleaned = re.sub(r"\s+\((AE|CC|DB|DG|HF)\)$", "", cleaned)
    cleaned = re.sub(
        r"^(Bounty|Collectible Set|Fishing Catch|Trophy Set|Activity|Favor|Quest|Radiant)\s*:?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\s+Trophy Set$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+Representative (Activity|Brawl|Favor)$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
    return cleaned


def name_variants(*values: str) -> set[str]:
    variants: set[str] = set()
    for value in values:
        if not value:
            continue
        cleaned = value.replace("*", "").replace("\u200e", "").strip()
        stripped = strip_prefix(cleaned)
        without_parenthetical = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
        candidates = {
            cleaned,
            stripped,
            without_parenthetical,
            strip_prefix(without_parenthetical),
            cleaned.replace("&", "and"),
            stripped.replace("&", "and"),
            cleaned.replace(" and ", " "),
            stripped.replace(" and ", " "),
        }

        normalized_cleaned = normalize(cleaned)
        if normalized_cleaned in NAME_ALIASES:
            candidates.add(NAME_ALIASES[normalized_cleaned])
        if "the fishing job" in normalized_cleaned:
            candidates.add("Fishing Job")
        if "the numbers job" in normalized_cleaned:
            candidates.add("Numbers Job")
        if "the burglary job" in normalized_cleaned:
            candidates.add("Burglary Job")
        if "the shill job" in normalized_cleaned:
            candidates.add("Shill Job")
        if "the sweep job" in normalized_cleaned:
            candidates.add("Sweep Job")
        if "the heist job" in normalized_cleaned:
            candidates.add("Heist Job")
        if "the bedlam job" in normalized_cleaned:
            candidates.add("Bedlam Job")
        if "dragonrider trophy" in normalized_cleaned:
            candidates.add("Dragonrider")
        if "hard worker trophy" in normalized_cleaned:
            candidates.add("Hard Worker")
        if "thief trophy" in normalized_cleaned:
            candidates.add("Thief")
        if "snake tongue trophy" in normalized_cleaned:
            candidates.add("Snake Tongue")

        for candidate in candidates:
            candidate = candidate.strip()
            if not candidate:
                continue
            variants.add(candidate)
            if ":" in candidate:
                before, after = [part.strip() for part in candidate.split(":", 1)]
                if before:
                    variants.add(before)
                if after:
                    variants.add(after)
            if " - " in candidate:
                before, after = [part.strip() for part in candidate.split(" - ", 1)]
                if before:
                    variants.add(before)
                if after:
                    variants.add(after)

    return {variant for variant in variants if variant}


def guide_contains_name(guide_normalized: str, *names: str) -> bool:
    for variant in name_variants(*names):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        if re.search(pattern, guide_normalized):
            return True
    return False


def guide_context_for_names(guide_normalized: str, *names: str, window: int = 900) -> str:
    windows: list[str] = []
    seen: set[tuple[int, int]] = set()
    for variant in name_variants(*names):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        for match in re.finditer(pattern, guide_normalized):
            start = max(0, match.start() - window)
            end = min(len(guide_normalized), match.end() + window)
            key = (start, end)
            if key in seen:
                continue
            seen.add(key)
            windows.append(guide_normalized[start:end])
            if len(windows) >= 8:
                return " ".join(windows)
    return " ".join(windows)


def rows_blob(
    coverage_rows: list[dict[str, str]],
    objective_row: dict[str, str],
    checklist_row: dict[str, str],
    guide_context: str,
) -> str:
    coverage_keys = (
        "record_type",
        "objective_name",
        "coverage_status",
        "player_facing_cue",
        "player_facing_location",
        "completion_status",
        "notes",
    )
    object_keys = (
        "objective_name",
        "category",
        "subcategory",
        "start_trigger",
        "completion_boundary",
        "trophy_relevance",
        "route_placement",
        "notes",
    )
    checklist_keys = (
        "checklist_entry",
        "mapping_type",
        "guide_location",
        "status",
        "prototype_status",
        "notes",
        "raw_detail",
    )
    return normalize(
        " ".join(
            [
                " ".join(" ".join(row.get(key, "") for key in coverage_keys) for row in coverage_rows),
                " ".join(objective_row.get(key, "") for key in object_keys),
                " ".join(checklist_row.get(key, "") for key in checklist_keys),
                guide_context,
            ]
        )
    )


def has_any(blob: str, terms: tuple[str, ...]) -> bool:
    return any(term in blob for term in terms)


def treatment_flags(
    coverage_rows: list[dict[str, str]],
    objective_row: dict[str, str],
    checklist_row: dict[str, str],
    guide_context: str,
) -> dict[str, str]:
    blob = rows_blob(coverage_rows, objective_row, checklist_row, guide_context)
    return {
        "target_treatment": "Y" if has_any(blob, TARGET_TERMS) else "N",
        "assignment_treatment": "Y" if has_any(blob, ASSIGNMENT_TERMS) else "N",
        "counter_treatment": "Y" if has_any(blob, COUNTER_TERMS) else "N",
        "boundary_treatment": "Y" if has_any(blob, BOUNDARY_TERMS) else "N",
        "fishing_treatment": "Y" if has_any(blob, FISHING_TERMS) else "N",
        "work_action_treatment": "Y" if has_any(blob, WORK_TERMS) else "N",
        "trophy_treatment": "Y" if has_any(blob, TROPHY_TERMS) else "N",
        "no_reroll_treatment": "Y" if has_any(blob, NO_REROLL_TERMS) else "N",
        "hold_or_stage_treatment": "Y" if has_any(blob, HOLD_TERMS) else "N",
        "route_resolution_treatment": "Y" if has_any(blob, ROUTE_RESOLUTION_TERMS) else "N",
        "exclusion_treatment": "Y" if has_any(blob, EXCLUSION_TERMS) else "N",
        "branch_treatment": "Y" if has_any(blob, BRANCH_TERMS) else "N",
    }


def coverage_indicates_guide_representation(coverage_rows: list[dict[str, str]]) -> bool:
    for row in coverage_rows:
        blob = normalize(
            " ".join(
                row.get(key, "")
                for key in ("coverage_status", "player_facing_cue", "player_facing_location", "completion_status", "notes")
            )
        )
        if has_any(blob, COMPLETED_COVERAGE_TERMS):
            return True
    return False


def expected_treatment_met(
    *,
    row_kind: str,
    category: str,
    subcategory: str,
    checklist_entry: str,
    mapping_type: str,
    flags: dict[str, str],
) -> bool:
    if flags["route_resolution_treatment"] == "Y" or flags["exclusion_treatment"] == "Y":
        return True
    if mapping_type == "Explicit exclusion":
        return flags["exclusion_treatment"] == "Y"
    if mapping_type == "Branch-route prototype" or category == "branch_route":
        return flags["branch_treatment"] == "Y"

    if "fishing" in subcategory or "fishing" in normalize(checklist_entry):
        return (
            flags["fishing_treatment"] == "Y"
            and (flags["target_treatment"] == "Y" or flags["route_resolution_treatment"] == "Y")
        )

    if subcategory in {"no_journal_activity_radiant", "no_journal_brawl_radiant", "no_journal_favor_radiant", "angi_archery_practice"}:
        return flags["work_action_treatment"] == "Y" and (
            flags["target_treatment"] == "Y" or flags["counter_treatment"] == "Y" or flags["boundary_treatment"] == "Y"
        )

    if category == "trophy":
        return flags["trophy_treatment"] == "Y" or flags["counter_treatment"] == "Y" or flags["branch_treatment"] == "Y"

    if subcategory in {"thieves_guild_restoration", "thieves_guild_job_type"}:
        return (
            flags["assignment_treatment"] == "Y"
            and flags["boundary_treatment"] == "Y"
            and flags["counter_treatment"] == "Y"
        )

    if subcategory in {"dawnguard_faction_finite", "dawnguard_faction_radiant", "volkihar_branch_radiant", "volkihar_branch_other"}:
        return (
            (flags["target_treatment"] == "Y" or flags["assignment_treatment"] == "Y")
            and (flags["boundary_treatment"] == "Y" or flags["branch_treatment"] == "Y" or flags["counter_treatment"] == "Y")
        )

    if category == "radiant":
        return (
            flags["target_treatment"] == "Y"
            or flags["assignment_treatment"] == "Y"
            or flags["counter_treatment"] == "Y"
            or flags["boundary_treatment"] == "Y"
            or flags["hold_or_stage_treatment"] == "Y"
            or flags["branch_treatment"] == "Y"
        )

    return any(value == "Y" for value in flags.values())


def joined(values: set[str] | list[str], limit: int = 6) -> str:
    clean_values = sorted({value for value in values if value})
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def audit_status_for(
    *,
    row_kind: str,
    coverage_rows: list[dict[str, str]],
    guide_name_match: bool,
    category: str,
    subcategory: str,
    checklist_entry: str,
    mapping_type: str,
    flags: dict[str, str],
) -> tuple[str, str, str]:
    coverage_has_exclusion = any("exclusion" in normalize(row.get("coverage_status", "")) for row in coverage_rows)
    if not coverage_rows:
        return (
            f"{row_kind}_missing_internal_coverage",
            "add_internal_radiant_counter_coverage_row",
            "No exact or mapped internal coverage row was found for this radiant/counter row.",
        )

    if flags["route_resolution_treatment"] == "Y":
        return (f"{row_kind}_route_resolution_recorded", "none_existing_route_resolution", "")

    if flags["exclusion_treatment"] == "Y" and (mapping_type == "Explicit exclusion" or coverage_has_exclusion):
        return (f"{row_kind}_excluded", "none", "")

    if not guide_name_match:
        return (
            f"{row_kind}_missing_guide_name",
            "add_player_facing_radiant_counter_reference",
            "Internal coverage exists, but the guide does not name this radiant/counter row clearly enough.",
        )

    if expected_treatment_met(
        row_kind=row_kind,
        category=category,
        subcategory=subcategory,
        checklist_entry=checklist_entry,
        mapping_type=mapping_type,
        flags=flags,
    ):
        return (f"{row_kind}_covered", "none", "")

    return (
        f"{row_kind}_missing_radiant_counter_treatment",
        "add_radiant_counter_treatment_context",
        "The guide/internal coverage names this row but lacks clear target/assignment/counter/boundary treatment.",
    )


def coverage_rollup(rows: list[dict[str, str]]) -> tuple[set[str], set[str], set[str], set[str]]:
    return (
        {row.get("coverage_status", "") for row in rows},
        {row.get("completion_status", "") for row in rows},
        {row.get("player_facing_location", "") for row in rows},
        {row.get("player_facing_cue", "") for row in rows},
    )


def objective_in_scope(row: dict[str, str]) -> bool:
    if row.get("category") in {"radiant", "trophy"}:
        return True
    if row.get("subcategory") in RADIANT_COUNTER_SUBCATEGORIES:
        return True
    return "fishing" in row.get("subcategory", "")


def checklist_in_scope(row: dict[str, str], scoped_objective_ids: set[str]) -> bool:
    return row.get("objective_id") in scoped_objective_ids


def main() -> int:
    objective_rows = read_csv(OBJECTIVES_CSV)
    objective_ids = {row["objective_id"] for row in objective_rows}
    objectives_by_id = {row["objective_id"]: row for row in objective_rows}
    scoped_objectives = [row for row in objective_rows if objective_in_scope(row)]
    scoped_objective_ids = {row["objective_id"] for row in scoped_objectives}

    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    scoped_checklist_rows = [row for row in matrix_rows if checklist_in_scope(row, scoped_objective_ids)]

    guide_normalized = normalize(MAIN_GUIDE.read_text(encoding="utf-8"))

    coverage_rows = read_csv(GUIDE_COVERAGE_CSV)
    coverage_by_record_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in coverage_rows:
        raw_record_id = row.get("objective_id", "")
        for objective_id in expand_objective_refs(raw_record_id, objective_ids):
            coverage_by_record_id[objective_id].append(row)
        for checklist_id in expand_checklist_refs(raw_record_id, checklist_ids):
            coverage_by_record_id[checklist_id].append(row)

    audit_rows: list[dict[str, str]] = []
    status_counts: Counter[str] = Counter()
    action_counts: Counter[str] = Counter()

    def append_audit_row(
        *,
        row_kind: str,
        record_id: str,
        name: str,
        objective_row: dict[str, str],
        checklist_row: dict[str, str],
        exact_coverage_rows: list[dict[str, str]],
        mapped_coverage_rows: list[dict[str, str]],
    ) -> None:
        all_coverage_rows = exact_coverage_rows + mapped_coverage_rows
        category = objective_row.get("category", "")
        subcategory = objective_row.get("subcategory", "")
        checklist_entry = checklist_row.get("checklist_entry", "")
        mapping_type = checklist_row.get("mapping_type", "")

        guide_context = guide_context_for_names(
            guide_normalized,
            name,
            objective_row.get("objective_name", ""),
            checklist_entry,
            checklist_row.get("matched_objective_name", ""),
        )
        flags = treatment_flags(all_coverage_rows, objective_row, checklist_row, guide_context)
        guide_name_match = (
            guide_contains_name(
                guide_normalized,
                name,
                objective_row.get("objective_name", ""),
                checklist_entry,
                checklist_row.get("matched_objective_name", ""),
            )
            or coverage_indicates_guide_representation(all_coverage_rows)
            or flags["route_resolution_treatment"] == "Y"
            or flags["exclusion_treatment"] == "Y"
        )
        audit_status, recommended_action, notes = audit_status_for(
            row_kind=row_kind,
            coverage_rows=all_coverage_rows,
            guide_name_match=guide_name_match,
            category=category,
            subcategory=subcategory,
            checklist_entry=checklist_entry,
            mapping_type=mapping_type,
            flags=flags,
        )
        coverage_statuses, completion_statuses, guide_locations, guide_cues = coverage_rollup(all_coverage_rows)
        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        audit_rows.append(
            {
                "row_kind": row_kind,
                "record_id": record_id,
                "name": name,
                "objective_id": objective_row.get("objective_id", ""),
                "category": category,
                "subcategory": subcategory,
                "route_placement": objective_row.get("route_placement", ""),
                "checklist_id": checklist_row.get("checklist_id", ""),
                "checklist_tab": checklist_row.get("checklist_tab", ""),
                "mapping_type": mapping_type,
                "exact_internal_coverage_rows": str(len(exact_coverage_rows)),
                "mapped_internal_coverage_rows": str(len(mapped_coverage_rows)),
                "internal_coverage_statuses": joined(coverage_statuses),
                "internal_completion_statuses": joined(completion_statuses),
                "internal_guide_locations": joined(guide_locations),
                "internal_guide_cues": joined(guide_cues),
                "guide_name_match": "Y" if guide_name_match else "N",
                "target_treatment": flags["target_treatment"],
                "assignment_treatment": flags["assignment_treatment"],
                "counter_treatment": flags["counter_treatment"],
                "boundary_treatment": flags["boundary_treatment"],
                "fishing_treatment": flags["fishing_treatment"],
                "work_action_treatment": flags["work_action_treatment"],
                "trophy_treatment": flags["trophy_treatment"],
                "no_reroll_treatment": flags["no_reroll_treatment"],
                "hold_or_stage_treatment": flags["hold_or_stage_treatment"],
                "route_resolution_treatment": flags["route_resolution_treatment"],
                "exclusion_treatment": flags["exclusion_treatment"],
                "branch_treatment": flags["branch_treatment"],
                "audit_status": audit_status,
                "recommended_action": recommended_action,
                "notes": notes,
            }
        )

    for objective_row in scoped_objectives:
        objective_id = objective_row["objective_id"]
        append_audit_row(
            row_kind="radiant_counter_objective",
            record_id=objective_id,
            name=objective_row["objective_name"],
            objective_row=objective_row,
            checklist_row={},
            exact_coverage_rows=coverage_by_record_id.get(objective_id, []),
            mapped_coverage_rows=[],
        )

    for checklist_row in scoped_checklist_rows:
        objective_id = checklist_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        checklist_id = checklist_row["checklist_id"]
        append_audit_row(
            row_kind="radiant_counter_checklist",
            record_id=checklist_id,
            name=checklist_row["checklist_entry"],
            objective_row=objective_row,
            checklist_row=checklist_row,
            exact_coverage_rows=coverage_by_record_id.get(checklist_id, []),
            mapped_coverage_rows=coverage_by_record_id.get(objective_id, []),
        )

    fieldnames = [
        "row_kind",
        "record_id",
        "name",
        "objective_id",
        "category",
        "subcategory",
        "route_placement",
        "checklist_id",
        "checklist_tab",
        "mapping_type",
        "exact_internal_coverage_rows",
        "mapped_internal_coverage_rows",
        "internal_coverage_statuses",
        "internal_completion_statuses",
        "internal_guide_locations",
        "internal_guide_cues",
        "guide_name_match",
        "target_treatment",
        "assignment_treatment",
        "counter_treatment",
        "boundary_treatment",
        "fishing_treatment",
        "work_action_treatment",
        "trophy_treatment",
        "no_reroll_treatment",
        "hold_or_stage_treatment",
        "route_resolution_treatment",
        "exclusion_treatment",
        "branch_treatment",
        "audit_status",
        "recommended_action",
        "notes",
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(audit_rows)

    print(f"Wrote {len(audit_rows)} radiant/counter audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
