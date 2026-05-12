#!/usr/bin/env python3
"""Build generated route-planning indexes from the reviewable source data."""

from __future__ import annotations

from collections import Counter, defaultdict
import csv
from dataclasses import dataclass
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
OBJECTIVES = DATA_DIR / "objectives" / "objectives.csv"
ROUTE_DIR = DATA_DIR / "route-planning"
ROUTE_INDEX = ROUTE_DIR / "objective-route-index.csv"
CONSTRAINT_INDEX = ROUTE_DIR / "objective-constraints.csv"
CONSTRAINT_DIR = DATA_DIR / "constraints"
LOCATION_GEOGRAPHY = DATA_DIR / "locations" / "location-geography.csv"

OBJ_RE = re.compile(r"OBJ-\d{6}")
OBJ_RANGE_RE = re.compile(r"OBJ-(\d{6})\s*(?:-|through|to)\s*OBJ-(\d{6})")
SN_RE = re.compile(r"SN-\d{6}(?:-[A-Za-z0-9_.-]+\.md)?")

ROUTE_INDEX_HEADER = [
    "objective_id",
    "objective_name",
    "category",
    "subcategory",
    "source_content",
    "route_placement",
    "routing_rigidity",
    "research_status",
    "validation_status",
    "objective_worldspace",
    "objective_region",
    "objective_hold",
    "objective_location",
    "location_record_ids",
    "coordinate_record_ids",
    "geography_record_ids",
    "primary_coordinate_worldspace",
    "primary_route_cluster",
    "primary_route_corridor",
    "primary_nearest_corridor_hub",
    "primary_nearest_major_carriage_origin",
    "primary_nearest_ferry_terminal",
    "primary_nearest_inn_or_rest",
    "primary_nearest_candidate_base",
    "primary_worldspace_access_model",
    "primary_transport_access_flags",
    "primary_cold_risk",
    "primary_barrier_flags",
    "primary_geography_confidence",
    "support_table_refs",
    "support_record_count",
    "support_location_count",
    "support_worldspaces",
    "support_regions",
    "support_holds",
    "support_locations",
    "support_route_treatments",
    "constraint_count",
    "constraint_types",
    "constraint_source_files",
    "constraint_severities",
    "hard_level_gate",
    "leveled_reward_threshold",
    "cell_entry_lock_risk",
    "missability",
    "bug_risk",
    "has_quest_conflict",
    "has_npc_dependency",
    "has_trophy_relevance",
    "survival_mode_relevance",
    "candidate_status",
    "route_index_status",
    "notes",
]

CONSTRAINT_HEADER = [
    "constraint_id",
    "objective_id",
    "objective_name",
    "constraint_type",
    "constraint_source_file",
    "source_section",
    "row_label",
    "constraint_summary",
    "routing_rule",
    "hard_save_name",
    "source_notes",
    "status",
    "severity",
    "route_phase_owner",
    "notes",
]

CONSTRAINT_TYPES = {
    "ae-creation-start-triggers.md": ("ae_start_trigger", "TB-022/TB-024"),
    "leveled-unique-items.md": ("leveled_reward", "TB-022/TB-024/TB-032"),
    "cell-entry-locks.md": ("cell_entry_lock", "TB-022/TB-024/TB-032"),
    "quest-conflicts-hard-saves.md": ("quest_conflict_or_branch", "TB-028/TB-032"),
    "trophy-dependencies.md": ("trophy_dependency", "TB-031F/TB-034/TB-037"),
    "npc-dependencies.md": ("npc_dependency", "TB-022/TB-025/TB-032"),
    "bug-prone-quests.md": ("bug_mitigation", "TB-032/TB-034/TB-037"),
    "radiant-boundaries.md": ("radiant_boundary", "TB-022/TB-026"),
    "survival-mode-constraints.md": ("survival_constraint", "TB-025/TB-034/TB-037"),
    "skill-perk-leveling-plan.md": ("progression_constraint", "TB-027/TB-034/TB-037"),
}

