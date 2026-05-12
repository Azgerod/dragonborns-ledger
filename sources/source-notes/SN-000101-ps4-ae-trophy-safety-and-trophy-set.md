# Source Note: PS4 AE Trophy Safety and Trophy Set

Status: researched.

Source note ID: SN-000101

## Claim

Skyrim Special Edition on PS4 uses the Special Edition trophy list, which includes the base game and the Dawnguard, Hearthfire, and Dragonborn add-on trophies by default. Anniversary Edition Creation Club content is trophy-safe official content, but non-Creation-Club Creations and mods disable trophy progress. Creation Club content does not add additional trophies.

## Routing Relevance

The guide must start from a clean, trophy-enabled PS4/PS5 save with official AE Creation Club content only. The route should not install or enable other Creations/mods mid-run, and it should use hard saves before high-risk trophy completions because UESP records occasional PS4 trophy-pop failures.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-12 | Special Edition PS4 list, add-on trophy count, Creation Club achievement note, and PS4 trophy-pop bug note. |
| SRC-000382 | Bethesda Support: Creations and achievements/trophies | 1 - Official | https://help.bethesda.net/app/answers/detail/a_id/39862/~/does-using-creations-disable-achievements/trophies-in-the-elder-scrolls-v%3A | 2026-05-12 | Official Creation Club versus other Creations/Mods trophy-safety rule. |
| SRC-000383 | Bethesda Support: Mods disable achievements/trophies | 1 - Official | https://help.bethesda.net/app/answers/detail/a_id/36635/~/why-am-i-not-earning-achievements-or-trophies-for-the-elder-scrolls-v%3A-skyrim | 2026-05-12 | Official mod-disabled trophy recovery rule. |
| SRC-000384 | PlayStation: The Elder Scrolls V: Skyrim | 1 - Official | https://www.playstation.com/en-us/games/the-elder-scrolls-v-skyrim/ | 2026-05-12 | PlayStation platform page for Skyrim Anniversary Edition and included official content. |

## Evidence Summary

UESP states that Special Edition has a separate achievement/trophy list for Steam, Xbox One, and PS4, and that because Special Edition includes the three major add-ons its list includes the add-on achievements by default. It also states that Creation Club content does not disable achievements and adds no additional achievements.

Bethesda Support confirms the current Creation Club distinction: Creation Club items, including Anniversary Edition bundled content, do not disable achievements/trophies, while other Creations or Mods do. Bethesda also says that after mods have been installed, trophy earning requires removing or disabling the mods and loading a save from before the mods were installed.

UESP records a PS4/Steam bug where an achievement can occasionally fail to unlock even after the in-game requirement is completed; the relevant no-console route response is to reload an earlier save and repeat the trophy action.

## Confidence and Open Questions

Confidence is high for setup rules and the trophy-list boundary. The exact platform UI wording for PS4/PS5 trophy notifications is not route-critical; the route only needs the clean-save rule and hard-save fallback.

## Linked Records

All trophy rows in `data/constraints/trophy-dependencies.md`; setup rule in `docs/guide-specification.md`.
