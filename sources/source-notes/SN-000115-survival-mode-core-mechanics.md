# Source Note: Survival Mode Core Mechanics

Status: researched.

Source note ID: SN-000115

## Claim

The main route must treat Survival Mode as a constant routing constraint after `Unbound`: hunger, fatigue, cold, reduced carry capacity, sleep-gated level-ups, no natural health regeneration, diseases/afflictions, and shrine changes all affect objective placement and preparation.

## Routing Relevance

Survival Mode turns normal route gaps into resource and safety checks. Route blocks need food, sleep, warmth, carry relief, cure access, and bed access before long trips, dungeon chains, crafting sessions, level-ups, or cold-region sweeps. TB-020 also needs this note because fatigue reduces beneficial potion strength and leveling requires sleeping in a bed.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Main Survival Mode feature list and route-relevant tips. |
| SRC-000416 | Skyrim:Cold | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Cold | 2026-05-12 | Cold, warmth, freezing water, and cold penalties. |
| SRC-000417 | Skyrim:Hunger | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hunger | 2026-05-12 | Hunger, food, hot soup, raw food, and stamina/weapon penalties. |
| SRC-000418 | Skyrim:Fatigue | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fatigue | 2026-05-12 | Fatigue, sleep recovery, outdoor-sleep cap, potion penalties, and regeneration penalties. |
| SRC-000421 | Skyrim:Inns | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Inns | 2026-05-12 | Inn lodging, food, 10-gold room rental, and Well Rested support. |

## Evidence Summary

UESP states that most Survival features are disabled until after `Unbound`, while the project specification requires Survival Mode on for the main route. Survival Mode hunger reduces available stamina and weapon effectiveness over time; cooked food restores more hunger than uncooked food, raw meat can cause Food Poisoning, and hot soups reduce cold while adding warmth.

Fatigue reduces available magicka, beneficial potion effectiveness, and magicka/stamina recovery. Indoor beds restore fatigue and can grant Rested or Well Rested, while outdoor sleeping cannot fully clear fatigue and can leave the character Drained. Survival Mode also requires sleeping in a bed to level up.

Cold reduces available health, movement speed, lockpicking, and pickpocketing, and maximum cold can kill. Warmth comes from suitable apparel and temporary aids such as torches and hot soup. Freezing water immediately increases cold and deals health damage until the player exits the water, unless protected by specific fire effects.

Survival Mode lowers initial carry weight from 300 to 150, gives weight to lockpicks and Anniversary Edition arrows, makes over-encumbrance drain stamina and increase fatigue faster, and halves the carry-weight benefit from Extra Pockets and the Steed Stone to 50 each. It also removes normal health regeneration, makes disease and affliction management more important, and changes shrines so most require a gold offering while fatigue can weaken blessing effects.

## Confidence and Open Questions

Confidence is high for the core mechanics and their route impact. Later route and TB-020 work still need to choose exact food defaults, race/default character assumptions, carry-capacity thresholds, shrine timing, and crafting/rest cycles. Those should be recommendations or route decisions, not new mechanics.

## Linked Records

`data/constraints/survival-mode-constraints.md`; TB-019; TB-020.