SUPPORT_SPECS = [
    ("skill_book_locations", DATA_DIR / "books" / "skill-books-locations.csv", ["objective_id"], "book_location_id"),
    ("spell_tome_locations", DATA_DIR / "books" / "spell-tomes-locations.csv", ["objective_id"], "book_location_id"),
    ("book_document_locations", DATA_DIR / "books" / "book-document-locations.csv", ["objective_id"], "book_location_id"),
    ("ae_item_members", DATA_DIR / "items" / "ae-item-members.csv", ["parent_objective_id", "existing_objective_id"], "item_member_id"),
    ("property_details", DATA_DIR / "properties" / "property-details.csv", ["parent_objective_id"], "property_detail_id"),
    ("skill_perk_catalog", DATA_DIR / "skills" / "skill-perk-catalog.csv", ["skill_100_objective_id", "perk_tree_objective_id"], "skill_record_id"),
    ("perk_rank_catalog", DATA_DIR / "skills" / "perk-rank-catalog.csv", ["parent_perk_tree_objective_id"], "perk_rank_record_id"),
    ("alchemy_effect_catalog", DATA_DIR / "skills" / "alchemy-effect-catalog.csv", ["objective_id"], "alchemy_record_id"),
    ("enchantment_learning_catalog", DATA_DIR / "skills" / "enchantment-learning-catalog.csv", ["objective_id"], "enchantment_record_id"),
    ("merchant_investment_catalog", DATA_DIR / "skills" / "merchant-investment-catalog.csv", ["objective_id"], "merchant_investment_record_id"),
    ("practical_crafting_system_catalog", DATA_DIR / "skills" / "practical-crafting-system-catalog.csv", ["objective_id", "existing_objective_ids"], "crafting_system_record_id"),
]


@dataclass(frozen=True)
class MarkdownRow:
    path: Path
    section: str
    headers: list[str]
    cells: list[str]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, header: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=header, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def pipe_join(values: list[str] | set[str], limit: int = 16) -> str:
    cleaned = sorted({value.strip() for value in values if value and value.strip()})
    if len(cleaned) <= limit:
        return " | ".join(cleaned)
    return " | ".join(cleaned[:limit] + [f"+{len(cleaned) - limit} more"])


def parse_objective_ids(text: str) -> list[str]:
    ids: set[str] = set()
    for match in OBJ_RANGE_RE.finditer(text):
        start = int(match.group(1))
        end = int(match.group(2))
        if start <= end and end - start <= 500:
            ids.update(f"OBJ-{number:06d}" for number in range(start, end + 1))
    ids.update(OBJ_RE.findall(text))
    return sorted(ids)


def split_multi_id_cell(value: str) -> list[str]:
    return parse_objective_ids(value)


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip().replace("<br>", " ") for cell in stripped.split("|")]


def is_separator(line: str) -> bool:
    cells = split_markdown_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def iter_markdown_table_rows(path: Path) -> list[MarkdownRow]:
    rows: list[MarkdownRow] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    section = ""
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if line.startswith("#"):
            section = line.lstrip("#").strip()

        if line.startswith("|") and index + 1 < len(lines) and is_separator(lines[index + 1]):
            headers = split_markdown_row(line)
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].strip().startswith("|"):
                cells = split_markdown_row(lines[cursor])
                if len(cells) < len(headers):
                    cells.extend([""] * (len(headers) - len(cells)))
                rows.append(MarkdownRow(path=path, section=section, headers=headers, cells=cells[: len(headers)]))
                cursor += 1
            index = cursor
            continue
        index += 1
    return rows


def row_dict(markdown_row: MarkdownRow) -> dict[str, str]:
    return dict(zip(markdown_row.headers, markdown_row.cells))


def first_nonempty(values: list[str]) -> str:
    for value in values:
        if value and value.strip():
            return value.strip()
    return ""


def header_value_summary(row: dict[str, str], limit: int = 5) -> str:
    parts = []
    for header, value in row.items():
        if value.strip() and "source" not in header.lower() and "status" not in header.lower():
            parts.append(f"{header}: {value.strip()}")
        if len(parts) == limit:
            break
    return " | ".join(parts)


def infer_routing_rule(row: dict[str, str]) -> str:
    rule_headers = [
        header
        for header in row
        if any(
            token in header.lower()
            for token in [
                "safe",
                "route",
                "canonical",
                "branch",
                "hard-save",
                "warning",
                "mitigation",
                "rule",
                "implication",
                "policy",
                "handoff",
            ]
        )
    ]
    return " | ".join(f"{header}: {row[header]}" for header in rule_headers if row[header].strip())


def infer_hard_save(row: dict[str, str]) -> str:
    for header, value in row.items():
        lower = header.lower()
        if value.strip() and ("hard-save name" in lower or lower == "hard-save" or lower == "hard save"):
            return value.strip()
    for header, value in row.items():
        lower = header.lower()
        if value.strip() and ("hard-save" in lower or "hard save" in lower):
            return value.strip()
    return ""


def infer_status(row: dict[str, str]) -> str:
    return first_nonempty([value for header, value in row.items() if header.lower() == "status"])


def infer_severity(constraint_type: str, row_text: str, hard_save: str) -> str:
    lowered = row_text.lower()
    if hard_save or "hard save" in lowered or "branch" in lowered:
        return "branch_or_hard_save"
    if constraint_type in {"leveled_reward", "cell_entry_lock", "trophy_dependency"}:
        return "hard_gate"
    if "confirmed" in lowered or "do not" in lowered or "must" in lowered:
        return "warning"
    if constraint_type in {"survival_constraint", "progression_constraint", "radiant_boundary"}:
        return "planning"
    return "review"


