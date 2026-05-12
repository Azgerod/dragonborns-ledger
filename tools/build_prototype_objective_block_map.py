#!/usr/bin/env python3
"""Build the TB-026 prototype objective-to-block map."""

from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ROUTE_DIR = REPO_ROOT / "data" / "route-planning"
ROUTE_INDEX = ROUTE_DIR / "objective-route-index.csv"
LOCATION_GEOGRAPHY = REPO_ROOT / "data" / "locations" / "location-geography.csv"
OUTPUT = ROUTE_DIR / "prototype-objective-block-map.csv"
TEMPLATE = ROUTE_DIR / "prototype-objective-block-map.template.csv"

BLOCK_CORRIDORS = {
    "G02": ["riverwood_helgen_road", "whiterun_central_plains", "rorikstead_western_road"],
    "G03": ["falkreath_pine_forest", "ivarstead_rift_pass"],
    "G04": ["riften_rift"],
    "G05": ["markarth_reach", "old_hroldan_reach_road"],
    "G06": ["kynesgrove_eastmarch_road", "windhelm_eastmarch"],
    "G07": ["solitude_haafingar", "dragon_bridge_haafingar_road", "morthal_marsh"],
    "G08": ["dawnstar_pale_coast", "nightgate_pale_pass", "winterhold_coast"],
    "G11": ["dayspring_canyon", "icewater_volkihar_ferry"],
    "G12": ["raven_rock_west", "thirsk_central", "skaal_north", "tel_mithryn_east"],
    "G13": ["manual_validation_required"],
}

CORRIDOR_BLOCK = {corridor: block for block, corridors in BLOCK_CORRIDORS.items() for corridor in corridors}

FIXED_EARLY = {
    "OBJ-000001": ("G01", "inserted_fixed_early", "opening_escape", "Opening quest anchor."),
    "OBJ-000002": ("G01", "inserted_fixed_early", "opening_warm_core", "Opening Riverwood/Whiterun route anchor."),
    "OBJ-000479": ("G00", "inserted_setup_support", "setup", "Survival Mode run setting."),
    "OBJ-000702": ("G00", "inserted_setup_support", "setup", "Survival food/warmth system coverage."),
    "OBJ-000705": (
        "G00",
        "inserted_setup_support",
        "TB-031E/TB-032",
        "System coverage only; actual camping-supply crafting waits for material, station, carry, Survival, checklist, and warning validation.",
    ),
}

GATE_OVERRIDES = {
    "OBJ-002038": (
        "G09",
        "held_hard_gate",
        "level_36_linked_dungeon_loop",
        "Forbidden Legend linked-dungeon source corridor extracted to the controlled level-36 loop.",
    ),
    "OBJ-002049": (
        "G09",
        "held_hard_gate",
        "level_36_linked_dungeon_loop",
        "Forbidden Legend linked-dungeon source corridor extracted to the controlled level-36 loop.",
    ),
    "OBJ-002122": (
        "G09",
        "held_hard_gate",
        "level_36_linked_dungeon_loop",
        "Forbidden Legend linked-dungeon source corridor extracted to the controlled level-36 loop.",
    ),
    "OBJ-002136": (
        "G09",
        "held_hard_gate",
        "level_36_linked_dungeon_loop",
        "Forbidden Legend linked-dungeon source corridor extracted to the controlled level-36 loop.",
    ),
    "OBJ-002148": (
        "G02",
        "held_hard_gate",
        "level_8_silent_moons",
        "Silent Moons/Lunar weapon handling stays in the central corridor after the level-8 gate and exact item handling validation.",
    ),
    "OBJ-002354": (
        "G10",
        "held_hard_gate",
        "level_46_sky_haven_dragonbane",
        "Sky Haven Temple source corridor extracted to the level-46 Dragonbane gate.",
    ),
}

