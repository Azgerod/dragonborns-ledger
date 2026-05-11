# Development Plan for Building the Guide

This file is the extracted development plan. `docs/guide-specification.md` remains the canonical project specification for guide requirements, while this file is the canonical home for the development sequence.

Because this guide is large, the writer should not attempt to write the final itinerary in one pass. The guide should be developed iteratively as a layered route-planning project, with each pass adding constraints, resolving conflicts, and validating coverage.

The development process should treat the final route as a constraint-satisfaction problem: every objective must be placed somewhere in the route, but placement is governed by level gates, quest dependencies, Survival Mode geography, trophy safety, leveled rewards, NPC survival, faction choices, lore escalation, and pacing.

## Pre-Research Setup - Lock the Data and Source Workflows

Before collecting gameplay facts, set up the structures that will hold them:

* Objective database schema and CSV conventions.
* Objective ID, category, status, route-placement, and routing-rigidity conventions.
* Source-note naming, citation, and bibliography workflow.
* Validation scripts for structural checks.
* Task-board statuses and dependencies for the next research pass.

This setup should contain no gameplay facts. Its purpose is to keep later research reviewable, cited, and easy to validate.

## Phase 1 - Build the Objective Database

Before writing route steps, compile a structured objective database.

Each objective should have fields such as:

* Objective name.
* Category: quest, trophy, AE Creation, collectible, location, unique item, property, spell, perk, radiant, etc.
* Source: base game, Dawnguard, Hearthfire, Dragonborn, AE Creation.
* Checklist mapping: spreadsheet row/tab/category if applicable.
* Start trigger.
* Completion condition.
* Region/hold/worldspace.
* Prerequisites.
* Recommended level.
* Hard minimum level, if any.
* Maximum leveled-reward threshold, if any.
* Cell-entry lock risk, if any.
* Quest/faction conflicts.
* NPC dependency.
* Trophy relevance.
* Unique rewards.
* Missability status.
* Bug-risk status.
* Survival Mode travel relevance.
* Whether it belongs to main route, branch route, option list, appendix, or excluded scope.

No routing should begin until the objective database has enough structure to prevent hidden omissions.

## Phase 2 - Build the Constraint Tables

Create separate research tables for hard constraints before route construction.

Required tables:

1. Leveled unique items and maximum acquisition thresholds.
2. Cell-entry-sensitive locations/items.
3. Quest conflicts and mutually exclusive choices.
4. Missable quests, rewards, NPCs, and collectibles.
5. Bug-prone quests requiring hard saves.
6. AE Creation start triggers and level gates.
7. PS4 trophy dependencies and missable trophies.
8. NPCs needed for quests, property, marriage, training, investment, or faction access.
9. Radiant quest boundaries.
10. Survival Mode travel constraints: cold regions, sleep/food/restock points, carriages/ferries, early safe storage.
11. Skill/perk/leveling requirements for all perks.
12. Crafting milestones needed for Legendary survivability.

These tables form the guide's routing laws. The writer should not trust memory for them.

## Phase 3 - Classify Objectives by Routing Rigidity

Before ordering everything, classify each objective by how rigidly it must be placed.

Suggested classes:

* Fixed early: must be done early for safety, access, or pacing.
* Fixed late: must be delayed for leveled rewards, difficulty, or lore gravity.
* Windowed: can be done only within a certain level/quest/faction window.
* Region-flexible: can be done whenever the route is nearby.
* Dependency-flexible: can be done once prerequisites are satisfied.
* Branch-only: belongs to an alternate branch route.
* Option-list: player chooses among isolated alternatives.
* Cleanup-safe: can be safely deferred to final cleanup.
* Excluded/unbounded: not required by the guide.

This prevents the writer from treating all objectives as equal. Hard constraints should anchor the route; flexible objectives should fill in around them.

## Phase 4 - Decide Canonical Route Anchors

Create a small set of route anchors before filling in detail.

Anchors should include:

* Start and setup.
* Early Survival Mode stabilization.
* Pre-dragon NPC safety sweep, if used.
* Dragon Rising / dragons entering the world.
* Major city/hold sweeps.
* Faction start points.
* Major faction completion points.
* Civil War / Season Unending coordination.
* Major Daedric/artifact phase gates.
* Dawnguard start and completion.
* Dragonborn/Solstheim start and completion.
* High-level AE Creation phase.
* Level 25, 27, 32, 36, 40, 46, and 60 reward gates.
* All-perks grind/leveling checkpoints.
* Final cleanup and checklist reconciliation.

The first route skeleton should be only these anchors, not detailed instructions.

## Phase 5 - Build a Level-Gated Route Skeleton

Next, produce a skeleton route organized around level bands and mandatory gates.

Possible level-band structure:

* Level 1-10: survival stabilization, local favors, early economy, safe travel, basic combat competence.
* Level 10-20: early holds, early faction introductions, low-risk AE systems, first properties.
* Level 20-30: broader hold work, mid-tier quests, first major faction arcs, some Daedric starts.
* Level 30-40: Nightingale armor-safe content, midgame faction development, stronger dungeons, Hearthfire/property expansion.
* Level 40-46: Shield of Solitude-safe content, Civil War/Main Quest coordination, preparation for high-tier rewards.
* Level 46-60: maximum-tier classic leveled rewards, late faction completions, high-level AE content, major supernatural/apocalyptic content.
* Level 60+: Dragonborn finalization, Miraak rewards, final high-level unique items, remaining mythic content.
* Post-core: all-skills/all-perks completion, final location clearing, final checklist reconciliation.

The actual level bands may change after research, but the route must explicitly account for known leveled reward thresholds.

## Phase 6 - Add Survival Mode Geography

After the level skeleton exists, reshape it around Survival Mode.

