#!/usr/bin/env python3
"""Build the TB-043 unresolved-risk report and row-level risk register."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GUIDE_COVERAGE_DIR = REPO_ROOT / "data" / "guide-coverage"
FINAL_STATUS = GUIDE_COVERAGE_DIR / "main-guide-v1-objective-final-status.csv"
COVERAGE_LEDGER = GUIDE_COVERAGE_DIR / "main-guide-v1-coverage.csv"
OUTPUT_REGISTER = GUIDE_COVERAGE_DIR / "main-guide-v1-unresolved-risk-register.csv"
OUTPUT_SUMMARY = GUIDE_COVERAGE_DIR / "main-guide-v1-unresolved-risk-summary.csv"
OUTPUT_REPORT = REPO_ROOT / "drafts" / "final-guide" / "unresolved-risk-report.md"

PRIOR_QA_AUDITS = [
    ("TB-038/TB-038R order and delayed-task QA", GUIDE_COVERAGE_DIR / "main-guide-v1-order-delayed-task-audit.csv"),
    ("TB-039 trophy, leveled-item, and cell-entry QA", GUIDE_COVERAGE_DIR / "main-guide-v1-trophy-leveled-cell-audit.csv"),
    ("TB-040 Survival Mode and Legendary difficulty QA", GUIDE_COVERAGE_DIR / "main-guide-v1-survival-legendary-audit.csv"),
    ("TB-041 branch and spoiler QA", GUIDE_COVERAGE_DIR / "main-guide-v1-branch-spoiler-audit.csv"),
    ("TB-042 simulated playtest QA", GUIDE_COVERAGE_DIR / "main-guide-v1-playtest-audit.csv"),
]

FIELDNAMES = [
    "objective_id",
    "objective_name",
    "category",
    "subcategory",
    "route_placement",
    "severity",
    "risk_owner",
    "affected_route_surface",
    "likely_followup",
    "guide_locations",
    "coverage_statuses",
    "completion_statuses",
    "evidence_note",
]

OWNER_BY_CATEGORY = {
    "ae_creation": "AE Creation quest and reward routing",
    "book_document": "Book and document source-location routing",
    "collectible": "Finite collectible and Fishing route policy",
    "crafting_unlock": "Crafting, alchemy, and progression routing",
    "location": "Location route validation",
    "misc_objective": "Hold favor and miscellaneous-objective routing",
    "npc_relationship": "Relationship and household option routing",
    "quest": "Quest route validation and insertion",
    "radiant": "Radiant and counter assignment routing",
    "spell_power": "Spell, shout, and power routing",
    "trophy": "Trophy and counter verification",
    "unique_item": "Unique item/member route routing",
}

OWNER_BY_CATEGORY_SUBCATEGORY = {
    ("ae_creation", "ae_item_consumable_set"): "AE Creation item-member policy",
}

FOLLOWUP_BY_CATEGORY = {
    "ae_creation": "Source-check the Creation-specific start, quest stages, reward preservation, and natural route insertion point.",
    "book_document": "Validate deterministic pickup/source location or record a tighter exclusion/data-reconciliation reason.",
    "collectible": "Choose deterministic acquisition route, preservation policy, and any counter/checklist recording method.",
    "crafting_unlock": "Validate ingredient/effect/crafting availability and place the action in an existing progression window.",
    "location": "Resolve discover/enter/clear/avoid timing from location and route-validation support data.",
    "misc_objective": "Validate quest/favor prerequisites, NPC/service state, and natural hold-route insertion point.",
    "npc_relationship": "Validate relationship unlock, household role, option/default status, and any NPC-state dependency.",
    "quest": "Source-check exact quest start/progress/completion boundaries and insert or explicitly exclude.",
    "radiant": "Resolve assignment policy, target handling, counter boundary, and no-reroll route language.",
    "spell_power": "Validate learn/acquire timing, prerequisite state, and whether the power belongs in main or branch continuity.",
    "trophy": "Confirm trophy/counter boundary and route the required check or branch action.",
    "unique_item": "Validate deterministic acquisition, branch/final-continuity handling, and preservation rule.",
}

HIGH_CATEGORIES = {"ae_creation", "quest", "radiant", "spell_power", "trophy", "unique_item"}
MEDIUM_CATEGORIES = {"collectible", "crafting_unlock", "location", "misc_objective", "npc_relationship"}
MEDIUM_CATEGORY_SUBCATEGORIES = {("ae_creation", "ae_item_consumable_set")}

FOLLOWUP_BY_CATEGORY_SUBCATEGORY = {
    ("ae_creation", "ae_item_consumable_set"): "Resolve obtainable member acquisition policy, deterministic food/source handling, and explicit exclusions without treating broad consumable sets as quest blockers.",
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


def md(value: object) -> str:
    return str(value).replace("|", "\\|")


def table(headers: list[str], rows: list[list[object]]) -> list[str]:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(md(value) for value in row) + " |")
    return output


def action_counts(path: Path) -> Counter[str]:
    return Counter((row.get("recommended_action") or "blank") for row in read_csv(path))


def format_counts(counter: Counter[str]) -> str:
    return ", ".join(f"{key}: {counter[key]}" for key in sorted(counter))


def severity(row: dict[str, str]) -> str:
    if row["route_placement"] == "branch_route":
        return "high"
    if (row["category"], row["subcategory"]) in MEDIUM_CATEGORY_SUBCATEGORIES:
        return "medium"
    if row["category"] in HIGH_CATEGORIES:
        return "high"
    if row["category"] in MEDIUM_CATEGORIES:
        return "medium"
    return "low"


def route_surface(guide_locations: str) -> str:
    if "Final Reconciliation" in guide_locations and "route-resolution" in guide_locations:
        return "Final Reconciliation route-resolution register"
    if "TB-038R order and delayed-task repair register" in guide_locations:
        return "TB-038R delayed-task carryforward"
    if "Collectible Reconciliation" in guide_locations or "Fishing route-resolution hold" in guide_locations:
        return "Collectible/Fishing reconciliation"
    if "Crafting, Enchanting, Alchemy, and Investments" in guide_locations:
        return "Crafting/alchemy/investment reconciliation"
    if "Books, Spells, and Documents" in guide_locations:
        return "Books/spells/documents reconciliation"
    return (guide_locations.split(" | ", 1)[0] if guide_locations else "Unspecified guide surface")


def coverage_notes_by_objective() -> dict[str, str]:
    by_objective: dict[str, list[str]] = defaultdict(list)
    for row in read_csv(COVERAGE_LEDGER):
        objective_id = row.get("objective_id", "")
        haystack = " ".join(
            [
                row.get("coverage_status", ""),
                row.get("completion_status", ""),
                row.get("notes", ""),
            ]
        ).lower()
        if objective_id and "route resolution" in haystack:
            note = row.get("notes", "").strip()
            status = row.get("coverage_status", "").strip()
            if note:
                by_objective[objective_id].append(note)
            elif status:
                by_objective[objective_id].append(status)
    return {objective_id: notes[0] for objective_id, notes in by_objective.items()}


def build_register() -> list[dict[str, str]]:
    notes = coverage_notes_by_objective()
    final_rows = [
        row
        for row in read_csv(FINAL_STATUS)
        if row.get("final_coverage_status") == "unresolved"
    ]
    rows: list[dict[str, str]] = []
    for row in final_rows:
        category = row["category"]
        rows.append(
            {
                "objective_id": row["objective_id"],
                "objective_name": row["objective_name"],
                "category": category,
                "subcategory": row["subcategory"],
                "route_placement": row["route_placement"],
                "severity": severity(row),
                "risk_owner": OWNER_BY_CATEGORY_SUBCATEGORY.get(
                    (category, row["subcategory"]),
                    OWNER_BY_CATEGORY.get(category, "General route resolution"),
                ),
                "affected_route_surface": route_surface(row["guide_locations"]),
                "likely_followup": FOLLOWUP_BY_CATEGORY_SUBCATEGORY.get(
                    (category, row["subcategory"]),
                    FOLLOWUP_BY_CATEGORY.get(category, "Validate and route or explicitly exclude."),
                ),
                "guide_locations": row["guide_locations"],
                "coverage_statuses": row["coverage_statuses"],
                "completion_statuses": row["completion_statuses"],
                "evidence_note": notes.get(row["objective_id"], "Explicit unresolved final-status row."),
            }
        )
    severity_order = {"high": 0, "medium": 1, "low": 2}
    rows.sort(key=lambda item: (severity_order[item["severity"]], item["category"], item["objective_id"]))
    return rows


def build_summary_rows(register: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for severity_name, count in sorted(Counter(row["severity"] for row in register).items()):
        rows.append(
            {
                "summary_group": "severity",
                "metric": severity_name,
                "count": str(count),
                "notes": "TB-043 triage severity; all rows remain required until resolved or explicitly re-scoped.",
            }
        )
    for category, count in sorted(Counter(row["category"] for row in register).items()):
        rows.append(
            {
                "summary_group": "category",
                "metric": category,
                "count": str(count),
                "notes": OWNER_BY_CATEGORY.get(category, "General route resolution"),
            }
        )
    for surface, count in sorted(Counter(row["affected_route_surface"] for row in register).items()):
        rows.append(
            {
                "summary_group": "affected_route_surface",
                "metric": surface,
                "count": str(count),
                "notes": "Dominant guide or QA surface carrying the explicit unresolved row.",
            }
        )
    for owner, count in sorted(Counter(row["risk_owner"] for row in register).items()):
        rows.append(
            {
                "summary_group": "risk_owner",
                "metric": owner,
                "count": str(count),
                "notes": "Likely follow-up owner inferred from objective category.",
            }
        )
    rows.append(
        {
            "summary_group": "all",
            "metric": "unresolved_rows",
            "count": str(len(register)),
            "notes": "All explicit unresolved objective rows from main-guide-v1-objective-final-status.csv.",
        }
    )
    return rows


def category_rows(register: list[dict[str, str]]) -> list[list[object]]:
    by_category: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in register:
        by_category[row["category"]].append(row)
    output: list[list[object]] = []
    for category in sorted(by_category):
        rows = by_category[category]
        severities = Counter(row["severity"] for row in rows)
        surfaces = Counter(row["affected_route_surface"] for row in rows)
        output.append(
            [
                category,
                len(rows),
                ", ".join(f"{key}: {severities[key]}" for key in sorted(severities)),
                OWNER_BY_CATEGORY.get(category, "General route resolution"),
                ", ".join(f"{key} ({value})" for key, value in surfaces.most_common(2)),
            ]
        )
    return output


def prior_qa_rows() -> list[list[object]]:
    rows: list[list[object]] = []
    for label, path in PRIOR_QA_AUDITS:
        actions = action_counts(path)
        rows.append([label, sum(actions.values()), format_counts(actions)])
    return rows


def build_report(register: list[dict[str, str]]) -> list[str]:
    severity_counts = Counter(row["severity"] for row in register)
    surface_counts = Counter(row["affected_route_surface"] for row in register)
    owner_counts = Counter(row["risk_owner"] for row in register)
    high_rows = [row for row in register if row["severity"] == "high"]
    medium_rows = [row for row in register if row["severity"] == "medium"]
    low_rows = [row for row in register if row["severity"] == "low"]

    lines: list[str] = [
        "# Unresolved Risk Report",
        "",
        "Status: TB-043 unresolved-risk report and final QA summary complete; result: Final QA complete with known unresolved route-resolution risks.",
        f"Generated: {date.today().isoformat()}.",
        "",
        "Scope: summarizes explicit `NEEDS ROUTE RESOLUTION` objective rows already carried by `main-guide-v1.md`, the internal coverage ledger, appendices, and Phase 15 QA artifacts. This pass does not resolve gameplay facts, accept risk, or perform broad gameplay research.",
        "",
        "## Result Summary",
        "",
    ]
    lines.extend(
        table(
            ["Check", "Result"],
            [
                ["Unresolved objective rows", len(register)],
                ["High-severity rows", severity_counts.get("high", 0)],
                ["Medium-severity rows", severity_counts.get("medium", 0)],
                ["Low-severity rows", severity_counts.get("low", 0)],
                ["Row-level register", rel(OUTPUT_REGISTER)],
                ["Summary CSV", rel(OUTPUT_SUMMARY)],
                ["Prior QA repair actions", "none; prior QA artifacts contain only no-action or explicit route-resolution states"],
            ],
        )
    )

    lines.extend(["", "## Severity Model", ""])
    lines.append("Severity is a triage priority for follow-up work, not permission to skip lower-severity rows.")
    lines.extend([""])
    lines.extend(
        table(
            ["Severity", "Definition"],
            [
                ["high", "Quest, trophy, radiant, spell/power, unique-item, AE Creation quest/reward, or branch-route unresolved rows that can affect completion state, reward preservation, counter/trophy proof, or branch continuity."],
                ["medium", "Collectible, crafting/progression, location, miscellaneous objective, relationship, or ordinary AE consumable/item-set rows that need exact route placement or policy before final closure."],
                ["low", "Book/document source-location rows, usually large inventory/data-reconciliation work rather than route-order blockers."],
            ],
        )
    )

    lines.extend(["", "## Category Summary", ""])
    lines.extend(table(["Category", "Rows", "Severity split", "Likely owner", "Dominant route surfaces"], category_rows(register)))

    lines.extend(["", "## Route Surface Summary", ""])
    lines.extend(
        table(
            ["Route or QA surface", "Rows"],
            [[surface, count] for surface, count in surface_counts.most_common()],
        )
    )

    lines.extend(["", "## Follow-Up Priority", ""])
    lines.extend(
        table(
            ["Priority", "Rows", "Recommended next action"],
            [
                [
                    "1. High-severity route-resolution rows",
                    len(high_rows),
                    "Resolve category by category, starting with quest/trophy/radiant/unique-item rows that affect completion proof or branch/final continuity.",
                ],
                [
                    "2. Medium-severity system and finite-set rows",
                    len(medium_rows),
                    "Resolve Fishing/collectible, crafting/alchemy, location, relationship, and hold-favor rows after high-severity routing is stable.",
                ],
                [
                    "3. Low-severity book/document rows",
                    len(low_rows),
                    "Run a dedicated book/document source-location reconciliation pass for deterministic pickup paths or explicit data exclusions.",
                ],
            ],
        )
    )

    lines.extend(["", "## Risk Owners", ""])
    lines.extend(table(["Likely owner", "Rows"], [[owner, count] for owner, count in owner_counts.most_common()]))

    lines.extend(["", "## Prior QA Closure", ""])
    lines.append("The final-risk report relies on the generated QA artifacts as current state. No broad gameplay research was performed.")
    lines.extend([""])
    lines.extend(table(["QA artifact", "Rows", "Recommended actions"], prior_qa_rows()))

    lines.extend(["", "## Review Notes", ""])
    lines.append(f"The guide should not be treated as fully closed while these {len(register)} explicit route-resolution rows remain. They are visible risk inventory, not hidden coverage gaps.")
    lines.append("")
    lines.append("A follow-up route-resolution phase should work from the row-level register, source-check only the selected bucket, update the relevant source notes and coverage rows, then regenerate the affected audits and this report.")
    return lines


def main() -> int:
    register = build_register()
    summary = build_summary_rows(register)
    write_csv(OUTPUT_REGISTER, FIELDNAMES, register)
    write_csv(OUTPUT_SUMMARY, ["summary_group", "metric", "count", "notes"], summary)
    OUTPUT_REPORT.write_text("\n".join(build_report(register)) + "\n", encoding="utf-8")
    print(f"Wrote {rel(OUTPUT_REGISTER)}")
    print(f"Wrote {rel(OUTPUT_SUMMARY)}")
    print(f"Wrote {rel(OUTPUT_REPORT)}")
    print(f"unresolved_rows: {len(register)}")
    print(format_counts(Counter(row["severity"] for row in register)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