COUNTER_MECHANIC_OVERRIDES = {
    "OBJ-000104": (
        "G02",
        "anchored_window",
        "TB-031F/TB-032/TB-034",
        "Hired Muscle/Scare My Enemy is a Companions representative radiant; accept if the seed offers it, with exact target and warnings handled downstream.",
    ),
    "OBJ-002787": (
        "G03",
        "anchored_window",
        "TB-032/TB-034",
        "Archery Practice belongs with Angi's Camp/southern route handling; TB-031G validates the route-access class, while exact warnings and step placement remain downstream.",
    ),
    "OBJ-002788": (
        "G07",
        "anchored_window",
        "TB-034/TB-037",
        "Firebrand Wine Case follows the Scoundrel's Folly/Solitude quest-item cue, not generic late cleanup.",
    ),
    "OBJ-002789": (
        "G02",
        "anchored_window",
        "TB-034/TB-037",
        "Map of Dragon Burials follows the A Blade in the Dark/Riverwood quest-item cue, not generic late cleanup.",
    ),
}

SUPPORT_LOCATION_BLOCK_HINTS = {
    "whiterun": "G02",
    "riverwood": "G02",
    "rorikstead": "G02",
    "east of whiterun": "G02",
    "goldenhills plantation": "G02",
    "east of rorikstead": "G02",
    "tundra homestead": "G02",
    "falkreath": "G03",
    "ivarstead": "G03",
    "lakeview manor": "G03",
    "north of pinewatch": "G03",
    "riften": "G04",
    "ratway beneath riften": "G04",
    "shadowfoot sanctum": "G04",
    "frostroot cave": "G04",
    "nchuanthumz": "G04",
    "markarth": "G05",
    "old hroldan": "G05",
    "bilegulch": "G05",
    "hendraheim": "G05",
    "windhelm": "G06",
    "kynesgrove": "G06",
    "mara's eye pond": "G06",
    "gallows hall": "G06",
    "solitude": "G07",
    "dragon bridge": "G07",
    "morthal": "G07",
    "ustengrav": "G07",
    "windstad manor": "G07",
    "myrwatch": "G07",
    "blackbone isle grotto": "G07",
    "dead man's dread": "G07",
    "dawnstar": "G08",
    "winterhold": "G08",
    "nightgate": "G08",
    "fort dunstad": "G08",
    "heljarchen hall": "G08",
    "bloodchill": "G08",
    "fort dawnguard": "G11",
    "dayspring": "G11",
    "volkihar": "G11",
    "raven rock": "G12",
    "solstheim": "G12",
    "skaal": "G12",
    "thirsk": "G12",
    "tel mithryn": "G12",
    "severin": "G12",
}

BRANCH_OWNER = "TB-029/TB-033"
CHECKLIST_OWNER = "TB-031F/TB-033"
PROGRESSION_OWNER = "TB-031E/TB-033"

LEVELED_GATE_OVERRIDES = {
    "OBJ-000010": ("Level 46+", "first_enter_cell"),
    "OBJ-000029": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-000031": ("Level 25+", "accept_reward"),
    "OBJ-000042": ("Level 46+", "accept_reward"),
    "OBJ-000043": ("Level 46+", "first_enter_cell"),
    "OBJ-000044": ("Level 32+", "start_quest"),
    "OBJ-000045": ("Level 46+", "reward_handoff"),
    "OBJ-000198": ("Level 40+", "accept_reward"),
    "OBJ-000216": ("Level 27+", "claim_reward"),
    "OBJ-000218": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-000419": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001566": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001571": ("Level 46+", "first_enter_cell"),
    "OBJ-001573": ("Level 46+", "first_enter_cell"),
    "OBJ-001575": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001596": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001750": ("Level 46+", "first_enter_cell"),
    "OBJ-001751": ("Level 46+", "first_enter_cell"),
    "OBJ-001752": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-001753": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-001754": ("Level 8+", "first_loot_or_clear"),
    "OBJ-001755": ("Level 8+", "first_loot_or_clear"),
    "OBJ-001756": ("Level 8+", "first_loot_or_clear"),
    "OBJ-001757": ("Level 8+", "first_loot_or_clear"),
    "OBJ-001758": ("Level 8+", "first_loot_or_clear"),
    "OBJ-001759": ("Level 8+", "first_loot_or_clear"),
    "OBJ-001760": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001761": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001762": ("Level 46+", "accept_reward"),
    "OBJ-001763": ("Level 46+", "reward_handoff"),
    "OBJ-001764": ("Level 27+", "claim_reward"),
    "OBJ-001765": ("Level 60+", "final_battle_corpse_appearance"),
    "OBJ-001766": ("Level 32+", "start_quest"),
    "OBJ-001767": ("Level 32+", "start_quest"),
    "OBJ-001768": ("Level 32+", "start_quest"),
    "OBJ-001769": ("Level 32+", "start_quest"),
    "OBJ-001770": ("Level 40+", "accept_reward"),
    "OBJ-001772": ("Level 25+", "accept_reward"),
    "OBJ-002038": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-002049": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-002122": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-002136": ("Level 36+", "read_or_exterior_spawn"),
    "OBJ-002148": ("Level 8+", "first_loot_or_clear"),
    "OBJ-002354": ("Level 46+", "first_enter_cell"),
}

