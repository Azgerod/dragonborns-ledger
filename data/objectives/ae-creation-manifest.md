# AE Creation Manifest

This is a parent-package manifest for the official Anniversary Edition / Anniversary Upgrade Creation Club bundle. It is not a route draft and does not replace later child objective rows for quests, unique items, homes, pets, mounts, spells, ingredients, crafting systems, locations, conflicts, bug risks, or level gates.

Primary support is `SN-000035-ae-bundle-membership-and-parent-inventory.md`, which cites Bethesda's official Anniversary Edition bundle article plus UESP's Creation Club inventory and cross-check pages. Every package below currently maps to one parent objective row in `objectives.csv`.

## Scope Rules

* Include only official AE Creation Club bundle content.
* Exclude later Verified Creator Program content and other non-AE Creations.
* Treat package-level start/acquisition hints as discovery notes only until detailed child passes validate route-ready triggers, level gates, conflicts, bugs, and rewards.
* Keep this manifest synchronized with parent rows `OBJ-000479` through `OBJ-000552`.

## Child Coverage

* `OBJ-000553` through `OBJ-000658` are source-list child rows for AE quest-bearing Creation content.
* Those child rows cite `SN-000036-ae-creation-quest-inventory.md`.
* Exact quest starts, prerequisites, completion stages, branches, rewards, bugs, and Survival Mode route implications remain deferred to later AE detail and constraint passes.
* `OBJ-000659` through `OBJ-000668` are source-list child rows for AE homes, Goldenhills Plantation, and Goldenhills farm operations.
* Those property rows cite `SN-000037-ae-homes-farm-property-systems.md`.
* Exact acquisition timing, safe-storage policy, display audit, family movement, farm steward/farmhand defaults, farm upgrade policy, and construction material planning remain deferred.
* `OBJ-000669` through `OBJ-000679` are source-list child rows for AE pets and creature followers.
* Those pet and follower rows cite `SN-000038-ae-pets-and-creature-followers.md`.
* `OBJ-000680` through `OBJ-000691` are source-list child rows for AE mounts and mount equipment.
* Those mount rows cite `SN-000039-ae-mounts-and-mount-equipment.md`.
* `OBJ-000692` is a source-list system row for Plague of the Dead zombies and cites `SN-000040-ae-creature-system-leftovers.md`.
* Zombie variants and night/world interactions are not treated as finite route encounters; exact warnings, Survival Mode implications, spell/ingredient links, and level-start handling remain deferred.
* `OBJ-000693` through `OBJ-000696` are source-list parent rows for AE magic, spell-tome, robe, and staff sets.
* Those spell and staff rows cite `SN-000041-ae-magic-spell-and-staff-sets.md`.
* `OBJ-000697` through `OBJ-000703` are source-list parent rows for AE ingredients, foods, consumables, soul gems, and crafting materials.
* Those ingredient, consumable, and material rows cite `SN-000042-ae-ingredient-consumable-and-material-sets.md`.
* `OBJ-000704` through `OBJ-000712` are source-list parent rows for AE practical crafting and equipment systems, including backpacks, camping supplies, ammunition/crossbows, jewelry, brawler gauntlets, fishing equipment, and staff-station coverage.
* Those crafting and practical-equipment rows cite `SN-000043-ae-crafting-and-practical-equipment-sets.md`.
* `OBJ-000713` through `OBJ-000727` are source-list parent rows for AE Alternative Armor sets.
* Those Alternative Armor parent rows cite `SN-000044-ae-alternative-armor-parent-sets.md`.
* `OBJ-000728` through `OBJ-000759` are source-list parent rows for AE unique, named, quest-reward, pet-equipment, mount-equipment, and related equipment sets.
* Those unique-equipment parent rows cite `SN-000045-ae-unique-equipment-parent-sets.md`.
* These TB-006E rows intentionally remain parent-set coverage only. Individual spell, ingredient, recipe, item-member, acquisition, preservation, checklist-mapping, level-gate, and route-placement decisions remain deferred to later item/checklist/crafting and constraint-table passes.

## Package-to-Child Reconciliation

TB-006F checked parent rows `OBJ-000479` through `OBJ-000552` against child-row parent references in `objectives.csv`.

