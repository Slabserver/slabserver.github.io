# Plugins
## Server Infrastructure & Gameplay

### Core
| Plugin | Description |
|--------|-------------|
|[MythicDungeons](https://www.spigotmc.org/resources/mythicdungeons.102699/)|The main plugin. This allows an instance of a world to be created. Then it's managed and deleted once all players have left. Same thing I used for the April fools for vault hunters|
|[WorldGuard](https://dev.bukkit.org/projects/worldguard)|Handles all the grief protection for the main world|
|CompassSwitcher*|Custom plugin to switch the world NBT of the compass. To "overworld" when dropped and the player's dimension when picked up. So all the filters work|
|[PlotSquared](https://www.spigotmc.org/resources/plotsquared-v7.77506/)|This allows users to always be able to claim a board. Since the ones in the lobby are limited and unprotected.|
|[ConditionalEvents](https://www.spigotmc.org/resources/conditionalevents-custom-actions-for-specific-events-1-8-1-20-6.82271/)|This plugin give a easy way to make events without needing to write plugins|


### Cosmetic
| Plugin | Description |
|--------|-------------|
|[ServerVariables]()|Allows variables to be stored about the server and player and queried via PlaceHolderAPI|
| [ Citizens](https://www.spigotmc.org/resources/citizens.13811/)|Used to create the NPCs in the lobby|
|[TAB](https://www.spigotmc.org/resources/tab-1-5-1-20-4.57806/)|Handles showing what dungeon the player is in, in tab|
|[DecentHolograms](https://www.spigotmc.org/resources/decentholograms-1-8-1-20-4-papi-support-no-dependencies.96927/)|Creates floating text around the lobby, like the leaderboards|
|[EpicRename](https://www.spigotmc.org/resources/epicrename.4341/)|Allows users to rename shulkerboxes|
|[AjLeaderboards](https://www.spigotmc.org/resources/ajleaderboards.85548/)|Will create leaderboards using values in PlaceHolderAPI and allowing them to queried using PlaceHolderAPI again|


### Utility 
| Plugin | Description |
|--------|-------------|
|[EssentialsX](https://essentialsx.net/)|Utility plugin to handle kits, spawn join message, etc.|
|[EssentialsXSpawn](https://essentialsx.net/)|Addon for EssentialsX|
|[AxShulkers](https://www.spigotmc.org/resources/axshulkers-open-your-shulkers-anywhere.112178/)|Allows shulkers to be opened without placing|
|[InventoryRollbackPlus](https://www.spigotmc.org/resources/inventory-rollback-plus-1-8-1-20-x.85811/)|Takes backups of the inventory so if a box is left in the world it can be restored|
|[LPC (LuckPerms Chat)](https://www.spigotmc.org/resources/lpc-chat-formatter-1-7-10-1-20.68965/)|Simple chat plugin to give chat colors from LuckPerms|
|[LuckPerms](https://luckperms.net/)|Permission system, mostly for the colors|
|NoStealingBook*|Custom plugin to just cancel taking a book from lectern without permission|



## Dependency Plugins / APIs (other plugins need these to work)
| Plugin | Description |
| -----------|---------
| [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)| |
| [ProtocolLib](https://www.spigotmc.org/resources/protocollib.1997/) | Needed for MythicDungeons|
| [WorldEdit](https://dev.bukkit.org/projects/worldedit) | Needed for worldguard


`*` Written by _Twist_!

# Technical changes

## Server changes
Disabled The Nether and End.

## Compasses
I had to deal with the NBT data for the compass, The world changes every time they game is cloned. (overworld != deckedout_1). The compasses must be set to the correct world to work.
Firstly I tried using commands but this got harder in multiplayer, since you can't modify the player directly. So I wrote a very simple plugin to listen to pick up and drop and convert it.

## Respawning
The respawn mechanic in MythicDungeons isn't like how deckedout works. It uses a checkpoint system, where every player goes to the same point. This breaks CoOp so I made a commandblock watching for a death that tps the user into the respawn point for the team they joined when they entered the dungeon. (This means you don't actually need to sleep in the bed)

## Book stealing
MythicDungeons didn't give a option to disable taking books from a lecterns, but you can't return them and you can soft lock the tutorial. So was just a simple plugin to cancel the event for those without the permission globally.

## Leaderboards
Honestly my favorite feature. This uses 3 plugins, ServerVariables, ajleaderboards and DecentHolograms. In the dungeon, I setup function events with redstone triggers to set the variables for the player using servervariables. This just runs a console command and injects the player names in the party. Then ajleaderboards will periodically check a players values via placeholderAPI and add them to a leader board. Then its just a simple as asking for a placeholder at the index of the position to show on the holograms.

## Boards
Boards were a challenge. I never planned to do this for the crossover server but ended up doing so once the idea of more players taking part floated around. It relies on PlotSquared and its schematic feature. Thanks to Dex it allows the same board to generated across the world where players can claim it and have it protected.    