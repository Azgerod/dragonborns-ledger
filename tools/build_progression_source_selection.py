#!/usr/bin/env python3
"""Build the TB-031E progression source-selection table.

This table is a planning artifact. It chooses route-planning defaults for
progression sources without converting them into final guide step order.
"""

from __future__ import annotations

import csv
from pathlib import Path
import re
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = REPO_ROOT / "data" / "constraints" / "progression-source-selections.csv"

SKILL_BOOKS = REPO_ROOT / "data" / "books" / "skill-books-locations.csv"
SPELL_TOMES = REPO_ROOT / "data" / "books" / "spell-tomes-locations.csv"
ENCHANTMENTS = REPO_ROOT / "data" / "skills" / "enchantment-learning-catalog.csv"
ALCHEMY = REPO_ROOT / "data" / "skills" / "alchemy-effect-catalog.csv"
MERCHANTS = REPO_ROOT / "data" / "skills" / "merchant-investment-catalog.csv"
CRAFTING = REPO_ROOT / "data" / "skills" / "practical-crafting-system-catalog.csv"
SKILLS = REPO_ROOT / "data" / "skills" / "skill-perk-catalog.csv"


COLUMNS = [
    "selection_id",
    "selection_type",
    "source_record_id",
    "objective_id",
    "name",
    "subcategory",
    "route_block",
    "selection_status",
    "selected_source",
    "source_location",
    "source_detail",
    "route_timing",
    "prerequisites_or_inputs",
    "avoid_until",
    "validation_owner",
    "source_note_refs",
    "notes",
]


COLLEGE_SPECIALIST = {
    "Alteration": "Tolfdir",
    "Conjuration": "Phinis Gestor",
    "Destruction": "Faralda",
    "Illusion": "Drevis Neloren",
    "Restoration": "Colette Marence",
}


