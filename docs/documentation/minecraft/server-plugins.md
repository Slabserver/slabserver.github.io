# Server Plugins

!!! info
    \* Plugin is written and maintained by the staff team

    ** Plugin is deprecated and subject to future removal

## Infrastructure & Gameplay

| Plugin | Description |
| - | - |
| {Survival} [AFKSleep](https://github.com/chrissamael/AfkSleep)* | Handles multiplayer sleep, AFK/Idle states and Discord `!playerlist` |
| {Survival} BlockPlaceLog* | Tracks Easyplace usage in Litematica |
| {Survival} [Bouncer](https://github.com/Slabserver/bouncer)* | Handles Resource World infrastructure (Bungeecord level) and network whitelist |
| {Survival} [Buster](https://github.com/Slabserver/Buster)* | Enables dynamic scaling of view and simulation distance, player counts, and mob caps |
| {Both} [DiscordSRV](https://www.spigotmc.org/resources/discordsrv.18494/) | Handles ingame chat synchronisation to Discord for the Survival and Creative servers|
| {Survival} DirectoryPlugin* | Handles stock summaries in the Google Sheet for the directory |
| {Survival} [DragonCandle](https://github.com/Slabserver/DragonCandle)* | _Explore... Descend... Discover..._ |
| {Creative} [F3NPerm](https://www.spigotmc.org/resources/f3nperm.46461/) | Enables gamemode switching using `F3 + N`  and `F3 + F4` on the Creative server
| {Survival} [FastChunkPregen](https://www.spigotmc.org/resources/fast-chunk-pregenerator.74429/) | Pre-generates chunks, primarily in the Resource World |
| {Survival} Fireworks* | Adds firework recipes to the crafting recipe book |
| {Survival} [Gatekeeper](https://github.com/Slabserver/Gatekeeper)* | Handles Resource World infrastructure (Paper level) |
| {Survival} [HuskSync](https://www.spigotmc.org/resources/husksync-sync-inventories-ender-chests-cross-server-advancements-map-art-stats-backups.97144/) | Synchronises player data to and from the Resource World |
| {Survival} [LightningFire](https://www.spigotmc.org/resources/lightning-fire.64389/)* ** | Prevents lightning from starting fires and torching bases |
| {Survival} [Pl3xMap](https://www.spigotmc.org/resources/pl3xmap.109697/) | Adds [map.slabserver.org](https://map.slabserver.org) |
| {Survival} [RawStats](https://github.com/GoldenDelicios/RawStats)* | Displays various player statistics in the sidebar, when enabled by staff |
| {Both} Shrug* | Adds the `/shrug` command to easily send the ¯\\\_(ツ)_/¯ emoticon in chat |
| {Survival} [ShulkerSaver](https://github.com/GoldenDelicios/ShulkerSaver)* ** | Prevents Shulker boxes being deleted by [MC-902](https://bugs.mojang.com/browse/MC-902), prior to the bugfix in Minecraft 1.21 |
| {Survival} [SeedWriter](https://github.com/GoldenDelicios/ShulkerSaver)* | Logs each Resource World seed for future reference |
| {Survival} [TAB](https://www.spigotmc.org/resources/tab-1-7-x-1-16-5-free-version.57806/) | Provides custom tablist configuration |
| {Survival} [TAB - Bridge](https://www.spigotmc.org/resources/tab-bridge.83966/) | Provides custom tablist configuration (Bungeecord level) |
| {Survival} [VentureChat](https://www.spigotmc.org/resources/venturechat.771/) | Improves chat features, and syncs chat across the Survival servers via Bungeecord |
| {Both} [Wrench](https://github.com/Slabserver/Wrench)* | Provides easier rotation of a wide varity of blocks |

## Administration

| Plugin | Description |
| - | - |
| [AdvancedBan](https://www.spigotmc.org/resources/advancedban.8695/) | Allows for synchronized bans across the network and tempbans |
| [Camera](https://github.com/GoldenDelicios/CameraPlugin)* | A better, survival-admod-friendly spectator mode |
| [Chunky](https://www.spigotmc.org/resources/chunky.81534/)* | A quick and efficient chunk pre-generator |
| [CollarCheck](https://github.com/GoldenDelicios/CollarCheck)* | Pet owner checks |
| [CoreProtect](https://www.spigotmc.org/resources/coreprotect.8631/) | Logs interactions in the world to a database |
| [EntityDetection](https://www.spigotmc.org/resources/entitydetection-tile-entity-support.20588) | Helps with lagbusting by finding chunks with high amounts of entities |
| [EntityGlo](https://github.com/Slabserver/EntityGlo)* | Helps with lagbusting by highlighting entities in a loaded area |
| :material-sword: [InventoryRollbackPlus](https://www.spigotmc.org/resources/inventory-rollback-plus-1-8-1-18-x.85811/) | Helps to easily restore player inventories if you die to glitches or bugs |
| :material-sword: LessEndermanGriefing| Reduces the blocks that Enderman can pick up, based on their current dimension |
| [LuckPerms](https://luckperms.net/) | Handles permission groups of staff and players |
| [OpenInv](https://dev.bukkit.org/projects/openinv) | Allows remote access to player inventories and Ender Chests |
| [PremiumVanish](https://www.spigotmc.org/resources/premiumvanish-stay-hidden-bungee-support.14404/) | Allows us to hide our presence on the server and observe xraying attempts |
| [Plan](https://www.spigotmc.org/resources/plan-player-analytics.32536/) | Provides player analytics for the activity and geological distribution of our playerbase |
[Spark](https://www.spigotmc.org/resources/spark.57242/) | Server health monitoring and the `/tps` command |
[WorldEdit](https://dev.bukkit.org/projects/worldedit) | Integrates with CoreProtect for easier operations |

## Datapacks

| Datapack | Description |
| - | - |
| Datapacks-S4* | Adds custom advancements and recipes for Slabserver |

## Dependency Plugins / APIs

| Plugin | Dependency |
| - | - |
| [NBT API](https://www.spigotmc.org/resources/nbt-api.7939/) | Gatekeeper
| [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) | Miscellaneous
| [ProtocolLib](https://www.spigotmc.org/resources/protocollib.1997/) | Miscellaneous
| [Vault](https://www.spigotmc.org/resources/vault.34315) | AFKSleep, Gatekeeper
| [XGlow](https://www.spigotmc.org/resources/xglow.85325/) | EntityGlo
| [yamler](https://www.spigotmc.org/resources/yamler.315/) | Miscellaneous


axiompaper
bouncerlite
coreprotect
discordsrv
invisitemframes (both)
f3nperm
libertybans
lite2edit
plotsquared
shrug
simpleback
simplereply
vault (afksleep is both?)
venturechat
worldeditbukkit
worldguardbukkit
worldguardextraflags
wrench