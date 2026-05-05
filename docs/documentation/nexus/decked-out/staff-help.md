# Decked Out - Staff help

## Inventory Rollback
By far the biggest problem is going to be a player running the dungeon putting their box down and then leaving the game for 5 minutes // exiting without the box. Since the world is instanced the box is deleted from existence.

To combat this I installed a rollback plugin to take snapshot of the players inventory. The plugin is [Inventory Rollback Plus](https://www.spigotmc.org/resources/inventory-rollback-plus-1-8-1-20-x.85811/). The main command is `/irp restore [name]` here you can follow the GUI.

!!!CAUTION
    Shulkers due to the plugin [axshulkers](https://www.spigotmc.org/resources/axshulkers-open-your-shulkers-anywhere.112178/) You need to dupe the shulker in creative. This is due to the dupe protection from that plugin. **If you don't do this the shulker box will be empty when placed!**

## Whitelisting
If you're using a vanilla whitelist all admins(light red name) have the `/whitelist` command. You can use `/whitelist add player` to add a player

## Moderation 
I added moderation to the admin role. You can ban, mute, invsee, gamemode, tp, and plot admin. This should help dealing with any issues. But don't hesitate to contact us for support. 

## Plotworld
I don't think I made it clear players need to run `/kit board` for the items for the board. This might cause confusion. 

## Fixing Decked Out

### CO-OP person walked through wrong door
Simply switch into spectator mode tp the the players affected and walk through the open door to stop the game. 
OR get the player who left from the wrong door to run `/stuck` to put them at the correct bed to stop the game.

### Catch all
If for what ever reason the dungeon breaks and you can't get your box, The force reset button can be used to trigger the game to stop. Grab your box and leave. 
!!!WARNING
    This should only be used if you think the dungeon has broke. Please try and tell us if you had to use it and why.



## Notes
* If a player leaves the dungeon they have 5 minutes to login before the world is deleted.
* Server can handle ~30 players with 10 tutorials and 6-7 decked outs running at once, the server wasn't happy at this tho ~45MSPT.
* Again don't hesitate to reach out for any issues.