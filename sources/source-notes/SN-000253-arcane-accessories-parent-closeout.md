# SN-000253 - Arcane Accessories Parent Closeout

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes `OBJ-000693` Arcane Accessories Spell Tome and Robe Set and reconciles the already-routed Ancient Tome Chest spell coverage with the non-unique robe members in `data/items/ae-item-members.csv`.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-001864 | Skyrim:Arcane Accessories | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arcane_Accessories | 2026-05-30 | Creation overview, official summary, vendor/container distribution, Hob's Fall Cave chest, AE journal/start behavior, robe auto-grant removal, and Radiant Raiment note. |
| SRC-000102 | Skyrim:Arcane Accessories Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arcane_Accessories_Items | 2026-05-30 | Robe member list, leveled-list distribution, level thresholds, template exclusion, and spell-tome member list. |
| SRC-000844 | Skyrim:The Lost Library | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Lost_Library | 2026-05-30 | Ancient Tome Chest location, no-journal AE behavior, reward boundary, and all sixteen spell names. |

## Route Decisions

The guide already routes the deterministic spell side of Arcane Accessories in `Bards College, Lost Library, and Instrument Roads`. At Hob's Fall Cave, the player opens the Ancient Tome Chest and reads all sixteen Arcane Accessories spell tomes. UESP records the chest as the fixed Hob's Fall source for every new spell and records `The Lost Library` reward as sixteen spell tomes. The Anniversary Edition behavior no longer puts the quest in the journal, so the player-facing route now treats the chest and learned spells as the completion boundary rather than expecting a visible journal quest.

The robe side should not become a vendor-restock or container-RNG grind. UESP's Creation overview says the robes and spells can appear through vendors and containers, and the item page records the ten robe variants as leveled-list enchanted robes with level thresholds. The same overview notes that the old automatic inventory grant was removed with the Anniversary Edition update and that leveled robes can be purchased at Radiant Raiment. None of those facts creates a fixed, deterministic, full-set acquisition route for the ten robe variants.

For the final guide, the ten robe variants are therefore accounted as non-unique leveled-list apparel members. The route allows natural purchase, loot, use, or storage if a robe appears during normal play, but it does not require reloads, shop cycling, or detours to force every variant. This is consistent with the route's no-reroll policy and with the unique-item preservation rule, because these robes are not unique quest rewards.

The two `Mage Robes` template rows in `data/items/ae-item-members.csv` remain excluded from player routing. UESP identifies them as template items for the enchanted robe versions and says they are not found in game.

## Coverage Summary

This pass closes `OBJ-000693` by marking the spell-tome members complete through the Ancient Tome Chest, marking the ten robe members as non-unique leveled-list apparel accounted by policy, and retaining the two template rows as excluded/internal. It also removes the later College vendor duplicate instructions for the sixteen Arcane Accessories spells, because the guide has already learned them in Hob's Fall Cave.

## Linked Records

OBJ-000568; OBJ-000693; OBJ-000920; OBJ-000978; OBJ-000986; OBJ-000987; OBJ-000991; OBJ-000998; OBJ-001000; OBJ-001004; OBJ-001008; OBJ-001011; OBJ-001013; OBJ-001014; OBJ-001015; OBJ-001016; OBJ-001031; OBJ-001033; ITEM-000001 through ITEM-000028; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/books/spell-tomes-locations.csv`; `data/items/ae-item-members.csv`; `data/constraints/progression-source-selections.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
