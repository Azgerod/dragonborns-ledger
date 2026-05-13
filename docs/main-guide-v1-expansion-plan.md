# Main Guide v1 Expansion Plan

Status: TB-035 reopened after review. This file is the coordination plan for expanding `drafts/final-guide/main-guide-v0.md` into a self-contained `drafts/final-guide/main-guide-v1.md`.

This plan is preparatory only. It does not expand the guide prose itself.

## Why This Exists

`main-guide-v0.md` is a useful MR-section scaffold, but it is not detailed enough for the intended final guide. The v1 guide must explicitly represent every objective row in `data/objectives/objectives.csv` and every checklist-relevant row already mapped by the project. A player should not need to consult the objective spreadsheet, route maps, support tables, source notes, or external appendices to know what to do next.

Appendices may still exist as verification material, but execution-critical instructions belong in the guide itself at the relevant route point.

## Current Input Inventory

Current counts, from the repository state on 2026-05-12:

| Input | Current rows | v1 use |
| --- | ---: | --- |
| `data/objectives/objectives.csv` | 2,789 | Every row must appear in `main-guide-v1.md` as a routed main instruction, branch instruction, option/default instruction, explicit exclusion, or `NEEDS ROUTE RESOLUTION` note. |
| `data/checklist-mapping/coverage-matrix.csv` | 3,697 | Every mapped checklist row must have an auditable guide location in `main-guide-v1.md`. |
| Main-route checklist rows | 3,160 | Must be placed directly in the main guide; rows with blank route blocks still need section assignment from objective/support context. |
| Branch checklist rows | 33 | Must be handled in explicit branch blocks inside `main-guide-v1.md`. |
| Option-list checklist rows | 75 | Must be handled in explicit option/default sections inside `main-guide-v1.md`. |
| Appendix-only checklist rows | 107 | Must be represented in the self-contained guide document; they cannot remain external-only execution requirements. |
| Explicit exclusion checklist rows | 322 | Must appear in an exclusion section with the reason, not disappear from the guide. |
| `data/route-planning/prototype-objective-block-map.csv` | 2,789 | Starting assignment layer for route blocks, dispositions, gates, parents, and deferred reasons. |
| `data/route-planning/objective-route-index.csv` | 2,789 | Starting workbench for category, geography, support-table, and constraint summaries. |
| `data/route-planning/objective-constraints.csv` | 1,847 | Gate/save/warning source for objectives with routing constraints. |
| `data/constraints/progression-source-selections.csv` | 594 | Source selections for skill books, spells, enchantments, alchemy, investments, crafting outputs, and grind blocks. |
| `data/locations/location-catalog.csv` | 467 | Location names and discover/clear policy inputs. |
| `data/locations/location-geography.csv` | 472 | Corridor and Survival Mode clustering support for location placement. |
| `data/books/skill-books-locations.csv` | 474 | Candidate copies for the 90 skill-book titles; v1 must state the chosen title/copy/read timing. |
| `data/books/spell-tomes-locations.csv` | 716 | Spell tome source candidates; v1 must state the selected source/timing or route resolution gap. |
| `data/books/book-document-locations.csv` | 607 | Quest, AE, Black Book, and checklist document candidates; v1 must name routed titles. |
| `data/items/ae-item-members.csv` | 1,165 | AE item/member expansion support for quests, equipment, ingredients, spells, crafting, and collectible-like sets. |
| `data/skills/enchantment-learning-catalog.csv` | 59 | Enchantment-learning rows; v1 must name effects and source families/items. |
| `data/skills/alchemy-effect-catalog.csv` | 190 | Ingredient/effect discovery rows; v1 must name ingredients and discovery method. |
| `data/skills/merchant-investment-catalog.csv` | 50 | Investment/default/exclusion rows; v1 must name merchant targets and timing. |
| `data/skills/practical-crafting-system-catalog.csv` | 13 | Practical crafting systems and selected outputs; v1 must name the output/action. |
| `data/properties/property-details.csv` | 127 | Homes, wings, services, upgrades, storage/display/family support; v1 must name the acquisitions and checks. |
| `data/npc/relationship-options.csv` | 240 | Spouse, child, steward, follower, pet, mount, bard, carriage, and farmhand option/default support. |

Refresh these counts with the standard validators before drafting if any data file changes.

## Required v1 Standard

`main-guide-v1.md` must be self-contained. The guide may have internal reference sections, but the reader must not need a separate appendix, spreadsheet, route map, or source note to execute the route.

