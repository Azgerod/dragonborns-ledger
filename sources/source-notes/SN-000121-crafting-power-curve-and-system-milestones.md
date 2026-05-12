# Source Note: Crafting Power Curve and System Milestones

Status: needs review.

Source note ID: SN-000121

## Claim

Crafting must be staged as both completion content and power support. The route must use Alchemy, Enchanting, Smithing, and the source-listed practical crafting systems, but it should not rush maximum crafting loops early because the specification requires a gradually increasing Legendary-difficulty power curve.

## Routing Relevance

This note supports TB-020 crafting policy and later TB-027/TB-030 placement of crafting blocks, recipes, material staging, and checklist coverage.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000279 | Skyrim:Smithing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Smithing | 2026-05-12 | Smithing stations, perk gates, tempering, skill XP, quest-gated materials, and Arcane Blacksmith bug note. |
| SRC-000272 | Skyrim:Enchanting | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting | 2026-05-12 | Enchanting requirements, disenchanting, Extra Effect, skill XP, Fortify Enchanting, and Staff Enchanter XP notes. |
| SRC-000281 | Skyrim:Alchemy | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alchemy | 2026-05-12 | Alchemy effects, Experimenter reset behavior, potion XP, ingredient gardening, and Fortify Restoration interaction. |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Source-listed activity/crafting-system boundary. |
| SRC-000298 | Skyrim:Atronach Forge | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Atronach_Forge | 2026-05-12 | Atronach Forge practical system support. |
| SRC-000119 | Skyrim:Staff Enchanter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_Enchanter | 2026-05-12 | Staff Enchanter practical system support. |
| SRC-000299 | Skyrim:Imbuing Chamber | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Imbuing_Chamber | 2026-05-12 | Imbuing Chamber practical system support. |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Survival Mode carry, food, and sleep constraints relevant to material staging. |
| SRC-000418 | Skyrim:Fatigue | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fatigue | 2026-05-12 | Fatigue effects on beneficial potion reliability. |

## Evidence Summary

Smithing is both a completion skill and a power gate. UESP lists perk requirements up to Dragon Armor at Smithing 100 and Arcane Blacksmith at Smithing 60. It also ties Stalhrim, Nordic Jewelry, Ghosts of the Tribunal, Ancient Ice, and other crafting access to quests or Creation content. Tempering can improve items again when skill, perks, or Fortify Smithing support improve, so the route can safely stage gear upgrades instead of making final gear immediately.

Enchanting requires an item, a learned enchantment, and a filled soul gem. Disenchanting destroys the source item, while many artifacts and unique items cannot be disenchanted. Extra Effect at Enchanting 100 applies only when creating an item, so final gear should be crafted after the perk and potion support are ready. Enchanting XP from creating items is not based on item value, and sleeping or Mage Stone bonuses can improve XP gain per enchantment.

Alchemy XP is proportional to potion value. UESP identifies gardens and greenhouses as reliable ingredient sources and notes that Experimenter can reveal ingredient properties, then be reset without forgetting those effects after Legendary skill reset. Fortify Restoration interactions can create extreme crafting loops and are explicitly treated as exploit-adjacent for this project.

Practical crafting systems include Alchemy, Enchanting, Staff Enchanting, Smithing, Atronach Forge, Baking, Bone Forge, Construction, Cooking, Imbuing Chamber, Mining, Smelting, and Tanning. Some are trophy actions, some are route actions, and some are checklist or representative system coverage. Survival Mode makes material staging more important because carry capacity is reduced and level-ups/rested bonuses require bed access.

## Policy Implications

| Topic | TB-020 policy |
| --- | --- |
| Artificer and Hard Worker | Place explicit low-risk actions early enough to verify trophies without giving the player final gear. |
| Smithing power | Use staged improvements; reserve maximum Smithing/Alchemy/Enchanting synergy for late-game or final cleanup. |
| Enchantment learning | Learn effects from non-preserved sources; never destroy a unique item solely to learn an enchantment. |
| Alchemy discovery | Use recipes, eating, and Experimenter deliberately; exact ingredient copies and recipe order remain TB-030 work. |
| Fortify Restoration loop | Do not baseline. It requires an explicit exploit decision if ever offered as an optional late cleanup shortcut. |
| Staff Enchanter and Imbuing Chamber | Include representative use after access is safe; exact outputs remain downstream. |
| Survival staging | Sleep before potion-dependent crafting blocks and use storage/material depots before heavy construction or forging work. |

## Confidence and Open Questions

Confidence is high that crafting must be staged and that exploit-level crafting should not be the default route.

Open questions for later work:

* exact recipes and source items for each enchantment and alchemy effect;
* final gear defaults and whether they should be optimized or merely sufficient;
* exact material quantities for Hearthfire, Smithing, Stalhrim, Atronach Forge, Staff Enchanter, and Imbuing Chamber actions;
* whether any post-game cleanup grind may use exploit-adjacent loops after trophies and route integrity are secure.

## Linked Records

`data/constraints/skill-perk-leveling-plan.md`; `data/skills/enchantment-learning-catalog.csv`; `data/skills/alchemy-effect-catalog.csv`; `data/skills/practical-crafting-system-catalog.csv`; `data/constraints/survival-mode-constraints.md`; `docs/task-board.md`.
