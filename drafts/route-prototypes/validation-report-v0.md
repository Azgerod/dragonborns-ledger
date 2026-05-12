# Route Prototype Validation Report v0

Status: TB-033 complete as a constraint-validation pass over the warning-layered prototype.

Scope: this validates the current route-planning artifacts before TB-034 turns them into a minimal numbered route prototype. It is not final route prose, not a playtest report, and not a final checklist step map. No broad gameplay research was added; the report consumes the existing source-backed objective rows, constraint tables, branch prototypes, checklist matrix, and route-planning indexes.

## Inputs Reviewed

| Input | Validation use |
| --- | --- |
| `drafts/route-prototypes/main-route-prototype-v0.md` | Primary warning-layered prototype under validation. |
| `data/route-planning/prototype-objective-block-map.csv` | Row-level prototype assignment and gate/status audit for 2,789 objectives. |
| `data/route-planning/objective-route-index.csv` and `objective-constraints.csv` | Generated objective-to-geography/support/constraint joins. |
| `data/checklist-mapping/coverage-matrix.csv` | Checklist coverage state for all 3,697 spreadsheet rows. |
| `data/constraints/leveled-unique-items.md` and `cell-entry-locks.md` | Leveled reward, entry/spawn, reward-time, and random reward validation. |
| `data/constraints/quest-conflicts-hard-saves.md` and `drafts/branch-routes/*.md` | Branch defaults, branch-only scope, hard saves, reload rules, and clean-continuity checks. |
| `data/constraints/trophy-dependencies.md`, `npc-dependencies.md`, `bug-prone-quests.md`, and `radiant-boundaries.md` | Trophy, NPC, bug, and radiant route-law validation. |
| `data/constraints/survival-mode-constraints.md`, `skill-perk-leveling-plan.md`, `progression-source-selection.md`, and `progression-source-selections.csv` | Survival, progression, all-skills/all-perks, source-selection, training, crafting, and reset-policy validation. |
| `data/checklist-mapping/counter-coverage-plan.md` and `data/locations/location-route-validation.md` | Counter, location discovery/clear, Delver/Explorer, and route-action validation. |

## Corrections Applied

| Finding | Correction |
| --- | --- |
| `cell-entry-locks.md` attached the Amulet of Articulation separated random-reward row to `OBJ-001770`, which is Shield of Solitude. | Corrected the affected objective to `OBJ-001771`, regenerated `objective-constraints.csv`, `objective-route-index.csv`, and `prototype-objective-block-map.csv`. |
| The warning layer lacked a named save for the Amulet of Articulation random-version reward. | Added `HS-TG-ARTICULATION-REWARD` to the hard-save register and main prototype. This is a reward-reroll save, not a branch save. |
| The route-block prose had stale direct-location counts for G03, G05, G07, and G08. | Updated the prose to match the generated block map: G03 58, G05 36, G07 67, and G08 63 direct location rows. |
| Several source-backed NPC/favor/action warnings were present in constraint tables but too implicit in the prototype warning layer. | Added explicit warnings for Vittoria Vici / `The Spiced Wine`, Captain Aldis branch exposure, Siddgeir's Falkreath rare-gift window, `The Whispering Door`, Malborn's follow-up, and the controlled no-follower brawl. |

## Validation Matrix

