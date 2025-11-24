---
date: 2022-11-05
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# October 2022
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of September - 5th Of October:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $6.08
Monthly Patreon Donations¹| $48.23
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $54.31
Existing Rollover Donations| $454.20
---|---
Dedicated Server Cost²| -$87.02
---|---
**Remaining Donation Funds** ³   |  **$421.49**

---

### State of the Slab
**Current staff tasks being tracked as of 1st Nov 2022⁴:**

![State of the Slab November 2022](./../../../assets/images/kanban/2022/November.png "State of the Slab November 2022")


**Here's a recap of the staff team actions throughout the last couple months:**

- As most of you know, we took measures to nullify the [Minecraft Player Reporting tool](https://www.minecraft.net/en-us/article/addressing-player-chat-reporting-tool) on our servers by making every chat message be sent by our server. In-game messages cannot be reported, and of course neither can any ingamechat messages. We've also made sure Mojang-signed public keys are not enforced on our server, so that players can connect with client mods like 'No Chat Reports'.
    - This was announced quite publicly in the Discord but I wanted to call it out explicitly here again as it's quite a significant stance to take against it, and people have expressed that acknowledging technical behind-the-scenes changes is a key thing they want from these transparency reports.

- We've taken a big decision to disable enderman griefing in most circumstances, after significant player feedback and discussion. Endermen can still pick up grass, mycelium, podzol, and melons in the End dimension, to preserve support for griefing based farms for those blocks. Thanks to all those that gave their input on this discussion.

- We made several changes for the Resource World. Most notably, players can now set a spawn point in the Resource World when they die, a gameplay change that had the added benefit of resolving other respawn bugs. We now also support Discord integration when the Main World is empty, so that players out on grand adventures when the server is otherwise empty can be a little less lonely.

- We increased our miscellaneous `entity-activation-range` on Slabserver to align with server render distance, to solve some issues with  Evokers in Minecarts not moving correctly, as seen in Decked Out gameplay.

- We've done some reviews and tightening of security measures on our dedicated server, following some best practices raised by community members.

- We gave The Tunnel a few minor QoL tweaks that had been on the backlog for a while. The 'infinite loop stage' now plays a dragon roar and an echoing page turning sound effect, to help those who are soloing this and could easily miss the dragon loot table behaviour. We also tweaked the smoke and lava particle effects around the doors in Stage 3, to help those using minimal particle settings.

- We attempted, and completely failed, to investigate an issue where a player managed to somehow respawn in The Tunnel after dying in Decked Out. I don't really have much to say other than this is one of the most bizarre things we've seen and can't even begin to understand why or how this happened, but thought I'd share because shit like this is just a day in the life for us and life is pain.

- We've done a lot of work with our old Coreprotect data, and still have a fair bit to do. I'll cover this fully in Nov's transparency report as I'm hoping to have completed this saga within the next week or so.

-	We've...got some redacted stuff on the board. I appreciate this isn't so helpful for you guys, but they're a couple of things we're just not ready to commit to publicly, and you should hear about both this year.

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>