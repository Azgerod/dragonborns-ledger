# SN-000207 - Book of Love and Agent of Mara Route

Status: targeted TB-044 route repair source note.

## Claim

`The Book of Love` can be closed deterministically after the earlier Ivarstead and Markarth stages by returning to Dinya Balu, completing the Ruki/Fenrig ghost stage at Gjukar's Monument, then returning to Dinya for the Agent of Mara reward. The reward appears in Active Effects as `Resist Magic`.

## Routing Relevance

The v1 guide had already completed the Fastred/Klimmek and Calcelmo/Faleen portions but left the final Dinya, Ruki, Fenrig, and Agent of Mara reward state open. TB-044 closes that high-severity quest/permanent-ability pair in a late Riften support window before the Whiterun and College return.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001513 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Book_of_Love | 2026-05-28 | Quest stages, Fastred/Calcelmo/Ruki sequence, Agent of Mara reward, and Ruki/Fenrig bug warnings. |
| SRC-001514 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Powers | 2026-05-28 | Agent of Mara active-effect listing and 15% Resist Magic effect. |

## Evidence Summary

UESP's quest page lists the sequence as Dinya in Riften, Fastred in Ivarstead, Calcelmo and Faleen in Markarth, then Ruki and Fenrig. After the Markarth stage, Dinya gives the player an Amulet of Mara for the final ghost stage at Gjukar's Monument. Ruki is at the monument; Fenrig is northwest of Fort Greymoor and south of the small headwater pond. Returning Fenrig to Ruki and then returning to Dinya completes the quest and awards Agent of Mara plus the amulet.

UESP's powers page lists Agent of Mara as a constant ability with 15% Resist Magic and notes that it appears in Active Effects under `Resist Magic`.

The quest page records several Ruki/Fenrig and Amulet of Mara bugs. For PS4 route safety, the guide now creates `HS-MARA-RUKI-FENRIG`, equips the quest amulet at Gjukar's Monument, walks Fenrig back without fast travel, and reloads that save if the scene stalls.

## Route Decision

Place the closure in `Guild Restoration and Amulet of Articulation`, while the player is already based in Riften and before the Whiterun/College return. This keeps the Riften Dinya turn-ins together, gives the route Agent of Mara before later hostile and spell-heavy work, and avoids leaving a quest/permanent-ability pair open until final reconciliation.

## Confidence and Open Questions

Confidence is high for the quest order, Gjukar/Fenrig placement, reward, and Active Effects label. The hard save remains a route safeguard because the final ghost scene has documented bugs and the target platform is PS4.

No open TB-044 route-resolution item remains for `OBJ-000194` or `OBJ-000803` after this repair.

## Linked Records

`OBJ-000194`; `OBJ-000803`; `CHK-QUESTS-0188`; `CHK-PERKS-3678`; `HS-MARA-RUKI-FENRIG`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/constraints/quest-conflicts-hard-saves.md`.
