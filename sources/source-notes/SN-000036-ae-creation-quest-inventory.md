# Source Note: AE Creation Quest Inventory

Status: needs review.

Source note ID: SN-000036

## Claim

UESP's Creation Club Quests index lists 106 named quest links across official Skyrim Creation Club packages. These rows are child quest inventory records for AE Creation content, not route-ready quest instructions.

## Routing Relevance

The specification requires all official AE Creation Club quests to be included. A source-backed quest inventory lets later passes validate exact start triggers, level gates, prerequisites, completion boundaries, rewards, conflicts, bugs, Survival Mode implications, and branch handling without losing track of which Creation package each quest belongs to.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000058 | Skyrim:Creation Club Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club_Quests | 2026-05-11 | Quest inventory grouped by Creation package. |
| SRC-000055 | Skyrim:Creation Club | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club | 2026-05-11 | Supports official Creation Club package context and AE bundle membership cross-check. |
| SN-000035 | AE Bundle Membership and Parent Creation Inventory | Local source note | sources/source-notes/SN-000035-ae-bundle-membership-and-parent-inventory.md | 2026-05-11 | Parent-package objective rows and official AE bundle scope. |

## Evidence Summary

UESP's Creation Club Quests page groups named quest links under Creation package headings. The page also notes that Creation Club quests are added by Creations and that new world interactions are not listed there, so this pass only creates quest child rows. UESP marks the page incomplete/outdated, so these rows should be treated as inventory coverage rather than validated routing facts.

This pass records 106 source-listed quest rows under the matching official AE parent package rows. It intentionally does not resolve exact route timing, start-trigger reliability, quest-stage boundaries, mutually exclusive outcomes, cell-entry risk, bug risk, reward preservation, or checklist synchronization details.

## Confidence and Open Questions

Confidence is high that the 106 rows match the current UESP Creation Club Quests index. Confidence is not yet high enough to route from these rows directly, because the index is not a substitute for individual quest-page validation. Later passes must check individual quest pages and supporting sources for start triggers, level gates, rewards, conflicts, bugs, and branch handling.

## Linked Records

OBJ-000553 through OBJ-000658.
