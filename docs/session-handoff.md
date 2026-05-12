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

TB-026 is complete. `drafts/route-prototypes/main-route-prototype-v0.md` now places flexible objective queues into route blocks `G00` through `G14`, records direct geography counts, non-geographic queue handling, support-objective policy, mandatory holds, and a TB-027 handoff. `data/route-planning/prototype-objective-block-map.csv` records a one-row-per-objective route-block/disposition/status/threshold/parent/defer assignment for all 2,784 objectives. No `data/objectives/objectives.csv` changes were needed.

The current next task is TB-027: integrate crafting, skills, perks, and grind blocks.

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
10. Read `data/objectives/route-rigidity-classification-notes.md`, `data/route-planning/README.md`, `data/route-planning/objective-route-index.csv`, `data/route-planning/objective-constraints.csv`, `data/route-planning/prototype-objective-block-map.csv`, `drafts/route-prototypes/route-anchors-v0.md`, `drafts/route-prototypes/level-gated-skeleton-v0.md`, `drafts/route-prototypes/survival-geography-pass-v0.md`, and `drafts/route-prototypes/main-route-prototype-v0.md` before TB-027 or later route-placement work.
11. Run `git status --short` and preserve unrelated existing changes.
12. For UESP page fetches, prefer `python3 tools/fetch_uesp.py 'Skyrim:Page Title' --mode wikitext` or `--mode html`; direct raw `curl` may trigger Cloudflare without a browser User-Agent. For Gamemap marker refreshes, use `python3 tools/fetch_uesp_gamemap.py`, regenerate coordinates with `python3 tools/build_location_coordinates.py`, then regenerate geography with `python3 tools/build_location_geography.py`. For route-planning index refreshes, run `python3 tools/build_route_planning_index.py`, `python3 tools/build_prototype_objective_block_map.py`, and optionally `python3 tools/build_route_planning_database.py`.

## Next Task Details

Start TB-027 by integrating crafting, skills, perks, and grind blocks into the progression layer. Use `data/constraints/skill-perk-leveling-plan.md`, `drafts/route-prototypes/main-route-prototype-v0.md`, `drafts/route-prototypes/survival-geography-pass-v0.md`, `drafts/route-prototypes/level-gated-skeleton-v0.md`, `data/route-planning/objective-route-index.csv`, `data/route-planning/objective-constraints.csv`, `data/route-planning/prototype-objective-block-map.csv`, and the relevant Phase 2 constraint tables.

Primary output:

* `drafts/route-prototypes/main-route-prototype-v0.md`
* `data/constraints/skill-perk-leveling-plan.md`
* `data/objectives/objectives.csv`, only if TB-027 needs source-backed canonical route-placement or rigidity refinements
* task-board status updates when complete

Research rules:

* Use current online sources if new gameplay facts become necessary, but prefer existing source-backed objective, constraint, route-planning, geography, and progression tables for this pass.
* Do not rely on memory for cell-entry locking, leveled item thresholds, conflicts, bugs, trophy behavior, missability, radiant availability, Survival Mode mechanics, perk prerequisites, crafting unlocks, or skill-system behavior.
* Mark unknowns explicitly instead of guessing.
* Use route-block containers `G00` through `G14` as the placement frame for training, crafting, shopping, skill-reset, and grind blocks.
* Include bounded fallback blocks for underleveled checkpoints before levels 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, and 252.
* Preserve the mandatory do-not-cross gates in `level-gated-skeleton-v0.md`.
* Preserve Survival support for rest, food, carry, storage, transport, warmth, and recovery after skill resets.
* Preserve unique-item ownership and the no-unique-disenchant baseline unless the specification explicitly changes.
* Preserve the gradual difficulty curve; do not rush overpowered crafting, gear, or exploit-adjacent leveling as the baseline.
* Preserve TB-023/TB-024/TB-025/TB-026 explicit deferrals for Hircine, Aetherial, Thirsk, Bittercup, Velehk Sain, Ghosts of the Tribunal, branch defaults, detailed warning prose, and checklist mapping.
* Do not write detailed black-box route steps beyond prototype-level section/block placement.
* Do not draft the final guide.

TB-026 support handoffs:

* `drafts/route-prototypes/main-route-prototype-v0.md` is complete and remains a flexible-objective insertion prototype, not final route prose.
* `data/route-planning/prototype-objective-block-map.csv` is complete and remains the generated TB-026 audit layer. Regenerate it with `python3 tools/build_prototype_objective_block_map.py` after route-index-affecting changes.
* It assigns 447 direct geography `location` rows into route blocks by corridor: G02 62, G03 59, G04 39, G05 38, G06 46, G07 68, G08 64, G11 15, G12 54, and G13 2.
* The Markdown records non-geographic queue treatment for 830 single support candidates, 319 multiple support candidates, 1,089 rows with no route-candidate data, 887 constraint-backed flexible rows, and 1,497 flexible rows without linked constraints; the CSV records individual route blocks, dispositions, statuses, thresholds, parent links, and defer reasons.
* It keeps support candidates conditional: homes, bases, merchants, book copies, spell sources, and property nodes are not automatically available until acquisition/source/storage/prerequisite validation.
* It preserves mandatory holds for Silent Moons/Lunar weapons, Mage's Circlet, The Pale Blade, Nightingale Armor, Forbidden Legend linked dungeons, Shield of Solitude, Chillrend, Dragonbane, Nightingale Blade/Bow, Miraak equipment, Legendary Dragon, Ebony Warrior, and all-perks completion.
* TB-027 should add progression support to this frame without choosing branch defaults, source-copy defaults, warning text, or checklist completion.

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
* TB-025 consumed the skeleton into `survival-geography-pass-v0.md`; TB-026 placed flexible queues within that frame; TB-027 may add progression blocks only when the mandatory gate checklist remains intact.
* The skeleton keeps source-tier reward policy conservative until a later explicit decision accepts a documented tradeoff.
* Branch defaults, detailed warning prose, skill-reset distribution, and checklist mapping remain assigned to later tasks.

TB-023 support handoffs:

* `drafts/route-prototypes/route-anchors-v0.md` is complete and remains anchor-only.
* Structural anchors are numbered `A00` through `A21`.
* The level/reward gate register is an input to TB-024, not a finished level skeleton.
* The branch and hard-save register records constraint-table hard-save names but does not route branch content.
* Flexible geography is now captured in TB-025; flexible objective insertion is now captured in TB-026; skill reset distribution, branch default selection, warning prose, and checklist mapping remain assigned to later tasks.

TB-022 support handoffs:

* `routing_rigidity` counts after TB-022: 1,558 `dependency_flexible`, 842 `region_flexible`, 211 `windowed`, 73 `fixed_late`, 41 `branch_only`, 29 `cleanup_safe`, 14 `excluded_unbounded`, 11 `option_list`, and 5 `fixed_early`.
* `route_placement` counts after TB-022: 2,685 `main_route`, 47 `branch_route`, 27 `appendix`, 14 `excluded`, and 11 `option_list`.
* `data/route-planning/objective-route-index.csv` now has no `needs_classification` rows.
* Unresolved branch-default rows are intentionally handed to TB-028; TB-027 and later route work should not choose canonical Aetherial, Hircine, Thirsk, Bittercup, or similar defaults before the branch matrix pass.
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
* Volkihar `New Allegiances` branch depth remains a TB-028 decision.

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
