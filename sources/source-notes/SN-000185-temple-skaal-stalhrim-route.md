# SN-000185 - Temple, Skaal, And Stalhrim Route

## Scope

Supports the v1 guide section `Temple Of Miraak, Skaal, And Stalhrim`.

This pass routes the Dragonborn main spine from the Temple of Miraak through `The Fate of the Skaal`, immediately secures `A New Source of Stalhrim`, pulls colocated All-Maker Stone and north-coast objectives into the same loop, and records why several nearby northern Solstheim candidates stay out of this section.

## Sources

| Source ID | Use |
| --- | --- |
| SRC-001252 | `Dragonborn` quest arrival state and Solstheim start context from the previous Raven Rock section. |
| SRC-001268 | Temple of Miraak quest route, Dragon Aspect word, Gatekeeper key, `Black Book: Waking Dreams`, and handoff to Frea/`The Fate of the Skaal`. |
| SRC-001269 | Temple of Miraak location state, Tree Stone approach, and Frea/cultist entry context. |
| SRC-001270 | `The Fate of the Skaal`, Saering's Watch, Bend Will first word, Wind Stone cleansing, North Wind, Frea follower unlock, `Cleansing the Stones`, and `The Path of Knowledge`. |
| SRC-001271 | Saering's Watch word-wall and dragon-lair context. |
| SRC-001272 | Bend Will source and Dragonborn progression context. |
| SRC-001273; SRC-001274; SRC-001275; SRC-001276 | All-Maker Stone power acquisition for Wind, Beast, Water, and Earth Stones. |
| SRC-000169; SRC-000178 | All-Maker Stone reacquisition and `Cleansing the Stones` circuit context. |
| SRC-000040; SRC-000041 | `A New Source of Stalhrim`, stalhrim crafting unlock, Deor/Fanari risk, Ancarion map handoff, Stalhrim Source map behavior, Smithing 80/Ebony Smithing crafting gate, and Stalhrim Source material context. |
| SRC-001277; SRC-001278; SRC-001279 | Abandoned Lodge, Northshore Landing, and Stalhrim Source local route details. |
| SRC-001280; SRC-000133 | `Ancient Ice`, Skjol's Journal, Horker Iceberg, Stalhrim Fur armor set, and Alternative Armors - Stalhrim Fur package members. |
| SRC-001282 | `Filial Bonds`, Torkild random encounter, Torkild's Letter to Wulf, and the `At the Summit of Apocrypha` turn-in conflict. |
| SRC-001283 | `Lost Legacy` start after `A New Source of Stalhrim`, Vahlok's Tomb, Amethyst Claw halves, Battle Fury words, and reward. |
| SRC-001284 | Ancarion's stalhrim sale objective start and later sale boundary. |
| SRC-001285; SRC-001286 | Benkongerike and `Lost Knowledge` routing reason. |
| SRC-001287; SRC-001288 | Netch Leather route scope and why `More Than You Can Chew` waits for a broader north-coast/Sun Stone/Fort Hraggstad pass. |
| SRC-001281 | Morwen/Bera necklace timing and Falkreath handoff for later Skaal-to-mainland routing. |
| SRC-001470 | `Feeding the Addiction`, Bralsa Drel, Geldis Sadri, and post-`Cleansing the Stones` Raven Rock favor timing. |
| SRC-001471 | `Skaal Village Dialogue`, Bera's Necklace, Runil delivery target, and Morwen reward timing. |

## Routing Decisions

The section begins from the post-Frostmoon Vampire Lord state, so fresh hostile content is useful for Vampire Lord mastery, but the guide still tells the player to revert before friendly hubs and All-Maker Stone fights where freed NPCs are nearby. The player-facing route keeps the transformation tracking concise and records actual perk progress only when perks are bought.

`The Temple of Miraak` is routed now because the previous Raven Rock/Frostmoon section deliberately held the Dragonborn main spine while Beast Blood and Raven Rock infrastructure were resolved. The temple also naturally supplies the second Dragon Aspect word and `Black Book: Waking Dreams`.

`The Fate of the Skaal` is kept intact: Frea to Skaal Village, Storn to Saering's Watch, Bend Will learned and unlocked, Wind Stone cleansed, North Wind acquired, and Storn's handoff completed. The Wind Stone fight is written as a controlled normal-form fight because Deor and Fanari are only protected before `A New Source of Stalhrim` starts, and losing them can block the stalhrim crafting path.

The guide adds two named hard saves for the stalhrim chain. `HS-SKAAL-STALHRIM-SCENE` protects the Deor/Fanari scene immediately after `The Fate of the Skaal`. `HS-SKAAL-ABANDONED-LODGE` protects the Baldor rescue and map handoff. Both are route-protective hard saves, not branch saves.

After `A New Source of Stalhrim` is started, the route pulls in nearby safe work: Edla/Nikulas, Wulf's `Filial Bonds` start, Beast Stone, `Ancient Ice`, Abandoned Lodge, Northshore Landing, Horker Iceberg/Stalhrim Fur, Stalhrim Source, Water Stone, and Earth Stone. This follows the current geographic-routing convention rather than leaving all All-Maker or Creation content for a later theme bucket.

The Ancarion stalhrim sale objective is started through the persuasion/deal path while Ancarion is available at Northshore Landing. It is not completed in this pass because `Stalhrim Crafter` still has the source-backed Smithing 80 and Ebony Smithing gate in project data. The later crafting block should craft one spare stalhrim item and sell that item to Ancarion.

