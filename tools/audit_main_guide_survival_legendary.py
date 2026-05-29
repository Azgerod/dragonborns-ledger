#!/usr/bin/env python3
"""Audit Survival Mode logistics and Legendary progression for TB-040."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
COVERAGE_LEDGER = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVE_STATUS = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-objective-final-status.csv"
SURVIVAL_CONSTRAINTS = REPO_ROOT / "data" / "constraints" / "survival-mode-constraints.md"
SKILL_PERK_PLAN = REPO_ROOT / "data" / "constraints" / "skill-perk-leveling-plan.md"
PROGRESSION_SELECTIONS = REPO_ROOT / "data" / "constraints" / "progression-source-selections.csv"
OBJECTIVE_CONSTRAINTS = REPO_ROOT / "data" / "route-planning" / "objective-constraints.csv"
LOCATION_GEOGRAPHY = REPO_ROOT / "data" / "locations" / "location-geography.csv"
OUTPUT_AUDIT = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-survival-legendary-audit.csv"
OUTPUT_SUMMARY = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-survival-legendary-summary.csv"


SURVIVAL_SECTIONS = {
    "Global Survival Rules": "survival_global_rule",
    "Travel Network Constraints": "survival_travel_network",
    "Cold and Regional Sequencing": "survival_cold_region",
    "Storage, Food, and Base Infrastructure": "survival_infrastructure",
}

PROGRESSION_SOURCE_TYPES = {
    "legendary_reset_distribution",
    "training_policy",
    "crafting_system_action",
    "progression_policy",
}

FIELDNAMES = [
    "audit_area",
    "check_id",
    "source_file",
    "source_section",
    "row_label",
    "check_type",
    "objective_id",
    "objective_name",
    "source_status",
    "guide_locations",
    "route_protection",
    "audit_status",
    "recommended_action",
    "evidence",
    "notes",
]


GLOBAL_SETUP_RULES = [
    (
        "TB040-SETUP-001",
        "Survival Mode activation",
        "The guide must turn Survival Mode on immediately after Helgen and keep it as the default.",
        [("survival mode is mandatory",), ("turn it on immediately after the escape",)],
    ),
    (
        "TB040-SETUP-002",
        "Survival Mode exception discipline",
        "Any Survival Mode exception must be explicit, narrow, and immediately reverted.",
        [("survival mode exception",), ("turn survival mode back on",)],
    ),
    (
        "TB040-SETUP-003",
        "Legendary difficulty baseline",
        "The route must start and remain on Legendary difficulty unless an explicit exception appears.",
        [("keep legendary difficulty on",), ("set the difficulty to legendary",)],
    ),
    (
        "TB040-SETUP-004",
        "Sleep-gated level-up policy",
        "Survival Mode level-ups and major power checks need proper-bed timing.",
        [("sleep in a proper bed",), ("level-up", "level up")],
    ),
    (
        "TB040-SETUP-005",
        "Hot-food cold preparation",
        "The route must preserve Fire Salts and explain hot food as cold-travel support.",
        [("fire salts",), ("hot food", "hot soup")],
    ),
    (
        "TB040-SETUP-006",
        "Camping is backup support",
        "Camping Supplies should not replace inns and owned beds as the normal sleep plan.",
        [("camping supplies",), ("do not depend on camps", "emergency support only")],
    ),
    (
        "TB040-SETUP-007",
        "Route discipline prevents unsafe detours",
        "The player-facing guide must forbid unplanned Creation starts, notes, rumors, locations, and detours.",
        [("route discipline",), ("courier letters",), ("creation prompts",)],
    ),
    (
        "TB040-SETUP-008",
        "Carry and sell-off discipline",
        "Survival carry pressure must be represented with sell-off, storage, and carry-space checks.",
        [("carry weight", "carry space"), ("sell ordinary",), ("storage", "store")],
    ),
]


SURVIVAL_TERM_RULES: dict[str, list[tuple[str, ...]]] = {
    "Main route after `Unbound`": [("survival mode is mandatory",), ("turn it on immediately",)],
    "Hunger and food": [("food",), ("hot food", "hot soup", "fire salts")],
    "Fatigue, sleep, and level-ups": [("fatigue",), ("sleep",), ("level-up", "level up")],
    "Cold, warmth, and freezing water": [("cold",), ("hot food", "hot soup"), ("warm", "cold gear")],
    "Reduced carry capacity": [("carry weight", "carry space"), ("storage", "store"), ("sell ordinary",)],
    "No natural health regeneration and disease pressure": [("healing",), ("cure disease", "shrine")],
    "Shrines and blessings": [("shrine",), ("sleep", "rest")],
    "Ordinary fast travel": [("route discipline",), ("carriage", "ferry", "horse")],
    "Major city carriage network": [("carriage",), ("stables", "stables")],
    "Hearthfire homestead carriages": [("carriage driver",), ("hearthfire", "lakeview", "windstad", "heljarchen")],
    "Ferries and boats": [("ferry",), ("raven rock", "windhelm")],
    "Horses and mounts": [("horse",), ("mount", "shadowmere", "arvak")],
    "Dragon riding": [("dragonrider",), ("bend will", "sahrotaar")],
    "Dead Man's Dread map travel": [("dead man's dread",), ("one-way", "ship map")],
    "Early warm/temperate core": [("early warm-core", "warm support"), ("riverwood", "whiterun")],
    "Northern coast, Pale, Winterhold": [("cold-weather",), ("dawnstar", "winterhold"), ("hot food",)],
    "Mountains and high passes": [("mountain",), ("hot food", "warm support")],
    "Source-listed cold interiors": [("cold gear", "hot food"), ("cold northern ruin", "icy reservoirs")],
    "Solstheim": [("solstheim",), ("raven rock", "severin manor"), ("hot food", "cold gear")],
    "Freezing water and coastal swims": [("icy reservoirs", "freezing waters"), ("hot food", "cold gear")],
    "Long dungeons and enclosed worldspaces": [("long dungeon chains", "long ruin"), ("food",), ("carry", "storage")],
    "Inns": [("inn",), ("food",), ("bed", "room")],
    "First approved safe storage": [("owned storage",), ("breezehome", "tundra homestead")],
    "City and AE homes": [("owned-home", "owned home"), ("sleep/storage", "safe storage")],
    "Goldenhills Plantation": [("goldenhills",), ("food, bed, and income base", "food, bed")],
    "Hearthfire homesteads": [("hearthfire",), ("materials", "carriage driver")],
    "Camping Supplies": [("camping supplies",), ("emergency support", "not depend on camps")],
    "Representative favors and work activities": [("hulda",), ("hard worker", "wood chopped")],
}


GEOGRAPHY_COLD_RULES: dict[str, list[tuple[str, ...]]] = {
    "regional_cold": [("cold-weather", "cold travel"), ("hot food", "warm support")],
    "source_listed_cold_interior": [("cold gear", "hot food"), ("cold northern ruin", "icy reservoirs")],
    "high_elevation_or_mountain": [("mountain",), ("hot food", "warm support")],
    "solstheim_cold_region": [("solstheim",), ("raven rock", "severin manor"), ("hot food", "cold gear")],
}


CRAFTING_TERM_RULES: dict[str, list[tuple[str, ...]]] = {
    "Alchemy": [("artificer potion", "arcadia's tutorial"), ("alchemy",)],
    "Enchanting": [("artificer enchanted-item", "enchant one disposable"), ("enchanting",)],
    "Staff Enchanting": [("staff enchanter",), ("staff of flames",)],
    "Smithing": [("iron dagger",), ("smithing",)],
    "Atronach Forge": [("atronach forge",), ("fire salts",)],
    "Baking": [("hearthfire",), ("kitchen",)],
    "Bone Forge": [("bone forge",), ("notes on the bone forge",)],
    "Construction": [("hearthfire homes", "master architect"), ("materials",)],
    "Cooking": [("cook one food item", "cooked food"), ("hard worker",)],
    "Imbuing Chamber": [("imbuing chamber",), ("mind control spider",)],
    "Mining": [("mine one ore",), ("hard worker",)],
    "Smelting": [("smelted", "smelting"), ("ingots",)],
    "Tanning": [("tanned", "tanning"), ("leather",)],
}


PROGRESSION_POLICY_TERM_RULES: dict[str, list[tuple[str, ...]]] = {
    "Scholar's Insight skill-book policy": [("scholar's insight",), ("skill-book", "skill book")],
    "Oghma Infinium timing policy": [("oghma infinium",), ("late skill gap", "path of magic")],
}


LOGISTICS_CATEGORIES = {
    "rest": ("sleep", "rest", "bed", "inn", "fatigue", "support stop"),
    "food_healing": ("food", "healing", "hot food", "hot soup", "cure disease"),
    "carry_storage": ("carry", "storage", "store", "empty", "sell ordinary", "owned storage"),
    "travel": ("travel", "carriage", "ferry", "horse", "ride", "road", "stables", "boat"),
    "save": ("rotating manual save", "hard save"),
}

ROUTE_SECTION_KEYWORDS = (
    "travel",
    "clear",
    "enter",
    "dungeon",
    "barrow",
    "fort",
    "cave",
    "crypt",
    "ruin",
    "tomb",
    "fight",
    "defeat",
    "kill",
    "cold",
    "solstheim",
    "mountain",
    "ferry",
    "carriage",
    "dragon",
    "branch",
)

REFERENCE_SECTION_HEADINGS = {
    "Late Location Reconciliation",
}


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


def csv_join(values: list[str]) -> str:
    return "; ".join(value for value in values if value)


def base_row(
    *,
    audit_area: str,
    check_id: str,
    source_file: str,
    source_section: str,
    row_label: str,
    check_type: str,
    objective_id: str = "",
    objective_name: str = "",
    source_status: str = "",
    guide_locations: str = "",
    route_protection: str = "",
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
        "objective_id": objective_id,
        "objective_name": objective_name,
        "source_status": source_status,
        "guide_locations": guide_locations,
        "route_protection": route_protection,
        "audit_status": audit_status,
        "recommended_action": recommended_action,
        "evidence": evidence,
        "notes": notes,
    }


def parse_markdown_tables(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current_section = ""
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            current_section = line[3:].strip()
        if current_section in SURVIVAL_SECTIONS and line.startswith("| ") and i + 1 < len(lines):
            delimiter = lines[i + 1]
            if set(delimiter.replace("|", "").strip()) <= {"-", ":", " "}:
                headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
                i += 2
                while i < len(lines) and lines[i].startswith("| "):
                    cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                    if len(cells) == len(headers):
                        row = dict(zip(headers, cells))
                        row["source_section"] = current_section
                        rows.append(row)
                    i += 1
                continue
        i += 1
    return rows


def coverage_by_objective(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    output: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        objective_id = row.get("objective_id", "")
        if objective_id:
            output.setdefault(objective_id, []).append(row)
    return output


def coverage_text(rows: list[dict[str, str]]) -> str:
    fields = ("coverage_status", "player_facing_cue", "player_facing_location", "completion_status", "notes")
    return " ".join(" ".join(row.get(field, "") for field in fields) for row in rows)


def explicit_route_resolution(final_row: dict[str, str], coverage_rows: list[dict[str, str]]) -> bool:
    text = " ".join(
        [
            final_row.get("final_coverage_status", ""),
            final_row.get("coverage_statuses", ""),
            final_row.get("completion_statuses", ""),
            coverage_text(coverage_rows),
        ]
    ).lower()
    return "unresolved" in final_row.get("final_coverage_status", "") or "needs route resolution" in text or "needs_route_resolution" in text


def final_status_result(
    area: str,
    final_row: dict[str, str],
    coverage_rows: list[dict[str, str]],
) -> tuple[str, str, str]:
    final_status = final_row.get("final_coverage_status", "")
    if final_status == "placed_in_main_guide":
        return "pass_progression_accounted_in_main_guide", "none", "Objective is represented in the current main guide coverage ledger."
    if final_status == "branch_handled":
        return "pass_branch_handled", "none", "Objective is represented by branch-first/reload guide handling."
    if final_status == "option_default_handled":
        return "pass_option_default_handled", "none", "Objective is represented by route default or option-list handling."
    if final_status == "excluded":
        return "pass_scope_exclusion", "none", "Objective has an explicit route-scope exclusion."
    if explicit_route_resolution(final_row, coverage_rows):
        return (
            "pass_existing_route_resolution",
            "none_existing_route_resolution",
            "Progression row remains visible through explicit NEEDS ROUTE RESOLUTION coverage.",
        )
    return (
        f"needs_{area}_review",
        "review_legendary_progression",
        "Progression row lacks placed, branch, option/default, exclusion, or explicit route-resolution coverage.",
    )


def setup_rows(guide_text: str) -> list[dict[str, str]]:
    rows = []
    for check_id, row_label, route_protection, groups in GLOBAL_SETUP_RULES:
        ok, found, missing = groups_found(guide_text, groups)
        rows.append(
            base_row(
                audit_area="setup_baseline",
                check_id=check_id,
                source_file=rel(MAIN_GUIDE),
                source_section="Guide Conventions and Setup",
                row_label=row_label,
                check_type="guide_global_rule",
                source_status="current_guide",
                guide_locations="Guide Conventions | Setup and Save Baseline",
                route_protection=route_protection,
                audit_status="pass_setup_rule_in_guide" if ok else "needs_setup_review",
                recommended_action="none" if ok else "review_survival_logistics",
                evidence=("Found guide terms: " + csv_join(found)) if ok else ("Missing guide terms: " + csv_join(missing)),
                notes="TB-040 setup check derived from the current guide's global player-facing rules.",
            )
        )
    return rows


def survival_constraint_rows(guide_text: str) -> list[dict[str, str]]:
    rows = []
    for index, row in enumerate(parse_markdown_tables(SURVIVAL_CONSTRAINTS), start=1):
        label = row["Region/objective"]
        groups = SURVIVAL_TERM_RULES.get(label, [(label.lower(),)])
        ok, found, missing = groups_found(guide_text, groups)
        action = "none"
        status = "pass_survival_constraint_represented"
        evidence = "Found guide terms: " + csv_join(found)

        if label == "Adventurer's Backpacks, followers, pets, and horses":
            status = "pass_carry_relief_with_explicit_backpack_resolution"
            action = "none_existing_route_resolution"
            evidence = (
                "Guide routes horse/pet carry support and keeps the Adventurer's Backpack set as an explicit "
                "NEEDS ROUTE RESOLUTION row."
            )
        elif not ok:
            status = "needs_survival_logistics_review"
            action = "review_survival_logistics"
            evidence = "Missing guide terms: " + csv_join(missing)

        rows.append(
            base_row(
                audit_area=SURVIVAL_SECTIONS[row["source_section"]],
                check_id=f"TB040-SURV-{index:03d}",
                source_file=rel(SURVIVAL_CONSTRAINTS),
                source_section=row["source_section"],
                row_label=label,
                check_type="survival_constraint",
                source_status=row["Status"],
                guide_locations="main-guide-v1.md global or route-section prose",
                route_protection=row["Route implication"],
                audit_status=status,
                recommended_action=action,
                evidence=evidence,
                notes=(
                    f"Source notes: {row['Source notes']}. "
                    "TB-040 uses existing source-backed Survival constraints; no broad gameplay research performed."
                ),
            )
        )
    return rows


def guide_sections(markdown: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^### (.+)$", markdown, flags=re.MULTILINE))
    output = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        next_h2 = re.search(r"^## ", markdown[start:end], flags=re.MULTILINE)
        if next_h2:
            end = start + next_h2.start()
        output.append((match.group(1).strip(), markdown[start:end]))
    return output


def section_rows(markdown: str) -> list[dict[str, str]]:
    rows = []
    for index, (heading, body) in enumerate(guide_sections(markdown), start=1):
        lower_body = body.lower()
        needs_logistics = any(keyword in lower_body for keyword in ROUTE_SECTION_KEYWORDS)
        categories = [
            category
            for category, terms in LOGISTICS_CATEGORIES.items()
            if any(term in lower_body for term in terms)
        ]
        if heading in REFERENCE_SECTION_HEADINGS:
            status = "pass_reference_or_reconciliation_section"
            action = "none"
            evidence = "Reference/reconciliation section; no standalone travel leg should be invented here."
        elif not needs_logistics:
            status = "pass_section_without_route_leg_pressure"
            action = "none"
            evidence = "No route-leg logistics keywords detected."
        elif len(categories) >= 2:
            status = "pass_section_has_survival_logistics_cues"
            action = "none"
            evidence = "Detected logistics cue categories: " + csv_join(categories)
        else:
            status = "needs_section_logistics_review"
            action = "review_survival_logistics"
            evidence = "Detected logistics cue categories: " + (csv_join(categories) or "none")

        rows.append(
            base_row(
                audit_area="guide_section_logistics",
                check_id=f"TB040-SECT-{index:03d}",
                source_file=rel(MAIN_GUIDE),
                source_section=heading,
                row_label=heading,
                check_type="guide_section_preparation_scan",
                source_status="current_guide",
                guide_locations=heading,
                route_protection="Route sections with travel, combat, cold, dungeon, or branch pressure should include overt prep/support cues.",
                audit_status=status,
                recommended_action=action,
                evidence=evidence,
                notes="Automated scan for explicit rest, food/healing, carry/storage, travel, or save cues; this is a QA locator, not a combat simulation.",
            )
        )
    return rows


def progression_constraint_rows() -> list[dict[str, str]]:
    final_by_id = {row["objective_id"]: row for row in read_csv(OBJECTIVE_STATUS)}
    coverage_by_id = coverage_by_objective(read_csv(COVERAGE_LEDGER))
    rows = []
    for source_row in read_csv(OBJECTIVE_CONSTRAINTS):
        if source_row["constraint_type"] != "progression_constraint":
            continue
        if source_row["source_section"] == "Queue Disposition":
            continue
        objective_id = source_row["objective_id"]
        final_row = final_by_id.get(objective_id, {})
        coverage_rows = coverage_by_id.get(objective_id, [])
        status, action, evidence = final_status_result("legendary_progression", final_row, coverage_rows)
        rows.append(
            base_row(
                audit_area="legendary_progression_constraint",
                check_id=source_row["constraint_id"],
                source_file=source_row["constraint_source_file"],
                source_section=source_row["source_section"],
                row_label=source_row["row_label"],
                check_type="progression_constraint",
                objective_id=objective_id,
                objective_name=source_row["objective_name"],
                source_status=source_row["status"],
                guide_locations=final_row.get("guide_locations", ""),
                route_protection=source_row["routing_rule"],
                audit_status=status,
                recommended_action=action,
                evidence=evidence,
                notes=(
                    f"Source notes: {source_row['source_notes']}. "
                    "TB-040 checks current coverage state for Legendary/progression constraints."
                ),
            )
        )
    return rows


def progression_selection_groups(row: dict[str, str]) -> list[tuple[str, ...]]:
    selection_type = row["selection_type"]
    name = row["name"]
    if selection_type == "legendary_reset_distribution":
        return [(name.lower(),), ("legendary reset", "legendary"), ("recover", "recovery")]
    if selection_type == "training_policy":
        return [(name.lower(),), ("trainer targets for this loop",), ("training",)]
    if selection_type == "crafting_system_action":
        return CRAFTING_TERM_RULES.get(name, [(name.lower(),)])
    if selection_type == "progression_policy":
        return PROGRESSION_POLICY_TERM_RULES.get(name, [(name.lower(),)])
    return [(name.lower(),)]


def progression_source_rows(guide_text: str) -> list[dict[str, str]]:
    rows = []
    selected_rows = [row for row in read_csv(PROGRESSION_SELECTIONS) if row["selection_type"] in PROGRESSION_SOURCE_TYPES]
    for row in selected_rows:
        ok, found, missing = groups_found(guide_text, progression_selection_groups(row))
        rows.append(
            base_row(
                audit_area=f"progression_source_{row['selection_type']}",
                check_id=row["selection_id"],
                source_file=rel(PROGRESSION_SELECTIONS),
                source_section=row["selection_type"],
                row_label=row["name"],
                check_type="progression_source_selection",
                objective_id=row["objective_id"],
                objective_name=row["name"],
                source_status=row["selection_status"],
                guide_locations="All-Perks Loop | Crafting, Enchanting, Alchemy, and Investments | route-specific sections",
                route_protection=row["route_timing"],
                audit_status="pass_progression_source_represented" if ok else "needs_progression_source_review",
                recommended_action="none" if ok else "review_legendary_progression",
                evidence=("Found guide terms: " + csv_join(found)) if ok else ("Missing guide terms: " + csv_join(missing)),
                notes=(
                    f"Selected source/default: {row['selected_source']}. "
                    f"Source notes: {row['source_note_refs']}. "
                    "TB-040 checks that survival-sensitive progression defaults are visible in v1 guide prose or tables."
                ),
            )
        )
    return rows


def geography_summary_rows(guide_text: str) -> list[dict[str, str]]:
    by_cold: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_access: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(LOCATION_GEOGRAPHY):
        by_cold[row["cold_risk"]].append(row)
        by_access[row["worldspace_access_model"]].append(row)

    rows = []
    for index, (cold_risk, geo_rows) in enumerate(sorted(by_cold.items()), start=1):
        groups = GEOGRAPHY_COLD_RULES.get(cold_risk, [("route discipline", "support stop", "owned storage")])
        ok, found, missing = groups_found(guide_text, groups)
        samples = ", ".join(row["location_name"] for row in geo_rows[:5])
        rows.append(
            base_row(
                audit_area="geography_cold_support",
                check_id=f"TB040-GEOG-COLD-{index:03d}",
                source_file=rel(LOCATION_GEOGRAPHY),
                source_section="cold_risk",
                row_label=cold_risk,
                check_type="geography_support_summary",
                source_status=f"{len(geo_rows)} geography rows",
                guide_locations="main-guide-v1.md regional and route-support prose",
                route_protection="Cold-risk groups should be supported by hot food, rest, cold gear, regional anchors, or route discipline before route prose depends on them.",
                audit_status="pass_geography_cold_support_represented" if ok else "needs_geography_cold_support_review",
                recommended_action="none" if ok else "review_survival_logistics",
                evidence=(
                    f"{len(geo_rows)} rows; sample locations: {samples}. Found guide terms: {csv_join(found)}"
                    if ok
                    else f"{len(geo_rows)} rows; sample locations: {samples}. Missing guide terms: {csv_join(missing)}"
                ),
                notes="Uses generated location-geography support data as a QA index; exact roads, passes, water, and quest access still belong to route-level validation.",
            )
        )

    for index, (access_model, geo_rows) in enumerate(sorted(by_access.items()), start=1):
        rows.append(
            base_row(
                audit_area="geography_transport_support",
                check_id=f"TB040-GEOG-ACCESS-{index:03d}",
                source_file=rel(LOCATION_GEOGRAPHY),
                source_section="worldspace_access_model",
                row_label=access_model,
                check_type="geography_support_summary",
                source_status=f"{len(geo_rows)} geography rows",
                guide_locations="main-guide-v1.md regional and route-support prose",
                route_protection="Transport/access classes should remain visible for no-fast-travel Survival route planning.",
                audit_status="pass_transport_support_layer_available",
                recommended_action="none",
                evidence=f"{len(geo_rows)} rows are classified with this access model.",
                notes="Transport/access support comes from generated geography data and is consumed by route sections where relevant.",
            )
        )
    return rows


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    areas = sorted({row["audit_area"] for row in rows})
    for area in areas:
        area_rows = [row for row in rows if row["audit_area"] == area]
        output.append({"metric": f"{area}:rows", "count": str(len(area_rows)), "notes": "Generated TB-040 audit rows."})
        for status, count in sorted(Counter(row["audit_status"] for row in area_rows).items()):
            output.append({"metric": f"{area}:status:{status}", "count": str(count), "notes": "Audit-status distribution."})
        for action, count in sorted(Counter(row["recommended_action"] for row in area_rows).items()):
            output.append({"metric": f"{area}:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    output.append({"metric": "all:rows", "count": str(len(rows)), "notes": "Generated TB-040 audit rows."})
    for action, count in sorted(Counter(row["recommended_action"] for row in rows).items()):
        output.append({"metric": f"all:recommended_action:{action}", "count": str(count), "notes": "Recommended-action distribution."})
    return output


def main() -> int:
    guide_markdown = MAIN_GUIDE.read_text(encoding="utf-8")
    guide_text = guide_markdown.lower()
    rows = (
        setup_rows(guide_text)
        + survival_constraint_rows(guide_text)
        + section_rows(guide_markdown)
        + progression_constraint_rows()
        + progression_source_rows(guide_text)
        + geography_summary_rows(guide_text)
    )
    write_csv(OUTPUT_AUDIT, FIELDNAMES, rows)
    write_csv(OUTPUT_SUMMARY, ["metric", "count", "notes"], summary_rows(rows))
    actions = Counter(row["recommended_action"] for row in rows)
    print(f"Wrote {OUTPUT_AUDIT.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUTPUT_SUMMARY.relative_to(REPO_ROOT)}")
    print(", ".join(f"{key}: {actions[key]}" for key in sorted(actions)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
