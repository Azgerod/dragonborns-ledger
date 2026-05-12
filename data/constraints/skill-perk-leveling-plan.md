# Skill, Perk, and Leveling Plan

Status: TB-027 integrated.

Scope: this is a constraint and progression-integration plan, not final route prose. It records hard requirements, risk boundaries, and writer recommendations for all-skills/all-perks, training, Legendary resets, crafting milestones, investments, material staging, and TB-027 route-block placement pressure. Checklist recipe/source-item mapping remains TB-030.

## Queue Disposition

| Input queue | Disposition |
| --- | --- |
| Objective rows `OBJ-002425` through `OBJ-002465` | Represented as hard skill, perk, level-252, Legendary reset, and Skill Master constraints below. |
| `data/skills/skill-perk-catalog.csv` and `data/skills/perk-rank-catalog.csv` | Used for skill/perk rank counts and per-skill reset policy. No new derived prerequisite graph added yet. |
| Enchantment, alchemy, merchant-investment, and practical-crafting catalogs | Represented as completion scope and crafting power-curve constraints. Exact source items, recipes, and checklist mappings remain later work. |
| Trophy, leveled-reward, NPC, bug, radiant, and Survival Mode constraints | Cross-referenced where they affect progression pacing, training access, late level gates, or crafting logistics. |
| Exploit and grind policy | Kept explicit. Fortify Restoration loops, trainer-gold recovery, attack-reload shop restocks, and follower-trainer recovery are not baseline route tools. |

## TB-027 Operating Rules

No new gameplay research was performed for TB-027. This section integrates the source-backed progression constraints already recorded in this file, `survival-mode-constraints.md`, `level-gated-skeleton-v0.md`, `survival-geography-pass-v0.md`, and `main-route-prototype-v0.md`.

| Rule | Route effect | Source notes |
| --- | --- | --- |
| Progression supports gates; it does not erase them. | Add training, crafting, and grind blocks before reward thresholds only when they do not cross the relevant reward, cell-entry, branch, NPC, bug, or Survival constraint. | SN-000092; SN-000094; SN-000119 |
| Planned level-ups require beds. | Place level checks, perk allocation, and attribute allocation at inns, homes, faction beds, or other verified proper beds; camps remain emergency support. | SN-000115; SN-000119 |
| Training is a limited per-level budget. | Use training to smooth slow skills and pre-gate underleveling, but do not depend on training for 90-100 completion or assume unused training carries forward. | SN-000120 |
| Crafting blocks need rest, storage, stations, and merchants. | Place Smithing, Enchanting, Alchemy, construction, and sales loops near safe storage, bed access, stations, and non-exploit restock patterns. | SN-000117; SN-000121; SN-000122 |
| Unique items are not enchantment fodder. | Enchantment learning must use disposable nonunique source items; unique-only or unobtainable effects stay excluded/audit-visible unless the specification changes. | SN-000083; SN-000121; SN-000122 |
| Skill books are progression tools and checklist rows. | Do not casually read every found skill book if it would waste high-skill value; TB-030 should choose exact copies and read timing by skill gap, route locality, and checklist coverage. | SN-000051; SN-000103; SN-000120 |
| Legendary resets are late infrastructure, not early pacing. | Repeated resets begin only after combat alternatives, beds, storage, materials, gold, and final recovery paths exist. The final state must restore every skill to 100. | SN-000119; SN-000120 |
| Transformation perk trees are separate. | Werewolf and Vampire Lord perk grinds are placed with faction/state windows and are not counted as the 251 normal skill perk ranks. | SN-000105 |
| Exploit-adjacent accelerators remain non-baseline. | Fortify Restoration loops, trainer-gold recovery, follower-trainer free training, save/attack/reload restocks, and repeated Lockpicking/Speech reset strategies are excluded baseline or deferred decisions. | SN-000120; SN-000121; SN-000122 |

## Hard Requirements

