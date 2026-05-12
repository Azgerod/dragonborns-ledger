# Session Handoff

Status: updated 2026-05-12.

This file exists to make a session switch cheap. It is a coordination note only; it does not add requirements beyond `docs/guide-specification.md`.

## Current Project State

Phase 1 source-list objective setup is closed. The objective database currently has 2,784 rows, and source notes currently run through `SN-000124-hub-corridor-geography-support.md`.

Phase 2 constraint-table research is reviewed. TB-011 through TB-021 are complete. TB-021A added the first computation-ready coordinate support layer for the location catalog, TB-021B added the hub/corridor geography support layer, and TB-021C added the route-planning index layer.

TB-022 is complete. All 2,784 objective rows now have classified `routing_rigidity` and `route_placement` values, with no remaining `unclassified` values in those fields. Classification notes are in `data/objectives/route-rigidity-classification-notes.md`.

TB-023 is complete. `drafts/route-prototypes/route-anchors-v0.md` now records structural anchors `A00` through `A21`, a level/reward gate register, a branch hard-save register, and explicit handoffs to later route passes.

TB-024 is complete. `drafts/route-prototypes/level-gated-skeleton-v0.md` now assigns anchors to level bands `S00` through `S15`, records mandatory do-not-cross gates, branch-gate placement, progression handoffs, and the Survival Mode geography handoff.

TB-025 is complete. `drafts/route-prototypes/survival-geography-pass-v0.md` now reshapes the level skeleton around Survival Mode corridor planning, prepared sweeps, rest/food/carry/storage/transport support, route-block containers `G00` through `G14`, and a TB-026 handoff.

TB-026 is complete. `drafts/route-prototypes/main-route-prototype-v0.md` now places flexible objective queues into route blocks `G00` through `G14`, records direct geography counts, non-geographic queue handling, support-objective policy, and mandatory holds. `data/route-planning/prototype-objective-block-map.csv` records a one-row-per-objective route-block/disposition/status/threshold/parent/defer assignment for all 2,784 objectives. No `data/objectives/objectives.csv` changes were needed.

TB-027 is complete. `data/constraints/skill-perk-leveling-plan.md` and `drafts/route-prototypes/main-route-prototype-v0.md` now include the progression overlay: route-block skill/crafting slots, bounded underleveled fallbacks before levels 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, and 252, and a conservative Legendary reset baseline. No new gameplay research or objective CSV changes were needed.

TB-028 is complete. `drafts/branch-routes/README.md` now contains the branch decision matrix, branch/default vocabulary, full-branch/reward-branch/trophy-branch/option-list classification, and the TB-029 prototype queue. `data/constraints/quest-conflicts-hard-saves.md` is updated with TB-028 defaults and branch classifications. Route-planning indexes were regenerated so `objective-constraints.csv`, `objective-route-index.csv`, and `prototype-objective-block-map.csv` reflect the new branch/trophy constraints; objective row counts remain stable and `data/objectives/objectives.csv` was not changed.

TB-029 is complete. `drafts/branch-routes/major-faction-branches-v0.md`, `drafts/branch-routes/solstheim-ae-branches-v0.md`, and `drafts/branch-routes/reward-and-trophy-branches-v0.md` now contain grouped branch prototypes with hard-save points, branch-exclusive objective/reward queues, reload points, and downstream warning/checklist/validation handoffs. The prototypes remain route-planning artifacts, not final guide prose. Follow-up cleanup added explicit TB-033 branch-verification expectations, Volkihar representative-radiant escalation language, and `The Gift` spouse-state coordination as a TB-030/TB-032 dependency.

The current next unblocked task is TB-032: add the warning and hard-save layer. TB-030 remains blocked until checklist input is available.

## Restart Checklist

At the start of the next session:

1. Read `AGENTS.md`.
2. Read `docs/guide-specification.md`.
3. Read `docs/development-plan.md`.
4. Read `docs/source-standards.md`.
5. Read `docs/decisions-log.md`.
6. Read `docs/task-board.md`.
7. Read `data/objectives/phase-2-research-inputs.md`.
8. Read `data/constraints/README.md`, then `data/constraints/ae-creation-start-triggers.md`, `data/constraints/leveled-unique-items.md`, `data/constraints/cell-entry-locks.md`, `data/constraints/quest-conflicts-hard-saves.md`, `data/constraints/trophy-dependencies.md`, `data/constraints/npc-dependencies.md`, `data/constraints/bug-prone-quests.md`, `data/constraints/radiant-boundaries.md`, `data/constraints/survival-mode-constraints.md`, and `data/constraints/skill-perk-leveling-plan.md` for Phase 2 overlaps.
9. Read `data/locations/location-catalog.csv`, `data/locations/location-coordinates.csv`, `data/locations/location-coordinate-reconciliation.md`, `data/locations/location-geography.csv`, and `data/locations/location-geography-reconciliation.md` before changing geography-sensitive tasks.
10. Read `data/objectives/route-rigidity-classification-notes.md`, `data/route-planning/README.md`, `data/route-planning/objective-route-index.csv`, `data/route-planning/objective-constraints.csv`, `data/route-planning/prototype-objective-block-map.csv`, `drafts/route-prototypes/route-anchors-v0.md`, `drafts/route-prototypes/level-gated-skeleton-v0.md`, `drafts/route-prototypes/survival-geography-pass-v0.md`, `drafts/route-prototypes/main-route-prototype-v0.md`, `drafts/branch-routes/README.md`, and the TB-029 branch prototype files before TB-032 or later route-placement work.
11. Run `git status --short` and preserve unrelated existing changes.
12. For UESP page fetches, prefer `python3 tools/fetch_uesp.py 'Skyrim:Page Title' --mode wikitext` or `--mode html`; direct raw `curl` may trigger Cloudflare without a browser User-Agent. For Gamemap marker refreshes, use `python3 tools/fetch_uesp_gamemap.py`, regenerate coordinates with `python3 tools/build_location_coordinates.py`, then regenerate geography with `python3 tools/build_location_geography.py`. For route-planning index refreshes, run `python3 tools/build_route_planning_index.py`, `python3 tools/build_prototype_objective_block_map.py`, and optionally `python3 tools/build_route_planning_database.py`.

## Next Task Details

Start TB-032 by adding the warning and hard-save layer. Use `docs/guide-specification.md`, `docs/decisions-log.md`, `data/constraints/quest-conflicts-hard-saves.md`, `data/constraints/bug-prone-quests.md`, `data/constraints/cell-entry-locks.md`, `data/constraints/leveled-unique-items.md`, `data/constraints/trophy-dependencies.md`, `data/constraints/npc-dependencies.md`, `data/constraints/radiant-boundaries.md`, `drafts/route-prototypes/level-gated-skeleton-v0.md`, `drafts/route-prototypes/main-route-prototype-v0.md`, and the TB-029 branch prototype files.

Primary output:

* concise warning/hard-save layer updates in `drafts/route-prototypes/main-route-prototype-v0.md` and/or a dedicated warning-layer section if that better preserves reviewability
* updates to `data/constraints/quest-conflicts-hard-saves.md` only if TB-032 discovers stale handoff wording
* task-board status updates when complete

Research rules:

* Use current online sources if new gameplay facts become necessary, but prefer existing source-backed objective, constraint, route-planning, geography, branch, bug, leveled-reward, cell-entry, and trophy tables for this pass.
* Do not rely on memory for quest conflicts, branch rewards, missable rewards, trophy behavior, bug risks, NPC dependencies, cell-entry locking, radiant availability, or AE branch behavior.
* Mark unknowns explicitly instead of guessing.
* Place warnings exactly where the current prototypes imply they belong; do not create broad generic warnings detached from a route block or branch point.
* Keep warning text concise: hard save here, do not enter/accept/loot/read/turn in yet, choose this reward, stop here, reload here.
* Preserve branch policy and TB-029 branch prototypes. Do not re-choose branch defaults unless a source-backed contradiction is found.
* TB-032 may finalize warning/action wording for Master Criminal, Hircine/Bloated Man's Grotto, Civil War/War Hero, Dawnguard/Volkihar, Dark Brotherhood, Thirsk, Bittercup, and reward branches, but checklist escalation remains TB-030.
* Treat `Battle of the Champions` equipment coverage as source-note dependent until TB-030/TB-033 verifies both equipment-set availability for checklist mapping.
* Do not draft the final guide.

TB-027 support handoffs:

