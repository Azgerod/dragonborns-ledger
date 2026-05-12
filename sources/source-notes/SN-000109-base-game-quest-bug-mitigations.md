# Source Note: Base-Game Quest Bug Mitigations

Status: researched.

Source note ID: SN-000109

## Claim

Several base-game quest bugs are relevant to a no-console PS4 route: Bards College objectives should avoid late-start and early-pickup states, `The Dainty Sload` should be completed with saves around Delvin/Erikur/Balmora Blue handoffs, `Blood on the Ice` should be completed in a tightly controlled Windhelm window before Hjerim use, and `No One Escapes Cidhna Mine` should not be triggered during active Thieves Guild special jobs or with risky item-smuggling/pet states.

## Routing Relevance

TB-017 converts bug notes into constraints only where a later route needs an order rule, hard save, or verification checkpoint. These rows should prevent permanent quest-item states, blocked side quests or trophy restoration, invalid Hjerim ownership/furnishing, failed Thieves Guild jobs, and PS4-unrecoverable quest progression issues.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000013 | Skyrim:Bards College | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bards_College | 2026-05-11 | College-level investigation and instrument bug summary. |
| SRC-000014 | Skyrim:Investigate the Bards College | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Investigate_the_Bards_College | 2026-05-11 | Late-start and early King Olaf's Verse risks. |
| SRC-000015 | Skyrim:Tending the Flames | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tending_the_Flames | 2026-05-11 | Festival, Elisif, Bound Until Death, Season Unending, and verse-choice caveats. |
| SRC-000016 | Skyrim:Finn's Lute | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Finn%27s_Lute | 2026-05-11 | Early-pickup and quest-item persistence risks. |
| SRC-000017 | Skyrim:Pantea's Flute | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pantea%27s_Flute | 2026-05-11 | Early-pickup and marker/turn-in risks. |
| SRC-000018 | Skyrim:Rjorn's Drum | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rjorn%27s_Drum | 2026-05-11 | Early-pickup and Special Edition Halldir trap risk. |
| SRC-000388 | Skyrim:The Dainty Sload | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Dainty_Sload | 2026-05-12 | Solitude Thieves Guild special-job steps and quest bugs. |
| SRC-000392 | Skyrim:Blood on the Ice | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Blood_on_the_Ice | 2026-05-12 | Windhelm quest initiation, progression, Strange Amulet, and Civil War bugs. |
| SRC-000393 | Skyrim:Hjerim | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hjerim | 2026-05-12 | Hjerim cleanup, purchase, and display bugs. |
| SRC-000394 | Skyrim:No One Escapes Cidhna Mine | 2 - UESP | https://en.uesp.net/wiki/Skyrim:No_One_Escapes_Cidhna_Mine | 2026-05-12 | Markarth prison quest bugs, inventory caveats, and follower/pet caveats. |

## Evidence Summary

UESP records Bards College bugs where the introductory investigation can become incompletable if started after joining or after early King Olaf's Verse pickup. The three instrument pages record early-pickup or quest-item persistence risks, and `Rjorn's Drum` adds a Special Edition Halldir failure where the player can be trapped in the room. `Tending the Flames` also carries late-step interactions with active `Bound Until Death` and `Season Unending` states.

`The Dainty Sload` page records several bugs that matter for `One with the Shadows`: Erikur can glitch off the map after many in-game days, Sabine can become hard to access, the ship may fail to render correctly, Balmora Blue may fail to enter inventory, and Delvin can offer the quest without starting it. The existing trophy and NPC notes also identify Erikur as a route dependency who becomes killable after `Bound Until Death`.

The `Blood on the Ice` page records multiple no-console risks: NPC death or missing Windhelm crime-scene actors can block initiation, capturing Windhelm before the crime-scene trigger can prevent the guard from appearing, beginning Dragonborn's first main quest before this investigation can prevent it from starting, early Hjerim entry or Strange Amulet pickup can break initiation, and several progression bugs can occur if the quest is left open or if the Strange Amulet is not sold to Calixto. The `Hjerim` page adds property-specific risks: the cleanup purchase can disappear or behave poorly after other furnishing choices, murder-scene containers can interact badly with cleanup, the house can remain unpurchasable, and dagger display cases can trap placed daggers.

The `No One Escapes Cidhna Mine` page records that triggering the Markarth arrest before reporting completed Delvin/Vex special jobs can fail those Thieves Guild jobs. It also warns against pre-killing mine guards, using the hotkeyed quest-item smuggling behavior, and bringing animals or Creation pets into Druadach Redoubt after siding with Madanach. A PSVR-only black-screen bug is explicitly not treated as a flat PS4 AE route constraint.

## Confidence and Open Questions

Confidence is high for route warnings around Bards, `The Dainty Sload`, Windhelm/Hjerim, and Cidhna Mine. Exact PS4 AE patch behavior for every UESP-listed bug is not individually proven, but the mitigation is low-cost and prevents no-console recovery problems. Hjerim final purchase timing still needs TB-021/TB-032 integration with Imperial Civil War routing.

## Linked Records

`data/constraints/bug-prone-quests.md`; OBJ-000047; OBJ-000050; OBJ-000060; OBJ-000182 through OBJ-000187; OBJ-000202; OBJ-001923.
