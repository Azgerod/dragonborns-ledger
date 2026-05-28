#!/usr/bin/env python3
"""Audit book, document, spell-tome, and shout representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-008. It checks every
book/document objective plus every Books, Spells, and Dragon Shouts checklist
row against the player-facing guide, internal guide coverage ledger, book
support tables, and progression source selections.
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
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-book-document-audit.csv"
BOOK_TABLE_PATHS = (
    REPO_ROOT / "data" / "books" / "skill-books-locations.csv",
    REPO_ROOT / "data" / "books" / "spell-tomes-locations.csv",
    REPO_ROOT / "data" / "books" / "book-document-locations.csv",
)
PROGRESSION_SELECTIONS_CSV = REPO_ROOT / "data" / "constraints" / "progression-source-selections.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

CHECKLIST_TABS = {"Books", "Spells", "Dragon Shouts"}
BOOK_RELATED_SUBCATEGORIES = {"dragon_shout", "black_book_power_set"}
SHORT_NAME_ALLOWLIST = {
    "calm",
    "fear",
    "fury",
    "king",
    "rout",
    "sithis",
    "thief",
    "warrior",
}

ACQUIRE_TERMS = (
    "acquire",
    "acquired",
    "buy",
    "collect",
    "create",
    "created",
    "found",
    "handle",
    "handled",
    "loot",
    "obtain",
    "pick up",
    "purchase",
    "receive",
    "reward",
    "selected source",
    "take",
    "vendor",
)
READ_LEARN_TERMS = (
    "choose",
    "chosen",
    "learn",
    "learned",
    "read",
    "reader",
    "shout",
    "tome",
    "word",
)
STORAGE_TERMS = ("preserve", "preserved", "store", "stored", "storage")
HOLD_TERMS = (
    "all perks",
    "all-perks",
    "do not read",
    "held",
    "left closed",
    "later",
    "pending",
    "staged",
    "unread",
)
DUPLICATE_TERMS = ("alternate", "covered", "duplicate", "not reread", "not required", "same item")
MASTER_GATE_TERMS = ("master ritual", "ritual spell", "skill gate", "alteration 90", "conjuration 90", "destruction 100", "illusion 100", "restoration 90")
ROUTE_RESOLUTION_TERMS = ("needs route resolution", "route-resolution", "route resolution")
EXCLUSION_TERMS = ("excluded", "exclusion", "not required", "outside required", "unofficial patch-only")
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


def strip_title_prefix(value: str) -> str:
    cleaned = value.replace("*", "").replace("\u200e", "").strip()
    cleaned = re.sub(r"\s+\((AE|CC|DB|DG|HF)\)$", "", cleaned)
    cleaned = re.sub(r"^(Skill Book|Spell Tome|Black Book)\s*:?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(
        r"\s+Black Book\s+(?:Perk Reset System|Shout Ability Choice Set|Power Choice Set|Ability Choice Set)$",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\s+\(book\)$", "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


def name_variants(*values: str) -> set[str]:
    variants: set[str] = set()
    for value in values:
        if not value:
            continue
        cleaned = value.replace("*", "").replace("\u200e", "").strip()
        stripped = strip_title_prefix(cleaned)
        without_parenthetical = re.sub(r"\s+\([^)]*\)$", "", cleaned).strip()
        without_the = stripped.replace("The ", "", 1).strip()

        for candidate in {cleaned, stripped, without_parenthetical, strip_title_prefix(without_parenthetical), without_the}:
            if not candidate:
                continue
            variants.add(candidate)
            if ":" in candidate:
                before, after = [part.strip() for part in candidate.split(":", 1)]
                if before:
                    variants.add(before)
                if after:
                    variants.add(after)
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


def rows_blob(*row_groups: list[dict[str, str]]) -> str:
    keys = (
        "record_type",
        "objective_name",
        "coverage_status",
        "player_facing_cue",
        "player_facing_location",
        "completion_status",
        "notes",
        "selection_type",
        "selection_status",
        "selected_source",
        "source_location",
        "source_detail",
        "route_timing",
        "book_title",
        "book_category",
        "location",
        "location_detail",
        "route_candidate_status",
    )
    return normalize(
        " ".join(
            " ".join(row.get(key, "") for key in keys)
            for rows in row_groups
            for row in rows
        )
    )


def has_any(blob: str, terms: tuple[str, ...]) -> bool:
    return any(term in blob for term in terms)


def treatment_flags(
    coverage_rows: list[dict[str, str]],
    book_rows: list[dict[str, str]],
    selection_rows: list[dict[str, str]],
) -> dict[str, str]:
    blob = rows_blob(coverage_rows, book_rows, selection_rows)
    return {
        "acquire_treatment": "Y" if has_any(blob, ACQUIRE_TERMS) else "N",
        "read_or_learn_treatment": "Y" if has_any(blob, READ_LEARN_TERMS) else "N",
        "storage_treatment": "Y" if has_any(blob, STORAGE_TERMS) else "N",
        "hold_or_stage_treatment": "Y" if has_any(blob, HOLD_TERMS) else "N",
        "duplicate_or_covered_treatment": "Y" if has_any(blob, DUPLICATE_TERMS) else "N",
        "master_gate_treatment": "Y" if has_any(blob, MASTER_GATE_TERMS) else "N",
        "route_resolution_treatment": "Y" if has_any(blob, ROUTE_RESOLUTION_TERMS) else "N",
        "exclusion_treatment": "Y" if has_any(blob, EXCLUSION_TERMS) else "N",
        "branch_treatment": "Y" if has_any(blob, BRANCH_TERMS) else "N",
    }


def expected_treatment_met(
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

    if checklist_tab == "Dragon Shouts" or subcategory == "dragon_shout":
        return flags["read_or_learn_treatment"] == "Y" or flags["hold_or_stage_treatment"] == "Y"

    if checklist_tab == "Spells" or subcategory == "spell_tome_title":
        return any(
            flags[key] == "Y"
            for key in (
                "acquire_treatment",
                "read_or_learn_treatment",
                "hold_or_stage_treatment",
                "master_gate_treatment",
            )
        )

    if subcategory in {"skill_book_title", "black_book_title", "black_book_power_set"}:
        return any(
            flags[key] == "Y"
            for key in (
                "acquire_treatment",
                "read_or_learn_treatment",
                "storage_treatment",
                "hold_or_stage_treatment",
                "duplicate_or_covered_treatment",
            )
        )

    if category == "book_document" or checklist_tab == "Books":
        return any(
            flags[key] == "Y"
            for key in (
                "acquire_treatment",
                "read_or_learn_treatment",
                "storage_treatment",
                "hold_or_stage_treatment",
                "duplicate_or_covered_treatment",
                "master_gate_treatment",
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
            "add_internal_book_document_coverage_row",
            "No exact or mapped internal coverage row was found for this book/document row.",
        )

    if flags["route_resolution_treatment"] == "Y":
        return (f"{row_kind}_route_resolution_recorded", "none_existing_route_resolution", "")

    if flags["exclusion_treatment"] == "Y" and (mapping_type == "Explicit exclusion" or coverage_has_exclusion):
        return (f"{row_kind}_excluded", "none", "")

    if not guide_name_match:
        return (
            f"{row_kind}_missing_guide_name",
            "add_player_facing_book_document_reference",
            "Internal coverage exists, but the guide does not name this book/document/spell/shout row.",
        )

    if expected_treatment_met(row_kind, category, subcategory, checklist_tab, mapping_type, flags):
        return (f"{row_kind}_covered", "none", "")

    return (
        f"{row_kind}_missing_book_document_treatment",
        "add_book_document_treatment_context",
        "The guide/internal coverage names this row but lacks clear pickup/read/learn/storage/hold treatment.",
    )


def coverage_rollup(rows: list[dict[str, str]]) -> tuple[set[str], set[str], set[str]]:
    return (
        {row.get("coverage_status", "") for row in rows},
        {row.get("completion_status", "") for row in rows},
        {row.get("player_facing_location", "") for row in rows},
    )


def main() -> int:
    objective_rows = read_csv(OBJECTIVES_CSV)
    objective_ids = {row["objective_id"] for row in objective_rows}
    objectives_by_id = {row["objective_id"]: row for row in objective_rows}
    book_objectives = [
        row
        for row in objective_rows
        if row.get("category") == "book_document" or row.get("subcategory") in BOOK_RELATED_SUBCATEGORIES
    ]

    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    book_checklist_rows = [row for row in matrix_rows if row.get("checklist_tab") in CHECKLIST_TABS]

    guide_normalized = normalize(MAIN_GUIDE.read_text(encoding="utf-8"))

    book_rows_by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in BOOK_TABLE_PATHS:
        for row in read_csv(path):
            row["_source_table"] = path.name
            book_rows_by_objective[row.get("objective_id", "")].append(row)

    selections_by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(PROGRESSION_SELECTIONS_CSV):
        selections_by_objective[row.get("objective_id", "")].append(row)

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
    ) -> None:
        category = objective_row.get("category", "")
        subcategory = objective_row.get("subcategory", "")
        book_rows = book_rows_by_objective.get(objective_id, [])
        selection_rows = selections_by_objective.get(objective_id, [])
        flags = treatment_flags(coverage_rows, book_rows, selection_rows)
        audit_status, recommended_action, notes = audit_status_for(
            row_kind,
            coverage_rows,
            guide_name_match,
            category,
            subcategory,
            checklist_tab,
            mapping_type,
            flags,
        )
        coverage_statuses, completion_statuses, guide_locations = coverage_rollup(coverage_rows)

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
                "book_category": joined({row.get("book_category", "") for row in book_rows}),
                "support_table_rows": str(len(book_rows)),
                "representative_sources": joined(
                    {
                        f"{row.get('location', '')}: {row.get('location_detail', '')}".strip(": ")
                        for row in book_rows
                        if row.get("route_candidate_status") == "provisional_objective_representative"
                    },
                    limit=3,
                ),
                "selection_type": joined({row.get("selection_type", "") for row in selection_rows}),
                "selection_status": joined({row.get("selection_status", "") for row in selection_rows}),
                "selected_source": joined({row.get("selected_source", "") for row in selection_rows}, limit=3),
                "source_location": joined({row.get("source_location", "") for row in selection_rows}, limit=3),
                "route_timing": joined({row.get("route_timing", "") for row in selection_rows}, limit=3),
                "guide_name_match": "Y" if guide_name_match else "N",
                "coverage_source": coverage_source,
                "internal_coverage_row_count": str(len(coverage_rows)),
                **flags,
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "recommended_action": recommended_action,
                "notes": notes,
            }
        )

    for objective_row in book_objectives:
        objective_id = objective_row["objective_id"]
        book_rows = book_rows_by_objective.get(objective_id, [])
        display_name = strip_title_prefix(objective_row["objective_name"])
        support_names = [row.get("book_title", "") for row in book_rows]
        coverage_rows = coverage_by_objective_id.get(objective_id, [])
        guide_name_match = guide_contains_name(guide_normalized, objective_row["objective_name"], display_name, *support_names)
        append_output(
            row_kind="book_document_objective",
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
        )

    for checklist_row in book_checklist_rows:
        checklist_id = checklist_row["checklist_id"]
        objective_id = checklist_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        book_rows = book_rows_by_objective.get(objective_id, [])
        display_name = strip_title_prefix(checklist_row["checklist_entry"])
        support_names = [row.get("book_title", "") for row in book_rows]
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        coverage_rows = exact_rows or mapped_objective_rows
        coverage_source = "exact_checklist" if exact_rows else "mapped_objective" if mapped_objective_rows else ""
        if checklist_row["checklist_tab"] == "Books" and objective_row.get("category") != "book_document":
            guide_name_match = guide_contains_name(guide_normalized, checklist_row["checklist_entry"], display_name)
        else:
            guide_name_match = guide_contains_name(
                guide_normalized,
                checklist_row["checklist_entry"],
                checklist_row.get("matched_objective_name", ""),
                display_name,
                *support_names,
            )
        append_output(
            row_kind="book_document_checklist",
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
        "book_category",
        "support_table_rows",
        "representative_sources",
        "selection_type",
        "selection_status",
        "selected_source",
        "source_location",
        "route_timing",
        "guide_name_match",
        "coverage_source",
        "internal_coverage_row_count",
        "acquire_treatment",
        "read_or_learn_treatment",
        "storage_treatment",
        "hold_or_stage_treatment",
        "duplicate_or_covered_treatment",
        "master_gate_treatment",
        "route_resolution_treatment",
        "exclusion_treatment",
        "branch_treatment",
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

    print(f"Wrote {len(output_rows)} book/document audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