| Area | Verdict | Evidence and TB-034 guardrail |
| --- | --- | --- |
| Checklist coverage | Pass at prototype level. | `coverage-matrix.csv` has 3,697 rows: 3,160 main-route prototype, 33 branch-route prototype, 75 option-list, 107 appendix, and 322 explicit exclusions. No `source_readiness_required`, `manual_review_required`, `scope_review_required`, or `unmatched` rows remain. TB-034 must preserve these mapped buckets when assigning step numbers. |
| AE Creation scope | Pass at prototype level. | AE parent/child rows flow through the objective database, checklist matrix, route block map, start-trigger table, and source-readiness resolutions. Courier/prerequisite and high-risk AE rows remain gated by their source rows; TB-034 must not route a Creation before its listed trigger/prerequisite. |
| Leveled rewards | Pass after correction. | Prototype thresholds cover Level 8+, 25+, 27+, 32+, 36+, 40+, 46+, and 60+ rows. The Amulet of Articulation is now treated as a random reward requiring a local save/reload policy rather than a level or cell-entry gate. |
| Cell-entry and spawn locks | Pass. | Riftweald, Sky Haven, Forbidden Legend-linked locations, Silent Moons, Kharjo target locations, Bloated Man's Grotto, and Whiterun first-visit examples have warning-layer coverage. Frostmere remains correctly separated from Pale Blade cell-entry locking. |
| Branch saves and reloads | Pass. | The main prototype and hard-save register both contain 20 named saves: 19 branch/outcome/trophy saves plus `HS-TG-ARTICULATION-REWARD`. The branch index contains the 19 branch/outcome saves, as expected. TB-034 must preserve the play-alternate-first, verify, reload, continue-canonical rule. |
| Trophy protection | Pass at prototype level. | Setup, trophy-pop fallback, War Hero, One with the Shadows, Oblivion Walker, Auriel's Bow, transformation trophies, location counters, Master Criminal, Thief, Snake Tongue, Hard Worker, Artificer, Legendary Dragon, Ebony Warrior, and all-perks gates are represented. Final trophy pops still require step-level verification saves once TB-034 assigns exact actions. |
| NPC and bug-prone quest dependencies | Pass after correction. | High-risk dependencies now have explicit warnings: Erikur/Dainty Sload, Vittoria, Aldis, Blood on the Ice/Hjerim, Falkreath/Helvard/Siddgeir, Whispering Door, Malborn, Daedric NPC states, Septimus/Oghma, Stalhrim, Severin, Tel Mithryn, Unearthed, Hearthfire/family, Elytra, and Kharjo. |
| Radiant boundaries | Pass. | Required gates, finite chains, representative rows, Thieves Guild 125 jobs, Dawnguard Lost Relic fillers, Volkihar branch radiants, and excluded failure states remain bounded by `radiant-boundaries.md` and `counter-coverage-plan.md`. TB-034 must route loops with counters rather than freeform grinding. |
| Location counters | Pass at planning level. | Direct location rows reconcile to 447 location assignments across G02-G13. Delver/Explorer handling follows `location-route-validation.md`: Angarvunde and Mistwatch do not count for Delver, duplicate markers do not double-count clears, and AE content locations follow parent content. |
| Survival Mode practicality | Pass at block level. | Route blocks preserve warm-core stabilization, prepared cold/mountain/coastal/Solstheim sweeps, proper-bed level-ups, carry/storage/food/warmth/cure preflight, ferry/carriage as logistics rather than fast travel, and candidate-base validation before use. |
| Progression and all-perks feasibility | Pass at policy level. | TB-027/TB-031E provide the all-skills/all-perks rule, level 252 target, reset pool, training limits, source selections, Oghma policy, crafting outputs, investments, enchantment learning, and alchemy discovery method. Exact reset counts cannot be computed until TB-034 assigns final route order, natural skill gains, training purchases, and cleanup actions; TB-034 must keep a final skill-state table as a validation output for TB-037/final QA. |
| Gradual power curve | Pass. | The prototype keeps early crafting light, delays repeated Legendary resets and final crafting loops, excludes major exploit baselines, and keeps high-tier reward loops behind their gates. TB-034 must not use late G14 crafting/reset logic as early route power. |
| Cleanup explicitness | Pass for prototype. | G14 is constrained to checklist reconciliation, late-level gates, post-branch resolution, post-progression requirements, and source/candidate selection. TB-034 must convert each cleanup bucket into explicit route steps rather than relying on "finish anything left." |

## TB-034 Intake Rules

| Rule | Reason |
| --- | --- |
| Do not reroute from counts alone. | Counts are queue sizes; each row still needs prerequisite, warning, NPC, bug, Survival, branch, and checklist validation at step placement. |
| Preserve every named hard save. | Branch, trophy, reward-reroll, and one-shot actions require local saves and clean continuation state. |
| Keep source-table row text above generated summaries. | Generated `constraint_type` values are indexing aids; for separated rows such as Amulet of Articulation, the Markdown row explains the real trigger. |
| Emit route-step checklist cues only after preserving the current coverage buckets. | Checklist mapping is complete at prototype level; step numbering must not orphan branch, option-list, appendix, or exclusion rows. |
| Carry final numerical progression validation forward explicitly. | Exact skill levels, reset counts, perk allocations, and final physical source-item checks depend on the TB-034 route order and cannot be responsibly fabricated before it exists. |

## Result

The warning-layered prototype is valid for TB-034 after the targeted corrections above. No earlier phase needs a full redo; the changes were narrow constraint-index and warning-layer corrections, and the generated route-planning indexes were rebuilt from the updated source files.