PARENT_OVERRIDES = {
    "OBJ-000010": ("OBJ-000010", "G10"),
    "OBJ-000029": ("OBJ-000029", "G09"),
    "OBJ-000031": ("OBJ-000031", "G08"),
    "OBJ-000042": ("OBJ-000042", "G10"),
    "OBJ-000043": ("OBJ-000043", "G10"),
    "OBJ-000044": ("OBJ-000044", "G04"),
    "OBJ-000045": ("OBJ-000045", "G10"),
    "OBJ-000198": ("OBJ-000198", "G07"),
    "OBJ-000216": ("OBJ-000216", "G08"),
    "OBJ-000218": ("OBJ-000218", "G09"),
    "OBJ-000419": ("OBJ-000419", "G13"),
    "OBJ-001566": ("OBJ-000419", "G13"),
    "OBJ-001571": ("OBJ-000043", "G10"),
    "OBJ-001573": ("OBJ-000010", "G10"),
    "OBJ-001575": ("OBJ-000419", "G13"),
    "OBJ-001596": ("OBJ-000419", "G13"),
    "OBJ-001750": ("OBJ-000043", "G10"),
    "OBJ-001751": ("OBJ-000010", "G10"),
    "OBJ-001752": ("OBJ-000218", "G09"),
    "OBJ-001753": ("OBJ-000218", "G09"),
    "OBJ-001754": ("OBJ-002148", "G02"),
    "OBJ-001755": ("OBJ-002148", "G02"),
    "OBJ-001756": ("OBJ-002148", "G02"),
    "OBJ-001757": ("OBJ-002148", "G02"),
    "OBJ-001758": ("OBJ-002148", "G02"),
    "OBJ-001759": ("OBJ-002148", "G02"),
    "OBJ-001760": ("OBJ-000419", "G13"),
    "OBJ-001761": ("OBJ-000419", "G13"),
    "OBJ-001762": ("OBJ-000042", "G10"),
    "OBJ-001763": ("OBJ-000045", "G10"),
    "OBJ-001764": ("OBJ-000216", "G08"),
    "OBJ-001765": ("OBJ-000419", "G13"),
    "OBJ-001766": ("OBJ-000044", "G04"),
    "OBJ-001767": ("OBJ-000044", "G04"),
    "OBJ-001768": ("OBJ-000044", "G04"),
    "OBJ-001769": ("OBJ-000044", "G04"),
    "OBJ-001770": ("OBJ-000198", "G07"),
    "OBJ-001772": ("OBJ-000031", "G08"),
    "OBJ-001641": ("OBJ-001980", "G03"),
    "OBJ-002038": ("OBJ-000218", "G09"),
    "OBJ-002049": ("OBJ-000218", "G09"),
    "OBJ-002122": ("OBJ-000218", "G09"),
    "OBJ-002136": ("OBJ-000218", "G09"),
    "OBJ-002148": ("OBJ-002148", "G02"),
    "OBJ-002354": ("OBJ-000010", "G10"),
    "OBJ-002524": ("OBJ-002148", "G02"),
    "OBJ-002787": ("OBJ-002204", "G03"),
    "OBJ-002788": ("OBJ-000040", "G07"),
    "OBJ-002789": ("OBJ-000007", "G02"),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def output_header() -> list[str]:
    with TEMPLATE.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def location_block_lookup() -> dict[str, str]:
    lookup: dict[str, str] = {}
    for row in read_csv(LOCATION_GEOGRAPHY):
        block = CORRIDOR_BLOCK.get(row["route_corridor"], "")
        if block:
            lookup[row["location_name"].casefold()] = block
    return lookup


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in value.split(" | ") if part.strip()]