Every objective row and checklist-relevant row must be visibly represented by name and, where practical, by ID. Use concise auditable tags such as:

* `[OBJ-000123]`
* `[CHECKLIST: Quest - OBJ-000123 - Objective Name]`
* `[CHECKLIST: CL-... - Checklist Entry]` when a checklist row has no direct objective ID.

The exact tag style may be refined during v1 drafting, but each row must be searchable by objective ID, checklist ID, objective name, or checklist entry.

The guide must not use category placeholders as route instructions. Banned or suspect phrases include:

* `route local`
* `safe local`
* `local objectives`
* `nearby objectives`
* `remaining finite`
* `remaining checklist`
* `as routed`
* `as needed`
* `selected sources`
* `support rows`
* `queue`
* `family`
* `cleanup`
* `verify checklist`
* `finish remaining`
* `collect local`
* `route books`
* `route locations`
* `corridor discoveries`
* `spell sources`
* `support objectives`

If a phrase like this remains for readability, it must be immediately followed by the full objective-level list and concrete actions covered by the phrase.

Use `NEEDS ROUTE RESOLUTION:` only when existing project data is insufficient after checking the relevant objective, checklist, route-planning, constraint, and support rows. The note must include:

* objective ID or checklist ID;
* objective/checklist name;
* the specific missing fact;
* the inputs already checked;
* the minimum next research or validation needed.

Do not use `NEEDS ROUTE RESOLUTION` as a generic deferral bucket.

## Per-Pass Workflow

Each MR pass must be small enough to review. If one MR section is too large to handle conscientiously, split it by category, location corridor, quest chain, or support-table slice before editing the guide.

For each pass:

1. Create or update `drafts/final-guide/main-guide-v1.md` from the current v1 draft state. Do not edit `main-guide-v0.md`; keep it as the scaffold/reference snapshot.
2. Identify all rows assigned to the section from `main-guide-v0.md`, `main-route-prototype-v0.md`, `prototype-objective-block-map.csv`, `objective-route-index.csv`, `coverage-matrix.csv`, and relevant support tables.
3. Expand the section with explicit instructions for each objective/checklist row. Name the quest, location, NPC, item, book, spell, shout, collectible, counter action, branch outcome, option/default, exclusion, or system output.
4. Preserve all hard gates, hard saves, branch reloads, Survival Mode logistics, and unique-item preservation rules.
5. Add checklist cues at the point of completion/acquisition/verification.
6. Add `NEEDS ROUTE RESOLUTION` notes only for genuinely unresolved rows.
7. Record the rows processed by the pass in the v1 coverage summary or coverage ledger.
8. Search the edited section for placeholder phrases before moving on.

## Per-MR Subtasks

The task board should surface the next active pass, but this table is the minimum required work breakdown. No MR section is allowed to be treated as "covered" until objective-level expansion for that section is complete.