| Requirement | Objective IDs | Constraint | Routing implication | Source notes | Status |
| --- | --- | --- | --- | --- | --- |
| All skills to 100 | `OBJ-002425` through `OBJ-002443` | Every skill tree must reach 100, and the final completion state should leave every skill at 100 after any Legendary resets. | Route must include natural use, training, books, quest rewards, crafting, and/or grind blocks for all 18 skills. | SN-000081; SN-000119 | needs_review |
| All skill perks | `OBJ-002444` through `OBJ-002462` | All 251 perk ranks across 180 perk nodes are required. Perks still require skill thresholds and prerequisite perks. | Perk allocation must be tracked; saved perk points are acceptable, but final cleanup must assign all ranks. | SN-000081; SN-000082; SN-000119 | needs_review |
| Level 252 target | `OBJ-002463` | Level 252 supplies enough perk points for all 251 skill perk ranks. | The route must include a late all-perks leveling plan beyond normal quest progression. | SN-000119 | needs_review |
| Legendary skill resets | `OBJ-002464` | Legendary resets are required for enough total levels, but each reset temporarily drops a skill to 15 and refunds that tree's perks. | Resets must be staged after combat readiness exists; reset skills must be recovered to 100 before final completion. | SN-000119 | needs_review |
| Survival sleep-gated level-ups | Progression support | In Survival Mode, level-ups require sleeping in a bed. | Perk allocation and attribute checkpoints must be placed near bed access; route should not assume on-the-road level-up menus. | SN-000115; SN-000119 | needs_review |
| Fatigue-sensitive crafting | Crafting support | Fatigue can reduce beneficial potion effectiveness. | Any potion-supported Smithing or Enchanting block should start after sleep/rest checks. | SN-000115; SN-000118; SN-000121 | needs_review |
| Training limits | Skill support | Training is limited to five purchased skill levels per character level; unused opportunities do not carry over; trainers cannot raise a skill past 90. | Use training deliberately after level-ups, with hard saves before expensive blocks; do not rely on training for final 90-100 gaps. | SN-000120 | needs_review |
| Skill books and quest skill rewards | `OBJ-000819` through `OBJ-000909`; quest support rows | One title/read or one quest reward should be counted deliberately; duplicate copies are not separate skill-book completion objectives. | Defer exact book copy and quest-reward timing to route placement, but reserve them as useful high-skill finishers. | SN-000103; SN-000119; SN-000120 | needs_review |
| Skill Master trophy | `OBJ-002465` | First skill reaching 100 satisfies the trophy, but project scope exceeds it. | Check trophy when the first planned skill hits 100; continue all-skills plan. | SN-000103; SN-000081; SN-000119 | needs_review |
| Transformation perk trees | `OBJ-000815` through `OBJ-000818` | Werewolf Mastered and Vampire Mastered require their separate 11-perk transformation trees and are not part of the 251 skill-perk count. | Complete transformation grind before permanent cures or faction/state changes that remove access. | SN-000105 | needs_review |
| Late level gates | `OBJ-002784`; `OBJ-000464`; leveled reward rows | Legendary Dragons begin at level 78, The Ebony Warrior requires level 80, and several unique rewards have maximum tiers at specific lower thresholds. | Leveling plan must coordinate reward delays and late combat readiness; all-perks level 252 is a final completion target, not a reason to rush early overleveling. | SN-000032; SN-000092; SN-000103; SN-000105 | needs_review |
| Enchantment learning | `OBJ-002466` through enchantment rows | Learn all non-destructively learnable enchantments; preserve unique items rather than disenchanting them. | Source-item selection must prefer disposable, nonunique items and mark unique-only/unobtainable effects as excluded audit rows. | SN-000083; SN-000121; SN-000122 | needs_review |
| Alchemy effect discovery | Alchemy effect rows | Discover all source-listed ingredient effects across base game, DLC, and AE Creation ingredients. | TB-030 must select exact ingredient copies and recipe/eating sequence; AE ingredient coverage cannot rely on older base-game-only recipe lists. | SN-000084; SN-000121; SN-000122 | needs_review |
| Merchant investments | `OBJ-002717` through `OBJ-002750` | Source-listed available investments require Speech progression and the Investor perk; bugged/unknown rows remain audit-only until resolved. | Protect merchant NPCs and replacements, acquire Investor before sweeps, and avoid Speech resets that remove Merchant/Fence support during selling blocks. | SN-000085; SN-000108; SN-000120; SN-000122 | needs_review |
| Practical crafting systems | `OBJ-002751` through `OBJ-002755`; support rows | Route must explicitly perform Artificer/Hard Worker actions and representative practical systems such as Atronach Forge, Staff Enchanter, and Imbuing Chamber. | Use low-risk early trophy crafts; save complex recipes, Staff Enchanter, Imbuing Chamber, and checklist-specific outputs for later system placement. | SN-000086; SN-000103; SN-000121; SN-000122 | needs_review |