def support_blocks(row: dict[str, str], location_lookup: dict[str, str]) -> list[str]:
    blocks: set[str] = set()
    for location in split_pipe(row["support_locations"]):
        lowered = location.casefold()
        if lowered in location_lookup:
            blocks.add(location_lookup[lowered])
            continue
        for hint, block in SUPPORT_LOCATION_BLOCK_HINTS.items():
            if hint in lowered:
                blocks.add(block)
                break
    return sorted(blocks)


def gate_status(row: dict[str, str]) -> str:
    if row["hard_level_gate"]:
        return "hard_level_gate"
    if row["objective_id"] in LEVELED_GATE_OVERRIDES or row["leveled_reward_threshold"]:
        return "leveled_reward"
    if "cell_entry_lock" in split_pipe(row["constraint_types"]):
        return "cell_entry_lock"
    if "quest_conflict_or_branch" in split_pipe(row["constraint_types"]):
        return "branch_or_conflict"
    if row["constraint_severities"]:
        return row["constraint_severities"]
    return "none"


def direct_block(row: dict[str, str]) -> str:
    return CORRIDOR_BLOCK.get(row["primary_route_corridor"], "")


def fixed_late_block(row: dict[str, str]) -> tuple[str, str]:
    name = row["objective_name"].casefold()
    constraint_types = split_pipe(row["constraint_types"])
    objective_id = row["objective_id"]
    if objective_id in {
        "OBJ-001754",
        "OBJ-001755",
        "OBJ-001756",
        "OBJ-001757",
        "OBJ-001758",
        "OBJ-001759",
    }:
        return "G02", "level_8_silent_moons"
    if objective_id in {"OBJ-000031", "OBJ-001772"}:
        return "G08", "level_25_mages_circlet"
    if objective_id in {"OBJ-000216", "OBJ-001764"}:
        return "G08", "level_27_pale_blade"
    if objective_id in {"OBJ-000198", "OBJ-001770"}:
        return "G07", "level_40_shield_of_solitude"
    if objective_id in {
        "OBJ-000042",
        "OBJ-000043",
        "OBJ-000045",
        "OBJ-001571",
        "OBJ-001573",
        "OBJ-001750",
        "OBJ-001751",
        "OBJ-001762",
        "OBJ-001763",
    }:
        return "G10", "level_46_classic_reward_loop"
    if objective_id in {
        "OBJ-000044",
        "OBJ-001766",
        "OBJ-001767",
        "OBJ-001768",
        "OBJ-001769",
    }:
        return "G04", "level_32_nightingale_armor_window"
    if objective_id in {
        "OBJ-000419",
        "OBJ-001566",
        "OBJ-001575",
        "OBJ-001596",
        "OBJ-001760",
        "OBJ-001761",
        "OBJ-001765",
    }:
        return "G13", "level_60_miraak_final"
    if objective_id in {"OBJ-000010", "OBJ-002354"}:
        return "G10", "level_46_sky_haven_dragonbane"
    if objective_id in {"OBJ-000029", "OBJ-000218", "OBJ-001752", "OBJ-001753"}:
        return "G09", "level_36_linked_dungeon_loop"
    if objective_id == "OBJ-001641":
        return "G03", "TB-028/TB-032"
    if objective_id in {"OBJ-000030", "OBJ-000032", "OBJ-000033", "OBJ-000034", "OBJ-000035"}:
        return "G08", "college_winterhold_depth"
    if "gauldur" in name or "saarthal" in name or "under saarthal" in name:
        return "G09", "level_36_linked_dungeon_loop"
    if any(term in name for term in ["chillrend", "dragonbane", "nightingale blade", "nightingale bow"]):
        return "G10", "level_46_classic_reward_loop"
    if "nightingale armor" in name or "nightingale boots" in name or "nightingale gloves" in name or "nightingale hood" in name:
        return "G04", "level_32_nightingale_armor_window"
    if "miraak" in name:
        return "G13", "level_60_miraak_final"
    if "deathbrand" in name or "stalhrim" in name or "karstaag" in name:
        return "G12", "solstheim_progression_window"
    if "ebony warrior" in name:
        return "G14", "level_80_ebony_warrior"
    if "legendary dragon" in name or row["objective_id"] == "OBJ-002784":
        return "G14", "level_78_legendary_dragon"
    if "all perks" in name or "level 252" in name or "legendary skill" in name or row["category"] == "skill_perk":
        return "G14", "level_252_all_perks_progression"
    if "the cause" in name:
        return "G13", "level_46_high_risk_ae"
    if "plague" in name or "bone wolf" in name or "bloodchill" in name or "hendraheim" in name or "ebony plate" in name:
        return "", "source_backed_late_ae_gate"
    if "cell_entry_lock" in constraint_types or "leveled_reward" in constraint_types:
        block = direct_block(row)
        return (block or "G14"), "source_backed_reward_or_cell_lock"
    return direct_block(row), "fixed_late_anchor"