| Subtask | Section | Starting source | Required expansion focus | Status |
| --- | --- | --- | --- | --- |
| TB-035P | Prep and standards | Repo docs | Record this plan, reopen TB-035, harden instructions, and point the next task at MR-001. | Done |
| TB-035-MR-001 | MR-001 - Setup And Save Baseline | G00 setup | AE entitlement, mod/Creation restrictions, Legendary/Survival setup, trophy-safe baseline, save policy, explicit exclusions created by setup scope. | Done |
| TB-035-MR-002 | MR-002 - Helgen, Riverwood, And First Survival Loop | G01 opening | `Unbound`, `Before the Storm`, Riverwood survival support, first bed/food/sell-off, opening objective and checklist cues. | Ready |
| TB-035-MR-003 | MR-003 - First Whiterun Visit | G01 Whiterun first-entry | Whiterun entry, Amren/Ysolda/Brenuin/Uthgerd, early favor/work/action counters, relationship/default handling. | Pending |
| TB-035-MR-004 | MR-004 - Bleak Falls Barrow And Dragon Rising | G01-G02 main quest opener | `Bleak Falls Barrow`, `Dragon Rising`, first dragon/shout/trophy rows, dragon-world activation warnings. | Pending |
| TB-035-MR-005 | MR-005 - First Storage, Horse, And Central Base Setup | G02 central support | Whiterun horse, Breezehome, Tundra Homestead, storage verification, property rows and support services. | Pending |
| TB-035-MR-006 | MR-006 - Early Work Actions And Local Economy | G02 central activities | Chop wood, crop sale, brawl, beggar/drunk favors, crafting tutorials, early economy and trophy-counter rows. | Pending |
| TB-035-MR-007 | MR-007 - Level 8 Silent Moons Gate | G02 level 8 gate | Silent Moons/Lunar weapon handling, level 8 gate, central Whiterun/Rorikstead locations and linked enchantment/item rows. | Pending |
| TB-035-MR-008 | MR-008 - Goldenhills Plantation | G02 Goldenhills | `The Unquiet Dead`, Goldenhills ownership, farm operations, staffing, crop/food/income rows, storage caveats. | Pending |
| TB-035-MR-009 | MR-009 - Companions Entry | G02-G03 Companions start | Companions opening quests, required early radiant gates, representative radiant rules, faction checklist cues. | Pending |
| TB-035-MR-010 | MR-010 - Companions Transformation Window | G03 Companions window | Werewolf route, Beast Form, Companions chain, Totems/Purity timing, Werewolf Mastered preparation. | Pending |
| TB-035-MR-011 | MR-011 - Falkreath Favor And Lakeview Protection | G03 Falkreath/Lakeview | Siddgeir/Falkreath favor, Lakeview prerequisites, Helvard protection, property/NPC dependency rows. | Pending |
| TB-035-MR-012 | MR-012 - Southern Warm Corridor | G03 southern sweep | Falkreath, Riverwood, Ivarstead, Lakeview construction, southern locations, books, misc objectives, Survival support. | Pending |
| TB-035-MR-013 | MR-013 - Hircine And Bloated Man's Grotto | G03 Hircine setup | Bolar's Oathblade, Bloated Man's Grotto state, Hircine branch save, Savior's Hide branch, Ring of Hircine main route. | Pending |
| TB-035-MR-014 | MR-014 - Riften Access | G04 Riften access | Riften entry, services/property candidates, Thieves Guild start, Riften objective rows safe before Nightingale gates. | Pending |
| TB-035-MR-015 | MR-015 - Early Thieves Guild Chain | G04 Thieves early chain | `A Chance Arrangement` through `Speaking With Silence`, city-job tally start, stop before `Hard Answers`, radiant recording method. | Pending |
| TB-035-MR-016 | MR-016 - Riften And Rift Sweep | G04 southeast sweep | Honeyside/Shadowfoot, Frost/`Promises to Keep`, Rift locations, books, support rows, mount/property/item cues. | Pending |
| TB-035-MR-017 | MR-017 - Level 32 Thieves Checkpoint | G04 level 32 checkpoint | Nightingale Armor readiness note only, no impossible chain order, progression fallback if below level 32. | Pending |
| TB-035-MR-018 | MR-018 - Reach Setup | G05 Reach setup | Markarth/Old Hroldan support, Reach locations, Vlindrel Hall, Sky Haven level-46 avoidance. | Pending |
| TB-035-MR-019 | MR-019 - Cidhna, Molag Bal, And Namira | G05 Cidhna/Molag/Namira | Cidhna Mine, `The House of Horrors`, `The Taste of Death`, Namira save/outcome, NPC/artifact warnings. | Pending |
| TB-035-MR-020 | MR-020 - Aetherium Setup | G05 Aetherium setup | `Lost to the Ages`, shard sequence, Aetherium objective rows, forge decision hold. | Pending |
| TB-035-MR-021 | MR-021 - Daedric Matrix | G05 Daedric matrix | All named Daedric quests in this block, artifacts, branch saves, sacrifice/default choices, Oblivion Walker accounting. | Pending |
| TB-035-MR-022 | MR-022 - Windhelm State And Hjerim | G06 Windhelm state | `Blood on the Ice`, Hjerim purchase/furnishing, Windhelm state risks, property/bug-save rows. | Pending |
| TB-035-MR-023 | MR-023 - Main Quest Staging Before Sky Haven | G06 main quest staging | Main quest from Greybeards through `A Cornered Rat`, stop before Sky Haven, shout/trophy rows. | Pending |
| TB-035-MR-024 | MR-024 - Eastmarch Support | G06 Eastmarch support | Malborn follow-up, Eastmarch/Windhelm locations, Gallows Hall, Hjerim support, books, ferry preparation. | Pending |
| TB-035-MR-025 | MR-025 - Solitude Prerequisites | G07 Solitude prerequisites | Solitude favors/dependencies, Captain Aldis, Erikur-sensitive work, pre-DB Solitude rows. | Pending |
| TB-035-MR-026 | MR-026 - Bards College | G07 Bards College | Bards induction, King Olaf's Verse, Finn's Lute, Pantea's Flute, Rjorn's Drum, trophy/book rows. | Pending |
| TB-035-MR-027 | MR-027 - Shield Of Solitude Gate | G07 Shield gate | `The Wolf Queen` line, level 40 Shield of Solitude gate, reward timing. | Pending |
| TB-035-MR-028 | MR-028 - Northwest And Coast Prepared Sweep | G07 northwest sweep | Solitude/Dragon Bridge/Morthal/coast/Windstad/Myrwatch locations, books, properties, cold/carry support. | Pending |
| TB-035-MR-029 | MR-029 - Dark Brotherhood Fork | G07 Dark Brotherhood fork | `Delayed Burial`, Abandoned Shack save, Destroy branch first, reload continuity, join-route default. | Pending |
| TB-035-MR-030 | MR-030 - Dark Brotherhood Main Route | G07-G10 Dark Brotherhood main | Main DB questline, contracts, Shadowmere, DB rewards, Solitude/Erikur/Bound Until Death risks. | Pending |
| TB-035-MR-031 | MR-031 - Northern Preflight | G08 north preflight | Prepared cold-travel checklist, bed/food/hot soup/warmth/cure/carry route support before Pale/Winterhold. | Pending |
| TB-035-MR-032 | MR-032 - College Opening | G08 College opening | `First Lessons`, College entry spell requirements, hold `Under Saarthal` and `Lost Legends` until level 36. | Pending |
| TB-035-MR-033 | MR-033 - Dawnstar, Pale Blade, And Vaermina | G08 Pale/Dawnstar | Dawnstar/Heljarchen/Frostmere, level 27 Pale Blade, Vaermina branch save/outcome, Kharjo target checks. | Pending |
| TB-035-MR-034 | MR-034 - Mage's Circlet Gate | G08 level 25+ | Level 25 Mage's Circlet gate, `Good Intentions` reward timing, College stop/resume boundary. | Pending |
| TB-035-MR-035 | MR-035 - Level 36 Linked-Dungeon Loop | G09 level 36 loop | `Under Saarthal`, `Forbidden Legend`, Folgunthur, Geirmund's Hall, Reachwater Rock, Gauldur rewards. | Pending |
| TB-035-MR-036 | MR-036 - College Completion | G09 College completion | College main chain completion, spells/powers/rewards, Mage's Circlet and linked-dungeon gate preservation. | Pending |
| TB-035-MR-037 | MR-037 - College Side Content And Velehk | G09 College side/outcome | College side quests, ritual spell quests, master spells, `Forgotten Names`, Velehk save/outcome. | Pending |
| TB-035-MR-038 | MR-038 - Level 46 Sky Haven And Dragonbane | G10 level 46 main quest | `Alduin's Wall`, first Sky Haven entry, Dragonbane maximum-tier acquisition. | Pending |
| TB-035-MR-039 | MR-039 - Level 46 Thieves Guild Rewards | G10 level 46 Thieves | `Hard Answers`, Nightingale Blade, `The Pursuit`, Chillrend, `Trinity Restored`, Nightingale Armor, `Blindsighted`, Nightingale Bow, `Darkness Returns`. | Pending |
| TB-035-MR-040 | MR-040 - Guild Restoration And Amulet Of Articulation | G10 Guild restoration | `Under New Management`, Amulet of Articulation save policy, 20 restoration jobs, 125-job counter method/totals. | Pending |
| TB-035-MR-041 | MR-041 - Civil War Stormcloak Branch | G10 Civil War branch | Stormcloak branch after hard save, branch-only objectives, War Hero/Season Unending warnings, reload. | Pending |
| TB-035-MR-042 | MR-042 - Imperial Civil War | G10 Imperial Civil War | Imperial main route, War Hero-safe fort handling, Hero of Skyrim, Battle of the Champions. | Pending |
| TB-035-MR-043 | MR-043 - Late Main Quest Coordination | G10 main quest coordination | `The Throat of the World` through `The Fallen`, Season Unending skip/contingency, Elder Knowledge/Alduin's Bane rows. | Pending |
| TB-035-MR-044 | MR-044 - Paarthurnax And Blades Branch | G10 Paarthurnax branch | Blades/Paarthurnax branch, Rebuilding the Blades, Dragon Hunting, reload, preserve Paarthurnax. | Pending |
| TB-035-MR-045 | MR-045 - Dawnguard Fork And Volkihar Branch | G11 Dawnguard fork | Bloodline save, Volkihar branch, rings/amulets, Volkihar radiants, `The Gift` conditional, reload/refuse Harkon. | Pending |
| TB-035-MR-046 | MR-046 - Dawnguard Main Route | G11 Dawnguard main | Dawnguard chain, Fort Dawnguard support, representative radiants, Lost Relic filler recording until all three relics. | Pending |
| TB-035-MR-047 | MR-047 - Aetherium Forge Branches | G11 Aetherium Forge | Staff/Shield branch audits, reloads, Aetherial Crown main outcome, artifact/trophy cues. | Pending |
| TB-035-MR-048 | MR-048 - Dawnguard Worldspaces | G11 Dawnguard worldspaces | Soul Cairn, Arvak, Unknown Books, Forgotten Vale, Auriel's Bow, paragons, Dawnguard locations/books. | Pending |
| TB-035-MR-049 | MR-049 - Werewolf, Vampire Lord, And Final Mortal Setup | G11 transformations | Werewolf Mastered, Vampire Mastered, Beast Form/totems, cure/final mortal state, transformation powers. | Pending |
| TB-035-MR-050 | MR-050 - Solstheim Entry | G12 Solstheim entry | Windhelm ferry, Raven Rock logistics, initial Solstheim discovery/rest/food/carry/storage boundaries. | Pending |
| TB-035-MR-051 | MR-051 - Raven Rock Core | G12 Raven Rock core | Dragonborn opening through `The Temple of Miraak`, `The Final Descent`, `Served Cold`, Severin Manor, local rows. | Pending |
| TB-035-MR-052 | MR-052 - Skaal And Stalhrim | G12 Skaal/Stalhrim | `The Fate of the Skaal`, `A New Source of Stalhrim`, stalhrim crafting unlock, Deor/Fanari state. | Pending |
| TB-035-MR-053 | MR-053 - Thirsk Branch And Nord Continuity | G12 Thirsk branch | Riekling branch first, reload, Nord-side `Retaking Thirsk`, Nord favors/relationships. | Pending |
| TB-035-MR-054 | MR-054 - Tel Mithryn And Black Books | G12 Tel Mithryn | Tel Mithryn quests, `Reluctant Steward`, `Old Friends`, Black Books, staff enchanter/imbuing support, spell/source rows. | Pending |
| TB-035-MR-055 | MR-055 - Unearthed And Ralis | G12 Unearthed/Ralis | `Unearthed` phases, payment/re-entry saves, Ralis branch save, spare Ralis main route, unique/follower rows. | Pending |
| TB-035-MR-056 | MR-056 - Solstheim Sweep | G12 Solstheim sweep | Deathbrand, Karstaag, Black Books, Solstheim locations, spell tomes, documents, collectibles, level 60 hold. | Pending |
| TB-035-MR-057 | MR-057 - Ghosts Of The Tribunal Branch | G12 Ghosts branch | Ghosts branch save, destroy-heretics branch and journal, reload, join/infiltrate main route, armory/crafting/follower rows. | Pending |
| TB-035-MR-058 | MR-058 - Bittercup Branches | G12 Bittercup branches | Power and Nothing branches, reloads, Fortune main route, Master Transmute and reward rows. | Pending |
| TB-035-MR-059 | MR-059 - Level 60 Miraak Finale | G12 level 60 Dragonborn final | `At the Summit of Apocrypha`, level 60 Miraak corpse/reward gate, Miraak equipment, Dragonborn finale rows. | Pending |
| TB-035-MR-060 | MR-060 - World-Eater's Eyrie And Dragonslayer | G13 main quest finale | Skuldafn, Sovngarde, `Dragonslayer`, separate-worldspace recovery, final main-quest trophy/location rows. | Pending |
| TB-035-MR-061 | MR-061 - High-Risk AE And Separate Worldspaces | G13 high-risk AE | `The Cause`, Deadlands, high-risk AE quest bundles, separate-worldspace Creation content, exit/recovery plans. | Pending |
| TB-035-MR-062 | MR-062 - Black Book Defaults And Progression Switches | G13 Black Book power defaults | Black Book powers/defaults, Waking Dreams resets, Scholar's Insight transition, crafting/progression switches. | Pending |
| TB-035-MR-063 | MR-063 - Location Counter Cleanup | G14 location counters | Every remaining location by name; discover/enter/clear/avoid action; Delver/Explorer/Solstheim Explorer verification. | Pending |
| TB-035-MR-064 | MR-064 - Collectible Reconciliation | G14 collectibles | Stones, masks, claws, bugs, paragons, treasure maps, fishing, pets, mounts, shouts, word walls, finite sets by name. | Pending |
| TB-035-MR-065 | MR-065 - Books, Spells, And Documents | G14 books/spells | All skill books, spell tomes, quest/AE documents, Black Books, learned-spell checks, Scholar's Insight read policy. | Pending |
| TB-035-MR-066 | MR-066 - Crafting, Enchanting, Alchemy, And Investments | G14 crafting/progression | Enchantments, alchemy effects, merchant investments, practical crafting systems, outputs, source items/families. | Pending |
| TB-035-MR-067 | MR-067 - Level 78 And Level 80 Gates | G14 level 78/80 gates | Legendary Dragon trophy/action at 78+, Ebony Warrior at 80+, late combat save/trophy checks. | Pending |
| TB-035-MR-068 | MR-068 - All-Perks Loop | G14 all-perks loop | Level 252+, all 251 perk ranks, skill 100 recovery, Legendary reset counts/distribution, underleveled fallback. | Pending |
| TB-035-MR-069 | MR-069 - Homes, Household, Services, Pets, And Mounts | G14 household/property/services | All homes, Hearthfire wings/services, spouse/children/stewards/bards/carriages/farmhands, pets, mounts, storage/display checks. | Pending |
| TB-035-MR-070 | MR-070 - Master Criminal Trophy Branch | G14 Master Criminal branch | 1,000-gold bounty in all nine holds, trophy verification, clean reload, NPC safety boundaries. | Pending |
| TB-035-MR-071 | MR-071 - Final Reconciliation | G14 final reconciliation | Final row-by-row coverage summary, trophy fallback checks, unique-item audit, branch-return audit, explicit unresolved rows. | Pending |