## Checkpoints

These are planning checkpoints for the later route. They are not final route section headings.

| Route phase | Expected level/skills | Power requirement | Training/grind block | Fallback if underleveled | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Early stabilization | Normal quest and travel leveling; no Legendary resets. | Basic offense, defense, food, bed access, storage, and early crafting stations. | Use only light, local training or skill books when convenient; perform explicit Artificer/Hard Worker actions with disposable materials. | Do nearby safe objectives, harvest materials, craft basic consumables, or train one weak support skill after sleeping. | SN-000103; SN-000115; SN-000120; SN-000121 | planning |
| Before level-gated reward routes | Raise level only as needed for selected reward thresholds; do not enter known lock locations too early. | Character should be strong enough for leveled-reward quest content without overpowered crafting. | Training can fill slow skills near thresholds, but do not consume all late skill books too early. | Delay quest entry, use safe regional objectives, or add a small training/crafting block before the gated quest. | SN-000092; SN-000094; SN-000120 | planning |
| Midgame crafting support | Smithing, Enchanting, and Alchemy become useful but not final-maxed by default. | Gear should keep Legendary difficulty viable without flattening the difficulty curve. | Use gardens, stored ingredients, soul gems, and smithing materials in bounded batches; avoid exploit loops. | Add sleep/rest, material restock, safe merchant sales, or trainer visits before hard combat gates. | SN-000117; SN-000118; SN-000121 | planning |
| Major faction and DLC progression | Combat and utility perks should support chosen questline states; transformation trees need planned access. | Do not reset active combat/armor skills before hard dungeons, Dawnguard/Vampire Lord work, or Dragonborn bosses. | Use paid training and natural quest play for slow support skills; place werewolf/vampire perk grind before permanent cure/final-state decisions. | Pause faction progression for a controlled skill block or temporary gear improvement. | SN-000097; SN-000105; SN-000119; SN-000120 | planning |
| Late level gates | Level 60+ for maximum Miraak rewards, 78+ for Legendary Dragon, 80+ for Ebony Warrior, and eventually 252 for all perks. | Late-game combat build, safe storage, soul/ingredient/material reserves, and travel logistics. | Begin repeatable Legendary reset plan only after stable combat alternatives and crafting infrastructure exist. | Use low-risk repeatable skills, training, crafting, and regional cleanup; avoid Lockpicking and repeated Speech resets as baseline targets. | SN-000032; SN-000092; SN-000103; SN-000105; SN-000119 | planning |
| Final completion sweep | All skills at 100, all 251 perk ranks assigned, all available investments complete, all planned crafting systems checked. | Final power can be high; trophy and unique preservation remain protected. | Complete remaining Legendary recovery, training gaps below 90, skill-book finishers, source-item disenchanting, alchemy effects, and crafting outputs. | If still short, add bounded late grind blocks with explicit before/after checks and no new route dependencies. | SN-000119; SN-000120; SN-000121; SN-000122 | planning |

## Route-Block Progression Overlay

These rows are TB-027 placement pressure for route blocks `G00` through `G14`. They do not replace objective placement, checklist mapping, branch routing, or final warning prose.