def support_selection_owner(row: dict[str, str]) -> str:
    category = row["category"]
    if category == "property":
        return "TB-031E/TB-032/TB-034"
    if category in {"trophy", "collectible"}:
        return "TB-031F"
    if category in {"book_document", "spell_power", "crafting_unlock"}:
        return "TB-031E"
    if category in {"unique_item", "ae_creation"}:
        return "TB-031B/TB-031E"
    return "TB-031B"


def unresolved_support_owner(row: dict[str, str]) -> str:
    category = row["category"]
    if category == "property":
        return "TB-031E/TB-032/TB-034"
    if category in {"book_document", "spell_power", "crafting_unlock"}:
        return "TB-031E"
    if category in {"trophy", "collectible"}:
        return "TB-031F"
    return "TB-031E/TB-034"


def dependency_anchor_owner(row: dict[str, str]) -> str:
    category = row["category"]
    if category in {"npc_relationship", "pet_mount"}:
        return "TB-032/TB-034/TB-035"
    if category == "property":
        return "TB-034/TB-035"
    if category == "radiant":
        return "TB-031F"
    if category == "unique_item":
        return "TB-031B/TB-031E/TB-034"
    if category in {"quest", "misc_objective", "ae_creation"}:
        return "TB-034"
    return "TB-034"


def non_main_assignment(row: dict[str, str]) -> tuple[str, str, str, str]:
    placement = row["route_placement"]
    if placement == "branch_route":
        return "", "held_branch_deferred", BRANCH_OWNER, "Branch-exclusive row; use the TB-029 branch prototype and validate reload/canonical restoration in TB-033."
    if placement == "option_list":
        return "", "held_option_list", "TB-031D route-default-decisions.md; TB-035 option presentation", "Isolated default/option selection, not routed as a main step."
    if placement == "appendix":
        return "", "held_appendix", "TB-031A/TB-031B/TB-036", "Reference/checklist row, not a main-route insertion step."
    if placement == "excluded":
        return "", "excluded_nonroute", "none", "Excluded audit or failure/random/unbounded row."
    return "", "out_of_scope", "review", "Non-main route placement not handled by TB-026."