`Lost Legacy` is accepted after Baldor is rescued because Tharstan starts it at Skaal Village after `A New Source of Stalhrim`; the next central-island route should complete Vahlok's Tomb rather than leaving the quest idle for a long period.

`Filial Bonds` is started now because Wulf is in Skaal Village and the route is already establishing Skaal side objectives. The guide names the natural acquisition action if Torkild appears during intervening Solstheim travel, but the row is no longer left open indefinitely: the Dragonborn finale section now forces an isolated Torkild search before Storn, using the UESP-listed possible encounter sites.

Benkongerike is deliberately held even though Saering's Watch is nearby. UESP records that `Lost Knowledge` is offered by Neloth after `The Gardener of Men` and can send the player to Benkongerike for `Black Book: Untold Legends`; Benkongerike also contains an East Empire Pendant, Telekinesis, and a Cyclone word. Holding the dungeon preserves the Neloth Black Book reward structure and keeps those colocated rows together.

`More Than You Can Chew` is also held. Its start is north-northwest of Skaal Village, but the quest's natural route reaches the riekling island, the Sun Stone coast, `Crafting with Netch Leather`, and a Fort Hraggstad armor/Boots of Blinding Speed follow-up. The section already routes the west/north stalhrim loop; splitting Netch Leather here would create a wide quest fragment before the Sun Stone/Tel Mithryn and mainland handoffs.

Morwen's Bera necklace favor is not started here. Its next stage is Runil in Falkreath, and the current route remains on Solstheim for several sections. The better start point is a later Skaal visit just before a mainland/Falkreath-aligned handoff.

Skaal Amulet is not routed here. The checklist data notes it as obtainable only from Frea by pickpocket/reverse-pickpocket handling. That belongs with the later pickpocket-capable unique-item reconciliation, not the immediate Skaal main quest handoff.

The Sun Stone is left for the Tel Mithryn side of the island, and the Tree Stone/Root of Power remains tied to the Dragonborn finale. Wind, Beast, Water, and Earth are routed now because they are safe once `Cleansing the Stones` is active and align with this section's movement through Skaal, Thirsk-adjacent, Northshore, Stalhrim Source, and Raven Rock.

`Feeding the Addiction` is routed on the Raven Rock return after the Earth Stone. This is the first natural Raven Rock service stop after freeing the town from Miraak's influence, and the quest stays entirely between Bralsa Drel and Geldis Sadri inside Raven Rock.

## Unresolved

`Filial Bonds` remains in progress after this section, but it is no longer a route-resolution gap. The later Miraak finale section closes it before `At the Summit of Apocrypha`, because UESP records that active finale quest as blocking Wulf's letter turn-in.

No other new `NEEDS ROUTE RESOLUTION` rows were introduced by this pass.

## Linked Records

OBJ-000413; OBJ-000414; OBJ-000415; OBJ-000416; OBJ-000434; OBJ-000435; OBJ-000436; OBJ-000437; OBJ-000438; OBJ-000439; OBJ-000447; OBJ-000462; OBJ-000469; OBJ-000476; OBJ-000513; OBJ-000516; OBJ-000566; OBJ-000628; OBJ-000726; OBJ-000729; OBJ-000765; OBJ-000772; OBJ-000789; OBJ-000790; OBJ-000791; OBJ-000792; OBJ-000793; OBJ-000794; OBJ-000817; OBJ-000921; OBJ-001064; OBJ-001066; OBJ-001308; OBJ-001332; OBJ-001333; OBJ-001379; OBJ-001489; OBJ-001506; OBJ-001724; OBJ-001856; OBJ-001872; OBJ-001892; OBJ-001971; OBJ-001972; OBJ-002029; OBJ-002137; OBJ-002166; OBJ-002171; OBJ-002183; OBJ-002188; OBJ-002317; OBJ-002365; CHK-QUESTS-0502; CHK-QUESTS-0504; CHK-QUESTS-0506; CHK-QUESTS-0508; CHK-QUESTS-0525; CHK-QUESTS-0526; CHK-QUESTS-0527; CHK-QUESTS-0528; CHK-QUESTS-0530; CHK-QUESTS-0532; CHK-QUESTS-0534; CHK-QUESTS-0535; CHK-QUESTS-0557; CHK-QUESTS-0637; CHK-QUESTS-0647; CHK-SPELLS-0727; CHK-DRAGON-SHOUTS-0958; CHK-DRAGON-SHOUTS-0966; CHK-LOCATIONS-1342; CHK-LOCATIONS-1343; CHK-LOCATIONS-1353; CHK-LOCATIONS-1375; CHK-LOCATIONS-1383; CHK-LOCATIONS-1384; CHK-LOCATIONS-1386; CHK-LOCATIONS-1389; CHK-LOCATIONS-1391; CHK-UNIQUE-GEAR-1782; CHK-BOOKS-2371; CHK-BOOKS-2402; CHK-BOOKS-2403; CHK-BOOKS-2443; CHK-BOOKS-2509; CHK-BOOKS-2528; CHK-COLLECTIBLE-ITEMS-2577; CHK-COLLECTIBLE-ITEMS-2578; CHK-RECRUITABLE-FOLLOWERS-2640.