* `data/constraints/skill-perk-leveling-plan.md` is complete for TB-027 and now records operating rules, route-block progression overlay, underleveled fallback register, and Legendary reset baseline.
* `drafts/route-prototypes/main-route-prototype-v0.md` now includes the same progression layer inside the route-block prototype.
* Progression support uses route blocks `G00` through `G14` but does not pick exact trainers, skill-book copies, spell-tome vendors, enchantment source items, alchemy recipes, investment circuit, or checklist cues.
* Preferred repeated Legendary reset pool is Alchemy, Smithing, Enchanting, Alteration, Conjuration, and Illusion; Restoration, Sneak, and Pickpocket are conditional; combat/armor skills are emergency-only; repeated Lockpicking and Speech resets are not baseline.
* Final route validation must still confirm all skills 100 after resets, level 252+, all 251 normal perk ranks, investments, enchantment learning, alchemy effects, practical crafting systems, and Survival bed/storage/carry support.

TB-026 support handoffs:

* `drafts/route-prototypes/main-route-prototype-v0.md` is complete and remains a flexible-objective insertion prototype, not final route prose.
* `data/route-planning/prototype-objective-block-map.csv` is complete and remains the generated TB-026 audit layer. Regenerate it with `python3 tools/build_prototype_objective_block_map.py` after route-index-affecting changes.
* It assigns 447 direct geography `location` rows into route blocks by corridor: G02 62, G03 59, G04 39, G05 38, G06 46, G07 68, G08 64, G11 15, G12 54, and G13 2.
* The Markdown records non-geographic queue treatment for 830 single support candidates, 319 multiple support candidates, 1,089 rows with no route-candidate data, 887 constraint-backed flexible rows, and 1,497 flexible rows without linked constraints; the CSV records individual route blocks, dispositions, statuses, thresholds, parent links, and defer reasons.
* It keeps support candidates conditional: homes, bases, merchants, book copies, spell sources, and property nodes are not automatically available until acquisition/source/storage/prerequisite validation.
* It preserves mandatory holds for Silent Moons/Lunar weapons, Mage's Circlet, The Pale Blade, Nightingale Armor, Forbidden Legend linked dungeons, Shield of Solitude, Chillrend, Dragonbane, Nightingale Blade/Bow, Miraak equipment, Legendary Dragon, Ebony Warrior, and all-perks completion.
* TB-027 added progression support to this frame before branch defaults were chosen. TB-028 has since resolved branch defaults in `drafts/branch-routes/README.md`; source-copy defaults, warning text, and checklist completion remain later work.

TB-025 support handoffs:

* `drafts/route-prototypes/survival-geography-pass-v0.md` is complete and remains a geography planning layer, not route prose.
* The file records terminology, a corridor support register, and prepared sweep requirements using `data/locations/location-geography.csv` and `data/constraints/survival-mode-constraints.md`.
* Route-block containers `G00` through `G14` are the TB-026/TB-027 route frame.
* Later route/progression passes should inspect `objective-route-index.csv`, `objective-constraints.csv`, and canonical objective/constraint rows before placing any objective into a block.
* Candidate bases in the corridor table are possible future logistics nodes, not available storage/rest until acquisition, ownership, safety, and storage validation are confirmed.
* Transport support in the corridor table is carriage/ferry/horse/road context, not automatic fast travel; inland corridors with no local ferry should not be treated as ferry-backed.
* Later route/progression passes should not treat straight-line geography as pathfinding; road, pass, water, quest-state, enemy, weather, and exact entrance validation remain required before prose.

TB-024 support handoffs:

* `drafts/route-prototypes/level-gated-skeleton-v0.md` is complete and remains a broad skeleton, not route prose.
* Skeleton bands are `S00` through `S15`.
* TB-025 consumed the skeleton into `survival-geography-pass-v0.md`; TB-026 placed flexible queues within that frame; TB-027 added progression blocks while preserving the mandatory gate checklist.
* The skeleton keeps source-tier reward policy conservative until a later explicit decision accepts a documented tradeoff.
* Branch defaults and branch prototypes are now captured in TB-028/TB-029; detailed warning prose, skill-reset distribution, and checklist mapping remain assigned to later tasks.

TB-023 support handoffs:

* `drafts/route-prototypes/route-anchors-v0.md` is complete and remains anchor-only.
* Structural anchors are numbered `A00` through `A21`.
* The level/reward gate register is an input to TB-024, not a finished level skeleton.
* The branch and hard-save register records constraint-table hard-save names but does not route branch content.
* Flexible geography is now captured in TB-025; flexible objective insertion is now captured in TB-026; skill reset distribution is now captured at prototype level in TB-027. Branch default selection and branch prototypes are now captured in TB-028/TB-029; warning prose and checklist mapping remain assigned to later tasks.

