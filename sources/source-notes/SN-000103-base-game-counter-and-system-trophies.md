# Source Note: Base-Game Counter and System Trophies

Status: researched.

Source note ID: SN-000103

## Claim

Base-game system trophies use counters or one-time system actions: side quests, miscellaneous objectives, work/crafting actions, locks and pockets, persuasion/bribe/intimidate, standing stones, property, jail escape, marriage, bounties, gold, cleared dungeons, skill level, discovered locations, skill books, dragon souls, shouts, and character level.

## Routing Relevance

The route should satisfy these counters naturally where possible, but some need explicit route controls: `Sideways` has unusual count exceptions, `Hero of the People` counts objectives rather than quests, `Master Criminal` should be staged as a controlled crime cleanup or hard-save branch, and `Delver` and `Explorer` need location-counter QA. Dedicated trophy tracker rows were added after TB-015 for the counter and level trophies that previously existed only as support objectives or table warnings.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-12 | Base-game general trophy requirements. |
| SRC-000019 | Skyrim:Side Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Side_Quests | 2026-05-11 | Sideways count rules and exceptions. |
| SRC-000020 | Skyrim:Miscellaneous Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests | 2026-05-11 | Hero of the People objective-count rules. |
| SRC-000168 | Skyrim:Standing Stone | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Standing_Stone | 2026-05-11 | Standing stone trophy context. |
| SRC-000183 | Skyrim:Skill Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skill_Books | 2026-05-11 | Reader count behavior. |
| SRC-000263 | Skyrim:Dungeons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeons | 2026-05-12 | Delver clearing context. |
| SRC-000265 | Category:Skyrim-Places-Discoverable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Discoverable | 2026-05-12 | Explorer location-discovery context. |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Skill Master and skill-level context. |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Artificer and Hard Worker activity context. |
| SRC-000385 | Skyrim:Dragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon | 2026-05-12 | Dragon souls, dragon-related trophies, and Legendary Dragon timing. |

## Evidence Summary

UESP's achievements page supplies the base requirements for these system trophies. The side-quest and miscellaneous-quest pages add routing-critical count caveats: `Sideways` usually follows side-quest completion but excludes or includes several unusual cases, while `Hero of the People` counts completed objectives rather than completed quests. The Skill Books page says `Reader` requires 50 different skill books out of 90, and it still counts books read after the related skill reaches 100.

The Dungeons page ties clearable locations to `Delver`, while the discoverable-place category ties map-marker discovery to `Explorer`. The Dragon page ties dragon souls to `Dragon Soul` and `Dragon Hunter`; it also says Legendary Dragons begin appearing in leveled lists at level 78, so `Legend` must be late even though the achievement itself is Dawnguard-labeled.

## Confidence and Open Questions

Confidence is high for trophy requirements. Dedicated tracker rows now exist for `Thief`, `Snake Tongue`, `Citizen`, `Wanted`, `Master Criminal`, `Golden Touch`, `Dragon Hunter`, and the base-game level trophies. Open items for TB-021/TB-022 are exact route placement, counter-check cadence, and whether any trophy rows should be split further for checklist mapping.

## Linked Records

OBJ-000219, OBJ-000220, OBJ-000221 through OBJ-000350, OBJ-000760 through OBJ-000788, OBJ-000909, OBJ-001919 through OBJ-001945, OBJ-001958 through OBJ-002407, OBJ-002465, OBJ-002751, OBJ-002752, OBJ-002762, OBJ-002764, OBJ-002765, OBJ-002773 through OBJ-002783.