def source_notes(row_text: str) -> str:
    return pipe_join(SN_RE.findall(row_text), limit=24)


def build_constraint_rows(objectives: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    next_id = 1
    for filename, (constraint_type, phase_owner) in CONSTRAINT_TYPES.items():
        path = CONSTRAINT_DIR / filename
        if not path.exists():
            continue
        for markdown_row in iter_markdown_table_rows(path):
            row = row_dict(markdown_row)
            row_text = " ".join(markdown_row.cells)
            objective_ids = [objective_id for objective_id in parse_objective_ids(row_text) if objective_id in objectives]
            if not objective_ids:
                continue
            label = first_nonempty(markdown_row.cells)
            hard_save = infer_hard_save(row)
            severity = infer_severity(constraint_type, row_text, hard_save)
            for objective_id in objective_ids:
                rows.append(
                    {
                        "constraint_id": f"RPCON-{next_id:06d}",
                        "objective_id": objective_id,
                        "objective_name": objectives[objective_id]["objective_name"],
                        "constraint_type": constraint_type,
                        "constraint_source_file": f"data/constraints/{filename}",
                        "source_section": markdown_row.section,
                        "row_label": label,
                        "constraint_summary": header_value_summary(row),
                        "routing_rule": infer_routing_rule(row),
                        "hard_save_name": hard_save,
                        "source_notes": source_notes(row_text),
                        "status": infer_status(row),
                        "severity": severity,
                        "route_phase_owner": phase_owner,
                        "notes": "Generated from the reviewed Markdown constraint tables; inspect the source row before writing final route prose.",
                    }
                )
                next_id += 1
    return rows


def add_support_record(
    support: dict[str, list[dict[str, str]]],
    objective_id: str,
    table_name: str,
    record_id: str,
    row: dict[str, str],
) -> None:
    support[objective_id].append(
        {
            "table": table_name,
            "record_id": record_id,
            "worldspace": row.get("worldspace", ""),
            "region": row.get("region", ""),
            "hold": row.get("hold", ""),
            "location": row.get("location", "") or row.get("property_name", "") or row.get("town_or_route", ""),
            "route_treatment": row.get("route_treatment", "") or row.get("route_candidate_status", ""),
        }
    )


def build_support_index() -> dict[str, list[dict[str, str]]]:
    support: dict[str, list[dict[str, str]]] = defaultdict(list)
    for table_name, path, id_columns, record_column in SUPPORT_SPECS:
        if not path.exists():
            continue
        for row in read_csv(path):
            record_id = row.get(record_column, "")
            target_ids: set[str] = set()
            for column in id_columns:
                target_ids.update(split_multi_id_cell(row.get(column, "")))
            for objective_id in target_ids:
                add_support_record(support, objective_id, table_name, record_id, row)
    return support


def build_geography_index() -> dict[str, list[dict[str, str]]]:
    by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    if not LOCATION_GEOGRAPHY.exists():
        return by_objective
    for row in read_csv(LOCATION_GEOGRAPHY):
        by_objective[row["objective_id"]].append(row)
    for rows in by_objective.values():
        rows.sort(key=lambda row: (row.get("coordinate_status") != "exact_marker", row["geography_record_id"]))
    return by_objective


def bool_text(value: str) -> str:
    return "yes" if value and value.strip() else "no"


def candidate_status(geography_rows: list[dict[str, str]], support_rows: list[dict[str, str]]) -> str:
    if len(support_rows) > 1:
        return "multiple_support_candidates"
    if len(support_rows) == 1:
        return "single_support_candidate"
    if len(geography_rows) > 1:
        return "multiple_geography_points"
    if len(geography_rows) == 1:
        return "single_geography_point"
    return "no_route_candidate_data"


def route_index_status(objective: dict[str, str], support_rows: list[dict[str, str]], constraints: list[dict[str, str]]) -> str:
    if objective["routing_rigidity"] == "unclassified" or objective["route_placement"] == "unclassified":
        return "needs_classification"
    if constraints:
        return "constraint_backed_needs_review"
    if len(support_rows) > 1:
        return "candidate_selection_needed"
    return "ready_for_route_pass"


def build_route_rows(
    objectives: dict[str, dict[str, str]],
    constraints: list[dict[str, str]],
    support: dict[str, list[dict[str, str]]],
    geography: dict[str, list[dict[str, str]]],
) -> list[dict[str, str]]:
    constraints_by_objective: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in constraints:
        constraints_by_objective[row["objective_id"]].append(row)

    rows: list[dict[str, str]] = []
    for objective_id, objective in objectives.items():
        objective_constraints = constraints_by_objective.get(objective_id, [])
        support_rows = support.get(objective_id, [])
        geography_rows = geography.get(objective_id, [])
        primary_geo = geography_rows[0] if geography_rows else {}
        support_locations = [row["location"] for row in support_rows if row["location"]]
        support_tables = Counter(row["table"] for row in support_rows)
        support_table_refs = " | ".join(f"{table}:{count}" for table, count in sorted(support_tables.items()))
        rows.append(
            {
                "objective_id": objective_id,
                "objective_name": objective["objective_name"],
                "category": objective["category"],
                "subcategory": objective["subcategory"],
                "source_content": objective["source_content"],
                "route_placement": objective["route_placement"],
                "routing_rigidity": objective["routing_rigidity"],
                "research_status": objective["research_status"],
                "validation_status": objective["validation_status"],
                "objective_worldspace": objective["worldspace"],
                "objective_region": objective["region"],
                "objective_hold": objective["hold"],
                "objective_location": objective["location"],
                "location_record_ids": pipe_join([row["location_record_id"] for row in geography_rows]),
                "coordinate_record_ids": pipe_join([row["coordinate_record_id"] for row in geography_rows]),
                "geography_record_ids": pipe_join([row["geography_record_id"] for row in geography_rows]),
                "primary_coordinate_worldspace": primary_geo.get("coordinate_worldspace", ""),
                "primary_route_cluster": primary_geo.get("route_cluster", ""),
                "primary_route_corridor": primary_geo.get("route_corridor", ""),
                "primary_nearest_corridor_hub": primary_geo.get("nearest_corridor_hub", ""),
                "primary_nearest_major_carriage_origin": primary_geo.get("nearest_major_carriage_origin", ""),
                "primary_nearest_ferry_terminal": primary_geo.get("nearest_ferry_terminal", ""),
                "primary_nearest_inn_or_rest": primary_geo.get("nearest_inn_or_rest", ""),
                "primary_nearest_candidate_base": primary_geo.get("nearest_candidate_base", ""),
                "primary_worldspace_access_model": primary_geo.get("worldspace_access_model", ""),
                "primary_transport_access_flags": primary_geo.get("transport_access_flags", ""),
                "primary_cold_risk": primary_geo.get("cold_risk", ""),
                "primary_barrier_flags": primary_geo.get("barrier_flags", ""),
                "primary_geography_confidence": primary_geo.get("geography_confidence", ""),
                "support_table_refs": support_table_refs,
                "support_record_count": str(len(support_rows)),
                "support_location_count": str(len({location for location in support_locations if location})),
                "support_worldspaces": pipe_join([row["worldspace"] for row in support_rows]),
                "support_regions": pipe_join([row["region"] for row in support_rows]),
                "support_holds": pipe_join([row["hold"] for row in support_rows]),
                "support_locations": pipe_join(support_locations, limit=12),
                "support_route_treatments": pipe_join([row["route_treatment"] for row in support_rows]),
                "constraint_count": str(len(objective_constraints)),
                "constraint_types": pipe_join([row["constraint_type"] for row in objective_constraints]),
                "constraint_source_files": pipe_join([row["constraint_source_file"] for row in objective_constraints]),
                "constraint_severities": pipe_join([row["severity"] for row in objective_constraints]),
                "hard_level_gate": objective["hard_level_gate"],
                "leveled_reward_threshold": objective["leveled_reward_threshold"],
                "cell_entry_lock_risk": objective["cell_entry_lock_risk"],
                "missability": objective["missability"],
                "bug_risk": objective["bug_risk"],
                "has_quest_conflict": bool_text(objective["quest_conflicts"]),
                "has_npc_dependency": bool_text(objective["npc_dependencies"]),
                "has_trophy_relevance": bool_text(objective["trophy_relevance"]),
                "survival_mode_relevance": objective["survival_mode_relevance"],
                "candidate_status": candidate_status(geography_rows, support_rows),
                "route_index_status": route_index_status(objective, support_rows, objective_constraints),
                "notes": "Generated routing workbench row; source CSVs and constraint tables remain canonical.",
            }
        )
    return rows


def main() -> int:
    objectives = {row["objective_id"]: row for row in read_csv(OBJECTIVES)}
    constraints = build_constraint_rows(objectives)
    support = build_support_index()
    geography = build_geography_index()
    route_rows = build_route_rows(objectives, constraints, support, geography)

    write_csv(CONSTRAINT_INDEX, CONSTRAINT_HEADER, constraints)
    write_csv(ROUTE_INDEX, ROUTE_INDEX_HEADER, route_rows)

    print(f"Wrote {CONSTRAINT_INDEX.relative_to(REPO_ROOT)} ({len(constraints)} rows).")
    print(f"Wrote {ROUTE_INDEX.relative_to(REPO_ROOT)} ({len(route_rows)} rows).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