| Block | Progression role | Training, crafting, and economy work | Reset/grind policy | Fallback use |
| --- | --- | --- | --- | --- |
| G00 Setup | Record Survival, Legendary, official AE scope, and no-mod/trophy baseline before any skill planning. | No in-world crafting or leveling. Explain that Camping Supplies are system coverage only until materials and forge/anvil access exist. | No resets or grind. | None. |
| G01 Opening warm core | Establish basic combat competence, first food/bed loop, and first carry discipline. | Use only route-natural tutorial crafting, food cooking, and sell-off. Save Artificer/Hard Worker completion for a controlled early station if the exact actions are not already safe. | No resets. Avoid deliberate non-combat overleveling. | If short of early levels, use nearby safe objectives, sleep, and light training rather than cold travel or high-risk AE starts. |
| G02 Central carry/storage | First practical training, crafting, food, storage, and merchant block. | Complete low-risk Artificer/Hard Worker actions when disposable materials and stations are available; begin material, ingredient, soul gem, and disposable enchanted-item storage. | No Legendary resets. Avoid final-max crafting. | Primary fallback before level 8 and a safe filler source before later central gates. |
| G03 Southern warm expansion | Build warm-route durability, property/material staging, and controlled combat growth. | Use Falkreath/Ivarstead-side inns, vendors, mines, food, and Lakeview-adjacent material planning only after property/NPC constraints are clear. | No resets. Do not use Hircine/Bloated Man's Grotto as casual grind support. | Warm fallback before levels 25, 27, 32, and 36 if local constraints are clear. |
| G04 Riften/southeast support | Add Thieves-side economy, Sneak/Pickpocket/Speech support, and later investment preparation. | Use Riften services and sales loops after NPC and faction constraints are checked; do not perform investment sweeps until Speech 70 and Investor are active. | No repeated Speech reset. Pickpocket/Sneak resets are late-only candidates, not early Thieves pacing. | Good fallback before 32 and 46 without starting `Trinity Restored` too early or accepting late reward handoffs. |
| G05 Western Reach and road inns | Support Smithing/material, Dwemer-style carry, and western combat readiness without crossing Sky Haven. | Stage heavy materials through storage and road-inn endpoints; use Markarth services after NPC/quest-state checks. | No combat/armor resets before Reach dungeons. | Usable before 40 or 46 only if Sky Haven, Cidhna, and Daedric branch risks remain closed. |
| G06 Eastmarch/Windhelm ferry hub | Build ferry, merchant, service, and future Solstheim preparation. | Use Windhelm services, sales, and training only after Blood on the Ice, Civil War, and NPC constraints are checked. Prepare ferry gold, food, hot soup ingredients, and carry relief. | No resets immediately before ferry or cold/coastal travel. | Safe filler before 46 or 60 if Windhelm state is controlled and no Solstheim overextension occurs. |
| G07 Solitude/northwest city/coast | Add Speech/Bards/service support, coastal readiness, and later investment/instrument pressure. | Use Solitude services and merchant planning while preserving Bards instrument assignment, Erikur-sensitive Thieves work, and Shield of Solitude timing. | Avoid Speech reset before investment and major selling work. | Fallback before 40 or 46, but do not take Falk's reward early. |
| G08 Pale/Winterhold prepared sweep | Advance mage skills, College support, and cold-region readiness under level-gate control. | Use College/Winterhold services, spell acquisition, and magic training only when the current Saarthal/Forbidden Legend lock is preserved. Oghma read/use stays late, not S05/S08 convenience. | Magic-skill resets are not active yet; build access and cost support first. | Fallback before 25, 27, 32, or 36 only through safe non-linked objectives and prepared cold logistics. |
| G09 Level-36 linked-dungeon loop | Convert the level-36 linked-dungeon gate into a controlled progression and reward block. | Enter rested, fed, warm, and with empty carry; use post-dungeon sell-off and training if needed. | No resets inside the linked-dungeon loop. | Opens only after 36; can support progress toward 40 and 46 once linked rewards are safe. |
| G10 Level-46 classic reward loop | Consume maximum-tier classic rewards and stabilize late combat power. | Pair reward quests with bed, storage, merchant, soul gem, and crafting review. Do not let final crafting outpace the intended difficulty curve. | No resets before reward dungeons. After rewards are secured, begin evaluating late reset infrastructure. | Main fallback before 60 once 46+ rewards are safely available. |
| G11 Dawnguard expedition | Support Dawnguard, transformation windows, Restoration/Archery growth, and branch-save logistics. | Place werewolf or vampire-form perk work only inside validated faction/state windows. Use Dawnguard services and radiants within source boundaries. | Do not reset active offense, armor, Restoration, or transformation-relevant support before Dawnguard hard content. | Fallback before 60, 78, or 80 if branch constraints are preserved and expedition support exists. |
| G12 Solstheim/Raven Rock spine | Support Dragonborn, Black Books, Staff Enchanter, Imbuing Chamber, island ingredients, and late magic/crafting systems. | Use Raven Rock as the restock spine; treat Severin as storage only after acquisition/storage validation. Staff Enchanter and Imbuing Chamber belong here or later when access and materials align. | Magic/crafting resets may begin only after safe bed/storage/material infrastructure and non-reset combat options exist. | Main fallback before 60 and a strong post-60 source of late progression before 78/80. |
| G13 Separate-worldspace/AE high-risk expeditions | Add manually validated high-risk progression only with exit/recovery paths. | Carry only required materials/items, sleep before entry, and route recovery after exit. Avoid final gear assumptions unless the block explicitly needs them. | No resets immediately before or inside separate-worldspace expeditions. | Fallback only after parent quest access and manual validation; never from counts alone. |
| G14 Late cleanup by corridor | Finish level 252, Legendary reset recovery, final crafting, investments, enchantment learning, alchemy effects, skill books, and remaining perk allocation. | Use established bases, merchant circuits, gardens/farms, material stockpiles, disposable enchantment sources, and final checklist synchronization. | Repeated reset loop lives here. Final state must restore all 18 skills to 100 and allocate all 251 normal perk ranks. | Final fallback for 78, 80, and 252 after route-safe objectives and earlier bounded options are exhausted. |

