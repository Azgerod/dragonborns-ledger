#!/usr/bin/env python3
"""Build a local SQLite workbench from the project's CSV data."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sqlite3


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
OUTPUT = DATA_DIR / "route-planning" / "route-planning.sqlite"

NAMED_TABLES = {
    DATA_DIR / "objectives" / "objectives.csv": "objectives",
    DATA_DIR / "route-planning" / "objective-route-index.csv": "objective_route_index",
    DATA_DIR / "route-planning" / "objective-constraints.csv": "objective_constraints",
}


def sanitize_identifier(value: str) -> str:
    identifier = re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_").lower()
    if not identifier:
        identifier = "table"
    if identifier[0].isdigit():
        identifier = f"t_{identifier}"
    return identifier


def table_name(path: Path) -> str:
    if path in NAMED_TABLES:
        return NAMED_TABLES[path]
    relative = path.relative_to(DATA_DIR).with_suffix("")
    return sanitize_identifier("_".join(relative.parts))


def load_csv(conn: sqlite3.Connection, path: Path, name: str) -> int:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        if not columns:
            return 0
        quoted_columns = ", ".join(f'"{column}" TEXT' for column in columns)
        conn.execute(f'DROP TABLE IF EXISTS "{name}"')
        conn.execute(f'CREATE TABLE "{name}" ({quoted_columns})')
        placeholders = ", ".join("?" for _ in columns)
        quoted_names = ", ".join(f'"{column}"' for column in columns)
        count = 0
        for row in reader:
            conn.execute(
                f'INSERT INTO "{name}" ({quoted_names}) VALUES ({placeholders})',
                [row.get(column, "") for column in columns],
            )
            count += 1
    return count


def create_views(conn: sqlite3.Connection) -> None:
    statements = [
        """
        CREATE VIEW route_objective_workbench AS
        SELECT
            r.*,
            o.start_trigger,
            o.prerequisites,
            o.completion_boundary,
            o.citations
        FROM objective_route_index r
        JOIN objectives o USING (objective_id)
        """,
        """
        CREATE VIEW route_unclassified_objectives AS
        SELECT *
        FROM route_objective_workbench
        WHERE routing_rigidity = 'unclassified'
           OR route_placement = 'unclassified'
        """,
        """
        CREATE VIEW route_hard_constraint_queue AS
        SELECT *
        FROM objective_constraints
        WHERE severity IN ('hard_gate', 'branch_or_hard_save', 'warning')
        """,
        """
        CREATE VIEW route_location_objectives_by_corridor AS
        SELECT
            objective_id,
            objective_name,
            category,
            route_placement,
            routing_rigidity,
            primary_coordinate_worldspace,
            primary_route_cluster,
            primary_route_corridor,
            primary_nearest_corridor_hub,
            primary_cold_risk,
            primary_worldspace_access_model,
            primary_geography_confidence
        FROM objective_route_index
        WHERE geography_record_ids <> ''
        ORDER BY primary_route_cluster, primary_route_corridor, objective_name
        """,
        """
        CREATE VIEW route_candidate_selection_queue AS
        SELECT *
        FROM route_objective_workbench
        WHERE CAST(support_record_count AS INTEGER) > 1
           OR candidate_status = 'multiple_geography_points'
        """,
    ]
    for name in [
        "route_objective_workbench",
        "route_unclassified_objectives",
        "route_hard_constraint_queue",
        "route_location_objectives_by_corridor",
        "route_candidate_selection_queue",
    ]:
        conn.execute(f"DROP VIEW IF EXISTS {name}")
    for statement in statements:
        conn.execute(statement)


def main() -> int:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()
    csv_paths = sorted(DATA_DIR.glob("**/*.csv"))
    with sqlite3.connect(OUTPUT) as conn:
        conn.execute("CREATE TABLE table_manifest (table_name TEXT PRIMARY KEY, csv_path TEXT NOT NULL, row_count TEXT NOT NULL)")
        for path in csv_paths:
            name = table_name(path)
            count = load_csv(conn, path, name)
            conn.execute(
                "INSERT INTO table_manifest (table_name, csv_path, row_count) VALUES (?, ?, ?)",
                (name, str(path.relative_to(REPO_ROOT)), str(count)),
            )
        create_views(conn)
        conn.execute("CREATE INDEX idx_objectives_objective_id ON objectives(objective_id)")
        conn.execute("CREATE INDEX idx_route_index_objective_id ON objective_route_index(objective_id)")
        conn.execute("CREATE INDEX idx_constraints_objective_id ON objective_constraints(objective_id)")
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
