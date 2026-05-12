#!/usr/bin/env python3
"""Validate skill/perk support table structure and cross-references."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "data" / "skills"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"

SKILL_COLUMNS = [
    "skill_record_id",
    "skill_name",
    "specialization",
    "source_content",
    "source_page",
    "source_id",
    "skill_100_objective_id",
    "perk_tree_objective_id",
    "perk_nodes",
    "perk_ranks",
    "skill_completion_boundary",
    "perk_completion_boundary",
    "legendary_reset_relevance",
    "route_treatment",
    "citations",
    "notes",
]

PERK_RANK_COLUMNS = [
    "perk_rank_record_id",
    "perk_node_record_id",
    "skill_record_id",
    "skill_name",
    "specialization",
    "perk_node_name",
    "perk_rank",
    "perk_max_ranks",
    "skill_requirement_level",
    "skill_requirement_text",
    "prerequisite_perks",
    "description",
    "form_id",
    "parent_perk_tree_objective_id",
    "source_content",
    "source_page",
    "source_id",
    "citations",
    "route_treatment",
    "notes",
]

SKILL_CONTROLLED_VALUES = {
    "specialization": {"magic", "combat", "stealth"},
    "source_content": {"base_game"},
    "route_treatment": {"source_listed_skill_tree"},
}

PERK_RANK_CONTROLLED_VALUES = {
    "specialization": {"magic", "combat", "stealth"},
    "source_content": {"base_game"},
    "route_treatment": {"source_listed_perk_rank"},
}


def read_csv(path: Path, expected_columns: list[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_columns:
            print(f"{path} has unexpected header.", file=sys.stderr)
            print(f"Expected: {expected_columns}", file=sys.stderr)
            print(f"Actual:   {reader.fieldnames}", file=sys.stderr)
            raise SystemExit(1)
        return list(reader)


def read_objectives() -> dict[str, dict[str, str]]:
    with OBJECTIVES.open(newline="", encoding="utf-8") as handle:
        return {row["objective_id"]: row for row in csv.DictReader(handle)}


def bibliography_ids() -> set[str]:
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    return set(re.findall(r"\bSRC-\d{6}\b", text))


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def validate_skill_table(path: Path) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path, SKILL_COLUMNS)
    objectives = read_objectives()
    sources = bibliography_ids()
    seen_ids: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        skill_record_id = row["skill_record_id"]
        if not re.fullmatch(r"SKILL-\d{6}", skill_record_id):
            errors.append(f"{path}:{line_number}: invalid skill_record_id {skill_record_id!r}")
        if skill_record_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate skill_record_id {skill_record_id}")
        seen_ids.add(skill_record_id)

        for column, allowed_values in SKILL_CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        for column, expected_subcategory in [
            ("skill_100_objective_id", "skill_100"),
            ("perk_tree_objective_id", "perk_tree"),
        ]:
            objective_id = row[column]
            objective = objectives.get(objective_id)
            if objective is None:
                errors.append(f"{path}:{line_number}: unknown {column} {objective_id}")
            elif objective["category"] != "skill_perk":
                errors.append(f"{path}:{line_number}: {column} is not a skill_perk row")
            elif objective["subcategory"] != expected_subcategory:
                errors.append(
                    f"{path}:{line_number}: {column} expected {expected_subcategory}, got {objective['subcategory']}"
                )

        for column in ["perk_nodes", "perk_ranks"]:
            value = row[column]
            if not value.isdigit() or int(value) <= 0:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        if not row["skill_completion_boundary"].strip():
            errors.append(f"{path}:{line_number}: missing skill_completion_boundary")
        if not row["perk_completion_boundary"].strip():
            errors.append(f"{path}:{line_number}: missing perk_completion_boundary")

    return errors


def validate_perk_rank_template(path: Path) -> list[str]:
    read_csv(path, PERK_RANK_COLUMNS)
    return []


def validate_perk_rank_table(path: Path) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path, PERK_RANK_COLUMNS)
    skill_rows = {
        row["skill_record_id"]: row
        for row in read_csv(SKILLS_DIR / "skill-perk-catalog.csv", SKILL_COLUMNS)
    }
    objectives = read_objectives()
    sources = bibliography_ids()
    seen_rank_ids: set[str] = set()
    node_id_by_key: dict[tuple[str, str], str] = {}
    ranks_by_node: dict[tuple[str, str], list[int]] = {}
    rank_totals_by_skill: dict[str, int] = {skill_id: 0 for skill_id in skill_rows}
    node_names_by_skill: dict[str, set[str]] = {skill_id: set() for skill_id in skill_rows}

    for line_number, row in enumerate(rows, start=2):
        rank_id = row["perk_rank_record_id"]
        if not re.fullmatch(r"PERKRANK-\d{6}", rank_id):
            errors.append(f"{path}:{line_number}: invalid perk_rank_record_id {rank_id!r}")
        if rank_id in seen_rank_ids:
            errors.append(f"{path}:{line_number}: duplicate perk_rank_record_id {rank_id}")
        seen_rank_ids.add(rank_id)

        node_id = row["perk_node_record_id"]
        if not re.fullmatch(r"PERKNODE-\d{6}", node_id):
            errors.append(f"{path}:{line_number}: invalid perk_node_record_id {node_id!r}")

        for column, allowed_values in PERK_RANK_CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        skill_id = row["skill_record_id"]
        skill_row = skill_rows.get(skill_id)
        if skill_row is None:
            errors.append(f"{path}:{line_number}: unknown skill_record_id {skill_id}")
        else:
            for column in ["skill_name", "specialization"]:
                if row[column] != skill_row[column]:
                    errors.append(
                        f"{path}:{line_number}: {column} {row[column]!r} does not match {skill_id}"
                    )
            if row["parent_perk_tree_objective_id"] != skill_row["perk_tree_objective_id"]:
                errors.append(
                    f"{path}:{line_number}: parent_perk_tree_objective_id does not match {skill_id}"
                )

        parent_id = row["parent_perk_tree_objective_id"]
        objective = objectives.get(parent_id)
        if objective is None:
            errors.append(f"{path}:{line_number}: unknown parent_perk_tree_objective_id {parent_id}")
        elif objective["category"] != "skill_perk" or objective["subcategory"] != "perk_tree":
            errors.append(f"{path}:{line_number}: parent objective is not a perk_tree row")

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        for column in ["perk_rank", "perk_max_ranks", "skill_requirement_level"]:
            value = row[column]
            if not value.isdigit():
                errors.append(f"{path}:{line_number}: invalid numeric {column} {value!r}")
                continue
            if column != "skill_requirement_level" and int(value) <= 0:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        if row["perk_rank"].isdigit() and row["perk_max_ranks"].isdigit():
            rank = int(row["perk_rank"])
            max_ranks = int(row["perk_max_ranks"])
            if rank > max_ranks:
                errors.append(f"{path}:{line_number}: perk_rank exceeds perk_max_ranks")

        if row["skill_requirement_level"] == "0" and row["skill_requirement_text"] != "none":
            errors.append(f"{path}:{line_number}: zero skill requirement should use text 'none'")
        if row["skill_requirement_level"] != "0" and row["skill_requirement_text"] == "none":
            errors.append(f"{path}:{line_number}: nonzero skill requirement lacks text")

        if not re.fullmatch(r"[0-9a-f]{8}", row["form_id"]):
            errors.append(f"{path}:{line_number}: invalid form_id {row['form_id']!r}")
        if not row["perk_node_name"].strip():
            errors.append(f"{path}:{line_number}: missing perk_node_name")
        if not row["description"].strip():
            errors.append(f"{path}:{line_number}: missing description")
        if not row["prerequisite_perks"].strip():
            errors.append(f"{path}:{line_number}: missing prerequisite_perks")

        key = (skill_id, row["perk_node_name"])
        previous_node_id = node_id_by_key.setdefault(key, node_id)
        if previous_node_id != node_id:
            errors.append(f"{path}:{line_number}: inconsistent node id for {key}")
        if row["perk_rank"].isdigit():
            ranks_by_node.setdefault(key, []).append(int(row["perk_rank"]))
        if skill_id in rank_totals_by_skill:
            rank_totals_by_skill[skill_id] += 1
            node_names_by_skill[skill_id].add(row["perk_node_name"])

    for key, ranks in ranks_by_node.items():
        skill_id, node_name = key
        expected = list(range(1, max(ranks) + 1))
        if sorted(ranks) != expected:
            errors.append(f"{path}: ranks for {skill_id} {node_name!r} are {sorted(ranks)}, expected {expected}")

    for skill_id, skill_row in skill_rows.items():
        expected_ranks = int(skill_row["perk_ranks"])
        actual_ranks = rank_totals_by_skill[skill_id]
        if actual_ranks != expected_ranks:
            errors.append(f"{path}: {skill_id} has {actual_ranks} perk-rank rows, expected {expected_ranks}")

        expected_nodes = int(skill_row["perk_nodes"])
        actual_nodes = len(node_names_by_skill[skill_id])
        if actual_nodes != expected_nodes:
            errors.append(f"{path}: {skill_id} has {actual_nodes} perk nodes, expected {expected_nodes}")

    return errors


def main() -> int:
    template = SKILLS_DIR / "skill-perk-catalog.template.csv"
    table = SKILLS_DIR / "skill-perk-catalog.csv"
    perk_rank_template = SKILLS_DIR / "perk-rank-catalog.template.csv"
    perk_rank_table = SKILLS_DIR / "perk-rank-catalog.csv"
    if not template.exists():
        print(f"Missing skill/perk template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing skill/perk catalog: {table}", file=sys.stderr)
        return 1
    if not perk_rank_template.exists():
        print(f"Missing perk-rank template: {perk_rank_template}", file=sys.stderr)
        return 1
    if not perk_rank_table.exists():
        print(f"Missing perk-rank catalog: {perk_rank_table}", file=sys.stderr)
        return 1

    errors = (
        validate_skill_table(template)
        + validate_skill_table(table)
        + validate_perk_rank_template(perk_rank_template)
        + validate_perk_rank_table(perk_rank_table)
    )
    if errors:
        print("Skill/perk table validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Skill/perk catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