## Underleveled Fallback Register

These are bounded fallback blocks for route writers. They are not permission to cross hard gates or to add uncited grind procedures.

| Checkpoint | Preferred fallback | Do not use as fallback | Release condition |
| --- | --- | --- | --- |
| Before level 8 | G02 local safe objectives, first bed/training check, low-risk food/crafting/material actions. | Silent Moons first loot/clear, cold sweeps, broad Daedric or AE starts. | Level 8 reached; Silent Moons/Lunar handling can be validated. |
| Before level 25 | Warm G02/G03/G04 filler, safe faction setup, local training after sleep, modest crafting/sales. | `Good Intentions` reward report, early Oghma read/use, final mage reward handoff. | Level 25 reached before Mage's Circlet reward claim. |
| Before level 27 | Continue warm/city-backed filler, safe training, material staging, and non-Pale reward objectives. | The Pale Blade claim/resolution or unsafe Frostmere/Kharjo target handling. | Level 27 reached and Pale Blade/Kharjo constraints checked. |
| Before level 32 | Riften/Thieves support that stops before `Trinity Restored`, city services, safe regional objectives. | Starting `Trinity Restored` or taking any late Nightingale reward handoff. | Level 32 reached for Nightingale armor-safe start. |
| Before level 36 | Warm or city-backed objectives, safe College access that does not cross the current linked-dungeon lock, training/crafting near beds. | Reading `Lost Legends` or pre-36 Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock handling under current constraints. | Level 36 reached; G09 linked-dungeon loop can be prepared. |
| Before level 40 | G09 post-36 linked work, Solitude/Bards support that avoids Falk reward handoff, controlled regional objectives. | Falk's final Shield of Solitude reward before 40. | Level 40 reached before reward handoff. |
| Before level 46 | Post-40 city, faction, regional, and crafting support that keeps Riftweald, Sky Haven, and source-tier Nightingale handoffs closed. | Riftweald Manor first entry, Sky Haven Temple first entry, Nightingale Blade/Bow reward handoffs. | Level 46 reached; G10 reward loop opens. |
| Before level 60 | G10 rewards, Dawnguard progression, supported Solstheim side work, high-level AE only after access checks, bounded training/crafting. | Final Miraak battle/corpse appearance. | Level 60 reached; final Miraak reward tier opens. |
| Before level 78 | Post-60 Dragonborn, Black Books, high-risk AE, transformation perk work, late crafting and first repeatable reset cycles if infrastructure exists. | Legendary Dragon hunt before 78 or resets that remove combat readiness. | Level 78 reached with a combat-ready dragon-hunt block. |
| Before level 80 | Same late support as level 78, plus short bounded training/crafting or cleanup if the route is only slightly short. | Ebony Warrior trigger/engagement before 80. | Level 80 reached with final combat checks. |
| Before level 252 | G14 repeated reset loop using the approved reset pool, final training below 90, skill-book/Oghma finishers, crafting, sales, and checklist-safe cleanup. | Repeated Lockpicking/Speech reset baseline, exploit loops, or ending with any reset skill below 100. | Level 252+ reached, every skill restored to 100, and all 251 normal perk ranks allocated. |

