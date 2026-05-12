#!/usr/bin/env python3
"""Fetch UESP Gamemap JSON data.

The modern UESP Gamemap app loads Skyrim marker data from a JSON endpoint.
This helper keeps the endpoint handling in one place so generated location
support tables can be refreshed without re-discovering the app internals.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_URL = "https://gamemap.uesp.net/db/gamemap.php"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 Chrome/124 Safari/537.36"
)


def api_get(params: dict[str, str | int]) -> dict:
    query = urlencode(params)
    request = Request(
        f"{API_URL}?{query}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_worlds(db: str = "sr") -> list[dict]:
    data = api_get({"action": "get_worlds", "db": db})
    worlds = data.get("worlds") or []
    return [world for world in worlds if int(world.get("enabled", 0)) == 1]


def fetch_locations(world_id: int, db: str = "sr") -> list[dict]:
    data = api_get({"action": "get_locs", "db": db, "world": world_id})
    return data.get("locations") or []


def fetch_all(db: str = "sr") -> dict:
    worlds = fetch_worlds(db)
    locations: list[dict] = []
    for world in worlds:
        world_locations = fetch_locations(int(world["id"]), db)
        for location in world_locations:
            location["worldName"] = world["name"]
            location["worldDisplayName"] = world["displayName"]
        locations.extend(world_locations)
    return {"db": db, "worlds": worlds, "locations": locations}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="sr", help="Gamemap database id. Defaults to Skyrim's 'sr'.")
    parser.add_argument(
        "--mode",
        choices=("worlds", "locations", "all"),
        default="all",
        help="Which data to fetch.",
    )
    parser.add_argument("--world", type=int, help="World id for --mode locations.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    try:
        if args.mode == "worlds":
            payload: object = fetch_worlds(args.db)
        elif args.mode == "locations":
            if args.world is None:
                print("--world is required when --mode locations is used.", file=sys.stderr)
                return 2
            payload = fetch_locations(args.world, args.db)
        else:
            payload = fetch_all(args.db)
    except Exception as exc:
        print(f"fetch_uesp_gamemap.py: {exc}", file=sys.stderr)
        return 1

    output = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
