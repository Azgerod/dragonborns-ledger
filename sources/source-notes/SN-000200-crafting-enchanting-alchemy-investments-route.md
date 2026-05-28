# SN-000200 - Crafting, Enchanting, Alchemy, And Investments Route

Status: route-writing source note for TB-035-MR-066.

## Scope

This note supports the v1 guide section `Crafting, Enchanting, Alchemy, and Investments`. The pass converts the old scaffold into a progression reconciliation block for practical crafting checks, enchantment learning, alchemy effect discovery, merchant investments, and the Golden Touch checkpoint.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000272 | Skyrim:Enchanting | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting | 2026-05-12 | Arcane enchanter, disenchanting, item destruction, and learned enchantment behavior. |
| SRC-000287 | Skyrim:Enchanting Effects | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting_Effects | 2026-05-12 | Source-listed apparel and weapon enchantment effects. |
| SRC-000294 | Skyrim:Ingredients | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ingredients | 2026-05-12 | Standard, Creation Club, and quest ingredient effect tables. |
| SRC-000296 | Skyrim:Merchants | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Merchants | 2026-05-12 | Invest column, merchant gold, and investment bug notes. |
| SRC-000286 | Skyrim:Speech | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speech | 2026-05-12 | Speech 70, Merchant, and Investor requirements. |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Practical crafting-system list plus Artificer and Hard Worker context. |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-12 | Artificer, Hard Worker, Golden Touch, and related trophy requirements. |
| SRC-000533 | Skyrim:Berit's Ashes | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Berit%27s_Ashes | 2026-05-13 | Berit's Ashes effects, bone meal equivalence, and respawning samples. |
| SRC-000959 | Skyrim:Jarrin Root | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Jarrin_Root | 2026-05-13 | One-copy Jarrin Root identity and alchemy-use consequences. |
| SRC-000973 | Skyrim:Salty Sea-Dogs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Salty_Sea-Dogs | 2026-05-13 | Fine-Cut Void Salts behavior, quest-sample caveats, and bug notes. |
| SRC-001080 | Skyrim:Corrupted Human Heart | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Corrupted_Human_Heart | 2026-05-13 | Spell Knight heart source, transformation choice, and effect profile. |
| SRC-001081 | Skyrim:Simon Rodayne's Heart | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Simon_Rodayne%27s_Heart | 2026-05-13 | Purified heart source, transformation choice, and effect profile. |

## Route Decisions

The practical crafting table confirms actions already routed elsewhere instead of repeating them without purpose. Hard Worker is complete from wood chopping, cooking, and mining. Atronach Forge, Staff Enchanter, Imbuing Chamber, smelting, tanning, cooking, smithing, and alchemy have player-facing actions already in the guide. Artificer still needs an explicit enchanted-item action after the earlier smithing and potion legs, so MR-066 has the player enchant one disposable nonunique item.

The enchantment-learning table names all 54 main-route learnable effects and keeps the four unique-only effects plus the unobtainable Briarheart Geis out of the main route. This follows the project policy that unique items are preserved and not destroyed merely to learn an enchantment.

The alchemy table names all 190 source-listed ingredient records and their effects. Most rows use the source method already selected in `data/constraints/progression-source-selections.csv`. Two quest-ingredient rows are handled as duplicate-effect records rather than extra quest-state actions: Farengar's Frost Salt is the same item as Frost Salts with a different name, and Fine-Cut Void Salts are the same item record as Void Salts except for quest naming. Jarrin Root is routed with a protected hard save and healing because the source says the Astrid sample is the only one available and can be used for alchemy if the Emperor is killed another way.

Corrupted Human Heart and Simon Rodayne's Heart remain `NEEDS ROUTE RESOLUTION` rows. The source pages say both Spell Knight heart variants share the Human Heart and Mort Flesh effects, but the quest transforms one one-time heart into the other. The project still needs to decide whether same-effect discovery is enough for these objective rows or whether an exact-item branch or main-state sacrifice is required.

The investment circuit requires Speech 70, Merchant, Investor, merchant access, and 16,500 gold for the 33 available investments. Bugged Unofficial Patch-only rows and unknown Ashfall's Tear rows remain audit rows rather than main-route actions under official PS4 AE policy.

Golden Touch is placed before final property and material spending because later home/furnishing work can spend down the economy before the 100,000-gold trophy state is observed.

## Coverage Notes

This pass appends MR-066 coverage rows for the practical crafting systems, Artificer, Hard Worker, Golden Touch, all enchantment-learning objectives, all alchemy ingredient-effect objectives, and all merchant investment/audit rows.

Fishing-source alchemy ingredients stay tied to the later Fishing pass before final Experimenter completion. Baking and detailed Hearthfire construction stay tied to the homes section. Corrupted Human Heart and Simon Rodayne's Heart are the only new route-resolution rows introduced here.
