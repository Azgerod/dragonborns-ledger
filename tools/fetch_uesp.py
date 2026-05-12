#!/usr/bin/env python3
"""Fetch UESP pages through the MediaWiki API.

Direct `action=raw` requests can be challenged by Cloudflare from this
environment. The MediaWiki API is reliable when called with a normal browser
User-Agent, and it gives us stable page metadata plus either wikitext or parsed
HTML for source-note work.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_URL = "https://en.uesp.net/w/api.php"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 Chrome/124 Safari/537.36"
)


def api_get(params: dict[str, str]) -> dict:
    query = urlencode(params)
    request = Request(f"{API_URL}?{query}", headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_wikitext(title: str) -> str:
    data = api_get(
        {
            "action": "query",
            "prop": "revisions",
            "titles": title,
            "rvprop": "content",
            "rvslots": "main",
            "format": "json",
        }
    )
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()), {})
    if "missing" in page:
        raise RuntimeError(f"UESP page not found: {title}")
    revisions = page.get("revisions") or []
    if not revisions:
        raise RuntimeError(f"UESP page has no revisions: {title}")
    return revisions[0]["slots"]["main"]["*"]


def fetch_html(title: str) -> str:
    data = api_get(
        {
            "action": "parse",
            "page": title,
            "prop": "text",
            "format": "json",
        }
    )
    if "error" in data:
        raise RuntimeError(data["error"].get("info", f"UESP parse failed: {title}"))
    return data["parse"]["text"]["*"]


def fetch_info(title: str) -> str:
    data = api_get(
        {
            "action": "query",
            "titles": title,
            "prop": "info",
            "inprop": "url",
            "format": "json",
        }
    )
    return json.dumps(data, indent=2, sort_keys=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="UESP page title, e.g. 'Skyrim:The Cause'")
    parser.add_argument(
        "--mode",
        choices=("wikitext", "html", "info"),
        default="wikitext",
        help="Output format to fetch.",
    )
    parser.add_argument("--output", type=Path, help="Optional file to write.")
    args = parser.parse_args()

    try:
        if args.mode == "wikitext":
            output = fetch_wikitext(args.title)
        elif args.mode == "html":
            output = fetch_html(args.title)
        else:
            output = fetch_info(args.title)
    except Exception as exc:
        print(f"fetch_uesp.py: {exc}", file=sys.stderr)
        return 1

    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