Result: all 74 AE parent package rows now have at least one source-list child row or child parent-set row. This is a source-list coverage check only. It does not validate individual item members, exact starts, level gates, conflicts, bugs, checklist mappings, or route placement.

| Parent row | Creation | Current child rows | Coverage lanes | Deferred detail |
| --- | --- | --- | --- | --- |
| OBJ-000479 | Survival Mode | OBJ-000702 | system/item | Survival constraints and food/item checklist detail remain deferred. |
| OBJ-000480 | Arcane Accessories | OBJ-000568, OBJ-000693 | quest, spell/power | Spell, robe, vendor/drop, checklist, and route details remain deferred. |
| OBJ-000481 | Arcane Archer Pack | OBJ-000569, OBJ-000570, OBJ-000706 | quest, crafting/equipment | Ammunition, recipe, checklist, and route details remain deferred. |
| OBJ-000482 | Chrysamere | OBJ-000578, OBJ-000736 | quest, unique/equipment | Quest constraints, acquisition timing, and preservation details remain deferred. |
| OBJ-000483 | Divine Crusader | OBJ-000583, OBJ-000584, OBJ-000728 | quest, unique/equipment | Quest constraints, acquisition timing, and preservation details remain deferred. |
| OBJ-000484 | Plague of the Dead | OBJ-000632, OBJ-000692, OBJ-000695, OBJ-000699 | quest, system/item, spell/power, crafting/equipment | Level-start, zombie-system, spell, ingredient, and Survival Mode details remain deferred. |
| OBJ-000485 | Ruin's Edge | OBJ-000634, OBJ-000742 | quest, unique/equipment | Quest constraints, acquisition timing, and preservation details remain deferred. |
| OBJ-000486 | Staff of Sheogorath | OBJ-000648, OBJ-000745 | quest, unique/equipment | Quest constraints, acquisition timing, and preservation details remain deferred. |
| OBJ-000487 | Stendarr's Hammer | OBJ-000649, OBJ-000746 | quest, unique/equipment | TB-044 routes acquisition after Vlindrel Hall storage is available: use Calcelmo museum access, take the 100-weight hammer from the Dwemer Museum southwest display, and preserve it in owned storage. |
| OBJ-000488 | Dwarven Armored Mudcrab | OBJ-000585, OBJ-000669, OBJ-000759 | quest, pet/mount, unique/equipment | Pet, spell/item, acquisition, and checklist details remain deferred. |
| OBJ-000489 | Lord's Mail | OBJ-000625, OBJ-000741 | quest, unique/equipment | Quest constraints, item-state handling, and preservation details remain deferred. |
| OBJ-000490 | Adventurer's Backpack | OBJ-000704 | crafting/equipment | Backpack variants, recipes, checklist, and Survival Mode logistics remain deferred. |
| OBJ-000491 | Camping | OBJ-000705 | crafting/equipment | Camping supplies, recipe/material, and Survival Mode route details remain deferred. |
| OBJ-000492 | Nix-Hound | OBJ-000629, OBJ-000670, OBJ-000703 | quest, pet/mount, system/item | Pet, food/item, Solstheim logistics, and checklist details remain deferred. |
| OBJ-000493 | Shadowrend | OBJ-000645, OBJ-000743 | quest, unique/equipment | Quest constraints, form handling, and preservation details remain deferred. |
| OBJ-000494 | Tundra Homestead | OBJ-000668 | property | Acquisition, safe-storage, display, furnishing, and family-use details remain deferred. |
| OBJ-000495 | Myrwatch | OBJ-000626, OBJ-000665, OBJ-000712 | quest, property, crafting/equipment | Acquisition, safe-storage, display, crafting-station, and route details remain deferred. |
| OBJ-000496 | Nordic Jewelry | OBJ-000630, OBJ-000709 | quest, crafting/equipment | Recipe, item-member, checklist, and route details remain deferred. |
| OBJ-000497 | Pets of Skyrim | OBJ-000631, OBJ-000672, OBJ-000673, OBJ-000674, OBJ-000675, OBJ-000676, OBJ-000757 | quest, pet/mount, unique/equipment | Pet assignment, equipment, checklist, and route details remain deferred. |
| OBJ-000498 | Rare Curios | OBJ-000697 | crafting/equipment | Ingredient, material, recipe, checklist, and merchant-route details remain deferred. |
| OBJ-000499 | Bone Wolf | OBJ-000576, OBJ-000671 | quest, pet/mount | Prerequisite, pet, checklist, and route details remain deferred. |
| OBJ-000500 | Staff of Hasedoki | OBJ-000647, OBJ-000744 | quest, unique/equipment | Quest constraints, acquisition timing, and preservation details remain deferred. |
| OBJ-000501 | Wild Horses | OBJ-000657, OBJ-000658, OBJ-000680, OBJ-000681, OBJ-000682, OBJ-000683, OBJ-000684, OBJ-000685, OBJ-000686, OBJ-000687, OBJ-000758 | quest, pet/mount, unique/equipment | Mount, saddle, map, checklist, and travel-logistics details remain deferred. |
| OBJ-000502 | Civil War Champions | OBJ-000579, OBJ-000732 | quest, unique/equipment | Civil War branch, reward, conflict, and preservation details remain deferred. |
| OBJ-000503 | Elite Crossbows | OBJ-000586, OBJ-000708 | quest, crafting/equipment | Crossbow acquisition, recipe, checklist, and route details remain deferred. |
| OBJ-000504 | Forgotten Seasons | OBJ-000611, OBJ-000612, OBJ-000613, OBJ-000688, OBJ-000701, OBJ-000739 | quest, pet/mount, system/item, unique/equipment | Dungeon, mount, item, reward, difficulty, and route details remain deferred. |
| OBJ-000505 | Saturalia Holiday Pack | OBJ-000643, OBJ-000689, OBJ-000734 | quest, pet/mount, unique/equipment | Outfit, mount, checklist, and northern-route details remain deferred. |
| OBJ-000506 | Sunder & Wraithguard | OBJ-000650, OBJ-000747 | quest, unique/equipment | TB-044 routes `Legends Lost` after Saints/Seducers, Keening, and Scholar's Insight: start from `Lost Caravan Guard's Note`, follow the caravan-note chain, clear Sightless Pit/Sightless Vault in one pass, and preserve Sunder and Wraithguard. |
| OBJ-000507 | Vigil Enforcer Armor Set | OBJ-000656, OBJ-000731 | quest, unique/equipment | Quest constraints, armor-member, and Hall of the Vigilant timing details remain deferred. |
| OBJ-000508 | Arms of Chaos | OBJ-000571, OBJ-000735 | quest, unique/equipment | Quest constraints, item-member, reward, and route details remain deferred. |
| OBJ-000509 | Shadowfoot Sanctum | OBJ-000644, OBJ-000667 | quest, property | Acquisition, safe-storage, display, furnishing, and family-use details remain deferred. |
| OBJ-000510 | Spell Knight Armor | OBJ-000646, OBJ-000730 | quest, unique/equipment | TB-044 routes `Crypt of the Heart`, Spell Knight armor reward branches, crafting unlock, documents, hard saves, and heart alchemy policy in SN-000244. |
| OBJ-000511 | Umbra | OBJ-000655, OBJ-000749 | quest, unique/equipment | Quest constraints, difficulty, acquisition, and preservation details remain deferred. |
| OBJ-000512 | Alternative Armors - Dwarven Mail | OBJ-000557, OBJ-000717 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000513 | Alternative Armors - Stalhrim Fur | OBJ-000566, OBJ-000726 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000514 | Dawnfang & Duskfang | OBJ-000580, OBJ-000581, OBJ-000737 | quest, unique/equipment | Quest constraints, weapon-state handling, and preservation details remain deferred. |
| OBJ-000515 | Expanded Crossbow Pack | OBJ-000707 | crafting/equipment | Crossbow acquisition, recipe, checklist, and route details remain deferred. |
| OBJ-000516 | Netch Leather Armor | OBJ-000628, OBJ-000729 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000517 | Alternative Armors - Daedric Mail | OBJ-000553, OBJ-000713 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000518 | Alternative Armors - Dragonscale | OBJ-000555, OBJ-000716 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000519 | Alternative Armors - Elven Hunter | OBJ-000560, OBJ-000720 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000520 | Alternative Armors - Ebony Plate | OBJ-000559, OBJ-000719 | quest, unique/equipment | Level-start, quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000521 | Alternative Armors - Steel Soldier | OBJ-000567, OBJ-000727 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000522 | Dead Man's Dread | OBJ-000582, OBJ-000660, OBJ-000738 | quest, property, unique/equipment | Quest, property, display, item-member, and route details remain deferred. |
| OBJ-000523 | Goblins | OBJ-000621, OBJ-000679, OBJ-000756 | quest, follower, unique/equipment | Follower, carried item, quest, and route details remain deferred. |
| OBJ-000524 | Saints & Seducers | OBJ-000635, OBJ-000636, OBJ-000637, OBJ-000638, OBJ-000639, OBJ-000640, OBJ-000641, OBJ-000642, OBJ-000677, OBJ-000678, OBJ-000698 | quest, pet/mount, crafting/equipment | Quest, pet, ingredient, branch/conflict, and item-member details remain deferred. |
| OBJ-000525 | Hendraheim | OBJ-000624, OBJ-000664 | quest, property | Acquisition, safe-storage, display, furnishing, and family-use details remain deferred. |
| OBJ-000526 | The Gray Cowl Returns! | OBJ-000654, OBJ-000748 | quest, unique/equipment | TB-044 routes the full quest after the all-perks audit, including the Gisli/deed branch note variant, Silverdrift key/chest/sword handling, Gray Cowl reward preservation, and item-member closeout. |
| OBJ-000527 | Alternative Armors - Daedric Plate | OBJ-000554, OBJ-000714 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000528 | Alternative Armors - Dragon Plate | OBJ-000556, OBJ-000715 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000529 | Alternative Armors - Dwarven Plate | OBJ-000558, OBJ-000718 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000530 | Alternative Armors - Iron | OBJ-000561, OBJ-000721 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000531 | Alternative Armors - Leather | OBJ-000562, OBJ-000722 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000532 | Alternative Armors - Orcish Plate | OBJ-000563, OBJ-000723 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000533 | Alternative Armors - Orcish Scaled | OBJ-000564, OBJ-000724 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000534 | Alternative Armors - Silver | OBJ-000565, OBJ-000725 | quest, unique/equipment | Quest constraints, armor-member, recipe, and checklist details remain deferred. |
| OBJ-000535 | Bittercup | OBJ-000572, OBJ-000573, OBJ-000574, OBJ-000755 | quest, unique/equipment | Outcome, branch/choice, reward, and route details remain deferred. |
| OBJ-000536 | Bloodchill Manor | OBJ-000575, OBJ-000659 | quest, property | Acquisition, safe-storage, display, family-use, and route details remain deferred. |
| OBJ-000537 | Bow of Shadows | OBJ-000577, OBJ-000752 | quest, unique/equipment | Quest constraints, NPC dependency, acquisition, and preservation details remain deferred. |
| OBJ-000538 | Farming | OBJ-000587, OBJ-000588, OBJ-000662 | quest, property | Farm staffing, upgrades, income, material, and route details remain deferred. |
| OBJ-000539 | Fearsome Fists | OBJ-000710 | crafting/equipment | Gauntlet variants, recipes, checklist, and route details remain deferred. |
| OBJ-000540 | Fishing | OBJ-000589, OBJ-000590, OBJ-000591, OBJ-000592, OBJ-000593, OBJ-000594, OBJ-000595, OBJ-000596, OBJ-000597, OBJ-000598, OBJ-000599, OBJ-000600, OBJ-000601, OBJ-000602, OBJ-000603, OBJ-000604, OBJ-000605, OBJ-000606, OBJ-000607, OBJ-000608, OBJ-000609, OBJ-000610, OBJ-000700 | quest, system/item | Quest, item, fish/ingredient, checklist, and representative-boundary details remain deferred. |
| OBJ-000541 | Gallows Hall | OBJ-000614, OBJ-000661, OBJ-000711 | quest, property, crafting/equipment | Acquisition, safe-storage, crafting-station, and route details remain deferred. |
| OBJ-000542 | Ghosts of the Tribunal | OBJ-000615, OBJ-000616, OBJ-000617, OBJ-000618, OBJ-000619, OBJ-000620, OBJ-000740 | quest, unique/equipment | Quest, faction/outcome, item-member, and preservation details remain deferred. |
| OBJ-000543 | Goldbrand | OBJ-000622, OBJ-000753 | quest, unique/equipment | Quest constraints, acquisition timing, and preservation details remain deferred. |
| OBJ-000544 | Headman's Cleaver | OBJ-000623, OBJ-000754 | quest, unique/equipment | Quest trigger, acquisition timing, and preservation details remain deferred. |
| OBJ-000545 | Horse Armor - Elven | OBJ-000690 | pet/mount | Active-mount, compatibility, storage, and checklist details remain deferred. |
| OBJ-000546 | Horse Armor - Steel | OBJ-000691 | pet/mount | Active-mount, compatibility, storage, and checklist details remain deferred. |
| OBJ-000547 | Nchuanthumz: Dwarven Home | OBJ-000627, OBJ-000666 | quest, property | Acquisition, safe-storage, display, furnishing, and route details remain deferred. |
| OBJ-000548 | Necromantic Grimoire | OBJ-000694 | spell/power | Spell, apparel, vendor/drop, checklist, and route details remain deferred. |
| OBJ-000549 | Redguard Elite Armaments | OBJ-000633, OBJ-000733 | quest, unique/equipment | Quest constraints, equipment-member, and preservation details remain deferred. |
| OBJ-000550 | Staves | OBJ-000696 | crafting/equipment | Staff member, crafting-station, checklist, and route details remain deferred. |
| OBJ-000551 | The Cause | OBJ-000651, OBJ-000652, OBJ-000750 | quest, unique/equipment | Level-gate, quest, difficulty, item-member, and route details remain deferred. |
| OBJ-000552 | The Contest | OBJ-000653, OBJ-000751 | quest, unique/equipment | Quest constraints, reward, item-member, and preservation details remain deferred. |

## Parent Package Rows

| Objective ID | Creation | UESP package categories | Package-level start/acquisition hint | Follow-up focus |
| --- | --- | --- | --- | --- |
| OBJ-000479 | Survival Mode | Gameplay | Creation can be turned on or off in Settings menu. For details, consult Help Menu. | Survival system constraints |
| OBJ-000480 | Arcane Accessories | Apparel; Weapons | Robes and Spells can be purchased at vendors and appear in containers. | Spells and equipment |
| OBJ-000481 | Arcane Archer Pack | Weapons | Telekinesis arrows are found in The Arcanaeum in the College of Winterhold, Soul Stealer Arrows can be found in Kagrumez. All other arrows can be purchased at vendors and appear in containers. | Crafting and equipment |
| OBJ-000482 | Chrysamere | Weapons | Weapon can be found in Forelhost southeast of Riften. | Unique item |
| OBJ-000483 | Divine Crusader | Apparel; Weapons | Armor can be found by exploring Four Skull Lookout far east-northeast of Markarth. | Unique items |
| OBJ-000484 | Plague of the Dead | Creatures; Gameplay | Quest "The Rising Dead" starts by reading an Anonymous Letter delivered by courier upon reaching level 5. | Quest and system |
| OBJ-000485 | Ruin's Edge | Weapons | Weapon is located in Stony Creek Cave far southeast of Windhelm. | Unique item |
| OBJ-000486 | Staff of Sheogorath | Weapons | Quest "Put a Fork in it" starts by reading a "Mysterious Note" at The Retching Netch in Raven Rock; the route waits until Tel Mithryn Staff Enchanter access is unlocked, then crafts the staff with the two netch quest items and two Heart Stones. | Quest and unique item |
| OBJ-000487 | Stendarr's Hammer | Weapons | Weapon can be taken from the Dwemer Museum in Markarth; TB-044 waits until late Markarth owned storage because the hammer weighs 100. | Unique item |
| OBJ-000488 | Dwarven Armored Mudcrab | Creatures | Pet can be purchased from Calcelmo in Markarth. | Pet |
| OBJ-000489 | Lord's Mail | Apparel | Quest "Gift of Kynareth" starts by reading "Letter to General Tullius" at Castle Dour in Solitude. | Quest and unique item |
| OBJ-000490 | Adventurer's Backpack | Apparel; Gameplay | Backpacks can be purchased at vendors and crafted via Forge. | Crafting and equipment |
| OBJ-000491 | Camping | Gameplay; World | Creation craftable via Forge. | Survival-adjacent system |
| OBJ-000492 | Nix-Hound | Creatures | Pet can be purchased from Revus Sarvani near Tel Mithryn or Geldis Sadri at The Retching Netch Corner Club in Raven Rock if the former is deceased. Hostile Nix-Hounds can be found in the Solstheim wilderness. | Pet and creature |
| OBJ-000493 | Shadowrend | Weapons | Quest "Through a Glass, Darkly" starts by claiming the weapon in the hot springs near the Atronach Stone. | Quest and unique item |
| OBJ-000494 | Tundra Homestead | World | House outside the city is purchased from the Jarl's Steward in Dragonsreach. | Property |
| OBJ-000495 | Myrwatch | World | Quest "Myrwatch" starts by traveling to the tower east of Morthal and reading "Hans's Journal" nearby. | Property and quest |
| OBJ-000496 | Nordic Jewelry | Apparel | Quest "Nordic Jewelry" starts by reading the Certificate of Authenticity obtained if you buy Nordic jewelry from Madesi, Bersi Honey-Hand, Endarie, or Belethor. | Crafting and equipment |
| OBJ-000497 | Pets of Skyrim | Creatures | Quest "Pets of Skyrim" starts by reading the note For Sale in The Bannered Mare. | Pets and quest |
| OBJ-000498 | Rare Curios | Gameplay | Items added to Khajiit merchant vendors. | Ingredients and crafting |
| OBJ-000499 | Bone Wolf | Creatures | Quest "Let Sleeping Wolves Lie" starts by reading the Letter from Bolgeir Bearclaw delivered by courier after completion of "The Wolf Queen Awakened". | Pet and quest |
| OBJ-000500 | Staff of Hasedoki | Weapons | Quest "The Staff of Hasedoki" starts by reading the Smuggler's Trade Notes at the bandit camp west of Dragonsreach. | Quest and unique item |
| OBJ-000501 | Wild Horses | Creatures; Gameplay | Quest Creature of Legend starts by reading Soran's Journal at the Arcanaeum. A map to other horses may be purchased at any hostler. | Mounts and quest |
| OBJ-000502 | Civil War Champions | Apparel; Weapons | Quest "Battle of the Champions" starts by reading Battle of Champions at The Drunken Huntsman in Whiterun or waiting for a letter from a commanding officer. | Quest and branch risk |
| OBJ-000503 | Elite Crossbows | Weapons | Quest "Night Hunter" starts by reading Kragrash's Letter at Ironback Hideout northwest of Solitude. | Quest and equipment |
| OBJ-000504 | Forgotten Seasons | Apparel; Creatures; Gameplay; World | Search for the Runoff Caverns west of Lost Valley Redoubt. | Quest and dungeon |
| OBJ-000505 | Saturalia Holiday Pack | Apparel; Creatures | Outfit and mount obtained from Agrane Peryval west of Dawnstar. | Mount and equipment |
| OBJ-000506 | Sunder & Wraithguard | Apparel; Weapons | Quest "Legends Lost" starts by reading the Lost Caravan Guard's Note at the New Gnisis Cornerclub in Windhelm; TB-044 completes it through the full caravan-note chain and Sightless Vault after Keening and Scholar's Insight are ready. | Quest and unique items |
| OBJ-000507 | Vigil Enforcer Armor Set | Apparel | Quest "Unholy Vigil" starts by reading the Letter to Keeper Carcette in the Hall of the Vigilant south of Dawnstar. | Quest and equipment |
| OBJ-000508 | Arms of Chaos | Apparel; Weapons | Quest "The Arms of Chaos" starts by reading Hyenril's Journal at Skytemple Ruins, north of the College of Winterhold. | Quest and unique items |
| OBJ-000509 | Shadowfoot Sanctum | World | House can be purchased from Vekel the Man in the Ragged Flagon in the Riften Ratway. | Property |
| OBJ-000510 | Spell Knight Armor | Apparel; Gameplay | Quest "Crypt of the Heart" starts by reading Crypt of the Heart - Draft at the Silver-Blood Inn in Markarth. | Quest and equipment |
| OBJ-000511 | Umbra | Weapons | Quest "Vile Whispers" starts by reading the Vigilant's Report in Champion's Rest, found in the mountains north-northeast of Riften. | Quest and unique item |
| OBJ-000512 | Alternative Armors - Dwarven Mail | Apparel | Quest "Fan Favorite" starts by reading Arena Fan's Note at a camp southeast of Ivarstead. | Quest and equipment |
| OBJ-000513 | Alternative Armors - Stalhrim Fur | Apparel | Quest "Ancient Ice" starts by reading Skjol's Journal at the camp south-southwest of Skaal Village. | Quest and equipment |
| OBJ-000514 | Dawnfang & Duskfang | Weapons | Quest "A Soul Divided" starts by exploring the Riften Ratway. | Quest and unique item |
| OBJ-000515 | Expanded Crossbow Pack | Weapons | Crossbows bought from Fletcher in Solitude; crafting unlocked once acquired. | Crafting and equipment |
| OBJ-000516 | Netch Leather Armor | Apparel | Quest "More Than You Can Chew" starts by reading the Peddler's Journal on a body of a Dark Elf north-northwest of Skaal Village and southeast of Haknir's Shoal. | Quest and equipment |
| OBJ-000517 | Alternative Armors - Daedric Mail | Apparel | Quest "Missing Merchant" starts by speaking to the innkeeper of Candlehearth Hall in Windhelm. | Quest and equipment |
| OBJ-000518 | Alternative Armors - Dragonscale | Apparel | Quest "Tilted Scales" starts by reading The Crimson Dirks, v4 in Candlehearth Hall in Windhelm. | Quest and equipment |
| OBJ-000519 | Alternative Armors - Elven Hunter | Apparel | Quest "Once a Hunter" starts by reading Guard Dossier: Aesrael in the Falkreath Barracks. | Quest and equipment |
| OBJ-000520 | Alternative Armors - Ebony Plate | Apparel | Quest "Heart of Crimson" starts by reading the Letter from Tyra Blood-Fire delivered by courier upon reaching level 32. | Quest and equipment |
| OBJ-000521 | Alternative Armors - Steel Soldier | Apparel | Quest "Over the Edge" starts by reading Suicide at Dragon Bridge in Four Shields Tavern at Dragon Bridge. | Quest and equipment |
| OBJ-000522 | Dead Man's Dread | Apparel; Weapons | Quest "The Restless" starts by reading the book The Restless at The Winking Skeever in Solitude. | Quest, property, and items |
| OBJ-000523 | Goblins | Creatures | Quest "Blue in the Face" starts by reading Letter to Clexius at The Bee and Barb in Riften. | Quest and creature |
| OBJ-000524 | Saints & Seducers | Apparel; Creatures; Gameplay; Weapons; World | Quest "Balance of Power" starts by talking to the traveling Khajiit Merchant Ri'saad. | Quest, items, and system |
| OBJ-000525 | Hendraheim | World | Quest "Hendraheim" starts by reading the Warrior's Challenge delivered by courier upon reaching level 10. | Property and quest |
| OBJ-000526 | The Gray Cowl Returns! | Apparel | Quest "The Gray Cowl of Nocturnal" starts by confronting a thief in the Riften graveyard; TB-044 routes it late after all-perks recovery. | Quest and unique item |
| OBJ-000527 | Alternative Armors - Daedric Plate | Apparel | Quest "Beyond the Grave" starts by reading Death of a Crimson Dirk in Dragonreach Dungeon in Whiterun. | Quest and equipment |
| OBJ-000528 | Alternative Armors - Dragon Plate | Apparel | Bones for a Crow starts by speaking to an innkeeper for Bounty for Crowstooth. | Quest and equipment |
| OBJ-000529 | Alternative Armors - Dwarven Plate | Apparel | Quest "Mightier than the Sword" starts by reading Looter's Note at the Silver-Blood Inn in Markarth. | Quest and equipment |
| OBJ-000530 | Alternative Armors - Iron | Apparel | Quest "Brothers in Irons" starts by reading Nightgate Inn Patron's Note in Nightgate Inn. | Quest and equipment |
| OBJ-000531 | Alternative Armors - Leather | Apparel | Double-Edged starts by reading Zaharia's Note at Cliffside Retreat. | Quest and equipment |
| OBJ-000532 | Alternative Armors - Orcish Plate | Apparel | Quest "Smith 'n Slash" starts by reading "Guard's Dossier: Yakhtu gra-Orkulg" at the Guard Barracks inside the gate in Whiterun. | Quest and equipment |
| OBJ-000533 | Alternative Armors - Orcish Scaled | Apparel | Quest "Gambler's Edge" starts by reading Guard's Dossier: Antonius at the Mistveil Keep Barracks in Riften. | Quest and equipment |
| OBJ-000534 | Alternative Armors - Silver | Apparel | Quest "When the Cat's Away" starts by reading M'Sharra's Diary at The Bannered Mare in Whiterun. | Quest and equipment |
| OBJ-000535 | Bittercup | World | A Dying Wish starts by reading Mysterious Altar in Dead Man's Drink; later choice branches deferred. | Quest and branch risk |
| OBJ-000536 | Bloodchill Manor | World | Quest "Guests for Dinner" starts by reading the Dinner Invitation delivered by courier upon reaching level 12. | Property and quest |
| OBJ-000537 | Bow of Shadows | Weapons | Quest "In the Shadows" starts by speaking to the Jarl's Steward in Dragonsreach. | Quest and unique item |
| OBJ-000538 | Farming | Gameplay; World | Quest "The Unquiet Dead" starts by investigating Goldenhills Plantation east of Rorikstead. | Property and system |
| OBJ-000539 | Fearsome Fists | Apparel | Items appear at vendors, in chests, and can be crafted at any forge. | Crafting and equipment |
| OBJ-000540 | Fishing | Gameplay | Initial quest, "Angler Acquaintances," starts by using any Fishing Supplies scattered across Skyrim. | Quest and system |
| OBJ-000541 | Gallows Hall | World | Quest "Dreams of the Dead" starts by reading Naara's Journal within the abandoned fort on the northern edge of Mara's Eye Pond. | Property and quest |
| OBJ-000542 | Ghosts of the Tribunal | Apparel; Weapons | Quest "Ghosts of the Tribunal" starts by reading Heretic Dossier: Blacksmith's Confessional at the Temple in Raven Rock. | Quest and items |
| OBJ-000543 | Goldbrand | Weapons | Quest "A Matter of Pride" starts by finding Eranya in the Sacellum of Boethiah east of Windhelm. | Quest and unique item |
| OBJ-000544 | Headman's Cleaver | Weapons | Quest "Blood in the Water" can be provided when asking an innkeeper if they have heard any rumors lately. | Quest and unique item |
| OBJ-000545 | Horse Armor - Elven | Apparel | Obtained via hostler at any stable. | Mount equipment |
| OBJ-000546 | Horse Armor - Steel | Apparel | Obtained via hostler at any stable. | Mount equipment |
| OBJ-000547 | Nchuanthumz: Dwarven Home | World | Quest starts by reading "Seeks-Ancient-Artifacts' Journal, v1" in The Frozen Hearth in Winterhold. | Property and quest |
| OBJ-000548 | Necromantic Grimoire | Gameplay | Items can be purchased at vendors and appear in containers. | Spells and equipment |
| OBJ-000549 | Redguard Elite Armaments | Apparel; Weapons | Quest "Interception" starts by talking to Azadi in Shor's Stone far north of Riften. | Quest and equipment |
| OBJ-000550 | Staves | Weapons | Items appear at vendors and in chests. | Equipment |
| OBJ-000551 | The Cause | Characters; Weapons; World | Quest "The Cause" starts by reading the Stranger's Plea delivered by courier upon reaching level 46. | Quest and fixed late content |
| OBJ-000552 | The Contest | Weapons | Quest "Caught in a Web" starts by reading Adonato Leotelli's Journal in Candlehearth Hall. | Quest and unique items |
