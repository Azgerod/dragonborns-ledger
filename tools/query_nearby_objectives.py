#!/usr/bin/env python3
"""Query nearby route objectives for a guide section pass.

This is a read-only drafting helper. It surfaces objectives from the generated
route-planning index by corridor, cluster, category, and text terms so guide
writers can perform the required proximity audit before deciding what to route
now, hold, or source-check further.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "data" / "route-planning" / "objective-route-index.csv"

OUTPUT_COLUMNS = [
    "objective_id",
    "objective_name",
    "category",
    "subcategory",
    "objective_location",
    "primary_route_corridor",
    "support_locations",
    "constraint_types",
    "constraint_severities",
    "candidate_status",
    "route_index_status",
    "notes",
]

TEXT_FIELDS = [
    "objective_id",
    "objective_name",
    "category",
    "subcategory",
    "objective_region",
    "objective_hold",
    "objective_location",
    "primary_route_cluster",
    "primary_route_corridor",
    "primary_nearest_corridor_hub",
    "primary_nearest_inn_or_rest",
    "primary_nearest_candidate_base",
    "support_table_refs",
    "support_worldspaces",
    "support_regions",
    "support_holds",
    "support_locations",
    "support_route_treatments",
    "constraint_types",
    "constraint_source_files",
    "constraint_severities",
    "notes",
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find objective rows near a route corridor, hub, place, or support term.",
    )
    parser.add_argument(
        "--index",
        default=str(DEFAULT_INDEX),
        help="Path to objective-route-index.csv.",
    )
    parser.add_argument("--corridor", action="append", default=[], help="Exact primary_route_corridor.")
    parser.add_argument("--cluster", action="append", default=[], help="Exact primary_route_cluster.")
    parser.add_argument("--category", action="append", default=[], help="Exact objective category.")
    parser.add_argument(
        "--text",
        action="append",
        default=[],
        help="Case-insensitive text term to match across objective/support/geography fields.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "csv"],
        default="markdown",
        help="Output format.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Maximum rows to print; 0 means no limit.")
    args = parser.parse_args()

    rows = list(read_rows(Path(args.index)))
    matches = [row for row in rows if matches_filters(row, args)]
    matches.sort(key=sort_key)

    if args.limit:
        matches = matches[: args.limit]

    if args.format == "csv":
        write_csv(matches)
    else:
        write_markdown(matches)

    return 0


def read_rows(path: Path) -> Iterable[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        yield from csv.DictReader(handle)


def matches_filters(row: dict[str, str], args: argparse.Namespace) -> bool:
    if args.corridor and row.get("primary_route_corridor", "") not in args.corridor:
        return False
    if args.cluster and row.get("primary_route_cluster", "") not in args.cluster:
        return False
    if args.category and row.get("category", "") not in args.category:
        return False

    terms = [term.casefold() for term in args.text]
    if terms:
        haystack = " | ".join(row.get(field, "") for field in TEXT_FIELDS).casefold()
        if not all(term in haystack for term in terms):
            return False

    return True


def sort_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (
        row.get("primary_route_corridor", ""),
        row.get("objective_location", "") or row.get("support_locations", ""),
        row.get("category", ""),
        row.get("objective_name", ""),
    )


def write_csv(rows: list[dict[str, str]]) -> None:
    writer = csv.DictWriter(__import__("sys").stdout, fieldnames=OUTPUT_COLUMNS)
    writer.writeheader()
    for row in rows:
        writer.writerow({column: row.get(column, "") for column in OUTPUT_COLUMNS})


def write_markdown(rows: list[dict[str, str]]) -> None:
    print("| " + " | ".join(OUTPUT_COLUMNS) + " |")
    print("| " + " | ".join("---" for _ in OUTPUT_COLUMNS) + " |")
    for row in rows:
        values = [markdown_cell(row.get(column, "")) for column in OUTPUT_COLUMNS]
        print("| " + " | ".join(values) + " |")


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


if __name__ == "__main__":
    raise SystemExit(main())
