# Skill, Perk, and Leveling Plan

Status: TB-021 reviewed.

Scope: this is a constraint plan, not route prose. It records hard requirements, risk boundaries, and writer recommendations for all-skills/all-perks, training, Legendary resets, crafting milestones, investments, and material staging. Exact route placement belongs to TB-027 and checklist recipe/source-item mapping belongs to TB-030.

## Queue Disposition

| Input queue | Disposition |
| --- | --- |
| Objective rows `OBJ-002425` through `OBJ-002465` | Represented as hard skill, perk, level-252, Legendary reset, and Skill Master constraints below. |
| `data/skills/skill-perk-catalog.csv` and `data/skills/perk-rank-catalog.csv` | Used for skill/perk rank counts and per-skill reset policy. No new derived prerequisite graph added yet. |
| Enchantment, alchemy, merchant-investment, and practical-crafting catalogs | Represented as completion scope and crafting power-curve constraints. Exact source items, recipes, and checklist mappings remain later work. |
| Trophy, leveled-reward, NPC, bug, radiant, and Survival Mode constraints | Cross-referenced where they affect progression pacing, training access, late level gates, or crafting logistics. |
| Exploit and grind policy | Kept explicit. Fortify Restoration loops, trainer-gold recovery, attack-reload shop restocks, and follower-trainer recovery are not baseline route tools. |

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

## Crafting and Completion Scope

| Area | Hard scope | Recommended timing | Source notes | Status |
| --- | --- | --- | --- | --- |
| Enchantment learning | 54 main-route learnable effects; four unique-preservation exclusions; one unobtainable exclusion. | Accumulate disposable source items gradually; perform final disenchanting check before unique-item cleanup. | SN-000083; SN-000122 | needs_review |
| Alchemy effect discovery | 190 source-listed ingredient records across base game, DLC, and AE Creation content. | Use eating, recipes, Experimenter, gardens/greenhouses/farms, and source-specific ingredients; exact route recipes deferred. | SN-000084; SN-000121; SN-000122 | needs_review |
| Merchant investments | 33 available investment rows; bugged/unknown rows remain audit-visible. | Do after Speech 70 and Investor, before any Speech reset, and while relevant merchants/replacements are alive and accessible. | SN-000085; SN-000108; SN-000122 | needs_review |
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

## TB-027 Handoff

Later route integration should:

* choose a conservative early combat build and attribute distribution before adding non-combat overleveling;
* decide which skills carry repeated Legendary resets and which should remain no-reset or one-reset;
* attach training blocks to bed/rest access and trainer availability;
* keep all known level-gated rewards and cell-entry locks visible when placing skill grinds;
* place crafting blocks near storage, merchant, bed, and station access;
* keep all exploit-adjacent methods optional or excluded unless the user explicitly changes policy;
* finish with a checklist that verifies all skills 100, level 252+, all 251 perk ranks allocated, all available investments made, enchantments learned, alchemy effects discovered, and practical crafting systems performed.