## Perk Accounting

| Skill | Target perks | Natural progression assumption | Legendary/reset plan | Notes | Status |
| --- | ---: | --- | --- | --- | --- |
| Alteration | 14 | Likely grows through utility casting, mage questing, and training. | Good late reset candidate after spell access and Magicka/cost support exist. | Ritual spell objective requires Alteration 90; do not spend all high-value boosts before that gate. | needs_review |
| Conjuration | 16 | Grows through summons, bound weapons, soul trap support, and College work. | Good late reset candidate once strong spells and Magicka support exist. | Conjuration can preserve combat power through summons, but reset timing still needs safe combat support. | needs_review |
| Destruction | 17 | Grows through combat casting and training; slower if weapon-first route dominates. | Avoid repeated resets unless another offense plan is already strong. | Combat damage skill; resetting before hard fights is risky. | needs_review |
| Enchanting | 13 | Grows through disenchanting, enchanting crafted/looted items, recharging, and staff-enchanting support. | Candidate late reset only after knowledge capture and before final gear crafting; recover to 100 for Extra Effect final gear. | Disenchanting destroys source items; final dual-effect gear must be made after Extra Effect is available. | needs_review |
| Illusion | 13 | Grows through utility/control spells and training. | Good late reset candidate after spell and cost support exist. | Master of the Mind is source-listed as a permanent effect after reset, but exact route use still needs verification. | needs_review |
| Restoration | 13 | Grows through healing, undead spells, Dawnguard content, and training. | Possible late reset, but avoid before Dawnguard/undead-heavy content if healing is core defense. | Restoration supports Survival no-health-regeneration pressure and vampire/undead contexts. | needs_review |
| Archery | 16 | Grows naturally if bows/crossbows are part of combat and Dawnguard work. | Avoid repeated resets until late; never reset alongside all other offense. | Weapon XP is not improved by tempering/enchantment damage; plan needs real target/combat volume. | needs_review |
| Block | 13 | Grows through shield/two-handed blocking in combat and training. | Avoid repeated resets; reset only when armor/offense can absorb the temporary loss. | Defensive skill reset can be dangerous on Legendary. | needs_review |
| Heavy Armor | 12 | Grows through being hit while wearing heavy armor and training. | Avoid repeated resets; not simultaneous with Light Armor and Block if defense depends on armor. | Final perk acquisition may require wearing full heavy sets for some perk utility. | needs_review |
| One-handed | 21 | Grows naturally if it is a primary combat style. | Avoid repeated resets unless alternate offense is established. | Highest rank count in the catalog; all weapon-style perks still required even if final build favors one style. | needs_review |
| Smithing | 10 | Grows through forging and tempering; material stockpiles and value matter. | Strong late reset candidate if materials and gold loop are planned, but avoid early max-crafting. | Arcane Blacksmith at 60 and Dragon Armor at 100 are important staged gates; Stalhrim and AE forging can be quest-gated. | needs_review |
| Two-handed | 19 | Grows naturally if used; otherwise likely needs training or deliberate combat blocks. | Avoid repeated resets unless alternate offense is established. | All style branches still need perks even if final build is not two-handed. | needs_review |
| Alchemy | 15 | Grows through potion/poison brewing, gardens, greenhouse/farm support, and ingredient discovery. | Strong late reset candidate after effect knowledge and material supply are secured. | Experimenter can reveal effects and then be reset without forgetting them; Fortify Restoration loop is not baseline. | needs_review |
| Light Armor | 10 | Grows through being hit while wearing light armor and training. | Avoid repeated resets; do not reset together with primary defensive alternatives. | Coordinate with Nightingale and armor-type reward behavior. | needs_review |
| Lockpicking | 11 | Grows from first-time lockpicking, broken picks, books, and training. | Do not use as repeated Legendary reset target; no reset or at most one late reset unless route proves enough new locks remain. | Previously picked locks do not grant XP again; Skeleton Key break prevention removes broken-pick XP. | needs_review |
| Pickpocket | 12 | Grows through pocketing/reverse-pickpocketing and can support Thief trophy. | Possible late reset candidate, but training/gold recovery loops are exploit-adjacent and not baseline. | Track 50 pockets for trophy separately from skill 100. | needs_review |
| Sneak | 13 | Grows through stealth movement and sneak attacks during route play. | Possible late reset candidate if stealth remains safe after reset. | Avoid early overleveling through isolated stealth grind before combat is stable. | needs_review |
| Speech | 13 | Grows through selling, buying, persuasion, bribe/intimidate checks, and training. | Prefer no repeated resets; if reset at all, do it after investments and major selling/fence work. | Investor investments persist, but losing Merchant/Fence temporarily changes sales routing. | needs_review |

