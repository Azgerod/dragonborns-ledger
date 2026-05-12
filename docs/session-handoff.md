# Session Handoff

Status: updated 2026-05-12.

This file exists to make a session switch cheap. It is a coordination note only; it does not add requirements beyond `docs/guide-specification.md`.

## Current Project State

Phase 1 source-list objective setup is closed. The objective database currently has 2,784 rows, and source notes currently run through `SN-000124-hub-corridor-geography-support.md`.

Phase 2 constraint-table research is reviewed. TB-011 through TB-021 are complete. TB-021A added the first computation-ready coordinate support layer for the location catalog, TB-021B added the hub/corridor geography support layer, and TB-021C added the route-planning index layer.

TB-022 is complete. All 2,784 objective rows now have classified `routing_rigidity` and `route_placement` values, with no remaining `unclassified` values in those fields. Classification notes are in `data/objectives/route-rigidity-classification-notes.md`.

The current next task is TB-023: build route anchors v0.

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
10. Read `data/objectives/route-rigidity-classification-notes.md`, `data/route-planning/README.md`, `data/route-planning/objective-route-index.csv`, and `data/route-planning/objective-constraints.csv` before TB-023 or later route-placement work.
11. Run `git status --short` and preserve unrelated existing changes.
12. For UESP page fetches, prefer `python3 tools/fetch_uesp.py 'Skyrim:Page Title' --mode wikitext` or `--mode html`; direct raw `curl` may trigger Cloudflare without a browser User-Agent. For Gamemap marker refreshes, use `python3 tools/fetch_uesp_gamemap.py`, regenerate coordinates with `python3 tools/build_location_coordinates.py`, then regenerate geography with `python3 tools/build_location_geography.py`. For route-planning index refreshes, run `python3 tools/build_route_planning_index.py` and optionally `python3 tools/build_route_planning_database.py`.

## Next Task Details

Start TB-023 by building `drafts/route-prototypes/route-anchors-v0.md` as an anchor-only planning artifact. Use `data/objectives/objectives.csv`, `data/objectives/route-rigidity-classification-notes.md`, `data/route-planning/objective-route-index.csv`, `data/route-planning/objective-constraints.csv`, and the Phase 2 constraint tables to identify route anchors from `fixed_early`, `fixed_late`, `windowed`, `branch_only`, and high-severity constraint-backed rows.

Primary output:

* `drafts/route-prototypes/route-anchors-v0.md`
* task-board status updates when complete

Research rules:

* Use current online sources if new gameplay facts become necessary, but prefer existing source-backed constraint tables for this anchor pass.
* Do not rely on memory for cell-entry locking, leveled item thresholds, conflicts, bugs, trophy behavior, missability, radiant availability, Survival Mode mechanics, perk prerequisites, crafting unlocks, or skill-system behavior.
* Mark unknowns explicitly instead of guessing.
* Do not write detailed route steps.
* Do not draft the final guide.

TB-022 support handoffs:

* `routing_rigidity` counts after TB-022: 1,558 `dependency_flexible`, 842 `region_flexible`, 211 `windowed`, 73 `fixed_late`, 41 `branch_only`, 29 `cleanup_safe`, 14 `excluded_unbounded`, 11 `option_list`, and 5 `fixed_early`.
* `route_placement` counts after TB-022: 2,685 `main_route`, 47 `branch_route`, 27 `appendix`, 14 `excluded`, and 11 `option_list`.
* `data/route-planning/objective-route-index.csv` now has no `needs_classification` rows.
* Unresolved branch-default rows are intentionally handed to TB-028; TB-023 should not choose canonical Aetherial, Hircine, Thirsk, Bittercup, or similar defaults while building anchors.
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
