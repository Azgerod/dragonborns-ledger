# Source Note: Completionist Crafting Scope and Investment Plan

Status: needs review.

Source note ID: SN-000122

## Claim

The crafting-adjacent completion scope is broader than the three crafting skills. The route must account for non-destructive enchantment learning, all source-listed ingredient effects, available merchant investments, practical crafting-system coverage, relevant trophy actions, and unique-item preservation.

## Routing Relevance

This note supports the TB-020 constraint plan and hands recipe, source-item, and checklist synchronization details to later route and checklist tasks.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000287 | Skyrim:Enchanting Effects | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting_Effects | 2026-05-12 | Enchantment-effect source list and non-learnable/unique-only effect distinctions. |
| SRC-000294 | Skyrim:Ingredients | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ingredients | 2026-05-12 | Base, Dawnguard, Dragonborn, AE Creation, and quest ingredient effect rows. |
| SRC-000296 | Skyrim:Merchants | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Merchants | 2026-05-12 | Merchant investment table, available/bugged/unknown merchant status, and NPC replacement notes. |
| SRC-000286 | Skyrim:Speech | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speech | 2026-05-12 | Speech perks, Investor/Merchant/Fence relevance, and commerce skill context. |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Legendary reset notes affecting retained enchantment and alchemy knowledge plus Speech investment caveats. |

## Evidence Summary

The TB-009 support tables establish the current source-list scope:

| Area | Current count | Route implication |
| --- | ---: | --- |
| Enchantment learning | 54 main-route learnable effects, four excluded unique-preservation effects, and one excluded unobtainable effect | Choose source items that can be disenchanted without destroying a preserved unique item. |
| Alchemy effect discovery | 190 source-listed ingredient records across base game, Dawnguard, Dragonborn, and AE Creation content | Discover all ingredient effects; exact recipe ordering and ingredient copy selection remain downstream. |
| Merchant investments | 33 available investment rows, 13 bugged/unofficial-patch-only rows, and four unknown audit rows | Acquire Speech 70 and Investor before investment sweeps; protect merchant NPCs and replacement merchants. |
| Practical crafting systems | 13 systems with existing objectives, new objective rows, route-action-only rows, or checklist-deferred treatment | Include representative or required actions without inflating non-finite systems into fake completion rows. |

UESP's Skills page also notes that learned alchemical properties and enchantments are retained through Legendary resets. That makes Alchemy and Enchanting viable late reset candidates after knowledge capture, but it also means the route cannot repeatedly gain XP from rediscovering the same alchemy properties or disenchanting the same known effect.

Speech is both a skill tree and a completion support system. Investments persist after the Investor perk is lost, but losing Merchant or Fence temporarily removes broad selling options. The route should therefore complete planned investment and selling sweeps before any Speech reset, or treat Speech as a no-reset or one-reset skill.

## Confidence and Open Questions

Confidence is high for the catalog counts and broad scope boundaries because they derive from TB-009 support tables and UESP source lists.

Open questions for later work:

* exact disenchantable source item per enchantment;
* exact all-effects recipe sequence, including AE ingredient coverage;
* whether four unknown AE investment audit rows become routeable after TB-021/TB-030 review;
* whether checklist mapping requires any additional recipe/output knowledge beyond source-listed practical systems.

## Linked Records

`data/skills/enchantment-learning-catalog.csv`; `data/skills/alchemy-effect-catalog.csv`; `data/skills/merchant-investment-catalog.csv`; `data/skills/practical-crafting-system-catalog.csv`; `sources/source-notes/SN-000083-enchantment-learning-scope.md`; `sources/source-notes/SN-000084-alchemy-ingredient-effect-discovery.md`; `sources/source-notes/SN-000085-merchant-investment-scope.md`; `sources/source-notes/SN-000086-practical-crafting-system-reconciliation.md`; `docs/task-board.md`.
