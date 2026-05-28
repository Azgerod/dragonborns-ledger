#!/usr/bin/env python3
"""Audit option/default checklist-row representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-004. It checks every
Option-list note row from the checklist coverage matrix against the
player-facing guide, relationship option support table, and internal coverage
ledger.
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
NPC_OPTIONS_CSV = REPO_ROOT / "data" / "npc" / "relationship-options.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-option-default-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

DEFAULT_EVIDENCE_BY_CATEGORY = {
    "quest": ("ysolda", "route default", "default spouse"),
    "follower_option": ("no permanent optional humanoid follower", "non default choices", "option set"),
}

SUPPORT_NAME_ALIASES = {
    "armored frost troll": "armored frost troll dg",
    "armored troll": "armored troll dg",
    "bran": "bran dg",
    "cusith": "cusith dg",
    "garmr": "garmr dg",
    "sceolang": "sceolang dg",
    "gregor": "gregor hf",
    "rayya": "rayya hf",
    "valdimar": "valdimar hf",
    "riekling warrior": "riekling riekling hunter riekling scout or riekling warrior",
    "frost": "frost black briar lodge",
    "shadowmere": "shadowmere dark brotherhood questline",
    "arvak": "arvak soul cairn and summoned soul cairn horse quest",
}

OPTION_COVERAGE_STATUSES = (
    "option",
    "availability",
    "branch",
    "complete",
    "placed",
    "staged",
    "not_available",
    "locked",
    "presented",
)

SHORT_NAME_ALLOWLIST = {"lob", "ria"}


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


def name_variants(value: str) -> set[str]:
    variants = {value.strip()}
    variants.add(re.sub(r"\([^)]*\)", "", value).strip())
    variants.add(value.replace("The ", "", 1).strip())
    return {variant for variant in variants if variant}


def guide_contains_name(guide_normalized: str, name: str) -> bool:
    for variant in name_variants(name):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4 and normalized_name not in SHORT_NAME_ALLOWLIST:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        if re.search(pattern, guide_normalized):
            return True
    return False


def joined(values: set[str] | list[str], limit: int = 6) -> str:
    clean_values = sorted({value for value in values if value})
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def support_lookup_key(name: str) -> str:
    normalized_name = normalize(name)
    return SUPPORT_NAME_ALIASES.get(normalized_name, normalized_name)


def support_matches_for(name: str, support_by_name: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    key = support_lookup_key(name)
    if key in support_by_name:
        return support_by_name[key]

    matches: list[dict[str, str]] = []
    for variant in name_variants(name):
        normalized_variant = normalize(variant)
        if normalized_variant in support_by_name:
            matches.extend(support_by_name[normalized_variant])
    return matches


def has_default_evidence(guide_normalized: str, category: str) -> bool:
    terms = DEFAULT_EVIDENCE_BY_CATEGORY.get(category, ())
    return all(term in guide_normalized for term in terms)


def rows_have_option_coverage(rows: list[dict[str, str]]) -> bool:
    blob = " ".join(
        " ".join(row.get(key, "") for key in ("record_type", "coverage_status", "completion_status", "notes")).lower()
        for row in rows
    )
    return any(term in blob for term in OPTION_COVERAGE_STATUSES)


def audit_status_for(
    exact_rows: list[dict[str, str]],
    mapped_objective_rows: list[dict[str, str]],
    guide_name_match: bool,
    default_evidence: bool,
    support_rows: list[dict[str, str]],
) -> tuple[str, str, str]:
    if exact_rows and guide_name_match and default_evidence:
        return ("option_row_covered", "none", "")

    if exact_rows and not guide_name_match:
        return (
            "internal_option_coverage_missing_guide_name",
            "add_player_facing_option_name",
            "Internal coverage exists, but the guide does not name this option row.",
        )

    if exact_rows:
        return ("option_row_covered_by_internal_coverage", "none", "")

    if guide_name_match and default_evidence and support_rows:
        return (
            "guide_option_name_missing_checklist_coverage",
            "add_internal_checklist_option_row",
            "Guide names this option and the support table validates it; add exact checklist coverage.",
        )

    if mapped_objective_rows and rows_have_option_coverage(mapped_objective_rows) and default_evidence:
        return (
            "aggregate_option_coverage_missing_checklist_row",
            "add_internal_checklist_option_row",
            "Mapped objective has option coverage, but this checklist row needs exact coverage.",
        )

    if not guide_name_match:
        return (
            "option_row_missing_from_guide_and_coverage",
            "add_player_facing_option_name_and_internal_coverage",
            "The guide must name this option or explicitly explain why it is not part of the option set.",
        )

    return (
        "option_row_needs_default_context",
        "add_default_context_or_internal_coverage",
        "Guide name match exists, but default/alternative option context is not clear.",
    )


def main() -> int:
    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    option_rows = [row for row in matrix_rows if row.get("mapping_type") == "Option-list note"]

    objective_ids = {row["objective_id"] for row in read_csv(OBJECTIVES_CSV)}

    support_rows = read_csv(NPC_OPTIONS_CSV)
    support_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in support_rows:
        support_by_name[normalize(row["name"])].append(row)

    guide_text = MAIN_GUIDE.read_text(encoding="utf-8")
    guide_normalized = normalize(guide_text)

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

    for option_row in option_rows:
        checklist_id = option_row["checklist_id"]
        objective_id = option_row.get("objective_id", "")
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        support_matches = support_matches_for(option_row["checklist_entry"], support_by_name)
        guide_name_match = guide_contains_name(guide_normalized, option_row["checklist_entry"])
        default_evidence = has_default_evidence(guide_normalized, option_row["category"])

        audit_status, recommended_action, notes = audit_status_for(
            exact_rows,
            mapped_objective_rows,
            guide_name_match,
            default_evidence,
            support_matches,
        )

        combined_rows = exact_rows or mapped_objective_rows
        coverage_statuses = {row.get("coverage_status", "") for row in combined_rows}
        completion_statuses = {row.get("completion_status", "") for row in combined_rows}
        guide_locations = {row.get("player_facing_location", "") for row in combined_rows}

        support_option_ids = {row.get("option_id", "") for row in support_matches}
        support_option_types = {row.get("option_type", "") for row in support_matches}
        support_treatments = {row.get("route_treatment", "") for row in support_matches}

        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        output_rows.append(
            {
                "checklist_id": checklist_id,
                "checklist_tab": option_row["checklist_tab"],
                "checklist_entry": option_row["checklist_entry"],
                "category": option_row["category"],
                "objective_id": objective_id,
                "matched_objective_name": option_row.get("matched_objective_name", ""),
                "support_option_ids": joined(support_option_ids),
                "support_option_types": joined(support_option_types),
                "support_route_treatments": joined(support_treatments),
                "guide_name_match": "Y" if guide_name_match else "N",
                "guide_default_context_match": "Y" if default_evidence else "N",
                "internal_checklist_coverage_row_count": str(len(exact_rows)),
                "internal_objective_coverage_row_count": str(len(mapped_objective_rows)),
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "recommended_action": recommended_action,
                "notes": notes,
            }
        )

    fieldnames = [
        "checklist_id",
        "checklist_tab",
        "checklist_entry",
        "category",
        "objective_id",
        "matched_objective_name",
        "support_option_ids",
        "support_option_types",
        "support_route_treatments",
        "guide_name_match",
        "guide_default_context_match",
        "internal_checklist_coverage_row_count",
        "internal_objective_coverage_row_count",
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

    print(f"Wrote {len(output_rows)} option/default audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