TRAINING_PLAN = {
    "Alchemy": (
        "G02/G10/G14",
        "Arcadia to expert range when useful; Babette for master-range training after Dark Brotherhood access.",
        "Whiterun / Dark Brotherhood Sanctuary",
        "Use as a major late support skill, but preserve ingredient discovery and stored materials before repeated resets.",
        "No follower/trainer gold recovery; no Fortify Restoration loop baseline.",
    ),
    "Alteration": (
        "G08/G14",
        "Tolfdir at the College of Winterhold.",
        "College of Winterhold",
        "Train after College access and before Alteration ritual or magic-reset blocks if the route is short.",
        "Do not spend all training if it would overlevel before reward gates.",
    ),
    "Archery": (
        "G11/G14",
        "Sorine Jurard after Dawnguard-side access; Niruin is a Thieves Guild backup.",
        "Fort Dawnguard / Ragged Flagon",
        "Use sparingly for combat readiness and final gaps; natural Dawnguard/crossbow play should do most work.",
        "Do not reset primary offense before hard combat.",
    ),
    "Block": (
        "G02/G14",
        "Njada Stonearm through Companions to expert range; Chief Larak only if Blood-Kin/master training is route-clean.",
        "Jorrvaskr / Mor Khazgur",
        "Use only to smooth defensive gaps; natural combat and final perk validation carry the rest.",
        "Do not reset Block with armor/offense before hard dungeons.",
    ),
    "Conjuration": (
        "G08/G12/G14",
        "Phinis Gestor to expert range; Talvas Fathryon or Falion for master range when Solstheim/Morthal access is clean.",
        "College of Winterhold / Tel Mithryn / Morthal",
        "Train before Conjuration ritual support and late magic-reset cycles.",
        "Do not require follower-trainer free training from Talvas.",
    ),
    "Destruction": (
        "G08/G14",
        "Faralda at the College of Winterhold.",
        "College of Winterhold",
        "Use for controlled combat casting support and final gaps rather than repeated reset baseline.",
        "Do not reset while Destruction is the active damage plan.",
    ),
    "Enchanting": (
        "G08/G12/G14",
        "Sergius Turrianus to expert range; Neloth for master range after Solstheim/Tel Mithryn access.",
        "College of Winterhold / Tel Mithryn",
        "Train around disenchanting and final gear batches; recover to 100 for Extra Effect final gear.",
        "Do not destroy preserved unique items for training or learning.",
    ),
    "Heavy Armor": (
        "G02/G11/G14",
        "Farkas after Companions access, with Isran as the Dawnguard-side master backup.",
        "Jorrvaskr / Fort Dawnguard",
        "Use for combat build support only if heavy armor remains relevant to the route.",
        "Do not reset defensive armor before hard combat.",
    ),
    "Illusion": (
        "G08/G14",
        "Drevis Neloren at the College of Winterhold.",
        "College of Winterhold",
        "Train after spell access and use as a preferred late magic reset if crowd-control support is safe.",
        "Do not assume master-spell setup before College readiness.",
    ),
    "Light Armor": (
        "G04/G14",
        "Grelka to expert range; Nazir for master range after Dark Brotherhood access.",
        "Riften Market / Dark Brotherhood Sanctuary",
        "Use for final perk gaps or if light-armor rewards are part of the active build.",
        "Do not reset defensive armor before hard combat.",
    ),
    "Lockpicking": (
        "G04/G14",
        "Vex at the Ragged Flagon.",
        "Ragged Flagon",
        "Use paid training for final gaps because useful lock XP is finite.",
        "No repeated Lockpicking Legendary reset baseline.",
    ),
    "One-handed": (
        "G02/G14",
        "Amren for common training; Athis to expert range; Chief Burguk only if Blood-Kin/master training is route-clean.",
        "Whiterun / Jorrvaskr / Dushnikh Yal",
        "Natural combat should do most work; use training for final gaps.",
        "Do not reset primary offense before hard combat.",
    ),
    "Pickpocket": (
        "G04/G14",
        "Silda the Unseen to expert range; Vipir the Fleet for master range after Thieves Guild access.",
        "Windhelm / Ragged Flagon",
        "Use after crime/trophy risk controls are in place; useful as a conditional late reset only.",
        "No trainer-gold pickpocket recovery baseline.",
    ),
    "Restoration": (
        "G08/G11/G14",
        "Colette Marence to expert range; Florentius Baenius for master range after Dawnguard Bolstering the Ranks.",
        "College of Winterhold / Fort Dawnguard",
        "Train before undead-heavy/Dawnguard gaps and final recovery; conditional reset only.",
        "Do not reset immediately before Survival recovery or undead-heavy content.",
    ),
    "Smithing": (
        "G02/G11/G14",
        "Balimund to expert range; Eorlund Gray-Mane or Gunmar for master range depending on route access.",
        "Riften / Skyforge / Fort Dawnguard",
        "Use with material stockpiles and staged gear upgrades; major late reset candidate.",
        "No early max-crafting power spike.",
    ),
    "Sneak": (
        "G04/G14",
        "Garvey to expert range; Delvin Mallory for master range.",
        "Markarth / Ragged Flagon",
        "Use as a conditional late reset or final gap filler after stealth route safety exists.",
        "Do not use isolated early stealth grind as baseline.",
    ),
    "Speech": (
        "G07/G14",
        "Revyn Sadri for early/common support; Giraud Gemane for master range after Bards College access.",
        "Windhelm / Bards College",
        "Complete Investor, planned investments, and major selling before any reset.",
        "No repeated Speech Legendary reset baseline.",
    ),
    "Two-handed": (
        "G02/G14",
        "Vilkas after Companions access; Wulf Wild-Blood is a Solstheim backup if needed.",
        "Jorrvaskr / Skaal Village",
        "Use for final gaps if two-handed is not naturally active in combat.",
        "Do not reset primary offense before hard combat.",
    ),
}


