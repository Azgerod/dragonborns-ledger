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

The player-facing guide and the internal coverage tracker are separate layers:

* The player-facing guide should read like a polished Skyrim route, with concise route instructions. Routine checklist logging is handled by the global guide policy; add explicit route bookkeeping only for non-obvious counters, branches, randomized assignments, options, or hidden state.
* The internal coverage tracker records objective IDs, checklist IDs, row counts, coverage status, staged/completed status, and unresolved notes. Use `data/guide-coverage/main-guide-v1-coverage.csv` for this unless a later task creates a better internal artifact.

Do not put objective IDs, coverage ledgers, row counts, coverage-matrix language, or "represented here" implementation prose in normal player-facing guide text unless the project deliberately adopts a final checklist-ID display format. Each row still must be auditable through the internal coverage tracker.

The MR identifiers are internal coordination labels, not player-facing chapter names. Player-facing guide headings should use route titles. The sequence and jurisdiction of these internal sections may be adjusted during expansion when objective-level routing shows that the broad scaffold would split or delay content poorly. When a section boundary changes, update the guide text, the coverage tracker, and this plan/task-board handoff rather than forcing objectives into the stale scaffold.

Follow `docs/main-guide-writing-conventions.md` for player-facing prose. The current convention is positive route instructions first: use global Route Discipline for broad prohibitions, audit all nearby safe objectives across every objective type, route safe same-location objectives while the player is already there, respect opening Survival stabilization before optional combat detours, time multi-location quest starts relative to the next routed progress point, keep tightly linked quest/location chains intact when splitting them would create artificial partial clears or fragile state, do not hold unrelated safe objectives merely because they share a hold/faction/theme with a later gated objective, keep local warnings rare and route-critical, avoid ordinary combat/loot micromanagement, and keep objective IDs/coverage mechanics in the internal tracker.

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
3. Run a nearby-objective audit for the section's locations, road corridors, hubs, service stops, dungeons, and support tables. Include all objective types: quests, quest progress, locations, collectibles, books/documents, spell tomes, properties, services, mounts, pets, favors, radiants, counters, crafting, investments, and relationship/default rows.
4. Expand the section with explicit instructions for each objective/checklist row. Name the quest, location, NPC, item, book, spell, shout, collectible, counter action, branch outcome, option/default, exclusion, or system output.
5. Preserve all hard gates, hard saves, branch reloads, Survival Mode logistics, and unique-item preservation rules.
6. Add checklist cues at the point of completion/acquisition/verification.
7. Add `NEEDS ROUTE RESOLUTION` notes only for genuinely unresolved rows.
8. Record the rows processed by the pass in `data/guide-coverage/main-guide-v1-coverage.csv` or another clearly internal coverage artifact, including source-backed reasons for nearby objectives held for later.
9. Search the edited section for placeholder phrases before moving on.

## Route-Block Subtasks

The task board should surface the next active pass, but this table is the minimum required work breakdown. Internal MR labels remain useful handles from the prototype, but the actual route-block jurisdiction must follow geography, quest state, and objective-level constraints. No route block is allowed to be treated as "covered" until objective-level expansion for that block is complete and any moved work has been removed from stale later buckets.