TB-022 support handoffs:

* `routing_rigidity` counts after TB-022: 1,558 `dependency_flexible`, 842 `region_flexible`, 211 `windowed`, 73 `fixed_late`, 41 `branch_only`, 29 `cleanup_safe`, 14 `excluded_unbounded`, 11 `option_list`, and 5 `fixed_early`.
* `route_placement` counts after TB-022: 2,685 `main_route`, 47 `branch_route`, 27 `appendix`, 14 `excluded`, and 11 `option_list`.
* `data/route-planning/objective-route-index.csv` now has no `needs_classification` rows.
* TB-028 resolved the branch defaults without rewriting objective CSV counts. Use `drafts/branch-routes/README.md` before placing Aetherial, Hircine, Thirsk, Bittercup, Ghosts of the Tribunal, Velehk, Frost, Ralis, or Battle of the Champions choices.
* TB-022 corrected `data/constraints/cell-entry-locks.md` cross-references so Nightingale Armor points to `OBJ-001766` through `OBJ-001769`, and Miraak's corpse-appearance lock includes `OBJ-001596` and `OBJ-001765` instead of Mage's Circlet.

TB-021A/TB-021B/TB-021C support handoffs:

* Phase 2 source-note, bibliography, and explicit objective references were validated during TB-021.
* `data/locations/location-coordinates.csv` contains 472 coordinate rows covering all 467 location catalog rows. It preserves multiple valid entrance markers instead of averaging them.
* `data/locations/location-geography.csv` contains 472 geography rows derived from the coordinate layer. It keeps raw coordinates out of the geography table and stores separate nearest corridor hub, major carriage origin, ferry terminal, inn/rest point, and candidate base fields.
* `data/route-planning/objective-route-index.csv` contains one generated row per objective, joining current classification, geography summaries, support-table candidate counts, and constraint summaries for TB-022 and later route passes.
* `data/route-planning/objective-constraints.csv` contains generated objective-to-constraint links from the reviewed Phase 2 Markdown tables. Inspect the source constraint row before turning any generated summary into route prose.
* `tools/build_route_planning_database.py` can create `data/route-planning/route-planning.sqlite` for local SQL queries; the SQLite file is generated output and ignored by git.
* Compute straight-line distances only when both rows have numeric `x`/`y` values and the same `coordinate_worldspace`. Do not compare Solstheim, Soul Cairn, Forgotten Vale, Skuldafn, Apocrypha, Deadlands, or other separate-worldspace points directly against Skyrim exterior points.
* Rows marked `proxy_marker` or `proxy_nearby_landmark` are good enough for coarse clustering but still need route validation before precise access-path decisions.
* Rows marked `unmapped_no_marker` or `unmapped_worldspace` are not distance-comparable until a later plugin-data extraction or manual route validation supplies a defensible point.
* TB-021B added `worldspace_access_model`, `transport_access_flags`, `cold_risk`, `barrier_flags`, and `geography_confidence`. These are route filters, not final pathfinding; road, pass, water, quest-state, enemy, and exact access validation still belongs to later route passes.
* Companions Hired Muscle should be accepted if the early seed offers it, but the guide should not require a new-game restart solely to force that representative radiant type.
* Thieves Guild 125 side jobs remain a source-backed completionist counter candidate pending checklist mapping.
* TB-028/TB-029 set Volkihar representative radiants and `New Allegiances` to branch-prototype coverage only. TB-030 may escalate representative radiants or all three named `New Allegiances` conversions only if checklist mapping creates named-variant or all-variant requirements. `The Gift` also needs spouse-state coordination before final branch routing.

Earlier Phase 2 handoffs to keep in view:

* Thieves Guild has a hard 20-job restoration gate and a source-backed 125-job Guild display/safe boundary; TB-030 should decide checklist treatment.
* Dawnguard Lost Relic may require semi-random side-radiant fillers; route phases should track actual fillers while cycling for all three relics.
* No-journal representative activity targets should be chosen with Survival Mode, thaneship, relationship, and economy overlap in mind.
* TB-020 marked all exploit-adjacent leveling/crafting accelerators as excluded baseline or deferred decisions; TB-021 confirmed that this matches the specification and decisions log.

## Validation Before Handoff

Run at least:

```bash
python3 tools/validate_all.py
git diff --check
```

If source notes or bibliography rows are added, also run the source-workflow validator directly if `tools/validate_all.py` output is not enough to identify source issues.