def main_assignment(row: dict[str, str], location_lookup: dict[str, str]) -> tuple[str, str, str, str]:
    objective_id = row["objective_id"]
    if objective_id in FIXED_EARLY:
        return FIXED_EARLY[objective_id]
    if objective_id in GATE_OVERRIDES:
        return GATE_OVERRIDES[objective_id]
    if objective_id in COUNTER_MECHANIC_OVERRIDES:
        return COUNTER_MECHANIC_OVERRIDES[objective_id]

    category = row["category"]
    rigidity = row["routing_rigidity"]
    candidate_status = row["candidate_status"]

    if objective_id in LEVELED_GATE_OVERRIDES:
        block, deferred = fixed_late_block(row)
        if not block:
            block = PARENT_OVERRIDES.get(objective_id, ("", ""))[1]
        return block, "held_hard_gate", deferred, "Level/reward-governed row; preserve the mapped threshold and trigger before final route prose."

    if category in {"skill_perk", "crafting_unlock"}:
        block = direct_block(row)
        return block, "progression_layer_integrated", PROGRESSION_OWNER, "TB-027 block policy is integrated; exact source, checklist, warning, and final validation work remains downstream."

    if rigidity == "fixed_late":
        block, deferred = fixed_late_block(row)
        return block, "held_hard_gate", deferred, "Fixed-late row; preserve level, reward, cell, quest-state, or progression gate."

    if rigidity == "windowed":
        block = direct_block(row)
        blocks = support_blocks(row, location_lookup) if not block else []
        if not block and len(blocks) == 1:
            block = blocks[0]
        deferred = "route_anchor_window"
        if row["has_quest_conflict"] == "yes" or "branch_or_hard_save" in split_pipe(row["constraint_severities"]):
            deferred = "TB-028/TB-032"
        return block, "anchored_window", deferred, "Windowed row; anchor, hard-save, faction, quest-state, or warning timing controls placement."

    if rigidity == "cleanup_safe":
        return "G14", "held_checklist_mapping", CHECKLIST_OWNER, "Cleanup-safe tracker waits for checklist synchronization."

    block = direct_block(row)
    if block:
        if block == "G13" or row["primary_geography_confidence"] == "none":
            return block, "manual_validation_required", "TB-032/TB-034", "Separate/manual geography row; TB-031G validates the access class, but final warning and route-step placement remain downstream."
        return block, "inserted_direct_geography", "route_block", "Direct geography row assigned by primary corridor; still needs row-level validation before prose."

    if candidate_status == "multiple_geography_points":
        return "", "held_candidate_selection", "TB-034", "Multiple geography points require exact point selection during final route placement."

    blocks = support_blocks(row, location_lookup)
    if candidate_status == "single_support_candidate":
        if len(blocks) == 1:
            if category == "property":
                return blocks[0], "support_candidate_conditional", "TB-032/TB-034", "Property/home candidate assigned to a regional block, but acquisition, ownership, safe storage, and support use remain conditional."
            return blocks[0], "inserted_support_candidate", "route_block", "Single support candidate assigned to the matching route block; availability remains conditional."
        return "", "support_candidate_conditional", unresolved_support_owner(row), "Single support candidate lacks a resolved route block; inspect support row before placement."

    if candidate_status == "multiple_support_candidates":
        if len(blocks) == 1:
            return blocks[0], "held_candidate_selection", support_selection_owner(row), "Multiple support candidates exist; one candidate block is visible but source selection remains open."
        return "", "held_candidate_selection", support_selection_owner(row), "Multiple support candidates require later source/copy/default selection."

    if category in {"trophy", "collectible"}:
        return "G14", "held_checklist_mapping", CHECKLIST_OWNER, "Counter/set coverage waits for checklist synchronization."
    if category in {"spell_power"}:
        return "", "held_progression_layer", PROGRESSION_OWNER, "Power/spell timing depends on progression, perk, or transformation planning."
    if category in {"unique_item", "quest", "radiant", "ae_creation", "pet_mount", "npc_relationship", "misc_objective", "book_document"}:
        return "", "dependency_anchor_pending", dependency_anchor_owner(row), "No route candidate data; place with parent quest, dependency, support table, or later checklist/default pass."

    return "", "dependency_anchor_pending", "TB-034", "No route candidate data; review before placement in the minimal route prototype."


