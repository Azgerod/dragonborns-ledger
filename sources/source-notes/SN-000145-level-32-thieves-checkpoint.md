# Source Note: Level 32 Thieves Checkpoint

Status: reviewed for TB-035-MR-017 draft placement.

Source note ID: SN-000145

## Claim

The v1 guide should treat level 32 as a Nightingale Armor readiness checkpoint only. It should not advance `Hard Answers`, `The Pursuit`, `Trinity Restored`, `Blindsighted`, or `Darkness Returns` here because the current route policy delays the whole late Thieves reward chain to level 46.

## Routing Relevance

The player exits the previous section with `Hard Answers` active after `Speaking With Silence`. `Hard Answers` is the next Thieves Guild quest and awards the Nightingale Blade, which the conservative source-tier policy holds for level 46+. `Trinity Restored` is later in the quest order and is the quest-start lock for Nightingale Armor at level 32+. Since `Hard Answers` and `The Pursuit` must occur before `Trinity Restored`, the checkpoint can only record readiness; it cannot route the armor claim.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000005 | Skyrim:Thieves Guild (faction) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Thieves_Guild_(faction) | 2026-05-12 | Thieves Guild primary quest order and restoration job context. |
| SRC-000325 | Skyrim:Leveled Item Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveled_Item_Quests | 2026-05-12 | Strongest-at thresholds and special notes for leveled quest rewards. |
| SRC-000328 | Skyrim:Hard Answers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hard_Answers | 2026-05-12 | Nightingale Blade reward and level-tier caveat. |
| SRC-000338 | Skyrim:Nightingale Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nightingale_Armor | 2026-05-12 | Nightingale Armor set level registers at the start of `Trinity Restored`. |
| SRC-000344 | Skyrim:Blindsighted | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Blindsighted | 2026-05-12 | Nightingale Bow reward timing. |
| SRC-000345 | Skyrim:Trinity Restored | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Trinity_Restored | 2026-05-12 | Nightingale Armor set reward timing and quest sequence. |
| SRC-000347 | Skyrim:The Pursuit | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Pursuit | 2026-05-12 | Riftweald Manor and Chillrend acquisition context. |

## Evidence Summary

The leveled-reward constraints record Nightingale Armor, Boots, Gloves, and Hood as strongest at level 32+, with the lock occurring when `Trinity Restored` starts. The same constraints record Nightingale Blade and Nightingale Bow as level-46 reward targets under the conservative source-tier policy, and Riftweald Manor/Chillrend as level-46-gated because Chillrend's level is set when Riftweald Manor is first entered.

The early Thieves route already stops after `Speaking With Silence`, with `Hard Answers` active but untouched. The quest order means the route cannot start `Trinity Restored` without completing `Hard Answers` and `The Pursuit` first. Therefore the level-32 section is a readiness checkpoint only: record whether the armor threshold is met, keep the entire late chain closed, and continue to the next routed geography block for real objectives and XP.

Delvin/Vex jobs remain closed here because they are city restoration radiants and have their own ledger/restoration block. The checkpoint does not create new objective completion; it preserves gates.

## Confidence and Open Questions

Confidence is high that no player-facing quest progress belongs in this checkpoint. The checkpoint exists to preserve a critical route invariant: level 32 is necessary for maximum Nightingale Armor, but the current main route still waits for level 46 before resuming late Thieves rewards. No TB-035-MR-017 `NEEDS ROUTE RESOLUTION` notes remain.

## Linked Records

OBJ-000042; OBJ-000043; OBJ-000044; OBJ-000045; OBJ-000046; OBJ-000048; OBJ-000180; OBJ-000807; OBJ-001559; OBJ-001571; OBJ-001576; OBJ-001750; OBJ-001762; OBJ-001763; OBJ-001766; OBJ-001767; OBJ-001768; OBJ-001769; OBJ-002312.