## Cross-Cutting Reconciliation Passes

These passes do not replace per-MR expansion. They are final safeguards after the MR passes have inserted objective-level instructions.

| Subtask | Purpose | Status |
| --- | --- | --- |
| TB-035-COV-001 | Objective ID audit: every `objective_id` in `data/objectives/objectives.csv` appears in `main-guide-v1.md` or in an explicit unresolved/exclusion line. | Pending |
| TB-035-COV-002 | Checklist ID audit: every row in `coverage-matrix.csv` appears in the guide by checklist ID, objective ID, or checklist entry plus mapping type. | Pending |
| TB-035-COV-003 | Branch audit: all 33 branch checklist rows and all branch-route objective rows are handled in branch-first/reload blocks inside the guide. | Pending |
| TB-035-COV-004 | Option/default audit: all option-list rows are named with the recommended default and the alternative option set. | Pending |
| TB-035-COV-005 | Exclusion audit: all explicit exclusions are named with the reason and scope boundary. | Pending |
| TB-035-COV-006 | Previous appendix-only audit: all 107 previous appendix-only checklist rows are represented in the guide document itself. | Pending |
| TB-035-COV-007 | Location audit: every location objective is named with discover/enter/clear/avoid timing and counter treatment. | Pending |
| TB-035-COV-008 | Books/documents audit: all skill books, spell tomes, Black Books, quest books, AE documents, and checklist documents are named with pickup/read timing. | Pending |
| TB-035-COV-009 | Collectibles audit: all finite collectible sets are named item-by-item with route timing. | Pending |
| TB-035-COV-010 | Crafting/progression audit: enchantments, alchemy effects, merchant investments, practical crafting outputs, perks, skills, and grind blocks are explicit. | Pending |
| TB-035-COV-011 | Radiant/counter audit: Thieves Guild jobs, Dawnguard Lost Relic, trophies, fishing, work actions, and representative radiants have target, boundary, and recording method. | Pending |
| TB-035-COV-012 | Placeholder search: run the banned-phrase search and remove or expand every hit. | Pending |
| TB-035-COV-013 | Final coverage summary: append totals for objective rows processed, placed in main guide, branch-handled, option/default-handled, excluded, and unresolved. | Pending |

## Validation Commands

Run the ordinary validators after metadata or data changes:

```bash
python3 tools/build_checklist_coverage.py
python3 tools/validate_all.py
git diff --check
```

When `main-guide-v1.md` exists, also run the placeholder audit:

```bash
python3 tools/check_main_guide_placeholders.py drafts/final-guide/main-guide-v1.md
```

## Downstream Impact

TB-036 appendices/reference tables are blocked until the v1 self-contained guide pass is complete or explicitly re-scoped. The old plan assumed appendices could carry much of the exhaustive detail. The new standard requires the guide document itself to carry objective-level execution instructions first.