def disposition(row: dict[str, str], route_block: str, status: str, deferred_to: str) -> str:
    placement = row["route_placement"]
    if placement == "branch_route":
        return "branch_deferred"
    if placement == "appendix":
        return "appendix"
    if placement == "excluded":
        return "excluded"
    if placement == "option_list":
        return "option_list"
    if status == "manual_validation_required":
        return "manual_validation"
    if status == "dependency_anchor_pending":
        return "dependency_anchor"
    if status == "support_candidate_conditional":
        return "conditional_support"
    if status in {"held_candidate_selection", "held_progression_layer", "progression_layer_integrated"}:
        return "later_pass"
    if status == "held_hard_gate" and deferred_to in {"TB-028/TB-032", "TB-028", "TB-032"}:
        return "later_pass"
    if status == "held_checklist_mapping":
        return "checklist_mapping"
    if status == "anchored_window":
        return "anchored_window"
    if status == "held_hard_gate" and not route_block:
        return "later_pass"
    if route_block:
        return "route_block"
    return "unassigned"


def reward_threshold(row: dict[str, str]) -> tuple[str, str]:
    return LEVELED_GATE_OVERRIDES.get(row["objective_id"], (row["leveled_reward_threshold"], ""))


def parent_info(row: dict[str, str], objective_names: dict[str, str]) -> tuple[str, str, str]:
    parent = PARENT_OVERRIDES.get(row["objective_id"])
    if not parent:
        return "", "", ""
    parent_id, parent_block = parent
    return parent_id, objective_names.get(parent_id, ""), parent_block


def build_row(
    row: dict[str, str],
    location_lookup: dict[str, str],
    objective_names: dict[str, str],
) -> dict[str, str]:
    if row["route_placement"] != "main_route":
        block, status, deferred, reason = non_main_assignment(row)
    else:
        block, status, deferred, reason = main_assignment(row, location_lookup)
    threshold, threshold_trigger = reward_threshold(row)
    parent_id, parent_name, parent_block = parent_info(row, objective_names)

    notes = "Generated TB-026 prototype assignment; source objective and constraint tables remain canonical."
    if status in {"inserted_direct_geography", "held_hard_gate"} and row["primary_route_corridor"]:
        notes += " Direct geography counts in the Markdown reflect source corridor membership; gate-extracted rows may be assigned to a later control block here."

    return {
        "objective_id": row["objective_id"],
        "objective_name": row["objective_name"],
        "category": row["category"],
        "route_placement": row["route_placement"],
        "routing_rigidity": row["routing_rigidity"],
        "route_block": block,
        "disposition": disposition(row, block, status, deferred),
        "source_corridor": row["primary_route_corridor"],
        "candidate_status": row["candidate_status"],
        "route_index_status": row["route_index_status"],
        "prototype_status": status,
        "gate_status": gate_status(row),
        "constraint_count": row["constraint_count"],
        "constraint_types": row["constraint_types"],
        "hard_level_gate": row["hard_level_gate"],
        "leveled_reward_threshold": threshold,
        "threshold_trigger": threshold_trigger,
        "parent_objective_id": parent_id,
        "parent_objective_name": parent_name,
        "parent_route_block": parent_block,
        "deferred_to": deferred,
        "reason": reason,
        "notes": notes,
    }


def main() -> int:
    location_lookup = location_block_lookup()
    rows = read_csv(ROUTE_INDEX)
    objective_names = {row["objective_id"]: row["objective_name"] for row in rows}
    header = output_header()
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=header, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(build_row(row, location_lookup, objective_names))
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)} ({len(rows)} rows).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
