# Session Handoff

Status: updated 2026-05-12.

This file exists to make a session switch cheap. It is a coordination note only; it does not add requirements beyond `docs/guide-specification.md`.

## Current Project State

Phase 1 source-list objective setup is closed. The objective database currently has 2,789 rows, and source notes currently run through `SN-000128-location-route-validation.md`.

Phase 2 constraint-table research is reviewed. TB-011 through TB-021 are complete. TB-021A added the first computation-ready coordinate support layer for the location catalog, TB-021B added the hub/corridor geography support layer, and TB-021C added the route-planning index layer.

TB-022 is complete. All current objective rows have classified `routing_rigidity` and `route_placement` values, with no remaining `unclassified` values in those fields. Classification notes are in `data/objectives/route-rigidity-classification-notes.md`; after TB-031F, generated route indexes cover 2,789 objectives.

TB-023 is complete. `drafts/route-prototypes/route-anchors-v0.md` now records structural anchors `A00` through `A21`, a level/reward gate register, a branch hard-save register, and explicit handoffs to later route passes.

TB-024 is complete. `drafts/route-prototypes/level-gated-skeleton-v0.md` now assigns anchors to level bands `S00` through `S15`, records mandatory do-not-cross gates, branch-gate placement, progression handoffs, and the Survival Mode geography handoff.

TB-025 is complete. `drafts/route-prototypes/survival-geography-pass-v0.md` now reshapes the level skeleton around Survival Mode corridor planning, prepared sweeps, rest/food/carry/storage/transport support, route-block containers `G00` through `G14`, and a TB-026 handoff.

TB-026 is complete. `drafts/route-prototypes/main-route-prototype-v0.md` now places flexible objective queues into route blocks `G00` through `G14`, records direct geography counts, non-geographic queue handling, support-objective policy, and mandatory holds. `data/route-planning/prototype-objective-block-map.csv` records a one-row-per-objective route-block/disposition/status/threshold/parent/defer assignment for all 2,789 current objectives.

TB-027 is complete. `data/constraints/skill-perk-leveling-plan.md` and `drafts/route-prototypes/main-route-prototype-v0.md` now include the progression overlay: route-block skill/crafting slots, bounded underleveled fallbacks before levels 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, and 252, and a conservative Legendary reset baseline. No new gameplay research or objective CSV changes were needed.

TB-028 is complete. `drafts/branch-routes/README.md` now contains the branch decision matrix, branch/default vocabulary, full-branch/reward-branch/trophy-branch/option-list classification, and the TB-029 prototype queue. `data/constraints/quest-conflicts-hard-saves.md` is updated with TB-028 defaults and branch classifications. Route-planning indexes were regenerated so `objective-constraints.csv`, `objective-route-index.csv`, and `prototype-objective-block-map.csv` reflect the new branch/trophy constraints; objective row counts remain stable and `data/objectives/objectives.csv` was not changed.

TB-029 is complete. `drafts/branch-routes/major-faction-branches-v0.md`, `drafts/branch-routes/solstheim-ae-branches-v0.md`, and `drafts/branch-routes/reward-and-trophy-branches-v0.md` now contain grouped branch prototypes with hard-save points, branch-exclusive objective/reward queues, reload points, and downstream warning/checklist/validation handoffs. The prototypes remain route-planning artifacts, not final guide prose. Follow-up cleanup added explicit TB-033 branch-verification expectations, Volkihar representative-radiant escalation language, and `The Gift` spouse-state coordination as a TB-031D/TB-032 dependency.

TB-030 is complete. `data/checklist-mapping/raw/Skyrim Checklist.xlsx` is the tracked raw checklist snapshot. `tools/build_checklist_coverage.py` generates `data/checklist-mapping/coverage-matrix.csv`, and `data/checklist-mapping/checklist-coverage-summary.md` records the intake counts and remaining explicit holds. After TB-031G, the matrix has 3,697 spreadsheet rows: 3,085 mapped to main-route prototype handling, 32 branch prototype rows, 75 option-list rows, 107 appendix rows, 320 explicit exclusions, and 78 typed source-readiness holds.

