# Aggregate Row Reconciliation

Status: TB-007G4 through TB-009F aggregate reconciliation current; downstream validation pending.

This audit closes the TB-007G aggregate/member-expansion phase and records the TB-009 skill/crafting reconciliation update. It does not introduce new gameplay claims. It classifies broad objective rows that might otherwise look like unfinished placeholders and states whether they are expanded, linked to a support table, intentionally parent-only, or explicitly delegated to a downstream task.

## Audit Rule

Rows were reviewed when they matched one or more of these markers:

* parent/package rows;
* `*_set`, `*_option*`, `*_system`, `*_pool`, or `*_parent` subcategories;
* trophy tracker rows;
* radiant placeholder or representative rows;
* rows whose notes already say parent, placeholder, candidate table, option table, or not duplicated.

The objective database remains authoritative for routed completion units. Support tables hold member/candidate/detail rows when one objective row would otherwise become too wide or repetitive.

## Resolution Matrix

Counts below are bucket counts, not a unique-row total, because a few rows legitimately belong to more than one bucket.

| Bucket | Rows | Resolution | Remaining action |
| --- | ---: | --- | --- |
| AE package parent rows | 74 | `data/objectives/ae-creation-manifest.md` maps each package parent to child quest, property, pet/mount, system, or item parent rows. Package rows stay parent-only package coverage records. | Exact triggers, gates, bugs, conflicts, and route placement remain in TB-011 and later constraint/route passes. |
| AE item, spell, consumable, material, crafting, armor, and unique-equipment parent rows | 67 | Expanded into `data/items/ae-item-members.csv`; summarized in `data/items/ae-item-member-reconciliation.md`. | Acquisition choice, crafting timing, unique preservation, checklist mapping, and power-curve validation remain downstream. |
| Book/document title coverage | 0 aggregate rows open | Current book/document objectives are title-level rows with acquisition/location candidates in `data/books/`; `data/books/book-document-reconciliation.md` reports no aggregate placeholder rows. | Re-open only if checklist mapping introduces checklist-only book/note titles not already represented. |
| Collectible set parent rows | 14 | Set parents are either followed by member objective rows, represented by existing title/artifact rows, or intentionally count-based. Dragon Priest Masks, Jiub pages, and Black Books avoid duplicate member rows because those members already exist elsewhere. | Route order, location synchronization, ownership/crime handling, bugs, and checklist mapping remain downstream. |
| Property, home, furnishing, service, and farm detail rows | 36 | Linked to `data/properties/property-details.csv`; summarized in `data/properties/property-detail-reconciliation.md`. | Safe-storage approval, display choices, economy/material timing, family defaults, bugs, and route timing remain downstream. |
| NPC relationship, household role, follower, pet, mount, housecarl, and thaneship option/set rows | 13 | Candidate/option coverage lives in `data/npc/relationship-options.csv`; thaneship and player-housecarl parent rows have child objective rows. | Default recommendations, NPC safety, quest conflicts, and checklist mapping remain downstream. |
| Trophy tracker rows | 15 | Parent-only tracker rows are intentional because trophies are validation/checklist overlays, not member lists. | PS4 trophy behavior, timing, and missability validation remain in TB-015. |
| Radiant placeholder, required-gate, representative, and property-defense rows | 58 | Explicitly delegated to TB-018. These are not silently unexpanded; their finite/representative/excluded boundary requires a dedicated radiant pass. | TB-018 must classify required, finite, representative, repeatable, appendix-only, and excluded radiant handling. |
| Leveled reward parent rows | 23 | Explicitly delegated to TB-012/TB-013. These rows track reward-tier and lock-timing questions, not missing item members. | Validate maximum thresholds, pickup/cell-entry locking, duplicate unique-item links, and route-safe acquisition timing. |
| Spell/power choice and pool rows outside AE item expansion | 12 | Parent-only choice/pool rows are intentional for dragon-soul economy, Standing Stone choices, Black Book choices, Paarthurnax meditation, Nightingale Agent powers, and werewolf totems. | Default recommendations, changeability, route timing, and checklist cues remain in power/route/constraint passes. |
| Civil War phase parent rows | 2 | Imperial and Stormcloak phase parent rows have child quest rows. The parent rows track phase structure and Season Unending variability. | Civil War, War Hero, Season Unending, branch, and Jarl-state handling remain in TB-014/TB-015 and branch-route passes. |
| AE/system rows that are not finite member lists | 2 | Plague of the Dead zombie-system and Goldenhills farm-system rows are covered by existing child/item/property data and downstream constraint tasks. | Survival, bug, start-trigger, repeatability, and route-boundary validation remain downstream. |
| Location coverage | 0 current aggregate rows open | TB-008A through TB-008D added source-list location catalog coverage for clearable, discoverable, and AE Creation place rows. | Checklist-only location exceptions remain deferred until external checklist mapping. |
| Skill/perk, enchantment, alchemy, merchant, and practical crafting coverage | 0 current aggregate rows open | TB-009A through TB-009F added support-table coverage and a closeout review for skill trees, individual perk ranks, enchantment learning, alchemy effect discovery, merchant investments, and practical crafting systems. | Recipe selection, perk allocation, source-item selection, work/activity radiant classification, and crafting power-curve timing remain TB-018/TB-020/downstream work. |

## Explicit Parent-Only Rows

Some parent rows should remain parent rows even after all member/detail tables exist:

| Row type | Why parent-only is correct |
| --- | --- |
| AE package rows | The package itself is a coverage unit; child rows and member tables hold the route-relevant gameplay surface. |
| Trophy tracker rows | Trophy validation cuts across quests/items/locations and should not duplicate every contributing objective. |
| Count-based collectible rows | Crimson Nirnroot tracks the required count; the route later chooses a practical path rather than treating every plant as a completion objective. |
| Duplicate-coverage collectible parents | Dragon Priest Masks, Jiub pages, and Black Books already have individual artifact/title/power rows elsewhere. |
| Choice/power-system rows | Standing Stones, Black Books, Paarthurnax meditation, Nightingale Agent, and werewolf totems need default recommendations and changeability validation rather than member pickup expansion. |
| Civil War phase rows | The phase parent captures variable hold-recapture structure; child quest rows already exist. |

## No Silent Placeholders

After this reconciliation, no known finite aggregate row is being carried forward as an unnamed placeholder. Each broad row is in one of these states:

* expanded into member/detail rows;
* linked to an option/candidate table;
* intentionally parent-only with a reason;
* explicitly delegated to a named downstream task.

The remaining objective-database work before TB-010 is not a hidden aggregate/member gap. TB-010 can now run the broader objective database review.