RESET_PLAN = {
    "Alchemy": ("preferred_repeated_reset", "G14", "Primary level-252 engine after Experimenter/discovery policy and renewable ingredient supply exist."),
    "Alteration": ("preferred_repeated_reset", "G14", "Magic reset engine after College spell access, Magicka support, and safe bed loop exist."),
    "Archery": ("avoid_repeated_reset", "G14", "Combat offense skill; train/use naturally and avoid repeated Legendary resets."),
    "Block": ("avoid_repeated_reset", "G14", "Defensive skill; reset only as emergency after combat alternatives are stable."),
    "Conjuration": ("preferred_repeated_reset", "G14", "Magic reset engine after summons, Soul Trap support, and Magicka/cost support exist."),
    "Destruction": ("combat_emergency_only", "G14", "Combat offense skill; avoid repeated resets unless another damage plan carries Legendary fights."),
    "Enchanting": ("preferred_repeated_reset", "G14", "Primary crafting reset after source effects are learned and before final gear is made; recover to 100."),
    "Heavy Armor": ("avoid_repeated_reset", "G14", "Defensive skill; do not reset alongside other defense/offense skills."),
    "Illusion": ("preferred_repeated_reset", "G14", "Magic reset engine after utility/control spell access and safe casting conditions exist."),
    "Light Armor": ("avoid_repeated_reset", "G14", "Defensive skill; final gaps through training/use rather than repeated resets."),
    "Lockpicking": ("excluded_repeated_reset", "G14", "Finite useful lock XP; baseline is no repeated Legendary reset."),
    "One-handed": ("combat_emergency_only", "G14", "Combat offense skill; avoid repeated resets unless a separate offense plan is active."),
    "Pickpocket": ("conditional_reset", "G14", "Conditional late reset only after crime/trophy risks and source inventory are controlled."),
    "Restoration": ("conditional_reset", "G14", "Conditional reset only after Dawnguard/undead-heavy and Survival recovery risks are safe."),
    "Smithing": ("preferred_repeated_reset", "G14", "Primary crafting reset engine after material, gold, storage, and power-curve controls exist."),
    "Sneak": ("conditional_reset", "G14", "Conditional reset only when stealth remains safe and does not replace combat readiness."),
    "Speech": ("excluded_repeated_reset", "G14", "Investments/selling/Fence support make repeated resets non-baseline; if used, only after all Speech-dependent work."),
    "Two-handed": ("combat_emergency_only", "G14", "Combat offense skill; avoid repeated resets unless a separate offense plan is active."),
}


