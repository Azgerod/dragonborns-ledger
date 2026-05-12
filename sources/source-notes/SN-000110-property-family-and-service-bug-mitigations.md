# Source Note: Property, Family, and Service Bug Mitigations

Status: researched.

Source note ID: SN-000110

## Claim

Hearthfire construction, personal stewards, bards, adoption, spouse/child movement, and house displays need route verification points because UESP records confirmed or official-game-relevant bugs around partial construction, steward assignment, steward furnishing, bard hiring, adoption eligibility, family moves, and property storage/display behavior.

## Routing Relevance

The route must build all three Hearthfire houses, furnish them enough for trophies and completion scope, assign household services, adopt children, and preserve safe storage. TB-017 should ensure later route drafts save before irreversible role assignments, avoid known bad build/hiring order, and verify that family/service moves actually take effect.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000032 | Skyrim:Construction | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Construction | 2026-05-12 | Hearthfire building process, furnishing notes, adoption room requirements, and construction bugs. |
| SRC-000033 | Skyrim:Adoption | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Adoption | 2026-05-12 | Adoption requirements, family moves, child pets, Proud Parent context, and adoption bugs. |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | House ownership/storage context and house-level caveats. |
| SRC-000244 | Skyrim:Marriage | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Marriage | 2026-05-12 | Spouse movement, spouse store, and marriage bug caveats. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Steward assignment permanence, furnishing behavior, services, and steward bugs. |
| SRC-000390 | Skyrim:Protected NPCs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Protected_NPCs | 2026-05-12 | Protected NPC status for spouse/follower role safety. |

## Evidence Summary

UESP's Construction page advises finishing building or furnishing each part at one time to avoid bugs and adding furnishings separately or in small groups to avoid resource-loss bugs. It records confirmed Hearthfire bugs where carpenter workbench menus can be blank, already-built items can remain listed, the Storage Room deck railings can block later connecting decks if built before Bedrooms or Armory, steward-bought furnishings may not appear, partially built wings can trap the player in an inside/outside cell state, and remodeling the Small House can lose improvements or container contents.

The Personal Steward page states that a steward assignment is permanent for a Hearthfire homestead and records bugs where stewards can vanish, furnishing dialogue can falsely require more gold, the same steward can be hired for more than one home and break steward behavior, hiring a bard before the Main Hall is built can make the bard fail to appear, a declined steward offer may not return, and some followers may not offer steward dialogue when Dragonborn is enabled. The same page confirms steward furnishing is gradual and does not cover the Cellar.

The Adoption page records that adoption and later moves can fail, that being denied for lack of a child room can block later adoption, that children or spouse may fail to move to a new home, and that child/pet dialogues can misfire. Construction and Adoption both confirm the room requirements: child-bedroom upgrades for city houses, or two single beds plus dresser in a Main Hall, or child beds plus child chests if the Hearthfire Bedrooms wing is built.

## Confidence and Open Questions

Confidence is high that hard saves and verification checkpoints are needed before steward assignment, bard hiring, adoption, and family moves. Exact default spouse, children, stewards, bards, carriage drivers, wing layouts, and self-build versus steward-furnishing policy remain downstream decisions for TB-019, TB-020, TB-028, and TB-032.

## Linked Records

`data/constraints/bug-prone-quests.md`; `data/properties/property-details.csv`; `data/npc/relationship-options.csv`; OBJ-000407 through OBJ-000412; OBJ-001945 through OBJ-001954; OBJ-001919 through OBJ-001925.