## Legendary Reset Baseline

This is the TB-027 reset policy for the prototype. Exact repetition counts remain a late-route calculation because they depend on natural quest experience, training use, skill-book timing, Oghma timing, and the final checklist route.

| Reset category | Skills | Baseline use | Safety condition |
| --- | --- | --- | --- |
| Preferred repeated reset pool | Alchemy, Smithing, Enchanting, Alteration, Conjuration, Illusion | Use in G14 and cautiously late G12-G13 only after supplies, spells, gold, beds, and recovery paths exist. | Never reset all combat support at once; recover each reset skill before final verification. |
| Conditional one-or-more reset pool | Restoration, Sneak, Pickpocket | Use only if the route needs additional levels after safer crafting/magic cycles, and only when faction/trophy/state risks are controlled. | Restoration cannot be dropped before undead-heavy or Survival recovery blocks; Pickpocket cannot rely on trainer-gold recovery as baseline. |
| Combat/defense emergency reset pool | Archery, One-handed, Two-handed, Destruction, Block, Heavy Armor, Light Armor | Avoid repeated resets. Use only after a separate offense/defense plan can carry Legendary combat. | Do not reset primary offense, armor, and Block together; do not enter hard combat while the active build is hollowed out. |
| Avoid repeated reset baseline | Lockpicking, Speech | No repeated baseline reset. Lockpicking has finite useful XP pressure; Speech controls investments, selling, Merchant/Fence support, and travel economy. | At most one late, explicitly justified reset after route proof; never as the normal all-perks engine. |

## Crafting and Completion Scope