CRAFT_ACTIONS = {
    "Alchemy": (
        "G02/G14",
        "Craft one early Restore Health potion for Artificer; run final value/XP batches only after sleep, storage, and ingredient stockpile checks.",
        "Alchemy lab; stored ingredients; later Experimenter 3 for discovery pass.",
    ),
    "Enchanting": (
        "G02/G14",
        "Enchant one disposable crafted item for Artificer after the first nonunique enchantment source is learned; reserve final dual-effect gear for Enchanting 100.",
        "Arcane enchanter; filled soul gem; disposable item; learned nonunique effect.",
    ),
    "Staff Enchanting": (
        "G12",
        "Craft Staff of Flames at a normal Staff Enchanter.",
        "Tel Mithryn Staff Enchanter after Reluctant Steward; unenchanted Destruction staff; Flames known; 1 Heart Stone.",
    ),
    "Smithing": (
        "G02/G14",
        "Forge one Iron Dagger for Artificer and use later material batches for Smithing recovery.",
        "Forge/anvil; 1 iron ingot; 1 leather strip.",
    ),
    "Atronach Forge": (
        "G08/G14",
        "Craft Fire Salts at The Midden Atronach Forge as representative practical-system use and Survival hot-soup support.",
        "Salt Pile; ruby/flawless ruby/silver ruby ring/gold ruby necklace; any Soul Gem.",
    ),
    "Baking": (
        "G14",
        "Use a Hearthfire oven only after homestead construction makes it route-natural; keep as property/checklist support, not an early requirement.",
        "Hearthfire home with kitchen/oven access and stored ingredients.",
    ),
    "Bone Forge": (
        "G06/G14",
        "Treat Bone Forge use as Gallows Hall property/system support after acquisition; exact skeleton output remains property/checklist validation.",
        "Gallows Hall acquisition and stored crafting ingredients.",
    ),
    "Construction": (
        "G14",
        "Build all three Hearthfire homes and wings through staged material depots for Master Architect/property completion.",
        "Purchased land, drafting tables/workbenches, lumber, stone, clay, iron fittings, locks, hinges, nails, glass/straw/goat horns where needed.",
    ),
    "Cooking": (
        "G01/G06/G14",
        "Cook ordinary food early for Hard Worker and Survival; stage Fire Salts for hot soup before cold expeditions.",
        "Cooking pot/spit; food ingredients; Fire Salts for hot soups.",
    ),
    "Imbuing Chamber": (
        "G12",
        "Create a Mind Control Spider as representative Imbuing Chamber use.",
        "White Ridge Barrow Imbuing Chamber; Albino Spider Pod; any Soul Gem.",
    ),
    "Mining": (
        "G02",
        "Mine one ore vein early for Hard Worker and continue route-natural ore gathering for Smithing.",
        "Pickaxe and safe ore vein.",
    ),
    "Smelting": (
        "G02/G14",
        "Smelt route-mined ore into ingots during Smithing/material staging.",
        "Smelter access and stored ore.",
    ),
    "Tanning": (
        "G02/G14",
        "Tan hides/leather and cut leather strips during Smithing/material staging.",
        "Tanning rack and hides/leather.",
    ),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def grouped_by(rows: Iterable[dict[str, str]], key: str) -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        out.setdefault(row[key], []).append(row)
    return out


def route_block_for_location(row: dict[str, str]) -> str:
    worldspace = row.get("worldspace", "")
    hold = row.get("hold", "")
    location = row.get("location", "")
    detail = row.get("location_detail", "")
    joined = f"{location} {detail}"

    if "Solstheim" in worldspace or "Solstheim" in joined or location in {"Raven Rock", "Tel Mithryn"}:
        return "G12"
    if worldspace in {"Soul Cairn", "Deadlands", "Skuldafn", "Apocrypha"}:
        return "G13"
    if "College of Winterhold" in joined or hold == "Winterhold":
        return "G08"
    if hold == "Whiterun Hold":
        return "G02"
    if hold == "Falkreath Hold":
        return "G03"
    if hold == "The Rift":
        return "G04"
    if hold == "The Reach":
        return "G05"
    if hold == "Eastmarch":
        return "G06"
    if hold in {"Haafingar", "Hjaalmarch"}:
        return "G07"
    if hold == "The Pale":
        return "G08"
    return "G14"


def score_book_copy(row: dict[str, str]) -> tuple[int, str]:
    score = 0
    if row.get("route_candidate_status") == "provisional_objective_representative":
        score += 50
    if not row.get("ownership_or_crime_notes"):
        score += 25
    if not row.get("quest_or_state_dependency"):
        score += 25
    if row.get("missability", "") in {"", "unknown", "none"}:
        score += 10
    hold_weight = {
        "Whiterun Hold": 18,
        "Falkreath Hold": 16,
        "The Rift": 14,
        "Eastmarch": 12,
        "The Reach": 10,
        "Haafingar": 10,
        "Winterhold": 8,
        "The Pale": 7,
        "Hjaalmarch": 6,
    }
    score += hold_weight.get(row.get("hold", ""), 0)
    text = " ".join(row.get(field, "") for field in ("location", "location_detail", "ownership_or_crime_notes", "quest_or_state_dependency")).lower()
    if any(term in text for term in ("stolen", "owned", "crime")):
        score -= 30
    if any(term in text for term in ("quest", "requires", "during")):
        score -= 10
    return score, row.get("book_location_id", "")


def choose_skill_book(rows: list[dict[str, str]]) -> dict[str, str]:
    return max(rows, key=score_book_copy)


def choose_spell_source(rows: list[dict[str, str]]) -> dict[str, str]:
    school = rows[0].get("skill_or_school", "")
    specialist = COLLEGE_SPECIALIST.get(school, "")
    for row in rows:
        if specialist and f"Purchase from {specialist}" in row.get("location_detail", ""):
            return row
    preferred_phrases = [
        "Learned when",
        "Reward",
        "Fixed location",
        "Found in",
        "Placed",
        "Quest reward",
    ]
    for phrase in preferred_phrases:
        for row in rows:
            detail = row.get("location_detail", "")
            if phrase.lower() in detail.lower() and "random" not in detail.lower():
                return row
    non_random = [row for row in rows if "random" not in row.get("location_detail", "").lower()]
    return non_random[0] if non_random else rows[0]


def enchantment_source(dis_sources: str) -> str:
    text = re.sub(r"\s+", " ", dis_sources).strip()
    if not text:
        return "No source selected."
    first = re.split(r"\bIncludes\b|(?<=\w) (?=All varieties of)|(?<=\w) (?=All weapons)", text)[0].strip()
    return first or text


def alchemy_method(row: dict[str, str]) -> tuple[str, str, str]:
    source_content = row.get("source_content", "")
    section = row.get("ingredient_section", "")
    note = row.get("source_note", "")
    merchant = row.get("merchant_availability", "")
    garden = row.get("garden_planting", "")

    if section == "quest":
        return (
            "quest_window_consumption",
            "Consume one copy only after the parent quest no longer needs it, with a hard save before the discovery pass.",
            "G14",
        )
    if "Khajiit" in note or "Khajiit" in merchant:
        return ("khajiit_caravan_purchase", "Buy one copy from Khajiit caravan stock and store it for the Experimenter pass.", "G06/G14")
    if "Fishing" in note or "Caught by Fishing" in note:
        return ("fishing_source", "Acquire during TB-031F fishing/counter route and store for the Experimenter pass.", "G14")
    if garden and garden not in {"", "not_listed", "None"}:
        return ("garden_or_greenhouse_grow", "Plant/grow or harvest one copy where route infrastructure supports it; store for Experimenter pass.", "G14")
    if source_content == "dragonborn":
        return ("solstheim_harvest_or_purchase", "Acquire during the Solstheim spine and store at the selected base.", "G12/G14")
    if source_content == "dawnguard":
        return ("dawnguard_parent_route", "Acquire during Dawnguard/Forgotten Vale parent routing and store for final discovery.", "G11/G14")
    if merchant not in {"", "None", "not_listed"}:
        return ("apothecary_purchase_or_route_harvest", "Buy or harvest one copy during regional service loops; store for Experimenter pass.", "G02/G14")
    return ("route_harvest", "Harvest one copy during natural regional routing and store for Experimenter pass.", "G14")


def investment_block(row: dict[str, str]) -> str:
    hold = row.get("hold", "")
    if hold == "Eastmarch":
        return "G06"
    if hold == "The Rift":
        return "G04"
    if hold == "Whiterun Hold":
        return "G02"
    if hold == "The Reach":
        return "G05"
    if hold in {"Haafingar", "Hjaalmarch"}:
        return "G07"
    if hold in {"The Pale", "Winterhold"}:
        return "G08"
    if hold == "Falkreath Hold":
        return "G03"
    if hold == "Solstheim":
        return "G12"
    return "G14"


def add_row(rows: list[dict[str, str]], counter: int, **values: str) -> int:
    rows.append(
        {
            "selection_id": f"PROGSEL-{counter:06d}",
            **{column: values.get(column, "") for column in COLUMNS if column != "selection_id"},
        }
    )
    return counter + 1


def main() -> int:
    rows: list[dict[str, str]] = []
    counter = 1

    for objective_id, candidates in sorted(grouped_by(read_csv(SKILL_BOOKS), "objective_id").items()):
        chosen = choose_skill_book(candidates)
        counter = add_row(
            rows,
            counter,
            selection_type="skill_book_copy",
            source_record_id=chosen["book_location_id"],
            objective_id=objective_id,
            name=chosen["book_title"],
            subcategory=chosen["skill_or_school"],
            route_block=route_block_for_location(chosen),
            selection_status="selected_default_copy_pending_route_validation",
            selected_source=chosen["location"],
            source_location=chosen["location"],
            source_detail=chosen["location_detail"],
            route_timing="Collect selected copy when its route block is safe; read after Scholar's Insight and high-skill timing check.",
            prerequisites_or_inputs=chosen["quest_or_state_dependency"],
            avoid_until="Do not read before Scholar's Insight unless final route explicitly documents the tradeoff.",
            validation_owner="TB-033/TB-034 final route and skill-state validation",
            source_note_refs=chosen["citations"],
            notes="One title-level skill book objective needs one selected copy; duplicate copies remain non-required alternates.",
        )

    for objective_id, candidates in sorted(grouped_by(read_csv(SPELL_TOMES), "objective_id").items()):
        chosen = choose_spell_source(candidates)
        detail = chosen["location_detail"]
        is_purchase = detail.lower().startswith("purchase from")
        counter = add_row(
            rows,
            counter,
            selection_type="spell_tome_source",
            source_record_id=chosen["book_location_id"],
            objective_id=objective_id,
            name=chosen["book_title"],
            subcategory=chosen["skill_or_school"],
            route_block=route_block_for_location(chosen),
            selection_status="selected_vendor_source" if is_purchase else "selected_fixed_or_scripted_source",
            selected_source=chosen["location"],
            source_location=chosen["location"],
            source_detail=detail,
            route_timing="Buy during the relevant College/service block if vendor-sourced; otherwise pair with parent quest/location.",
            prerequisites_or_inputs=chosen["quest_or_state_dependency"],
            avoid_until="Random loot is not baseline; do not require a source not selected in this table.",
            validation_owner="TB-033 spell-source and final learned-spell validation",
            source_note_refs=chosen["citations"],
            notes="College specialist vendors are preferred where source-listed; fixed/scripted sources are used where a vendor source is not the clean default.",
        )

    for row in read_csv(ENCHANTMENTS):
        learnable = row["route_treatment"] == "source_listed_enchantment_learning"
        counter = add_row(
            rows,
            counter,
            selection_type="enchantment_learning_source",
            source_record_id=row["enchantment_record_id"],
            objective_id=row["objective_id"],
            name=row["enchantment_name"],
            subcategory=row["effect_group"],
            route_block="G14" if learnable else "",
            selection_status="selected_nonunique_or_creation_source_family" if learnable else row["route_treatment"],
            selected_source=enchantment_source(row["disenchant_sources"]) if learnable else row["preservation_conflict_item"],
            source_location="Arcane enchanter and acquired disposable source item" if learnable else "Excluded/audit only",
            source_detail=row["disenchant_sources"],
            route_timing="Store source items as found; disenchant after source-item preservation checks and before final enchanting validation." if learnable else "Do not learn in main-route continuity.",
            prerequisites_or_inputs="Arcane enchanter access; source item not unique-preserved; unlearned effect." if learnable else row["learning_policy"],
            avoid_until="Do not disenchant unique-preservation exclusions; do not assume random stock before the item is verified.",
            validation_owner="TB-033 enchantment-learning validation",
            source_note_refs=row["citations"],
            notes="Exact physical item can be any source-listed nonunique member of the selected family; random/vendor availability must be verified in final route inventory.",
        )

    for row in read_csv(ALCHEMY):
        method, timing, block = alchemy_method(row)
        effects = " | ".join(row[f"effect_{idx}"] for idx in range(1, 5))
        counter = add_row(
            rows,
            counter,
            selection_type="alchemy_ingredient_source",
            source_record_id=row["alchemy_record_id"],
            objective_id=row["objective_id"],
            name=row["ingredient_name"],
            subcategory=row["source_content"],
            route_block=block,
            selection_status=method,
            selected_source=method,
            source_location=row["merchant_availability"] or row["source_note"],
            source_detail=effects,
            route_timing=timing,
            prerequisites_or_inputs="One ingredient copy; Alchemy 50 and Experimenter 3 for one-eat all-effects discovery policy.",
            avoid_until="Do not consume quest/one-time ingredients before parent quest and preservation checks are complete.",
            validation_owner="TB-033 alchemy-effect validation",
            source_note_refs=row["citations"],
            notes=row["source_note"] or row["notes"],
        )

    for row in read_csv(MERCHANTS):
        available = row["invest_status"] == "available"
        counter = add_row(
            rows,
            counter,
            selection_type="merchant_investment",
            source_record_id=row["merchant_investment_record_id"],
            objective_id=row["objective_id"],
            name=row["merchant_name"],
            subcategory=row["hold"],
            route_block=investment_block(row) if available else "",
            selection_status="selected_investment_circuit" if available else row["invest_status"],
            selected_source=row["store_name"],
            source_location=f"{row['town_or_route']} / {row['hold']}",
            source_detail=row["availability_notes"],
            route_timing="Invest during the first safe regional merchant sweep after Speech 70 and Investor are active." if available else "Do not route as required investment unless TB-033 later validates official PS4 AE availability.",
            prerequisites_or_inputs="Speech 70; Investor perk; merchant alive/accessible; no active hostile/faction state.",
            avoid_until="Complete before any Speech reset or role/default change that can affect merchant access.",
            validation_owner="TB-033 investment validation",
            source_note_refs=row["citations"],
            notes=row["notes"],
        )

    for row in read_csv(CRAFTING):
        block, action, inputs = CRAFT_ACTIONS.get(row["system_name"], ("G14", row["notes"], "Route-validated materials."))
        counter = add_row(
            rows,
            counter,
            selection_type="crafting_system_action",
            source_record_id=row["crafting_system_record_id"],
            objective_id=row["objective_id"] or row["existing_objective_ids"],
            name=row["system_name"],
            subcategory=row["system_type"],
            route_block=block,
            selection_status=row["route_treatment"],
            selected_source=action,
            source_location="Route station selected by block policy",
            source_detail=row["notes"],
            route_timing="Perform where the selected station, materials, bed/rest support, storage, and Survival carry constraints are all satisfied.",
            prerequisites_or_inputs=inputs,
            avoid_until="Do not use material-recovery exploits or early max-crafting power spikes.",
            validation_owner="TB-033 crafting-system validation",
            source_note_refs=row["citations"],
            notes="TB-031E chooses a representative output/action where the source table intentionally left system use open.",
        )

    for row in read_csv(SKILLS):
        skill = row["skill_name"]
        block, trainer, location, timing, avoid = TRAINING_PLAN[skill]
        counter = add_row(
            rows,
            counter,
            selection_type="training_policy",
            source_record_id=row["skill_record_id"],
            objective_id=row["skill_100_objective_id"],
            name=skill,
            subcategory=row["specialization"],
            route_block=block,
            selection_status="selected_training_block",
            selected_source=trainer,
            source_location=location,
            source_detail=row["notes"],
            route_timing=timing,
            prerequisites_or_inputs="Use at most five paid sessions per character level; trainers cannot raise skills above 90.",
            avoid_until=avoid,
            validation_owner="TB-033 final skill-state validation",
            source_note_refs="SN-000120-training-and-skill-boost-constraints.md",
            notes="Training is a smoothing tool, not the sole route to skill 100.",
        )

    for row in read_csv(SKILLS):
        skill = row["skill_name"]
        status, block, notes = RESET_PLAN[skill]
        counter = add_row(
            rows,
            counter,
            selection_type="legendary_reset_distribution",
            source_record_id=row["skill_record_id"],
            objective_id=row["skill_100_objective_id"],
            name=skill,
            subcategory=row["specialization"],
            route_block=block,
            selection_status=status,
            selected_source=status,
            source_location="Late progression loop",
            source_detail=row["legendary_reset_relevance"],
            route_timing="G14 baseline; cautiously late G12/G13 only after combat alternatives, beds, storage, and recovery paths exist.",
            prerequisites_or_inputs="Skill at 100 before each Legendary reset; final route must restore every skill to 100 and allocate all 251 perk ranks.",
            avoid_until="Do not reset active offense/defense/support before hard content or before required service/investment work.",
            validation_owner="TB-033 final skill-state validation",
            source_note_refs="SN-000119-leveling-perk-points-and-legendary-reset-plan.md | SN-000120-training-and-skill-boost-constraints.md",
            notes=notes,
        )

    manual_rows = [
        (
            "progression_policy",
            "BLACKBOOK-SCHOLARS-INSIGHT",
            "OBJ-000797",
            "Scholar's Insight skill-book policy",
            "Black Book power",
            "G12/G14",
            "selected_until_skill_books_read",
            "Use Scholar's Insight before the planned skill-book reading pass; switch to final Black Book defaults after skill-book completion.",
            "Black Book power swap surface",
            "Read selected skill books late enough to preserve progression value.",
            "Do not casually read skill books before this power is active unless final route documents a specific tradeoff.",
            "SN-000051-skill-books-and-reader.md",
        ),
        (
            "progression_policy",
            "OGHMA-INFINIUM-TIMING",
            "OBJ-001079",
            "Oghma Infinium timing policy",
            "Quest skill reward",
            "G14",
            "selected_late_gap_closer",
            "Read/use late on the skill group with the largest remaining pre-100 gap; if the final route needs a fixed default, use Magic unless TB-033 final skill-state math chooses otherwise.",
            "Discerning the Transmundane / Oghma Infinium",
            "Acquire through the controlled Septimus window; do not use until progression math is known.",
            "Do not use to raise skills already at 100; hard-save before reading because the reward can fail to grant all points.",
            "SN-000053-black-books-and-unique-quest-books.md | SN-000126-progression-source-selection-and-grind-policy.md",
        ),
    ]
    for item in manual_rows:
        (
            selection_type,
            source_record_id,
            objective_id,
            name,
            subcategory,
            block,
            status,
            selected,
            location,
            timing,
            avoid,
            refs,
        ) = item
        counter = add_row(
            rows,
            counter,
            selection_type=selection_type,
            source_record_id=source_record_id,
            objective_id=objective_id,
            name=name,
            subcategory=subcategory,
            route_block=block,
            selection_status=status,
            selected_source=selected,
            source_location=location,
            source_detail=timing,
            route_timing=timing,
            prerequisites_or_inputs="Route must satisfy parent quest/book power access first.",
            avoid_until=avoid,
            validation_owner="TB-033 final skill-state validation",
            source_note_refs=refs,
            notes="Manual TB-031E progression policy row.",
        )

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} progression source-selection rows to {OUTPUT.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
