# tools

Validation and maintenance scripts live here.

Prefer small tools that support coverage checks, checklist mapping, source-note consistency, or other repeatable QA tasks.

Current tools:

| Tool | Purpose |
| --- | --- |
| `validate_all.py` | Runs all lightweight repository validators. |
| `validate_objectives.py` | Basic objective CSV header validation. |
| `validate_coverage.py` | Basic coverage-matrix structure validation. |
| `validate_sources.py` | Basic source workflow structure validation. |
| `validate_books.py` | Book/document location table structural validation. |
| `validate_npc_options.py` | Relationship, household role, follower, pet, and mount option table structural validation. |
| `validate_items.py` | AE item-member table structural validation. |
| `validate_properties.py` | Property detail table structural validation. |
| `validate_locations.py` | Location catalog structural validation. |
| `validate_skills.py` | Skill/perk and individual perk-rank support table structural validation. |
| `validate_enchantments.py` | Enchantment-learning support table structural validation. |
| `validate_alchemy.py` | Alchemy ingredient-effect support table structural validation. |
| `validate_merchants.py` | Merchant investment support table structural validation. |
| `validate_crafting_systems.py` | Practical crafting-system support table structural validation. |
| `fetch_uesp.py` | Fetches UESP pages through the MediaWiki API with a browser User-Agent for source-note research. |