TB-031 is complete. `tools/validate_coverage.py` now validates the real 24-column checklist coverage matrix, including unique checklist IDs, allowed mapping/status/match values, ID/source/block formats, status-specific blank-field rules, and required branch/exclusion/review fields. `tools/build_checklist_coverage.py` now marks non-investable merchant appendix rows with explicit `support_table_only` metadata instead of leaving them structurally unmatched.

TB-031A is complete. `data/checklist-mapping/checklist-scope-review.md` records the scope decision: all 312 broad regular-book rows from the raw checklist are explicit exclusions from required route and appendix coverage, with `match_source=book_scope_review`. No `scope_review_required` rows remain.

TB-031B is complete. `data/checklist-mapping/checklist-manual-review.md` records the manual-review resolution. `coverage-matrix.csv` now has no `manual_review_required` or `unmatched` rows. 195 formerly manual rows map to existing source-backed objective/support handling, and 90 checklist-only rows are typed `source_readiness_required` holds with named owners.

TB-031C is complete. `data/checklist-mapping/checklist-escalation-decisions.md` records no all-target radiant escalation, required Thieves Guild 125-job counter coverage, canonical/default promotions, and branch-only holds. `coverage-matrix.csv` now has 3,076 main-route prototype rows, 30 branch prototype rows, 75 option-list rows, 107 appendix rows, 319 explicit exclusions, and 90 typed source-readiness holds. TB-031C also promoted canonical Thirsk Nord-side rows, Aetherial Crown, and Ring of Hircine to main-route handling, and moved `The Pit` to the Bittercup Power branch.

TB-031D is complete. `data/route-planning/route-default-decisions.md` records route-shaping defaults for first safe storage, main base/home, property service timing, transport infrastructure, spouse/children/stewards/farm steward, Black Book powers, final transformation state, and representative no-journal activity/favor targets. Default-sensitive source notes, constraints, support rows, generated owner labels, and checklist coverage were updated.

TB-031E is complete. `data/constraints/progression-source-selection.md` and generated `data/constraints/progression-source-selections.csv` record selected skill-book copies/read policy, spell-tome source defaults, enchantment source families, alchemy source methods, merchant investment circuit rules, crafting outputs/material staging, training blocks, Legendary reset distribution, Oghma timing, and exploit exclusions. `tools/build_checklist_coverage.py` now maps the TB-031E-owned `Damage Stamina` and `Kesh Fiber (AE)` aliases to source-backed objectives. `coverage-matrix.csv` now has 3,081 main-route prototype rows, 30 branch prototype rows, 75 option-list rows, 107 appendix rows, 319 explicit exclusions, and 85 typed source-readiness holds.

TB-031F is complete. `data/checklist-mapping/counter-coverage-plan.md` and `SN-000127-checklist-counter-route-mechanics.md` record counter/action rules for trophy counters, Thieves Guild side jobs, Dawnguard `Lost Relic`, Fishing, work actions, support-only lumber/milling treatment, and trophy-pop fallbacks. TB-031F also added `OBJ-002785` through `OBJ-002789`, mapped `Scare My Enemy` to Hired Muscle, updated the Paarthurnax/Blades branch prototype, and regenerated route/checklist indexes.

TB-031G is complete. `data/locations/location-route-validation.md` and `SN-000128-location-route-validation.md` record Delver/Explorer mechanics, normal clear-trigger policy, Angarvunde/Mistwatch exceptions, duplicate and secondary marker treatment, AE content-location handling, coordinate exception rules, separate-worldspace/manual geography handling, and the `The Chill*` official-scope exclusion. TB-031G updated location/objective support rows, regenerated route/checklist indexes, and reduced source-readiness holds to 78.

TB-031H is complete. `docs/source-objective-readiness-audit.md` records the source/objective/support-table/generated-index readiness audit. `sources/source-notes/README.md` now defines source-note status semantics, generated route/checklist/progression outputs no longer name TB-031H as a future owner, and the remaining 78 `source_readiness_required` rows are assigned to TB-036.

