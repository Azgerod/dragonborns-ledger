#!/usr/bin/env python3
"""Audit finite collectible representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-009. It checks collectible
objectives, Collectible Items checklist rows, relevant Unique Gear rows, and
known collectible-linked support rows against the player-facing guide, the
internal guide coverage ledger, and item/member support tables.
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
ITEM_MEMBERS_CSV = REPO_ROOT / "data" / "items" / "ae-item-members.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-collectible-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

COLLECTIBLE_CHECKLIST_TABS = {"Collectible Items"}
UNIQUE_GEAR_TAB = "Unique Gear"
DRAGON_PRIEST_MASK_SUBCATEGORY = "artifact_dragon_priest_mask"
LOCKET_OF_SAINT_JIUB_OBJECTIVE = "OBJ-001721"
JIUB_PAGE_RE = re.compile(r"^Jiub's Opus \(Page \d+\)$")

ACQUIRE_TERMS = (
    "accept",
    "accepted",
    "acquire",
    "acquired",
    "bring",
    "brought",
    "buy",
    "collect",
    "collected",
    "claim",
    "claimed",
    "complete",
    "completed",
    "harvest",
    "harvested",
    "loot",
    "looted",
    "obtain",
    "pick up",
    "purchase",
    "receive",
    "received",
    "recover",
    "recovered",
    "retrieve",
    "retrieved",
    "reward",
    "take",
    "taken",
)
USE_TURN_IN_TERMS = (
    "activate",
    "activated",
    "cache",
    "combined",
    "consume",
    "consumed",
    "count",
    "counter",
    "display",
    "place",
    "placed",
    "record",
    "returned",
    "show",
    "sold",
    "tracking",
    "turn in",
    "turned in",
    "use",
    "used",
)
STORAGE_TERMS = ("preserve", "preserved", "safe container", "safe storage", "store", "stored", "storage")
HOLD_TERMS = (
    "carry forward",
    "conditional",
    "deferred",
    "do not",
    "held",
    "if ",
    "later",
    "not completed",
    "not routed",
    "pending",
    "staged",
    "stays unresolved",
    "wait",
)
ROUTE_RESOLUTION_TERMS = ("needs route resolution", "route-resolution", "route resolution", "unresolved")
EXCLUSION_TERMS = ("excluded", "exclusion", "not required", "outside required")
BRANCH_TERMS = ("branch", "reloaded", "alternate branch")


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


def strip_collectible_prefix(value: str) -> str:
    cleaned = value.replace("*", "").replace("\u200e", "").strip()
    cleaned = re.sub(r"\s+\((AE|CC|DB|DG|HF)\)$", "", cleaned)
    cleaned = re.sub(r"\s+\(Dragon Priest Mask\)$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(
        r"^(Artifact|Bug in a Jar|Collectible Set|Dragon Claw|Fishing Catch|Kagrumez Resonance Gem|Leveled Reward|Paragon|Quest Item|Stone of Barenziah|Treasure Map|Unique Item)\s*:?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
    return cleaned


def name_variants(*values: str) -> set[str]:
    variants: set[str] = set()
    for value in values:
        if not value:
            continue
        cleaned = value.replace("*", "").replace("\u200e", "").strip()
        stripped = strip_collectible_prefix(cleaned)
        without_parenthetical = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
        without_the = stripped.replace("The ", "", 1).strip()

        for candidate in {cleaned, stripped, without_parenthetical, strip_collectible_prefix(without_parenthetical), without_the}:
            if not candidate:
                continue
            variants.add(candidate)
            variants.add(re.sub(r"^Raven Rock\s+", "", candidate).strip())
            variants.add(re.sub(r"\s+\d+$", "", candidate).strip())
            if normalize(candidate) == "bugs in a jar":
                variants.add("bugs in jars")
            if ":" in candidate:
                before, after = [part.strip() for part in candidate.split(":", 1)]
                if before:
                    variants.add(before)
                if after:
                    variants.add(after)
                    variants.add(re.sub(r"^Raven Rock\s+", "", after).strip())
                    variants.add(re.sub(r"\s+\d+$", "", after).strip())

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


def rows_blob(
    coverage_rows: list[dict[str, str]],
    item_rows: list[dict[str, str]],
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
    item_keys = (
        "item_name",
        "item_category",
        "route_treatment",
        "source_section",
        "source_table_detail",
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
                " ".join(" ".join(row.get(key, "") for key in item_keys) for row in item_rows),
                " ".join(objective_row.get(key, "") for key in object_keys),
                " ".join(checklist_row.get(key, "") for key in checklist_keys),
            ]
        )
    )


def has_any(blob: str, terms: tuple[str, ...]) -> bool:
    return any(term in blob for term in terms)


def treatment_flags(
    coverage_rows: list[dict[str, str]],
    item_rows: list[dict[str, str]],
    objective_row: dict[str, str],
    checklist_row: dict[str, str],
) -> dict[str, str]:
    blob = rows_blob(coverage_rows, item_rows, objective_row, checklist_row)
    return {
        "acquire_treatment": "Y" if has_any(blob, ACQUIRE_TERMS) else "N",
        "use_or_turn_in_treatment": "Y" if has_any(blob, USE_TURN_IN_TERMS) else "N",
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

    if subcategory in {
        "stone_of_barenziah_set",
        "treasure_map_set",
        "east_empire_pendant_set",
        "black_book_set",
        "jiub_opus_page_set",
        "dragon_claw_set",
        "bug_in_jar_set",
        "dragon_priest_mask_set",
        "aetherium_shard_set",
        "paragon_set",
        "reaper_gem_fragment_set",
        "kagrumez_resonance_gem_set",
        "fishing_species_set",
        "crimson_nirnroot_count_set",
    }:
        return any(
            flags[key] == "Y"
            for key in (
                "acquire_treatment",
                "use_or_turn_in_treatment",
                "storage_treatment",
                "hold_or_stage_treatment",
            )
        )

    if category == "collectible" or checklist_tab == "Collectible Items" or row_kind.endswith("unique_gear"):
        return any(
            flags[key] == "Y"
            for key in (
                "acquire_treatment",
                "use_or_turn_in_treatment",
                "storage_treatment",
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
    if not coverage_rows:
        return (
            f"{row_kind}_missing_internal_coverage",
            "add_internal_collectible_coverage_row",
            "No exact or mapped internal coverage row was found for this collectible row.",
        )

    if flags["route_resolution_treatment"] == "Y":
        return (f"{row_kind}_route_resolution_recorded", "none_existing_route_resolution", "")

    if flags["exclusion_treatment"] == "Y" and (mapping_type == "Explicit exclusion" or coverage_has_exclusion):
        return (f"{row_kind}_excluded", "none", "")

    if not guide_name_match:
        return (
            f"{row_kind}_missing_guide_name",
            "add_player_facing_collectible_reference",
            "Internal coverage exists, but the guide does not name this collectible/checklist row clearly enough.",
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
        f"{row_kind}_missing_collectible_treatment",
        "add_collectible_treatment_context",
        "The guide/internal coverage names this row but lacks clear acquire/use/turn-in/storage/hold treatment.",
    )


def coverage_rollup(rows: list[dict[str, str]]) -> tuple[set[str], set[str], set[str], set[str]]:
    return (
        {row.get("coverage_status", "") for row in rows},
        {row.get("completion_status", "") for row in rows},
        {row.get("player_facing_location", "") for row in rows},
        {row.get("player_facing_cue", "") for row in rows},
    )


def relevant_unique_gear_row(checklist_row: dict[str, str], objective_row: dict[str, str]) -> bool:
    if checklist_row.get("checklist_tab") != UNIQUE_GEAR_TAB:
        return False
    return (
        objective_row.get("subcategory") == DRAGON_PRIEST_MASK_SUBCATEGORY
        or objective_row.get("objective_id") == LOCKET_OF_SAINT_JIUB_OBJECTIVE
    )


def collectible_linked_objective(objective_row: dict[str, str]) -> bool:
    return (
        objective_row.get("category") == "collectible"
        or objective_row.get("subcategory") == DRAGON_PRIEST_MASK_SUBCATEGORY
        or objective_row.get("objective_id") == LOCKET_OF_SAINT_JIUB_OBJECTIVE
        or bool(JIUB_PAGE_RE.match(objective_row.get("objective_name", "")))
    )


def main() -> int:
    objective_rows = read_csv(OBJECTIVES_CSV)
    objective_ids = {row["objective_id"] for row in objective_rows}
    objectives_by_id = {row["objective_id"]: row for row in objective_rows}

    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    collectible_checklist_rows = [row for row in matrix_rows if row.get("checklist_tab") in COLLECTIBLE_CHECKLIST_TABS]
    unique_gear_rows = [
        row
        for row in matrix_rows
        if relevant_unique_gear_row(row, objectives_by_id.get(row.get("objective_id", ""), {}))
    ]

    collectible_objectives = [
        row for row in objective_rows if collectible_linked_objective(row)
    ]

    guide_normalized = normalize(MAIN_GUIDE.read_text(encoding="utf-8"))

    item_rows_by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    if ITEM_MEMBERS_CSV.exists():
        for row in read_csv(ITEM_MEMBERS_CSV):
            for objective_id in {row.get("parent_objective_id", ""), row.get("existing_objective_id", "")}:
                if objective_id:
                    item_rows_by_objective[objective_id].append(row)

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
    ) -> None:
        category = objective_row.get("category", "")
        subcategory = objective_row.get("subcategory", "")
        item_rows = item_rows_by_objective.get(objective_id, [])
        flags = treatment_flags(coverage_rows, item_rows, objective_row, checklist_row)
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
                "item_member_rows": str(len(item_rows)),
                "item_member_names": joined({row.get("item_name", "") for row in item_rows}, limit=5),
                "item_member_route_treatments": joined({row.get("route_treatment", "") for row in item_rows}, limit=5),
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

    for objective_row in collectible_objectives:
        objective_id = objective_row["objective_id"]
        item_rows = item_rows_by_objective.get(objective_id, [])
        display_name = strip_collectible_prefix(objective_row["objective_name"])
        item_names = [row.get("item_name", "") for row in item_rows]
        coverage_rows = coverage_by_objective_id.get(objective_id, [])
        guide_name_match = guide_contains_name(guide_normalized, objective_row["objective_name"], display_name, *item_names)
        append_output(
            row_kind="collectible_objective",
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
        )

    for checklist_row in collectible_checklist_rows:
        checklist_id = checklist_row["checklist_id"]
        objective_id = checklist_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        display_name = strip_collectible_prefix(checklist_row["checklist_entry"])
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        coverage_rows = exact_rows or mapped_objective_rows
        coverage_source = "exact_checklist" if exact_rows else "mapped_objective" if mapped_objective_rows else ""
        guide_name_match = guide_contains_name(
            guide_normalized,
            checklist_row["checklist_entry"],
            checklist_row.get("matched_objective_name", ""),
            display_name,
            objective_row.get("objective_name", ""),
        )
        append_output(
            row_kind="collectible_checklist",
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
        )

    for checklist_row in unique_gear_rows:
        checklist_id = checklist_row["checklist_id"]
        objective_id = checklist_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        display_name = strip_collectible_prefix(checklist_row["checklist_entry"])
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        coverage_rows = exact_rows or mapped_objective_rows
        coverage_source = "exact_checklist" if exact_rows else "mapped_objective" if mapped_objective_rows else ""
        guide_name_match = guide_contains_name(
            guide_normalized,
            checklist_row["checklist_entry"],
            checklist_row.get("matched_objective_name", ""),
            display_name,
        )
        append_output(
            row_kind="collectible_unique_gear",
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
        "item_member_rows",
        "item_member_names",
        "item_member_route_treatments",
        "guide_name_match",
        "coverage_source",
        "internal_coverage_row_count",
        "acquire_treatment",
        "use_or_turn_in_treatment",
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

    print(f"Wrote {len(output_rows)} collectible audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
