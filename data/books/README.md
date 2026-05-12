# data/books

Book and document reference tables live here.

Use this layer for source-backed member inventories and all known acquisition locations before route placement chooses a specific copy. The objective database can contain one row per required unique title, while the location tables preserve every source-listed copy that may be useful for routing.

Do not use this directory for final guide prose.

## Row Policy

Book/document objective rows are title-level completion targets. Duplicate physical copies, vendor sources, quest rewards, and other acquisition routes belong only in the location/acquisition tables as route candidates.

Aggregate, collection, or series pages are not completion objectives by themselves. If a series is in scope, each in-scope member title should have its own objective row and acquisition rows. If a member title is outside the current source-backed scope, leave it deferred until checklist mapping or a later explicit expansion task promotes it.

## Files

* `book-locations.template.csv` defines the shared header for book/location tables.
* `skill-books-locations.csv` records every UESP-listed copy/location for each required skill book title. Duplicate copies are route candidates only, not separate completion objectives.
* `spell-tomes-locations.csv` records source-listed acquisition candidates for each required spell tome title, including merchant, found, quest reward, crafting, pet-recruitment, and generic random-loot sources where sourced. Duplicate acquisition sources are route candidates only, not separate completion objectives.
* `book-document-locations.csv` records source-listed acquisition candidates for required Black Books, quest books, unique books, AE books, and other checklist-scoped documents. Broad quest-document and AE-document passes are split into reviewable child tasks.
* `book-document-reconciliation.md` summarizes the current source-index coverage, explicit exclusions, and checklist-dependent deferrals for book/document work.

In book-location tables, `source_content` describes the content source of that specific copy or acquisition location. A base-game skill book may therefore have a Dragonborn, Dawnguard, or AE Creation copy listed as a route candidate while the objective row itself remains `base_game`.