The writer should group objectives by travel practicality:

* Regional sweeps should minimize long-distance travel.
* Cold northern routes should be grouped and prepared for.
* Inns, homes, carriages, ferries, food sources, camping, and safe storage should be integrated into the route.
* The guide should avoid assuming fast travel.
* When a route step requires a long journey, it should include restock/rest instructions if needed.

This phase may require moving otherwise-flexible objectives earlier or later to avoid bad Survival Mode routing.

## Phase 7 - Insert Flexible Objectives into Regional Passes

Once hard gates and geography are established, insert flexible objectives into the route whenever the player is naturally nearby.

This is where the writer should place:

* Local side quests.
* Miscellaneous favors.
* Skill books.
* Stones of Barenziah.
* Word walls.
* Clearable dungeons.
* Local AE starts.
* Homes and property upgrades.
* Merchant investments.
* Nearby collectibles.
* Representative radiant quests.

The rule is: if an objective is safe and the route is already nearby, do it then unless delaying improves reward tier, difficulty curve, or narrative escalation.

## Phase 8 - Layer in Crafting, Skills, Perks, and Grinding

After the quest/location skeleton exists, add skill and perk progression.

The writer should:

* Estimate expected level and skill growth at each major checkpoint.
* Insert small distributed training/grinding/crafting blocks where needed.
* Ensure combat power keeps pace with level increases.
* Avoid early best-in-slot crafting unless necessary.
* Decide which skills, if any, will be made Legendary and repeated for all perks.
* Use exploits only if they prevent worse grinding and are bounded, trophy-safe, and justified.

This pass should produce explicit level checkpoints and fallback instructions if the player is underleveled.

## Phase 9 - Add Branch Routes and Option Lists

After the main route is stable, add branch routes.

For each branch point:

1. Identify whether it deserves full branch routing or option-list treatment.
2. If fully routed, place the branch immediately after the hard save and before the main-route choice.
3. Include only branch-exclusive content.
4. Avoid duplicating objectives that will occur in the main route.
5. Tell the player exactly when to reload and resume the main route.

For isolated non-consequential choices, provide an option list and recommended default instead of branching.

## Phase 10 - Add Checklist Synchronization

Once route placement is stable, add checklist cues.

Every spreadsheet-tracked objective should be mapped to:

* A main-route step;
* A branch-route step;
* An option-list note;
* An appendix-only checklist; or
* An explicit exclusion note.

The writer should maintain a coverage matrix showing each checklist objective and its guide location. The final guide should have no orphaned checklist objectives.

## Phase 11 - Add Warning Layer

After the route exists, add the warning layer.

Warnings should be concise and placed exactly where needed:

* Hard save here.
* Do not enter this location before level X.
* Do not turn in this quest yet.
* Do not sell/disenchant this item.
* Choose the artifact-awarding option.
* Stop this questline after this step.
* Complete this NPC-dependent content before dragons/Civil War/Dark Brotherhood/etc.

Warnings should not become lore essays or full walkthrough explanations.

## Phase 12 - Validate Against Constraint Tables

Before drafting the polished guide, validate the route against every constraint table.

Validation questions:

* Is every checklist objective mapped?
* Are all trophies protected?
* Are all AE Creations included?
* Are all leveled rewards acquired at maximum tier?
* Are cell-entry-sensitive locations avoided until safe?
* Are all known quest conflicts handled?
* Are all branch decisions hard-saved?
* Are NPC-dependent quests routed before realistic NPC-death risks?
* Are all required radiants bounded?
* Are all perks achievable under the planned leveling path?
* Does Survival Mode routing remain practical?
* Does the route preserve gradual difficulty escalation?
* Are all cleanup tasks explicitly routed rather than implied?

## Phase 13 - Produce a Minimal Prototype Route

Before writing the full guide, create a prototype route with only:

* Section headings.
* Step numbers.
* Objective names.
* Level gates.
* Hard saves.
* Checklist categories.
* Stop/return points.

This prototype should be reviewed for structure before prose is added.

The prototype route should answer: "Does the whole run basically fit together?"

## Phase 14 - Expand into Black-Box Instructions

Only after the prototype route is validated should the writer expand steps into final black-box instructions.

Expansion should add:

* Start locations/triggers.
* Completion boundaries.
* Short warnings.
* Checklist cues.
* Survival restock/rest notes.
* Recommended default choices.
* Branch instructions.

Expansion should not add unnecessary walkthrough detail.

## Phase 15 - Final QA and Playtest Passes

The final guide should receive multiple QA passes:

1. Coverage pass: every objective accounted for.
2. Order pass: no delayed task depends on reader memory.
3. Trophy pass: no trophy risks introduced.
4. Leveled-item pass: no inferior rewards acquired early.
5. Survival pass: travel/rest/cold/carry assumptions are valid.
6. Legendary pass: combat difficulty is plausible at each phase.
7. Checklist pass: cues align with spreadsheet entries.
8. Spoiler pass: unnecessary story explanation removed.
9. Branch pass: branches include only alternate content and return cleanly.
10. Playtest or simulated playtest pass: verify route feasibility in practice.

## Recommended Development Deliverables

The writer should produce the guide through intermediate deliverables:

1. Objective database.
2. Constraint tables.
3. Scope/exclusion confirmation.
4. Level-gated route skeleton.
5. Survival Mode regional route skeleton.
6. Main-route prototype.
7. Branch-route prototype.
8. Checklist coverage matrix.
9. Skill/perk/grind plan.
10. Warning/hard-save table.
11. Final black-box guide draft.
12. QA checklist and unresolved-risk report.

Each deliverable should be reviewable before the next layer is built. This prevents the writer from burying routing mistakes inside polished prose.