The current next task is TB-031I: close the final Phase 10 deferred-work audit before TB-032 starts.

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
9. Read `data/locations/location-catalog.csv`, `data/locations/location-coordinates.csv`, `data/locations/location-coordinate-reconciliation.md`, `data/locations/location-geography.csv`, `data/locations/location-geography-reconciliation.md`, and `data/locations/location-route-validation.md` before changing geography-sensitive tasks.
10. Read `data/checklist-mapping/README.md`, `data/checklist-mapping/checklist-coverage-strategy.md`, `data/checklist-mapping/checklist-coverage-summary.md`, `data/checklist-mapping/checklist-scope-review.md`, `data/checklist-mapping/checklist-manual-review.md`, `data/checklist-mapping/checklist-escalation-decisions.md`, `data/checklist-mapping/counter-coverage-plan.md`, `data/route-planning/route-default-decisions.md`, `data/constraints/progression-source-selection.md`, `data/constraints/progression-source-selections.csv`, `data/checklist-mapping/coverage-matrix.csv`, `docs/source-objective-readiness-audit.md`, and `docs/deferred-work-audit.md` before TB-031I or later checklist/coverage work.
11. Read `data/objectives/route-rigidity-classification-notes.md`, `data/route-planning/README.md`, `data/route-planning/objective-route-index.csv`, `data/route-planning/objective-constraints.csv`, `data/route-planning/prototype-objective-block-map.csv`, `drafts/route-prototypes/route-anchors-v0.md`, `drafts/route-prototypes/level-gated-skeleton-v0.md`, `drafts/route-prototypes/survival-geography-pass-v0.md`, `drafts/route-prototypes/main-route-prototype-v0.md`, `drafts/branch-routes/README.md`, and the TB-029 branch prototype files before TB-032 or later route-placement work.
12. Run `git status --short` and preserve unrelated existing changes.
13. For UESP page fetches, prefer `python3 tools/fetch_uesp.py 'Skyrim:Page Title' --mode wikitext` or `--mode html`; direct raw `curl` may trigger Cloudflare without a browser User-Agent. For Gamemap marker refreshes, use `python3 tools/fetch_uesp_gamemap.py`, regenerate coordinates with `python3 tools/build_location_coordinates.py`, then regenerate geography with `python3 tools/build_location_geography.py`. For route-planning index refreshes, run `python3 tools/build_route_planning_index.py`, `python3 tools/build_prototype_objective_block_map.py`, and optionally `python3 tools/build_route_planning_database.py`.

## Next Task Details

Start TB-031I by re-scanning deferral language and closing the Phase 10 deferred-work audit before TB-032 warning placement starts. Use `docs/deferred-work-audit.md`, `docs/source-objective-readiness-audit.md`, `docs/task-board.md`, `docs/session-handoff.md`, `data/checklist-mapping/checklist-coverage-summary.md`, `data/checklist-mapping/checklist-coverage-strategy.md`, `data/checklist-mapping/coverage-matrix.csv`, `data/route-planning/README.md`, `data/route-planning/prototype-objective-block-map.csv`, current route prototypes, current branch prototypes, and `docs/source-standards.md`.

Primary output:

* final updates to `docs/deferred-work-audit.md`
* targeted wording cleanup where active prose still hides a route-affecting deferral behind generic `later`, `manual validation`, `needs review`, `source readiness`, or stale task-owner language
* task-board and handoff status updates when complete
* regenerated route/checklist indexes only if canonical metadata changes require it

TB-031I rules:

* Treat TB-031A through TB-031H as complete unless the scan finds a concrete inconsistency.
* For each active deferral phrase, confirm it is completed, assigned to a specific later task with a reason, or recorded as an unresolved risk.
* Distinguish historical task-board/session-handoff history from current unresolved work.
* Do not do broad gameplay research. If a concrete row needs a gameplay correction, source-check only that row and cite it under `docs/source-standards.md`.
* Run `python3 tools/build_checklist_coverage.py`, `python3 tools/validate_all.py`, and `git diff --check`; run route/progression generators first only if metadata changes affect generated labels.

TB-032 should wait until TB-031I is complete. When starting TB-032, use the warning-layer rules from the task board and do not re-open already resolved checklist/default/progression/location/readiness buckets inside warning prose.

TB-027 support handoffs:

