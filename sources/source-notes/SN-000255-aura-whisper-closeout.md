# SN-000255 - Aura Whisper Closeout

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes `OBJ-000762` Aura Whisper by replacing the unsafe Northwind-first word order with a Valthume-first route. It also updates the linked Northwind Summit, Valthume, and Volunruud location/quest rows that supply the three words.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000934 | Skyrim:Aura Whisper | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Aura_Whisper | 2026-05-30 | Three word identities, word-wall locations, and the confirmed Valthume word-order bug. |
| SRC-000666 | Skyrim:Northwind Summit | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Northwind_Summit | 2026-05-30 | Northwind Summit access, dragon-lair state after `Dragon Rising`, and Aura Whisper word wall. |
| SRC-000665 | Skyrim:Northwind Mine | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Northwind_Mine | 2026-05-30 | Lower mine traversal from Shor's Stone, `Death Blow of Abernanit` placement, summit exit, and non-clearable caveat. |
| SRC-001867 | Skyrim:Valthume | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Valthume | 2026-05-30 | Valthume zones, Iron Claw door solution, third opaque-vessel gate, word wall, and word-wall access bugs. |
| SRC-001439 | Skyrim:Evil in Waiting | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Evil_in_Waiting | 2026-05-30 | Valdar route, three Opaque Vessels, Hevnoraak ritual, mask/staff reward, Aura Whisper word reward, and Valthume bug notes. |
| SRC-000930 | Skyrim:Volunruud | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Volunruud | 2026-05-30 | Volunruud layout, Heddic notes, ceremonial weapons, Kvenel chamber, Aura Whisper word wall, and Dragon Priest Dagger. |
| SRC-000931 | Skyrim:Silenced Tongues | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Silenced_Tongues | 2026-05-30 | `Silenced Tongues` start/completion, Eduj/Okin reward, Aura Whisper word reward, door-trigger bugs, and Kvenel loot handling. |

## Route Decisions

UESP maps Aura Whisper words to Laas at Northwind Summit, Yah at Valthume, and Nir at Volunruud. The same Aura Whisper source records a confirmed bug: if the player learns the first word at Northwind Summit or Volunruud before visiting Valthume, Valthume can advance the shout out of order and the remaining word wall can stop functioning. Because this route is for PS4, console-command recovery is not available. The guide therefore must not learn Northwind Summit or Volunruud Aura Whisper before Valthume.

The earlier Riften road section already traversed Northwind Mine from Shor's Stone, but it learned the Northwind Summit word before the later Valthume route. That sequence is now changed. The guide still uses Northwind Mine as a sourced local pass and keeps `Death Blow of Abernanit` closed there for the Scholar's Insight plan, but it explicitly holds Northwind Summit and the word wall until after Valthume.

Valthume becomes the first Aura Whisper source in the Reach/Peryite route. The guide clears `Evil in Waiting`, takes the Iron Claw, uses the Dragon - Hawk - Wolf claw solution, collects the three Opaque Vessels, learns Aura Whisper: Yah from the Valthume word wall before either other Aura Whisper word, performs the ritual, defeats Hevnoraak, and preserves Hevnoraak and Hevnoraak's Staff.

After Valthume, the guide closes the delayed Northwind Summit word as a controlled return from Reach support: travel to Riften/Shor's Stone support, enter Northwind Mine from the lower entrance, climb to Northwind Summit, defeat the dragon, let soul absorption settle before opening menus, learn Aura Whisper: Laas, and clear the dragon lair. This keeps the Northwind location clear and shout word in a bug-safe order.

Volunruud stays in the Dark Brotherhood/`The Silence Has Been Broken` route because that section already sends the player there and bundles `Silenced Tongues`, Heddic's notes, Eduj, Okin, Dragon Priest Dagger, and Aura Whisper: Nir. Since Valthume and Northwind are complete by then, Volunruud safely closes the aggregate shout. The source-listed vampire-follower and Kvenel throne bugs are not active route blockers at this point: the route has not started Dawnguard/Serana, and the existing guide already saves before Kvenel and tells the player to let him move off the throne before killing him.

Unlocking or using Aura Whisper still depends on the route's dragon-soul pool and global shout mechanics. This closeout only resolves learn order and source coverage.

## Coverage Summary

This pass closes `OBJ-000762` and checklist rows `CHK-DRAGON-SHOUTS-0889`, `CHK-DRAGON-SHOUTS-0890`, and `CHK-DRAGON-SHOUTS-0891`. It changes the Riften Northwind step from a premature word-wall completion to an intentional hold, makes Valthume the first word source, adds a post-Valthume Northwind Summit return for Laas and the clear, and leaves Volunruud Nir as the final word.

## Linked Records

OBJ-000762; OBJ-000211; OBJ-000215; OBJ-002106; OBJ-002107; OBJ-002180; OBJ-002182; CHK-DRAGON-SHOUTS-0889; CHK-DRAGON-SHOUTS-0890; CHK-DRAGON-SHOUTS-0891; CHK-LOCATIONS-1167; CHK-LOCATIONS-1281; CHK-LOCATIONS-1283; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/locations/location-catalog.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
