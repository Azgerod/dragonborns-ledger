# Source Note: Dragonborn and AE Bug Mitigations

Status: researched.

Source note ID: SN-000111

## Claim

Dragonborn and AE rows needing TB-017 handling include `A New Source of Stalhrim`, `Served Cold`, `Reluctant Steward`, `Old Friends`, `Unearthed`, Thirsk, Dragonrider, and Elytra pet recruitment. The highest route-impact risks are quest-start NPC scene interruption, inaccessible Varona blocking `The Hidden Twilight`, Kolbjorn phase/relic handling, Thirsk combat/objective timing, dragon-riding instability, and a source-listed Elytra follower-dialogue bug.

## Routing Relevance

Dragonborn quests feed trophies, Black Books, Stalhrim crafting, Severin Manor, Solstheim location routing, followers, and unique items. AE pet rows are checklist-relevant. A no-console route needs save points and verification after each bug-prone handoff rather than assuming all quest stages can be repaired.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000038 | Skyrim:The Chief of Thirsk Hall | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Chief_of_Thirsk_Hall | 2026-05-11 | Riekling-side Thirsk branch and bug notes. |
| SRC-000039 | Skyrim:Retaking Thirsk | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Retaking_Thirsk | 2026-05-11 | Nord-side Thirsk branch, favor availability, and bug notes. |
| SRC-000040 | Skyrim:A New Source of Stalhrim | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_New_Source_of_Stalhrim | 2026-05-11 | Skaal scene, Deor/Fanari dependency, Abandoned Lodge, and marker bugs. |
| SRC-000042 | Skyrim:Served Cold | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Served_Cold | 2026-05-11 | Raven Rock Owner quest and Severin Manor ownership bugs. |
| SRC-000044 | Skyrim:Dragon Riding | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Riding | 2026-05-12 | Bend Will mechanics, rideable dragon exclusions, Dragonrider context, and riding bugs. |
| SRC-000085 | Skyrim:My Pet Elytra (Dementia) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:My_Pet_Elytra_(Dementia) | 2026-05-11 | Demented Elytra quest and shared Mania dialogue bug note. |
| SRC-000086 | Skyrim:My Pet Elytra (Mania) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:My_Pet_Elytra_(Mania) | 2026-05-11 | Manic Elytra quest and follower-dialogue bug note. |
| SRC-000373 | Skyrim:Unearthed | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unearthed | 2026-05-12 | Kolbjorn excavation phases, Ahzidal relic timing, Ralis journals, and bug notes. |
| SRC-000395 | Skyrim:Reluctant Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reluctant_Steward | 2026-05-12 | Varona corpse, steward-candidate, Black Book, and staff enchanter bug notes. |
| SRC-000396 | Skyrim:Old Friends | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Old_Friends | 2026-05-12 | Neloth locator spell and Ildari heart animation bugs. |

## Evidence Summary

`A New Source of Stalhrim` tells the player not to talk to the Skaal villagers until their conversation finishes, and its bug section confirms that interrupting the Deor/Fanari conversation can make Deor unusable and the quest unattainable. The same source records marker and Abandoned Lodge key risks, while existing NPC notes record the need to protect Deor and Fanari until the quest starts.

`Served Cold` records possible objective, Severin Manor ownership, house-stat, and final progression bugs; these are best handled by saves before the tomb surveillance, Severin Manor infiltration, and Ashfallow Citadel finale, followed by verifying ownership before using the manor as safe storage. `Reluctant Steward` records a confirmed Varona corpse/no-marker/inaccessible-body bug that can block access to `Black Book: The Hidden Twilight` and the Tel Mithryn staff enchanter room. `Old Friends` records a confirmed Neloth locator-spell bug and a confirmed Ildari heart animation bug.

`Unearthed` records phase and cleanup risks: courier progress can stall, the second-visit door can prematurely lock access, Ralis journals can become permanent quest items, leaving without collecting `Black Book: Filament and Filigree` can interact with journal cleanup, and Ahzidal relics have phase-specific availability. Thirsk pages record branch bugs around killing rieklings too quickly on the Nord side and Riekling follower availability on the Riekling side. Dragon Riding records several confirmed ride-state bugs and non-rideable dragon exclusions, supporting saves before each Dragonrider attempt. The Elytra pet pages record a USSEP-fixed dialogue-stage check affecting Mania follower acceptance, so official PS4 AE needs a save-and-verify warning until platform behavior is tested.

## Confidence and Open Questions

Confidence is high for Stalhrim, Reluctant Steward, Unearthed, Thirsk, and Dragonrider warnings. Confidence is moderate for Elytra because UESP records a bug but not a no-console workaround; the route should keep it as a platform-test item rather than silently assuming both pets can be recruited. `Served Cold` bugs appear likely but mostly verification-oriented, not a reason to reorder the whole Raven Rock chain.

## Linked Records

`data/constraints/bug-prone-quests.md`; OBJ-000424; OBJ-000436; OBJ-000448; OBJ-000449; OBJ-000454; OBJ-000455; OBJ-000465; OBJ-000477; OBJ-000677; OBJ-000678.

