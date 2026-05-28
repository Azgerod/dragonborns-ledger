#!/usr/bin/env python3
"""Audit crafting and progression representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-010. It checks skill/perk,
crafting unlock, enchantment-learning, alchemy-effect, merchant-investment,
practical crafting, level-gate, and grind-loop rows against the player-facing
guide, the internal guide coverage ledger, and the skill/crafting support
tables.
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
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-crafting-progression-audit.csv"

SKILL_PERK_CSV = REPO_ROOT / "data" / "skills" / "skill-perk-catalog.csv"
PERK_RANK_CSV = REPO_ROOT / "data" / "skills" / "perk-rank-catalog.csv"
ENCHANTMENT_CSV = REPO_ROOT / "data" / "skills" / "enchantment-learning-catalog.csv"
ALCHEMY_CSV = REPO_ROOT / "data" / "skills" / "alchemy-effect-catalog.csv"
MERCHANT_INVESTMENT_CSV = REPO_ROOT / "data" / "skills" / "merchant-investment-catalog.csv"
PRACTICAL_CRAFTING_CSV = REPO_ROOT / "data" / "skills" / "practical-crafting-system-catalog.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

CHECKLIST_TABS = {"Perks", "Learned Alchemy Effects", "Enchanting Effects", "Merchants"}
CRAFTING_TROPHY_SUBCATEGORIES = {
    "crafting_activity_trophy",
    "crafting_trophy",
    "general_trophy",
    "level_trophy",
    "skill_trophy",
}
EXTRA_PROGRESS_SUBCATEGORIES = {
    "college_master_skill_quest",
    "tutorial_misc",
}

LEARN_DISCOVER_TERMS = (
    "discover",
    "discovered",
    "discovery",
    "disenchant",
    "effect",
    "effects",
    "eat",
    "eating",
    "experimenter",
    "learn",
    "learned",
    "reveal",
    "revealed",
    "source item",
)
CRAFT_ACTION_TERMS = (
    "alchemy lab",
    "arcane enchanter",
    "bake",
    "baking",
    "brew",
    "construct",
    "construction",
    "cook",
    "cooked",
    "craft",
    "crafted",
    "enchant",
    "enchanted",
    "forge",
    "forged",
    "imbuing chamber",
    "mine",
    "mined",
    "potion",
    "smelt",
    "smelted",
    "smith",
    "smithed",
    "staff enchanter",
    "tan",
    "tanned",
)
INVESTMENT_TERMS = (
    "500 gold",
    "invest",
    "invested",
    "investment",
    "investor",
    "merchant",
    "merchant perk",
    "speech 70",
)
SKILL_PERK_TERMS = (
    "100",
    "252",
    "assign",
    "assigned",
    "level",
    "legendary",
    "perk",
    "perks",
    "rank",
    "ranks",
    "reset",
    "skill",
    "trainer",
    "training",
)
STORAGE_TERMS = ("preserve", "preserved", "safe storage", "store", "stored", "storage")
HOLD_TERMS = (
    "deferred",
    "do not",
    "held",
    "if ",
    "later",
    "not completed",
    "not routed",
    "pending",
    "staged",
    "wait",
)
ROUTE_RESOLUTION_TERMS = ("needs route resolution", "route-resolution", "route resolution", "unresolved")
EXCLUSION_TERMS = (
    "bugged",
    "do not chase",
    "excluded",
    "exclusion",
    "not required",
    "official ps4 ae",
    "unique item preserved",
    "unobtainable",
    "unknown ae investment status",
    "unofficial patch-only",
)
BRANCH_TERMS = ("branch", "reloaded", "alternate branch")
SHORT_NAME_ALLOWLIST = {"bee"}
PERK_NAME_ALIASES = {
    "adv armors": "Advanced Armors",
    "arcane smith": "Arcane Blacksmith",
    "aug flames 1": "Augmented Flames 1",
    "aug flames 2": "Augmented Flames 2",
    "aug frost 1": "Augmented Frost 1",
    "aug frost 2": "Augmented Frost 2",
    "aug shock 1": "Augmented Shock 1",
    "aug shock 2": "Augmented Shock 2",
    "concenpoison": "Concentrated Poison",
    "champion stance": "Champion's Stance",
    "daedric smith": "Daedric Smithing",
    "dual casting": "Dual Casting",
    "dwarven smith": "Dwarven Smithing",
    "ebony smith": "Ebony Smithing",
    "element protect": "Elemental Protection",
    "elven smith": "Elven Smithing",
    "glass smith": "Glass Smithing",
    "great crit char": "Great Critical Charge",
    "insight enchanter": "Insightful Enchanter",
    "key master gozer": "Keymaster",
    "magic res 1": "Magic Resistance 1",
    "magic res 2": "Magic Resistance 2",
    "magic res 3": "Magic Resistance 3",
    "master mind": "Master of the Mind",
    "muffled moves": "Muffled Movement",
    "novice": "Novice",
    "orcish smith": "Orcish Smithing",
    "paralysing strike": "Paralyzing Strike",
    "reflective blows": "Reflect Blows",
    "snake blood": "Snakeblood",
    "steel smith": "Steel Smithing",
    "stealth rank 1": "Stealth 1",
    "stealth rank 2": "Stealth 2",
    "stealth rank 3": "Stealth 3",
    "stealth rank 4": "Stealth 4",
    "stealth rank 5": "Stealth 5",
    "tower of str": "Tower of Strength",
    "windwalker": "Wind Walker",
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


def strip_progression_prefix(value: str) -> str:
    cleaned = value.replace("*", "").replace("\u200e", "").strip()
    cleaned = re.sub(r"\s+\((AE|CC|DB|DG|HF)\)$", "", cleaned)
    cleaned = re.sub(
        r"^(Acquire All|Discover Alchemy Effects|Invest in Merchant|Learn Enchantment|Learn Weapon Enchantment|Raise)\s*:?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\s+to\s+100$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+Perks$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+Trophy Set$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
    return cleaned


def name_variants(*values: str) -> set[str]:
    variants: set[str] = set()
    for value in values:
        if not value:
            continue
        cleaned = value.replace("*", "").replace("\u200e", "").strip()
        stripped = strip_progression_prefix(cleaned)
        without_parenthetical = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
        candidates = {
            cleaned,
            stripped,
            without_parenthetical,
            strip_progression_prefix(without_parenthetical),
            cleaned.replace("&", "and"),
            stripped.replace("&", "and"),
            cleaned.replace(" and ", " "),
            stripped.replace(" and ", " "),
        }

        normalized_cleaned = normalize(cleaned)
        if "plague of the dead mort flesh ingredient set" in normalized_cleaned:
            candidates.add("Mort Flesh")
        if "camping supplies crafting system" in normalized_cleaned:
            candidates.add("Camping Supplies")
        if "expanded crossbow pack weapon and crafting set" in normalized_cleaned:
            candidates.add("Expanded Crossbow Pack")
            candidates.add("Expanded Crossbow Pack Weapon")
        if "elite crossbows weapon and crafting set" in normalized_cleaned:
            candidates.add("Elite Crossbows")
            candidates.add("Elite Crossbows Weapon")
        if "nordic jewelry equipment and crafting set" in normalized_cleaned:
            candidates.add("Nordic Jewelry")
        if "myrwatch crafting station access" in normalized_cleaned:
            candidates.add("Myrwatch")
        if "reach all skills 100" in normalized_cleaned:
            candidates.add("all 18 skills are at 100")
            candidates.add("all 18 skills")
        if "reach player level 252 for all perks" in normalized_cleaned:
            candidates.add("level 252")
            candidates.add("252 or higher")
        if "use legendary skill resets for perk point completion" in normalized_cleaned:
            candidates.add("Legendary resets")
            candidates.add("Legendary reset")
        if "complete all source listed available merchant investments" in normalized_cleaned:
            candidates.add("investment circuit")
            candidates.add("available investments")
        if "staff enchanting" in normalized_cleaned:
            candidates.add("Staff Enchanter")
        if "kesh fiber" in normalized_cleaned:
            candidates.add("Kresh Fiber")

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
                    variants.add(after.replace("&", "and"))
                    variants.add(after.replace(" and ", " "))
    return {variant for variant in variants if variant}


def guide_contains_name(guide_normalized: str, *names: str) -> bool:
    for variant in name_variants(*names):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4 and normalized_name not in SHORT_NAME_ALLOWLIST:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        if re.search(pattern, guide_normalized):
            return True
    return False


def guide_contains_parts(guide_normalized: str, *parts: str) -> bool:
    return all(guide_contains_name(guide_normalized, part) for part in parts if part)


def perk_name_candidates(perk_name: str) -> list[str]:
    candidates = [perk_name]
    normalized_perk = normalize(perk_name)
    if normalized_perk in PERK_NAME_ALIASES:
        candidates.append(PERK_NAME_ALIASES[normalized_perk])
    return candidates


def rows_blob(
    coverage_rows: list[dict[str, str]],
    support_rows: list[dict[str, str]],
    objective_row: dict[str, str],
    checklist_row: dict[str, str],
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
    support_keys = (
        "skill_name",
        "skill_completion_boundary",
        "perk_completion_boundary",
        "legendary_reset_relevance",
        "perk_node_name",
        "perk_rank",
        "skill_requirement_text",
        "enchantment_name",
        "learning_policy",
        "preservation_conflict_item",
        "ingredient_name",
        "effect_1",
        "effect_2",
        "effect_3",
        "effect_4",
        "discovery_policy",
        "merchant_name",
        "store_name",
        "invest_status",
        "investment_policy",
        "system_name",
        "system_type",
        "coverage_status",
        "route_treatment",
        "notes",
    )
    object_keys = ("objective_name", "category", "subcategory", "route_placement", "notes")
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
                " ".join(" ".join(row.get(key, "") for key in support_keys) for row in support_rows),
                " ".join(objective_row.get(key, "") for key in object_keys),
                " ".join(checklist_row.get(key, "") for key in checklist_keys),
            ]
        )
    )


def has_any(blob: str, terms: tuple[str, ...]) -> bool:
    return any(term in blob for term in terms)


def treatment_flags(
    coverage_rows: list[dict[str, str]],
    support_rows: list[dict[str, str]],
    objective_row: dict[str, str],
    checklist_row: dict[str, str],
) -> dict[str, str]:
    blob = rows_blob(coverage_rows, support_rows, objective_row, checklist_row)
    return {
        "learn_or_discover_treatment": "Y" if has_any(blob, LEARN_DISCOVER_TERMS) else "N",
        "craft_action_treatment": "Y" if has_any(blob, CRAFT_ACTION_TERMS) else "N",
        "investment_treatment": "Y" if has_any(blob, INVESTMENT_TERMS) else "N",
        "skill_or_perk_treatment": "Y" if has_any(blob, SKILL_PERK_TERMS) else "N",
        "storage_treatment": "Y" if has_any(blob, STORAGE_TERMS) else "N",
        "hold_or_stage_treatment": "Y" if has_any(blob, HOLD_TERMS) else "N",
        "route_resolution_treatment": "Y" if has_any(blob, ROUTE_RESOLUTION_TERMS) else "N",
        "exclusion_treatment": "Y" if has_any(blob, EXCLUSION_TERMS) else "N",
        "branch_treatment": "Y" if has_any(blob, BRANCH_TERMS) else "N",
    }


def expected_treatment_met(
    *,
    row_kind: str,
    category: str,
    subcategory: str,
    checklist_tab: str,
    mapping_type: str,
    flags: dict[str, str],
) -> bool:
    if flags["route_resolution_treatment"] == "Y" or flags["exclusion_treatment"] == "Y":
        return True
    if flags["branch_treatment"] == "Y" and mapping_type == "Branch-route prototype":
        return True
    if mapping_type == "Explicit exclusion":
        return flags["exclusion_treatment"] == "Y"

    if checklist_tab == "Perks" or category == "skill_perk" or subcategory in {"level_trophy", "skill_trophy"}:
        return flags["skill_or_perk_treatment"] == "Y" or flags["hold_or_stage_treatment"] == "Y"
    if checklist_tab == "Learned Alchemy Effects" or subcategory in {"alchemy_ingredient_effect_discovery", "all_alchemy_effects"}:
        return flags["learn_or_discover_treatment"] == "Y" or flags["hold_or_stage_treatment"] == "Y"
    if checklist_tab == "Enchanting Effects" or subcategory in {"enchantment_learning", "all_enchantments_non_destructive"}:
        return flags["learn_or_discover_treatment"] == "Y" or flags["hold_or_stage_treatment"] == "Y"
    if checklist_tab == "Merchants" or subcategory in {"merchant_investment", "all_merchant_investments"}:
        return flags["investment_treatment"] == "Y" or flags["hold_or_stage_treatment"] == "Y"
    if subcategory in {
        "crafting_activity_trophy",
        "crafting_trophy",
        "practical_crafting_system",
        "tutorial_misc",
    }:
        return flags["craft_action_treatment"] == "Y" or flags["hold_or_stage_treatment"] == "Y"
    if category == "crafting_unlock" or row_kind == "progression_support":
        return any(
            flags[key] == "Y"
            for key in (
                "craft_action_treatment",
                "learn_or_discover_treatment",
                "investment_treatment",
                "skill_or_perk_treatment",
                "hold_or_stage_treatment",
            )
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
    checklist_tab: str,
    mapping_type: str,
    flags: dict[str, str],
) -> tuple[str, str, str]:
    coverage_has_exclusion = any("exclusion" in normalize(row.get("coverage_status", "")) for row in coverage_rows)
    if not coverage_rows and row_kind != "progression_support":
        return (
            f"{row_kind}_missing_internal_coverage",
            "add_internal_crafting_progression_coverage_row",
            "No exact or mapped internal coverage row was found for this crafting/progression row.",
        )

    if flags["route_resolution_treatment"] == "Y":
        return (f"{row_kind}_route_resolution_recorded", "none_existing_route_resolution", "")

    if flags["exclusion_treatment"] == "Y" and (mapping_type == "Explicit exclusion" or coverage_has_exclusion or row_kind == "progression_support"):
        return (f"{row_kind}_excluded", "none", "")

    if not guide_name_match:
        return (
            f"{row_kind}_missing_guide_name",
            "add_player_facing_crafting_progression_reference",
            "Internal/support coverage exists, but the guide does not name this crafting/progression row clearly enough.",
        )

    if expected_treatment_met(
        row_kind=row_kind,
        category=category,
        subcategory=subcategory,
        checklist_tab=checklist_tab,
        mapping_type=mapping_type,
        flags=flags,
    ):
        return (f"{row_kind}_covered", "none", "")

    return (
        f"{row_kind}_missing_crafting_progression_treatment",
        "add_crafting_progression_treatment_context",
        "The guide/internal coverage names this row but lacks clear learn/discover/craft/invest/skill/perk/hold treatment.",
    )


def coverage_rollup(rows: list[dict[str, str]]) -> tuple[set[str], set[str], set[str], set[str]]:
    return (
        {row.get("coverage_status", "") for row in rows},
        {row.get("completion_status", "") for row in rows},
        {row.get("player_facing_location", "") for row in rows},
        {row.get("player_facing_cue", "") for row in rows},
    )


def objective_in_scope(row: dict[str, str]) -> bool:
    if row.get("category") in {"crafting_unlock", "skill_perk"}:
        return True
    if row.get("category") == "trophy" and row.get("subcategory") in CRAFTING_TROPHY_SUBCATEGORIES:
        return True
    return row.get("subcategory") in EXTRA_PROGRESS_SUBCATEGORIES


def checklist_in_scope(row: dict[str, str]) -> bool:
    if row.get("checklist_tab") not in CHECKLIST_TABS:
        return False
    if row.get("checklist_tab") == "Merchants":
        return bool(row.get("objective_id"))
    return True


def support_record_id(row: dict[str, str]) -> str:
    for key in (
        "skill_record_id",
        "perk_rank_record_id",
        "enchantment_record_id",
        "alchemy_record_id",
        "merchant_investment_record_id",
        "crafting_system_record_id",
    ):
        if row.get(key):
            return row[key]
    return ""


def main() -> int:
    objective_rows = read_csv(OBJECTIVES_CSV)
    objective_ids = {row["objective_id"] for row in objective_rows}
    objectives_by_id = {row["objective_id"]: row for row in objective_rows}
    scoped_objectives = [row for row in objective_rows if objective_in_scope(row)]

    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    scoped_checklist_rows = [row for row in matrix_rows if checklist_in_scope(row)]

    guide_normalized = normalize(MAIN_GUIDE.read_text(encoding="utf-8"))

    support_by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    support_rows: list[dict[str, str]] = []

    for row in read_csv(SKILL_PERK_CSV):
        row["_support_table"] = SKILL_PERK_CSV.name
        support_rows.append(row)
        for objective_key in ("skill_100_objective_id", "perk_tree_objective_id"):
            if row.get(objective_key):
                support_by_objective[row[objective_key]].append(row)

    for row in read_csv(PERK_RANK_CSV):
        row["_support_table"] = PERK_RANK_CSV.name
        support_rows.append(row)
        if row.get("parent_perk_tree_objective_id"):
            support_by_objective[row["parent_perk_tree_objective_id"]].append(row)

    for row in read_csv(ENCHANTMENT_CSV):
        row["_support_table"] = ENCHANTMENT_CSV.name
        support_rows.append(row)
        if row.get("objective_id"):
            support_by_objective[row["objective_id"]].append(row)

    for row in read_csv(ALCHEMY_CSV):
        row["_support_table"] = ALCHEMY_CSV.name
        support_rows.append(row)
        if row.get("objective_id"):
            support_by_objective[row["objective_id"]].append(row)

    for row in read_csv(MERCHANT_INVESTMENT_CSV):
        row["_support_table"] = MERCHANT_INVESTMENT_CSV.name
        support_rows.append(row)
        if row.get("objective_id"):
            support_by_objective[row["objective_id"]].append(row)

    for row in read_csv(PRACTICAL_CRAFTING_CSV):
        row["_support_table"] = PRACTICAL_CRAFTING_CSV.name
        support_rows.append(row)
        if row.get("objective_id"):
            support_by_objective[row["objective_id"]].append(row)
        for objective_id in OBJECTIVE_ID_RE.findall(row.get("existing_objective_ids", "")):
            support_by_objective[objective_id].append(row)

    support_rows_for_direct_audit = [
        row
        for row in support_rows
        if (
            row.get("_support_table") == PRACTICAL_CRAFTING_CSV.name
            or (row.get("_support_table") == MERCHANT_INVESTMENT_CSV.name and not row.get("objective_id"))
        )
    ]

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

    def append_output(
        *,
        row_kind: str,
        row_id: str,
        display_name: str,
        objective_id: str,
        checklist_id: str,
        checklist_entry: str,
        checklist_tab: str,
        mapping_type: str,
        coverage_rows: list[dict[str, str]],
        coverage_source: str,
        guide_name_match: bool,
        objective_row: dict[str, str],
        checklist_row: dict[str, str],
        support_rows_for_row: list[dict[str, str]],
    ) -> None:
        category = objective_row.get("category", "")
        subcategory = objective_row.get("subcategory", "")
        flags = treatment_flags(coverage_rows, support_rows_for_row, objective_row, checklist_row)
        audit_status, recommended_action, notes = audit_status_for(
            row_kind=row_kind,
            coverage_rows=coverage_rows,
            guide_name_match=guide_name_match,
            category=category,
            subcategory=subcategory,
            checklist_tab=checklist_tab,
            mapping_type=mapping_type,
            flags=flags,
        )
        coverage_statuses, completion_statuses, guide_locations, guide_cues = coverage_rollup(coverage_rows)

        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        output_rows.append(
            {
                "row_kind": row_kind,
                "row_id": row_id,
                "objective_id": objective_id,
                "checklist_id": checklist_id,
                "display_name": display_name,
                "checklist_entry": checklist_entry,
                "category": category,
                "subcategory": subcategory,
                "checklist_tab": checklist_tab,
                "mapping_type": mapping_type,
                "route_placement": objective_row.get("route_placement", ""),
                "source_content": objective_row.get("source_content", ""),
                "support_table_rows": str(len(support_rows_for_row)),
                "support_tables": joined({row.get("_support_table", "") for row in support_rows_for_row}),
                "support_names": joined(
                    {
                        row.get("skill_name", "")
                        or row.get("perk_node_name", "")
                        or row.get("enchantment_name", "")
                        or row.get("ingredient_name", "")
                        or row.get("merchant_name", "")
                        or row.get("system_name", "")
                        for row in support_rows_for_row
                    },
                    limit=8,
                ),
                "guide_name_match": "Y" if guide_name_match else "N",
                "coverage_source": coverage_source,
                "internal_coverage_row_count": str(len(coverage_rows)),
                **flags,
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "guide_cues": joined(guide_cues, limit=5),
                "recommended_action": recommended_action,
                "notes": notes,
            }
        )

    for objective_row in scoped_objectives:
        objective_id = objective_row["objective_id"]
        support_for_row = support_by_objective.get(objective_id, [])
        display_name = strip_progression_prefix(objective_row["objective_name"])
        support_names = [
            row.get("skill_name", "")
            or row.get("enchantment_name", "")
            or row.get("ingredient_name", "")
            or row.get("merchant_name", "")
            or row.get("system_name", "")
            for row in support_for_row
        ]
        coverage_rows = coverage_by_objective_id.get(objective_id, [])
        guide_name_match = guide_contains_name(guide_normalized, objective_row["objective_name"], display_name, *support_names)
        append_output(
            row_kind="progression_objective",
            row_id=objective_id,
            display_name=display_name,
            objective_id=objective_id,
            checklist_id="",
            checklist_entry="",
            checklist_tab="",
            mapping_type="",
            coverage_rows=coverage_rows,
            coverage_source="objective",
            guide_name_match=guide_name_match,
            objective_row=objective_row,
            checklist_row={},
            support_rows_for_row=support_for_row,
        )

    for checklist_row in scoped_checklist_rows:
        checklist_id = checklist_row["checklist_id"]
        objective_id = checklist_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        support_for_row = support_by_objective.get(objective_id, [])
        display_name = strip_progression_prefix(checklist_row["checklist_entry"])
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        coverage_rows = exact_rows or mapped_objective_rows
        coverage_source = "exact_checklist" if exact_rows else "mapped_objective" if mapped_objective_rows else ""

        if checklist_row["checklist_tab"] == "Learned Alchemy Effects" and ":" in checklist_row["checklist_entry"]:
            ingredient, effect = [part.strip() for part in checklist_row["checklist_entry"].split(":", 1)]
            support_ingredient_names = [row.get("ingredient_name", "") for row in support_for_row if row.get("ingredient_name", "")]
            guide_name_match = guide_contains_parts(guide_normalized, ingredient, effect) or any(
                guide_contains_parts(guide_normalized, support_ingredient_name, effect)
                for support_ingredient_name in support_ingredient_names
            )
        elif checklist_row["checklist_tab"] == "Perks" and ":" in checklist_row["checklist_entry"]:
            skill_or_bucket, perk = [part.strip() for part in checklist_row["checklist_entry"].split(":", 1)]
            skill_name = skill_or_bucket.replace(" Perks", "")
            guide_name_match = any(
                guide_contains_parts(guide_normalized, skill_name, candidate)
                for candidate in perk_name_candidates(perk)
            )
        elif checklist_row["checklist_tab"] == "Merchants":
            merchant_names = [row.get("merchant_name", "") for row in support_for_row]
            guide_name_match = guide_contains_name(guide_normalized, checklist_row["checklist_entry"], display_name, *merchant_names)
        else:
            support_names = [
                row.get("enchantment_name", "")
                or row.get("ingredient_name", "")
                or row.get("merchant_name", "")
                or row.get("system_name", "")
                for row in support_for_row
            ]
            guide_name_match = guide_contains_name(
                guide_normalized,
                checklist_row["checklist_entry"],
                checklist_row.get("matched_objective_name", ""),
                display_name,
                *support_names,
            )

        append_output(
            row_kind="progression_checklist",
            row_id=checklist_id,
            display_name=display_name,
            objective_id=objective_id,
            checklist_id=checklist_id,
            checklist_entry=checklist_row["checklist_entry"],
            checklist_tab=checklist_row["checklist_tab"],
            mapping_type=checklist_row.get("mapping_type", ""),
            coverage_rows=coverage_rows,
            coverage_source=coverage_source,
            guide_name_match=guide_name_match,
            objective_row=objective_row,
            checklist_row=checklist_row,
            support_rows_for_row=support_for_row,
        )

    for support_row in support_rows_for_direct_audit:
        row_id = support_record_id(support_row)
        objective_id = support_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        existing_objective_ids = expand_objective_refs(support_row.get("existing_objective_ids", ""), objective_ids)
        coverage_rows: list[dict[str, str]] = []
        coverage_source = ""
        if objective_id:
            coverage_rows = coverage_by_objective_id.get(objective_id, [])
            coverage_source = "objective" if coverage_rows else ""
        elif existing_objective_ids:
            for existing_objective_id in existing_objective_ids:
                coverage_rows.extend(coverage_by_objective_id.get(existing_objective_id, []))
            coverage_source = "existing_objectives" if coverage_rows else ""

        display_name = (
            support_row.get("system_name")
            or support_row.get("merchant_name")
            or support_row.get("enchantment_name")
            or support_row.get("ingredient_name")
            or row_id
        )
        guide_name_match = guide_contains_name(
            guide_normalized,
            display_name,
            support_row.get("store_name", ""),
            support_row.get("town_or_route", ""),
        )
        append_output(
            row_kind="progression_support",
            row_id=row_id,
            display_name=display_name,
            objective_id=objective_id,
            checklist_id="",
            checklist_entry="",
            checklist_tab="",
            mapping_type="",
            coverage_rows=coverage_rows,
            coverage_source=coverage_source,
            guide_name_match=guide_name_match,
            objective_row=objective_row,
            checklist_row={},
            support_rows_for_row=[support_row],
        )

    fieldnames = [
        "row_kind",
        "row_id",
        "objective_id",
        "checklist_id",
        "display_name",
        "checklist_entry",
        "category",
        "subcategory",
        "checklist_tab",
        "mapping_type",
        "route_placement",
        "source_content",
        "support_table_rows",
        "support_tables",
        "support_names",
        "guide_name_match",
        "coverage_source",
        "internal_coverage_row_count",
        "learn_or_discover_treatment",
        "craft_action_treatment",
        "investment_treatment",
        "skill_or_perk_treatment",
        "storage_treatment",
        "hold_or_stage_treatment",
        "route_resolution_treatment",
        "exclusion_treatment",
        "branch_treatment",
        "audit_status",
        "coverage_statuses",
        "completion_statuses",
        "guide_locations",
        "guide_cues",
        "recommended_action",
        "notes",
    ]

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} crafting/progression audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
