# Source Note: Skill and Perk Foundation

Status: needs review.

Source note ID: SN-000081

## Claim

Skyrim has 18 skills grouped into Magic, Combat, and Stealth specializations. The skill system contains 180 perk nodes and 251 perk ranks across those skill trees. One perk point is awarded when the character's overall level increases, and unlocking every perk rank requires a level/perk-point plan using Legendary skill resets.

## Routing Relevance

The specification requires all skills to 100 and all perks acquired. This source note supports the TB-009A objective rows and skill support table without deciding final perk allocation, training order, grind blocks, exploit policy, or which skills should be made Legendary.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Skill list, specialization grouping, perk counts, Legendary skill reset rules, perk-point notes, and skill-related achievements. |

## Evidence Summary

The UESP Skills page lists 18 skills in three specializations:

| Specialization | Skills |
| --- | --- |
| Magic | Alteration; Conjuration; Destruction; Enchanting; Illusion; Restoration |
| Combat | Archery; Block; Heavy Armor; One-handed; Smithing; Two-handed |
| Stealth | Alchemy; Light Armor; Lockpicking; Pickpocket; Sneak; Speech |

The same page states that there are 180 skill perks, or 251 when all perk ranks are counted. Its skill table gives per-tree perk node and perk-rank counts; those counts are captured in `data/skills/skill-perk-catalog.csv`.

The page states that one perk point is awarded when the character's overall level increases and that most perks have skill-level requirements plus prerequisite perks. It also explains that Legendary skills can be reset after reaching 100, returning the skill to 15 and refunding the perk points assigned to that skill. UESP notes that Legendary resets allow the player to exceed the old level cap and eventually gain enough perk points for every skill perk; it gives level 252 as the level needed to unlock all skill perks.

The page's achievement section lists Skill Master as the achievement for getting a skill to 100. PS4 trophy-specific validation remains deferred to TB-015.

## Confidence and Open Questions

Confidence is high for the skill list, specialization grouping, perk counts, and baseline Legendary reset mechanics on the current UESP page.

Open questions for later work:

* individual perk names, prerequisites, and rank requirements;
* exact route order for skill training and perk allocation;
* which skills, if any, should be made Legendary repeatedly;
* how to distribute skill leveling so Legendary difficulty does not produce an overleveled but underpowered character;
* whether any exploit or accelerated loop is acceptable under the project's exploit policy;
* PS4 trophy validation for Skill Master and other skill/crafting-adjacent trophies.

## Linked Records

`data/objectives/objectives.csv` rows `OBJ-002425` through `OBJ-002465`; `data/skills/skill-perk-catalog.csv`; `docs/task-board.md`.