* `data/constraints/skill-perk-leveling-plan.md` is complete for TB-027 and now records operating rules, route-block progression overlay, underleveled fallback register, Legendary reset baseline, and the TB-031E source-selection overlay.
* `drafts/route-prototypes/main-route-prototype-v0.md` now includes the same progression layer inside the route-block prototype.
* `data/constraints/progression-source-selection.md` and `data/constraints/progression-source-selections.csv` pick trainer blocks, skill-book copy defaults, spell-tome sources, enchantment source families, alchemy source methods, investment circuit rules, crafting outputs, Oghma timing, and reset distribution.
* Preferred repeated Legendary reset pool is Alchemy, Smithing, Enchanting, Alteration, Conjuration, and Illusion; Restoration, Sneak, and Pickpocket are conditional; combat/armor skills are emergency-only; repeated Lockpicking and Speech resets are not baseline.
* Final route validation must still confirm exact numeric reset counts, all skills 100 after resets, level 252+, all 251 normal perk ranks, investments, enchantment learning, alchemy effects, practical crafting systems, and Survival bed/storage/carry support.

TB-026 support handoffs:

* `drafts/route-prototypes/main-route-prototype-v0.md` is complete and remains a flexible-objective insertion prototype, not final route prose.
* `data/route-planning/prototype-objective-block-map.csv` is complete and remains the generated TB-026 audit layer. Regenerate it with `python3 tools/build_prototype_objective_block_map.py` after route-index-affecting changes.
* It assigns 447 direct geography `location` rows into route blocks by corridor: G02 62, G03 59, G04 39, G05 38, G06 46, G07 68, G08 64, G11 15, G12 54, and G13 2.
* The Markdown records non-geographic queue treatment for 830 single support candidates, 319 multiple support candidates, 1,098 rows with no route-candidate data, 1,082 constraint-backed flexible rows, and 1,534 flexible rows without linked constraints; the CSV records individual route blocks, dispositions, statuses, thresholds, parent links, and defer reasons.
* It keeps support candidates conditional: homes, bases, merchants, book copies, spell sources, and property nodes are not automatically available until acquisition/source/storage/prerequisite validation.
* It preserves mandatory holds for Silent Moons/Lunar weapons, Mage's Circlet, The Pale Blade, Nightingale Armor, Forbidden Legend linked dungeons, Shield of Solitude, Chillrend, Dragonbane, Nightingale Blade/Bow, Miraak equipment, Legendary Dragon, Ebony Warrior, and all-perks completion.
* TB-027 added progression support to this frame before branch defaults were chosen. TB-028 has since resolved branch defaults in `drafts/branch-routes/README.md`, TB-031E has resolved progression source-copy/source-family defaults, TB-031F has resolved counter mechanics, and TB-031G has resolved location route-validation mechanics. Warning text, final path placement, and final checklist completion remain later work.

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
* Branch defaults and branch prototypes are now captured in TB-028/TB-029, progression source/reset distribution is captured in TB-031E, counter mechanics are captured in TB-031F, and location route-validation mechanics are captured in TB-031G; detailed warning prose, final route placement, and final checklist mapping remain assigned to later tasks.

TB-023 support handoffs:

* `drafts/route-prototypes/route-anchors-v0.md` is complete and remains anchor-only.
* Structural anchors are numbered `A00` through `A21`.
* The level/reward gate register is an input to TB-024, not a finished level skeleton.
* The branch and hard-save register records constraint-table hard-save names but does not route branch content.
* Flexible geography is now captured in TB-025; flexible objective insertion is now captured in TB-026; progression/reset distribution is now captured in TB-027/TB-031E. Branch default selection and branch prototypes are now captured in TB-028/TB-029, counter mechanics are captured in TB-031F, and location route-validation mechanics are captured in TB-031G; warning prose, final route placement, and final checklist mapping remain assigned to later tasks.

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
* Thieves Guild 125 side jobs are required completionist counter coverage. TB-031F chose city-tally, rejection/reload, Raven Rock/Riften, job-type, and total-counter policy; TB-033 still validates final restoration/display/safe state.
* TB-031C kept Volkihar representative radiants and `New Allegiances` at one branch instance/conversion. TB-031D recommends Ysolda for the spouse default; TB-032 must verify the branch save setup for `The Gift` or mark that branch quest conditional.

Earlier Phase 2 handoffs to keep in view:

* Thieves Guild has a hard 20-job restoration gate and a source-backed 125-job Guild display/safe boundary. TB-031C decided the 125-job boundary is required completionist counter coverage; TB-031F now records the job mix, rejection policy, Raven Rock/Riften handling, and counter tracking rules.
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
