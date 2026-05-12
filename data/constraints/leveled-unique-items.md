# Leveled Unique Items

Status: needs review.

Use this table for unique rewards whose level tier, pickup timing, or location-entry timing can affect route order.

This is the TB-012 constraint pass. It records thresholds and lock timing only; it does not place route steps.

Source handling note: UESP direct raw fetches should use `tools/fetch_uesp.py`, which calls the MediaWiki API with a browser User-Agent. The table cites source notes rather than embedding long page evidence inline.

## Queue Disposition

| Input queue | Disposition |
| --- | --- |
| Associated quest row `OBJ-000198` | Reduced to the Shield of Solitude reward-timing constraint for The Wolf Queen Awakened. |
| 23 leveled reward parent rows (`OBJ-001750` through `OBJ-001772`) | Reduced to one threshold/lock row per item below. |
| Confirmed cell-entry or location-spawn locks | Handed forward to TB-013 for exact warning placement. |
| Bugs, quest conflicts, and route placement | Deferred to TB-014, TB-017, TB-020, and later route phases as appropriate. |

## Constraint Table

| Objective IDs | Item | Content source | Maximum threshold / best useful version | Acquisition or lock event | Safe acquisition rule for later route | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OBJ-001750 | Chillrend | Base game | Level 46+ | Level is determined when Riftweald Manor is first entered. | Do not enter Riftweald Manor before level 46 if the route wants maximum Chillrend. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001751 | Dragonbane | Base game | Level 46+ | Found in Sky Haven Temple during Alduin's Wall; UESP warns not to enter Sky Haven Temple before level 46 for the best version. | Do not enter Sky Haven Temple before level 46. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001752 | Gauldur Blackblade | Base game | Level 36+ | Boss and weapon level can be set when Lost Legends is read or when any related dungeon exterior spawns. | Do not read Lost Legends or approach Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock before level 36 unless the route accepts a lower-tier blade and bow. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001753 | Gauldur Blackbow | Base game | Level 36+ | Boss and weapon level can be set when Lost Legends is read or when any related dungeon exterior spawns. | Do not read Lost Legends or approach Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock before level 36 unless the route accepts a lower-tier blade and bow. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001754 | Lunar Iron Mace | Base game | Level 6+ individually; level 8+ for best Silent Moons Camp pass | Random leveled Lunar weapon placement at Silent Moons Camp. | Visit/loot Silent Moons Camp at level 8+ for the best overall Lunar weapon candidate pool; if touched too early, leave and wait 30 days for respawn validation. | SN-000093-lunar-weapon-spawn-thresholds.md | needs_review |
| OBJ-001755 | Lunar Iron Sword | Base game | Level 6+ individually; level 8+ for best Silent Moons Camp pass | Random leveled Lunar weapon placement at Silent Moons Camp. | Visit/loot Silent Moons Camp at level 8+ for the best overall Lunar weapon candidate pool; if touched too early, leave and wait 30 days for respawn validation. | SN-000093-lunar-weapon-spawn-thresholds.md | needs_review |
| OBJ-001756 | Lunar Iron War Axe | Base game | Level 6+ individually; level 8+ for best Silent Moons Camp pass | Random leveled Lunar weapon placement at Silent Moons Camp. | Visit/loot Silent Moons Camp at level 8+ for the best overall Lunar weapon candidate pool; if touched too early, leave and wait 30 days for respawn validation. | SN-000093-lunar-weapon-spawn-thresholds.md | needs_review |
| OBJ-001757 | Lunar Steel Mace | Base game | Level 8+ | Random leveled Lunar weapon placement at Silent Moons Camp. | Visit/loot Silent Moons Camp at level 8+ for the best overall Lunar weapon candidate pool; if touched too early, leave and wait 30 days for respawn validation. | SN-000093-lunar-weapon-spawn-thresholds.md | needs_review |
| OBJ-001758 | Lunar Steel Sword | Base game | Level 8+ | Random leveled Lunar weapon placement at Silent Moons Camp. | Visit/loot Silent Moons Camp at level 8+ for the best overall Lunar weapon candidate pool; if touched too early, leave and wait 30 days for respawn validation. | SN-000093-lunar-weapon-spawn-thresholds.md | needs_review |
| OBJ-001759 | Lunar Steel War Axe | Base game | Level 8+ | Random leveled Lunar weapon placement at Silent Moons Camp. | Visit/loot Silent Moons Camp at level 8+ for the best overall Lunar weapon candidate pool; if touched too early, leave and wait 30 days for respawn validation. | SN-000093-lunar-weapon-spawn-thresholds.md | needs_review |
| OBJ-001760 | Miraak's Sword | Dragonborn | Level 60+ | Level is determined after Miraak's corpse appears at the end of At the Summit of Apocrypha. | Do not finish the final Miraak battle before level 60 if the route wants maximum Miraak equipment. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001761 | Miraak's Staff | Dragonborn | Level 60+ | Level is determined after Miraak's corpse appears at the end of At the Summit of Apocrypha. | Do not finish the final Miraak battle before level 60 if the route wants maximum Miraak equipment. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001762 | Nightingale Blade | Base game | Level 46+ is the source-listed maximum; level 36-45 is the practical best-use tier if tempering matters | Given by Karliah during Hard Answers. | Before route skeleton, decide whether the project wants maximum source tier at 46+ or the temperable 36-45 tier. Do not reward before that selected window. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001763 | Nightingale Bow | Base game | Level 46+ | Given by Karliah after Blindsighted. | Do not complete the Karliah reward handoff for Blindsighted before level 46. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001764 | The Pale Blade | Base game | Level 27+ | Reward/taken from Ra'jirr during The Pale Lady; TB-012 sources do not settle first-entry locking. | Do not claim/resolve The Pale Blade before level 27; TB-013 should decide whether Frostmere Crypt first entry also needs a warning. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001765 | Miraak (Dragon Priest Mask) | Dragonborn | Level 60+ | Level is determined after Miraak's corpse appears at the end of At the Summit of Apocrypha; armor type depends on higher armor skill, with light armor if tied. | Do not finish the final Miraak battle before level 60 if the route wants maximum Miraak equipment; later route defaults must account for light/heavy/tie behavior. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001766 | Nightingale Armor | Base game | Level 32+ | Level registers at the start of Trinity Restored, not when the armor is received. | Do not start Trinity Restored before level 32 if the route wants maximum Nightingale armor. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001767 | Nightingale Boots | Base game | Level 32+; highest Muffle magnitude has limited practical utility | Level registers at the start of Trinity Restored, not when the armor is received. | Do not start Trinity Restored before level 32 if the route wants maximum Nightingale armor; keep the Muffle utility caveat for final review. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001768 | Nightingale Gloves | Base game | Level 32+ | Level registers at the start of Trinity Restored, not when the armor is received. | Do not start Trinity Restored before level 32 if the route wants maximum Nightingale armor. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001769 | Nightingale Hood | Base game | Level 32+ | Level registers at the start of Trinity Restored, not when the armor is received. | Do not start Trinity Restored before level 32 if the route wants maximum Nightingale armor. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-000198; OBJ-001770 | Shield of Solitude | Base game | Level 40+ | Reward from Falk Firebeard at the end of The Wolf Queen Awakened; associated quest access starts earlier than maximum reward tier. | Do not take the final Falk reward before level 40. The quest can be available earlier, but the reward threshold is 40+. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001771 | Amulet of Articulation | Base game | No level threshold; strongest version is random at any level | Brynjolf gives the amulet after the Guild Master ceremony; all seven player versions are equally likely at all levels. | Hard save before the reward conversation with Brynjolf and reload until the strongest version is awarded, if the route chooses to optimize this random reward. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |
| OBJ-001772 | Mage's Circlet | Base game | Level 25+ | Given by Savos Aren during Good Intentions. | Do not report to Savos for the Good Intentions reward before level 25. | SN-000092-leveled-quest-reward-thresholds-and-locks.md | needs_review |

## TB-013 Cell-Entry Handoff

Confirmed or likely location-entry warnings to harden in TB-013:

| Subject | Handoff |
| --- | --- |
| Chillrend | Confirmed first-entry lock for Riftweald Manor; warning should block entering the house before level 46. |
| Dragonbane | Alduin's Wall page explicitly warns against entering Sky Haven Temple before level 46. |
| Gauldur Blackblade and Gauldur Blackbow | Forbidden Legend page ties boss/item levels to reading Lost Legends or spawning any related dungeon; warning must cover Lost Legends plus Folgunthur, Saarthal, Geirmund's Hall, and Reachwater Rock approaches before level 36. |
| Lunar weapons | Silent Moons Camp has random leveled Lunar placements and a low-level/respawn caveat; warning should keep first collection at level 8+ or require a respawn reset. |
| The Pale Blade | TB-012 confirms the level 27+ reward target but does not settle whether Frostmere Crypt first entry itself locks the item; TB-013 should verify before route placement. |
