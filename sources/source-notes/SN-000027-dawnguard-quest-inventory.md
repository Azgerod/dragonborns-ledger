# Source Note: Dawnguard Quest Inventory

Status: needs review.

Source note ID: SN-000027

## Claim

The Dawnguard add-on quest inventory is represented at source-list level in the objective database. Dawnguard-aligned quests are marked for the canonical main route, Volkihar-aligned quests are marked as branch-route objectives, and shared main-quest objectives are represented once.

The UESP Dawnguard Quests page also lists `Find out about the Dawnguard` as the initial hook. This pass records that hook as the start trigger for the `Dawnguard` objective instead of adding a standalone objective row, keeping the entered rows aligned with the page's stated 39 new-quest inventory.

## Routing Relevance

This pass gives later route and constraint work a complete Dawnguard quest-objective inventory without prematurely deciding exact travel order, warning placement, reward handling, or radiant repetition policy. The canonical project route joins the Dawnguard; the Volkihar questline remains branch-only because it is mutually exclusive with Dawnguard membership on the same continuity.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000024 | Skyrim:Dawnguard Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dawnguard_Quests | 2026-05-11 | Lists Dawnguard main, faction, side, and miscellaneous quests. |
| SRC-000025 | Skyrim:Dawnguard (faction) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dawnguard_(faction) | 2026-05-11 | Lists Dawnguard membership path, main questline structure, and Dawnguard radiant/finite quest availability. |
| SRC-000026 | Skyrim:Volkihar Vampire Clan | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Volkihar_Vampire_Clan | 2026-05-11 | Lists Volkihar membership path, branch questline structure, and Volkihar radiant/other quest inventory. |

## Evidence Summary

UESP's Dawnguard Quests page states that the add-on adds 39 new quests and organizes them into main, faction, side, and miscellaneous buckets. It states that no journal quest appears immediately on installation and that the first main quest begins by hearing about vampire hunters from an NPC.

The Dawnguard faction page describes the Dawnguard membership path: speak with Isran at Fort Dawnguard, complete the early Dawnguard setup, then reject Lord Harkon's offer during `Bloodline`. It lists the Dawnguard primary questline and identifies `Bolstering the Ranks` as optional. It also lists Dawnguard radiant work after `A New Order`, says `Ancient Technology` can be done six times, and says `Lost Relic` can be done three times after `Bolstering the Ranks`.

The Volkihar Vampire Clan page describes the Volkihar membership path: after `Awakening`, escort Serana to Castle Volkihar and accept Harkon's gift during `Bloodline`; it identifies this as the opportunity to join the clan. It lists the Volkihar primary questline and Volkihar radiant/other quest inventory. These rows are branch-route objectives because the project specification keeps Dawnguard as the canonical main route.

## Confidence and Open Questions

Confidence is high for quest inventory and branch/main separation. Later passes still need exact prerequisites, individual completion boundaries, reward preservation, NPC dependencies, bug risks, radiant stopping rules, trophy behavior, Survival Mode routing implications, and hard-save placement.

## Linked Records

OBJ-000351 through OBJ-000389.
