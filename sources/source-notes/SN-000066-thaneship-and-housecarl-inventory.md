# Source Note: Thaneship and Housecarl Inventory

Status: needs review.

Source note ID: SN-000066

## Claim

The objective database needs source-list coverage for all nine hold thaneships and all player-appointed housecarls available through those thaneships. Winterhold has a thaneship but no source-listed player housecarl or residence.

## Routing Relevance

Thaneships affect property access, housecarl/follower availability, honorary weapons, local reputation, Civil War state handling, and later NPC-dependency validation. Recording them as relationship rows keeps later route, branch, warning, and checklist passes from losing these prerequisites inside miscellaneous quest rows or property rows.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000242 | Skyrim:Thane | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Thane | 2026-05-12 | Lists hold thane quests, Jarl/Civil War variants, required favors/quests, residences, housecarls, and honorary weapons. |
| SRC-000243 | Skyrim:Housecarl | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Housecarl | 2026-05-12 | Lists housecarls available to the player and distinguishes them from Jarls' housecarls. |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | Cross-checks city-home and Hearthfire-house housecarl associations. |

## Evidence Summary

UESP's Thane page table lists nine hold titles: Eastmarch, Falkreath, Haafingar, Hjaalmarch, the Pale, the Reach, the Rift, Whiterun, and Winterhold. For each hold it gives the relevant Jarl path or Civil War replacement path, associated favor or quest requirements, residence where applicable, housecarl where applicable, and honorary weapon. The table marks Hearthfire residences and housecarls for Falkreath, Hjaalmarch, and the Pale, and lists Winterhold with no residence and no housecarl.

UESP's Housecarl page states that every housecarl appointed to the player is also available as a follower, then lists the housecarls available to the player: Argis the Bulwark, Calder, Gregor, Iona, Jordis the Sword-Maiden, Lydia, Rayya, and Valdimar. The page separates those player housecarls from Jarls' housecarls, so Jarl bodyguards are not treated as standalone completion objectives in this source-list pass.

## Confidence and Open Questions

Confidence is high for the source-list thaneship and player-housecarl membership. Exact Civil War/Season Unending effects, current-Jarl prerequisites, Riften exceptions, Eastmarch/Hjerim/Blood on the Ice sequencing, minor-hold Hearthfire interactions, housecarl death or dismissal risks, and route-level follower use remain deferred to later conflict, NPC, bug, and route passes.

## Linked Records

OBJ-001926 through OBJ-001944.