| Subtask | Section | Starting source | Required expansion focus | Status |
| --- | --- | --- | --- | --- |
| TB-035P | Prep and standards | Repo docs | Record this plan, reopen TB-035, harden instructions, and point the next task at MR-001. | Done |
| TB-035-MR-001 | MR-001 - Setup And Save Baseline | G00 setup | AE entitlement, mod/Creation restrictions, Legendary/Survival setup, trophy-safe baseline, save policy, explicit exclusions created by setup scope. | Done |
| TB-035-MR-001R | Revise MR-001 player-facing/internal split | MR-001 correction | Remove audit/report prose from the guide, move objective IDs and coverage status to `data/guide-coverage/main-guide-v1-coverage.csv`, and keep MR-001 readable as player instructions. | Done |
| TB-035-MR-002 | Internal MR-002 - Helgen, Riverwood, And First Survival Loop | G01 opening | `Unbound`, `Before the Storm`, Guardian Stones, Riverwood survival support, Alvor support and woodcutter's axe, Alvor `Blacksmithing Tutorial`, first bed/food/sell-off, `The Golden Claw` start, `A Lovely Letter` in Faendal's favor, both forged letters, Faendal follower/steward staging, Embry drunk-favor default, Hero of the People 2/50, opening objective and checklist cues. Holds Treasure Map I for the early economy/Riverwood loop after settlement support stabilizes. | Done; revised for geographic routing and opening stabilization |
| TB-035-MR-003 | Internal MR-003 - First Day In Whiterun | G01 Whiterun first-entry | Whiterun Stables/Whiterun/Dragonsreach discovery, `Before the Storm`, Farengar Dragonstone objective, Adrianne/Proventus greatsword, Farengar/Arcadia frost salts, Arcadia `Alchemy Tutorial`, Carlotta/Mikael, Ysolda and Amren starts, Brenuin beggar and Argonian Ale, Lars/Braith, Andurs/Hall of the Dead Stone, Hulda chop wood, Uthgerd brawl, Hero of the People 9/50, Hard Worker wood 1/3, conditional Snake Tongue Persuade slot, and relationship/default handling. | Done; revised for geographic routing |
| TB-035-MR-004 | Internal MR-004 - Bleak Falls Barrow And Dragon Rising | G01-G02 main quest opener | `Bleak Falls Barrow`, `The Golden Claw` completion after Riverwood start, `Dragon Rising`, first dragon/shout/trophy rows, dragon-world activation warnings, and `In My Time Of Need` availability handoff to the next coherent Whiterun block. | Done; pending user review |
| TB-035-MR-005 | Internal MR-005 - Saadia, First Horse, And Western Road Support | G02 central support | Post-`Dragon Rising` `In My Time Of Need` start and Saadia-default completion, Swindler's Den quest sweep/discovery, first Whiterun horse, Elven Horse Armor, Swindler's Den cooking for Hard Worker 2/3, and economy-supported staging for Breezehome/Tundra instead of assuming early house money. | Done; pending user review |
| TB-035-MR-006 | Internal MR-006 - Guardian Stones Cache And Whiterun Farm Loop | G02 central activities | Routes Treasure Map I camp and Riverwood chest after support stabilizes, learns Clairvoyance from Riverwood Trader, discovers Pelagia Farm, Chillfurrow Farm, and Battle-Born Farm, completes the Alfhild Battle-Born crop-sale representative, advances the Breezehome fund without buying a house prematurely, and records why Embershard/Hard Worker mining/Artificer stay bundled for later. | Done; revised for farm-road coverage |
| TB-035-MR-007 | Internal MR-007 - Halted Stream And Silent Moons Level Gate | G02 level 8 gate | Whitewatch Tower discovery, Halted Stream Camp clear, Hard Worker mining completion, Transmute Mineral Ore, Poacher's Axe, Ysolda Mammoth Tusk completion, conditional Amren turn-in only if the active marker points to Halted Stream, level-8 Silent Moons clear, Lunar weapon exact-form tracking, and Silent Moons Enchant source staging. | Done; pending user review |
| TB-035-MR-008 | MR-008 - Goldenhills Plantation | G02 Goldenhills | `The Unquiet Dead`, Goldenhills ownership, farm operations, staffing, crop/food/income rows, storage caveats. | Done |
| TB-035-MR-009 | MR-009 - Companions Entry | G02-G03 Companions start | Companions opening quests, required early radiant gates, representative radiant rules, faction checklist cues. | Done |
| TB-035-MR-010 | MR-010 - Companions Transformation Window | G03 Companions window | Post-`Proving Honor` radiant gate, `The Silver Hand`, Beast Form/Blood Oath, Gallows Rock, two Aela revenge radiants, and transformation-state staging. | Done |
| TB-035-MR-011 | MR-011 - Falkreath Favor And Lakeview Protection | G03 Falkreath/Lakeview | Siddgeir target branches, Falkreath help, conditional Lakeview land/foundation, Rayya, The Woodsman's Friend, Half-Moon Mill, The Lady Stone, Glenmoril Coven pre-clear, `Blood's Honor`, and conditional carryover for Cracked Tusk/Knifepoint or sub-level-14 saves. | Done |
| TB-035-MR-012 | MR-012 - Southern Warm Corridor | G03 southern sweep | Falkreath/Riverwood/Ivarstead warm-route continuation, conditional MR-011 carryover, Lakeview construction if available, southern locations, books, misc objectives, Survival support. | Done |
| TB-035-MR-013 | MR-013 - Hircine And Bloated Man's Grotto | G03 Hircine setup | Bolar's Oathblade, Bloated Man's Grotto state, Hircine branch save, Savior's Hide branch, Ring of Hircine main route. | Done |
| TB-035-MR-014 | MR-014 - Riften Access | G04 Riften access | First Riften city loop, stables, city favors, fishery setup, skooma-chain start, `A Chance Arrangement` deliberate failure, Ratway items and Skritch, `Taking Care of Business`, `Meet the Family`, Galathil, and property/Frost/Guardian holds. | Done |
| TB-035-MR-015 | Internal MR-015 - Goldenglow, Honningbrew, Solitude, And Snow Veil | G04 Thieves early chain plus forced Solitude visit | `Loud and Clear` through `Speaking With Silence`, Goldenglow/Honningbrew/Snow Veil larceny and book/document rows, Firebrand Wine Case, safe first-Solitude city favors and Blue Palace/Pelagius Wing objectives pulled forward by `Scoundrel's Folly`, Gulum-Ei confession branch save, Thieves job ledger creation at zero jobs, and stop before `Hard Answers` for the level-46 Nightingale Blade gate. | Done |
| TB-035-MR-016 | Internal MR-016 - Riften Thaneship, Frost, And Rift Roads | G04 southeast sweep | Riften Temple/Jail/Meadery handoffs, Ivarstead-linked quest progress, broad Rift clearable and discovery pass, Shor's Stone/Darkwater/Northwind work, `Supply and Demand`, `Promises to Keep`, Frost, Honeyside, Thane of the Rift, Iona, and explicit holds for Shadowfoot, late Thieves, Dawnguard, Daedric, AE, and high-risk bundles. | Done |
| TB-035-MR-017 | Internal MR-017 - Nightingale Armor Readiness Check | G04 level 32 checkpoint | Player-facing level-state check only: record whether level 32 is reached, keep `Hard Answers`, `The Pursuit`, `Trinity Restored`, Riftweald/Chillrend, `Blindsighted`, Nightingale Bow, and `Darkness Returns` closed for the level-46 late Thieves chain, and hand off below-level play to the next routed geography block. | Done |
| TB-035-MR-018 | Internal MR-018 - Reach Setup | G05 Reach setup | Player-facing section is now `Markarth, Nchuand-Zel, And Old Hroldan`: Markarth stable/city/Understone setup, Salvius/Left Hand work activities, Markarth deliveries, `The Forsworn Conspiracy` staged at the Shrine of Talos, Calcelmo/Faleen `The Book of Love` stage, `My Pet Mudcrab`, `Nimhe`, `The Lost Expedition`, Dwemer Museum Stone of Barenziah, The Lover Stone, Soljund's Sinkhole, Old Hroldan setup, and holds for Cidhna/Molag/Namira, Temple of Dibella, property/thane, late Thieves, and Sky Haven/Dragonbane. | Done |
| TB-035-MR-019 | Internal MR-019 - Cidhna, Molag Bal, And Namira | G05 Cidhna/Molag/Namira | Player-facing section is now `Markarth Prison, Daedric Rites, And Reach Redoubts`: Shrine of Talos investigation completion, Cidhna Mine both-reward path, Molag Bal, Degaine/Dibella, Namira branch/main outcomes, Lisbet/Hjalti/Logrolf overlapping target pool handling, Broken Tower, conditional Forsworn redoubts, Liar's Retreat, Blind Cliff, Reachcliff Cave, Red Eagle branch if targeted, and holds for Orc/Forgemaster, Redguard Elite, property/thane, investments, and Sky Haven/Dragonbane. | Done |
| TB-035-MR-020 | Internal MR-020 - Aetherium Setup | G05 Aetherium setup | Player-facing section is now `Arkngthamz And The First Aetherium Shards`: read `The Aetherium Wars` in Markarth, start `Lost to the Ages`, route Arkngthamz through Katria, Zephyr, tonal lock, and the first shard, route Deep Folk Crossing and its shard, and hold Raldbthar, Dwarven Storeroom/Mzulft, Forge reward branches, Aetherial Crown, and Taron Dreth for concrete Dark Brotherhood, College/Eastmarch, branch-save, and post-forge route reasons. | Done |
| TB-035-MR-021 | Internal MR-021 - Daedric Matrix reshaped | G05 Peryite/Bthardamz | Player-facing section is now `Peryite's Shrine And Bthardamz`: deterministic Peryite ingredient staging, Shrine to Peryite, Kesh, Bthardamz, Afflicted's Note, Spellbreaker, and Oblivion Walker 5/15. The remaining Daedric quests from the old matrix are redistributed to their concrete geography, level-gate, branch-save, follower-state, or target-aware route windows. | Done |
| TB-035-MR-022 | Internal MR-022 - Windhelm State And Hjerim reshaped | G06 Windhelm state | Player-facing section is now `Windhelm Murder Investigation And White Phial`: Windhelm farm loop, first-entry `The White Phial`, Wylandriah's Soul Gem, Forsaken Cave, Marked for Death: Aus, direct-Wuunferth `Blood on the Ice`, Palace Stone of Barenziah, Calixto museum uniques, selected Windhelm favors, and explicit Hjerim/property/Eastmarch/AE holds. | Done |
| TB-035-MR-023 | Internal MR-023 - High Hrothgar, Ustengrav, Morthal, And The Embassy | G06 main quest staging plus retrospective Hjaalmarch insertion | Player-facing section is now `High Hrothgar, Ustengrav, Morthal, And The Embassy`: Greybeards training, Klimmek's `Climb the Steps`, Ustengrav, pulled-forward Morthal/Hjaalmarch work (`Laid to Rest`, Movarth's Lair, Hjaalmarch thane, Myrwatch, Stonehills, Windstad land/foundation, linked delivery turn-ins), Horn/Delphine handoff, Map of Dragon Burials, Kynesgrove/Sahloknir, Iddra's Kynesgrove favor, `Diplomatic Immunity`, Embassy/Reeking Cave documents and Stone of Barenziah, `A Cornered Rat`, Esbern-room documents, and `Alduin's Wall` parked before Karthspire/Sky Haven for the level-46 Dragonbane gate. | Done |
| TB-035-MR-024 | Internal MR-024 - Windhelm Follow-Up And Eastmarch Roads | G06 Eastmarch support | Player-facing section is now `Windhelm Follow-Up And Eastmarch Roads`: Malborn's `Find the Thalmor Assassin`, Refugees' Rest, Candlehearth AE starts, `Tilted Scales`, Yorgrim Overlook, `Caught in a Web`, Cronvangr/Arachnia, Riverside Shack/Treasure Map III pickup, Ansilvund/Ghostblade/Stone/Frost Salts, Dravynea, Kynesgrove and Darkwater ore sales, Sondas delivery, conditional Derkeethus/Darkwater Pass, Mara's Eye Pond/Den, `Dreams of the Dead`, Gallows Hall ownership, Staff of Worms, Bloodworm Helm, Helm of Oreyn Bearclaw, Altar/Bone Forge unlock, and explicit holds for randomized retrievals, Stony Creek/Bards, Hjerim/thane, Sam/Morvunskar, and Solstheim. | Done |
| TB-035-MR-025 | Internal MR-025 - Solitude Coast, Dragon Bridge, Wild Horse, And Wolfskull | G07 Solitude prerequisites reshaped plus retrospective Dragon Bridge insertion | Player-facing section is now `Solitude Coast, Dragon Bridge, Wild Horse, And Wolfskull`: Katla crop sale, Solitude Stables `Horse Whisperer`, Map of Wild Horses, `Wild Horse Notes`, Solitude Sawmill/Hjorunn firewood, Dapple Brown Wild Horse, Solitude Lighthouse/Treasure Map III cache, The Steed Stone, Dragon Bridge discovery, Azzada crop sale, Horgeir firewood, `Dragon's Breath Mead`, `Over the Edge`, Steel Soldier armor/documents, Wolfskull pre-quest clear-state protection, `The Man Who Cried Wolf`, `Necromancer's Ritual`, `Elisif's Tribute`, `Lorcalin's Orders`, and explicit holds for Wolf Queen/Shield/Bone Wolf, Proudspire/thane, Captain Aldis, Broken Oar/coast radiants, Treasure Map VIII, and Dainty Sload. | Done |
| TB-035-MR-026 | Internal MR-026 - Bards College, Lost Library, And Instrument Roads | G07 Bards College reshaped | Player-facing section is now `Bards College, Lost Library, And Instrument Roads`: Bards investigation, `Tending the Flames`, Dead Men's Respite, Ruby Dragon Claw, King Olaf's Verse, Whirlwind Sprint Wuld, Bards College checklist books, all three Bards instrument quests, Stony Creek Cave, Ruin's Edge, Treasure Map X, Bliss Bug in a Jar, White Spotted Wild Horse, Hob's Fall Cave, `The Lost Library`, Ancient Tome Chest spells, Halldir's Cairn, Halldir's Staff, and Raise Zombie; Korir and Runil are now left for later isolated random-assignment handling. | Done |
| TB-035-MR-027 | Internal MR-027 - Potema, Shield Of Solitude, And Bone Wolf | G07 Shield gate reshaped | Player-facing section is now `Potema, Shield Of Solitude, And Bone Wolf`: level-40 Falk letter start, Styrr and `Turn Undead`, Potema's Catacombs, `Legend of Krately House` selected-copy pickup, max-tier Shield of Solitude, Blue Palace `Lost Legends`, Folgunthur, Daynas Valen's Journal/Notes, Ivory Dragon Claw, Writ of Sealing (Mikrul), max-tier Gauldur Blackblade, Frost Breath: Krah, Bone Wolf courier follow-up, `Let Sleeping Wolves Lie`, `Necromancer's Journal`, Bone Wolf, and Expanded Crossbow Pack staged for the later crossbow/crafting pass. | Done |
| TB-035-MR-028 | MR-028 - Northwest And Coast Prepared Sweep | G07 remaining northwest sweep | Player-facing section is now `Haafingar Caves, Volskygge, And Night Hunter`: Sybille/Pinemoon, Clearpine, Volskygge/Kest/Volsung, conditional Kahvozein's Fang, Widow's Watch visit, Ironback/Night Hunter, Elite Crossbows base rewards, and Ravenscar. Shadowgreen/Noster, Broken Oar/Ahtar, Dainty Sload, Meridia/Kilkreath, Lost Echo, and Solitude AE/Civil War spaces remain staged. | Done |
| TB-035-MR-029 | MR-029 - Dark Brotherhood Fork | G07 Dark Brotherhood fork | Player-facing section is now `Cicero, Aventus, And The Sanctuary Door`: `Delayed Burial`, Loreius Farm, `Innocence Lost`, Mysterious Note, `HS-DB-ABANDONED-SHACK`, branch-only `Destroy the Dark Brotherhood!`, main-route `With Friends Like These...`, Abandoned Shack, Meeko's Shack/Meeko, first Dark Brotherhood Sanctuary entry, Shrouded sets, Sanctuary Stone, Marked for Death: Lun, and `Sanctuary`/Nazir first-contract pickup. | Done |
| TB-035-MR-030A | Internal MR-030 - First Brotherhood Contracts And Muiri's Revenge | G07-G10 Dark Brotherhood reshaped | Player-facing section is now `First Brotherhood Contracts And Muiri's Revenge`: retrospective Dawnstar/Beitild ore-sale insertion, Nazir's first three contracts, Anga's Mill/Aeri, Aeri's Note delivery, Beitild/Narfi/Ennodius, `Mourning Never Comes`, optional Nilsine, House of Clan Shatter-Shield Stone, Raldbthar, Aegisbane, Raldbthar Aetherium Shard, Great Lift at Raldbthar, Muiri's Ring, and `Whispers in the Dark` start. | Done |
| TB-035-MR-030B | Internal MR-030 continuation - Whispers, Solitude Jobs, And The Wedding Assassination | G07-G10 Dark Brotherhood/Thieves interlock | Completed `Whispers in the Dark`, exactly five Solitude Delvin/Vex jobs, `The Dainty Sload`, Lurbuk/Hern, Volunruud/`Silenced Tongues`, `The Silence Has Been Broken`, Firiniel's End, `Bound Until Death`, Vittoria wedding gear, and Summon Spectral Assassin. | Complete |
| TB-035-MR-030C | Internal MR-030 continuation - Security, Shadowmere, And The Brotherhood Endgame | G10 Dark Brotherhood endgame plus Nightgate AE insertion | Completed `Breaching Security`, Olava's Token, `Locate the Assassin of Old`, Deepwood Redoubt, Hag's End, Predator's Grace, Ancient Shrouded set, Slow Time: Tiid, Bloodthorn, Shadowmere, Dawnstar Sanctuary, Cicero spare-state, `Recipe for Disaster`, Nightgate `Brothers in Irons`, preserved Jarrin Root, `To Kill an Empire`, `Death Incarnate`, `Hail Sithis!`, the Katariah, Dawnstar Sanctuary restoration, hidden treasure, and one representative `The Dark Brotherhood Forever` contract. Retrospective audit moved `Lost Legends`/Folgunthur earlier to the Bone Wolf route; Balbus's Fork remains one unresolved underlying objective, represented by two coverage rows, pending a deterministic random-encounter policy. | Done |
| TB-035-MR-031 | MR-031 - Northern Preflight | G08 north preflight | Player-facing section is now `Dawnstar, Vaermina, And Cold-Weather Setup`: cooks hot food at Dawnstar Sanctuary, crafts Camping Supplies at Dawnstar using Windpeak/Rustleif support, routes Rustleif, Silus's museum start, full `Waking Nightmare`/Nightcaller Temple/Skull branch handling, and Skald's giant-bounty target; Wayfinder and Frida retrievals now remain unstarted for later isolated random-assignment handling. | Done |
| TB-035-MR-032 | MR-032 - College Opening | G08 College opening reshaped | Player-facing section is now `Winterhold, College Entry, And Saarthal`: routes Birna/Coral Claw, College entry/Faralda spell test, Gatekeeper, `First Lessons`, `Out of Balance`, Malur, Whistling Mine/Thorgar, Shrine of Azura/Nelacar, conditional Winterhold thane, `Under Saarthal`, Enchanted Rings, Saarthal Amulet, Writ of Sealing (Jyrik), Staff of Jyrik, Ice Form: Nus, College Stone of Barenziah, `Swift as an Arrow`, Brelyna, J'zargo, `Forgotten Names`, and Velehk's map/cache; retrospectively moves Haran/Ranmir/`Drowned Sorrows` into the earlier Hob's Fall road. | Done |
| TB-035-MR-033 | MR-033 - Dawnstar, Pale Blade, And Heljarchen | G08 Pale/Dawnstar reshaped | Player-facing section is now `Dawnstar, Pale Blade, And Heljarchen`: Leigelf/Karl, Unholy Vigil, Saturalia/Reindeer, Yngvild, Conjure Haunting Spirit fixed-source revision, High Gate/Anska/Vokun, Lord Stone/Frostmere/Pale Blade, all four Pale giant camps, Treasure Map VI and cache, Skald bounty, Thane of the Pale, Gregor, Heljarchen Hall purchase, foundation, and Land Baron; Kharjo is now left unstarted for later isolated random-assignment handling. | Done |
| TB-035-MR-034 | Internal MR-034 - Fellglow Keep And Good Intentions | G08 College continuation | Player-facing section is now `Fellglow Keep And Good Intentions`: completes `Hitting the Books`, Fellglow Stone of Barenziah, fixed-source Sparks, three stolen quest books, Urag reward skill-book preservation, Arniel part-one start, `Good Intentions`, Mage's Circlet, and Tolfdir's alembic; stale level-25 gate removed because route already passed level 40. | Done |
| TB-035-MR-035 | Internal MR-035 - Mzulft And The Winterhold Crisis | G09 College/Mzulft continuation | Player-facing section is now `Mzulft And The Winterhold Crisis`: takes Mirabelle's Mzulft lead, routes Dwarven Storeroom's final Aetherium Shard, collects ten Dwemer Cogs for Arniel, clears Mzulft, acquires `Research Log`, fixed-source `Spell Tome: Flames` and `Spell Tome: Frostbite`, completes `Revealing the Unseen` and `Containment`, receives Savos Aren's Amulet and Torc of Labyrinthian, and starts `The Staff of Magnus`. | Done |
| TB-035-MR-036 | MR-036 - Labyrinthian And The Eye Of Magnus | G09 College finale | Player-facing section now completes Labyrinthian, Lost Valkygg, Shalidor's Maze, `The Staff of Magnus`, `The Eye of Magnus`, College restoration, Arch-Mage state, Wooden Mask, Diadem, Dismay: Maar, Heal Other, Equilibrium, Steadfast Ward, Ancient Helmet, Slow Time: Ul, Staff of Magnus, Morokei, Archmage's Robes, and Arch-Mage's Boots. | Done |
| TB-035-MR-037 | MR-037 - Gauldur Legend Finale | G09 Gauldur finale | Player-facing section is now `Gauldur Legend Finale`: finishes `Forbidden Legend` through Geirmund's Hall and Reachwater Rock, routes `Geirmund's Epitaph`, `Writ of Sealing (Sigdis)`, max-tier Gauldur Blackbow, Emerald Dragon Claw, `Ancient Edict`, The Gauldur Amulet, and Sideways tracking if still open; moves `Words and Philosophy` from Geirmund to the later Apocrypha/The Winds of Change Scholar's Insight source. | Done |
| TB-035-MR-037A | MR-037A - College Errands, Arniel, Septimus, And Aetherium | G09 College side/outcome reshaped | Player-facing section routes representative Sergius/Tolfdir repeatables, finishes `Arniel's Endeavor`, routes Keening and Summon Arniel's Shade, moves Aetherium Forge branches forward from the old Dawnguard bucket, keeps the Aetherial Crown on the main route, starts `Discerning the Transmundane` through Attunement Sphere/Blank Lexicon, and uses the Atronach Forge Fire Salts recipe. Onmund, Urag random-dungeon radiants, master rituals, Blackreach/Oghma, and College vendor tome buying remain staged for concrete skill/target/progression reasons. | Done |
| TB-035-MR-038 | MR-038 - Karthspire, Sky Haven, And Dragonbane | G10 level 46 main quest | Player-facing section is now `Karthspire, Sky Haven, And Dragonbane`: completes `Alduin's Wall`, Karthspire Camp/Karthspire markers, Sky Haven Temple first entry, maximum Dragonbane, Blades armor/sword rows, and `Remanada`; holds Blades recruitment/research and Spell Knight/Crypt of the Heart for concrete follower/random-lair and one-time heart/reward policy reasons. | Done |
| TB-035-MR-039 | MR-039 - Level 46 Thieves Guild Rewards | G10 level 46 Thieves | Player-facing section is now `Nightingale Rewards And The Skeleton Key`: completes `Hard Answers`, `The Pursuit`, `Trinity Restored`, `Blindsighted`, and `Darkness Returns`; routes Nightingale Blade, Chillrend, Nightingale Armor set, Nightingale Bow, Vald's Debt, Spider Control Rod, larceny items, Eyes of the Falmer, Irkngthand, Twilight Sepulcher, and Nightingale Agent default; stages Bronze Water/Fishing, skill books, Calcelmo artifact/investment/vendor rows, and Delvin/Vex restoration jobs for concrete route reasons. | Done |
| TB-035-MR-040 | MR-040 - Guild Restoration And Amulet Of Articulation | G10 Guild restoration | Player-facing section is now `Guild Restoration And Amulet Of Articulation`: completes `Toying With The Dead`, pulls `Possible Rivals`, runs controlled Markarth/Whiterun/Windhelm Delvin/Vex city jobs, covers Fishing and Bedlam job types, completes `Silver Lining`, `Imitation Amnesty`, `Thieves Guild Caravan Fence Quest`, Uttering Hills preclear, `Summerset Shadows`, `Under New Management`, strongest Amulet of Articulation policy, Guild Master's Armor set, 125-job counter, restored Flagon merchants, caravan fences, Shadowfoot Sanctum purchase; stages `Mace Etiquette`, Onmund, Shadowfoot displays/family moves, Bronze Water/Fishing, Blades work, and later branch content for concrete route reasons. | Done |
| TB-035-MR-041 | MR-041 - Civil War Stormcloak Branch | G10 Civil War branch | Stormcloak branch after hard save, branch-only objectives, War Hero/Season Unending warnings, reload. | Pending |
| TB-035-MR-042 | MR-042 - Imperial Civil War | G10 Imperial Civil War | Imperial main route, War Hero-safe fort handling, Hero of Skyrim, Battle of the Champions. | Pending |
| TB-035-MR-043 | MR-043 - Late Main Quest Coordination | G10 main quest coordination | `The Throat of the World` through `The Fallen`, Season Unending skip/contingency, Elder Knowledge/Alduin's Bane rows. | Pending |
| TB-035-MR-044 | MR-044 - Paarthurnax And Blades Branch | G10 Paarthurnax branch | Blades/Paarthurnax branch, Rebuilding the Blades, Dragon Hunting, reload, preserve Paarthurnax. | Pending |
| TB-035-MR-045 | MR-045 - Dawnguard Fork And Volkihar Branch | G11 Dawnguard fork | Bloodline save, Volkihar branch, rings/amulets, Volkihar radiants, `The Gift` conditional, reload/refuse Harkon. | Pending |
| TB-035-MR-046 | MR-046 - Dawnguard Main Route | G11 Dawnguard main | Dawnguard chain, Fort Dawnguard support, representative radiants, Lost Relic filler recording until all three relics. | Pending |
| TB-035-MR-047 | MR-047 - Aetherium Forge Branches | G11 Aetherium Forge | Moved earlier into TB-035-MR-037A because all four shards were ready and the Ruins of Bthalft convector overlapped Arniel's route. Keep this row as a stale-scaffold audit reminder only; do not recreate a later player-facing Aetherium Forge section. | Done |
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
| TB-035-MR-071 | MR-071 - Final Reconciliation | G14 final reconciliation | Final row-by-row coverage summary, trophy/counter boundary checks, unique-item audit, branch-return audit, explicit unresolved rows. | Pending |

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