| Area | Hard scope | Recommended timing | Source notes | Status |
| --- | --- | --- | --- | --- |
| Enchantment learning | 54 main-route learnable effects; four unique-preservation exclusions; one unobtainable exclusion. | Accumulate disposable source items gradually; perform final disenchanting check before unique-item cleanup. | SN-000083; SN-000122 | needs_review |
| Alchemy effect discovery | 190 source-listed ingredient records across base game, DLC, and AE Creation content. | Use eating, recipes, Experimenter, gardens/greenhouses/farms, and source-specific ingredients; exact route recipes deferred. | SN-000084; SN-000121; SN-000122 | needs_review |
| Merchant investments | 33 available investment rows; bugged/unknown rows remain audit-visible. | Do after Speech 70 and Investor, before any Speech reset, and while relevant merchants/replacements are alive and accessible; TB-030 maps the exact merchant circuit. | SN-000085; SN-000108; SN-000122 | needs_review |
| Artificer | Make one smithed item, one enchanted item, and one potion. | Do early with low-risk materials, then continue broader crafting plan later. | SN-000103; SN-000121 | needs_review |
| Hard Worker | Chop wood, mine ore, and cook food. | Do early in a controlled settlement or mine visit; Survival food planning makes cooking naturally useful. | SN-000103; SN-000113; SN-000121 | needs_review |
| Hearthfire construction | Build all three Hearthfire houses and all wings for Master Architect; material plan needed. | Stage materials through safe storage and transport infrastructure rather than carrying everything at once. | SN-000030; SN-000105; SN-000117; SN-000121 | needs_review |
| Atronach Forge | Practical system objective exists. | Use a representative recipe after access is safe; exact recipe/output deferred to checklist mapping. | SN-000086; SN-000121 | needs_review |
| Staff Enchanter | Practical system objective exists. | Use after Solstheim/Tel Mithryn or other safe access; do not rely on patched Myrwatch XP bug. | SN-000086; SN-000121 | needs_review |
| Imbuing Chamber | Practical system objective exists. | Use during Dragonborn/White Ridge Barrow or cleanup when ingredients and access align. | SN-000086; SN-000121 | needs_review |
| Smelting, tanning, mining, cooking, baking, and support actions | Represented as route actions or system coverage rather than fake finite completion rows. | Place where materials are naturally needed; checklist may add specific outputs later. | SN-000086; SN-000113; SN-000121; SN-000122 | needs_review |

## Exploit and Grind Policy

| Method | Baseline treatment | Reason | Source notes | Status |
| --- | --- | --- | --- | --- |
| Fortify Restoration crafting loop | Not baseline. | It can produce extreme Alchemy/Smithing/Enchanting results and violates the gradual power-curve default unless explicitly approved as late optional cleanup. | SN-000121 | deferred_decision |
| Trainer-follower free training | Not baseline. | UESP treats it as an exploit/fix-dependent behavior and official PS4 route planning should not depend on it. | SN-000120 | excluded_baseline |
| Trainer-gold pickpocket recovery | Not baseline. | It creates crime, failure, and overleveling risks and can leave combat underdeveloped. | SN-000120 | excluded_baseline |
| Save/attack/reload merchant restock | Not baseline. | It is a restock exploit; normal 48-hour restock or route-natural merchant circuits are preferred. | SN-000121 | excluded_baseline |
| Essential-target weapon grind | Not baseline yet. | It may be efficient but is grind-like and target-specific; route should first use natural combat, training, and bounded late cleanup. | SN-000119 | deferred_decision |
| Repeated Lockpicking Legendary resets | Not baseline. | Useful locks are finite because already picked locks do not grant XP again. | SN-000119 | excluded_baseline |
| Repeated Speech Legendary resets | Not baseline. | Speech checks are mostly one-time, buying/selling requires large value turnover, and losing Merchant/Fence affects route logistics. | SN-000119; SN-000122 | excluded_baseline |

## TB-027 Result and Handoff

TB-027 integrates progression at the route-block layer. It does not create final route steps, choose every trainer, select every skill-book copy, choose every enchantment source item, or map every checklist row.

Later passes should:

* TB-028/TB-029: choose branch defaults before placing branch-sensitive transformation, artifact, and faction-state grind windows;
* TB-030: choose exact skill-book copies, spell-tome sources, disposable enchantment source items, alchemy recipes/ingredient copies, investment circuit, crafting outputs, and checklist cues;
* TB-032: convert gate and reset risks into concise warning prose at the exact route steps;
* TB-033: validate that every gate, Survival support point, perk rank, skill recovery, investment, crafting system, enchantment, alchemy effect, and final all-skills/all-perks condition is satisfied.
