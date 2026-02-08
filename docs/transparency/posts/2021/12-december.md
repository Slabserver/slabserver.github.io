---
date: 2021-12-07
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# December 2021
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of November - 5th Of December:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $19.86
Monthly Patreon Donations¹| $80.51
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $100.37
Existing Rollover Donations| $382.95
---|---
[SoYouStart] Dedicated Server Cost²| -$0.00 (payments now stopped)
[Ionos] Dedicated Server Cost²| -$0.00 (first month free)
---|---
**Remaining Donation Funds** ³   |  **$483.32**

---

### State of the Slab
**Current staff tasks being tracked as of 7th of December 2021⁴:**

![State of the Slab December 2021](./../../../assets/images/kanban/2021/December.png "State of the Slab December 2021")

**Here's a recap of the staff team actions throughout the last month:**

- We’ve finally completed our server move to Ionos! Every single game server and Discord bot has now been migrated, and we are no longer paying for our SoYouStart server. [Our documentation](../../../documentation/minecraft/server-architecture.md) has also been updated accordingly.
    - This move has been months in the works, and not only has this come with a performance bump and increased storage space, it finally unblocked a couple other items on our ZenHub boards, most notably:
        - We’ve fixed the dreaded ‘join survival but end up on creative’ bug!
        - We’ve moved hosting of stats, dynmap, and bluemap back onto our server, rather than have them hosted externally by Frogperson.
        - As part of this migration, our server IP and several ports have changed, so if you weren’t already, please use our slabserver.org links, particularly with the survival/creative join bug now addressed.
        - We’re finally able to continue our CoreProtect database migration to MySQL, started way back in February and paused for nearly 6 months due to lack of storage space!
    - As part of this move, we’ve deleted our Gmod, Terraria, and Building Game servers that had been powered off for several months, and have no plans to rehost in the foreseeable future.
    - _I’ll take this moment to speak more personally about the server move. We internally committed to moving to a better host on 27th July, so it’s been a long long journey to get us to this point. Everything from scouring options, discussing cost and locations in staff channels and #suggestions, getting our server order past Ionos’s fraud detection, breaking down the monolithic task of our data migration into more manageable chunks and then the painstaking task of ensuring no regressions along the way. A huge amount of thanks to Chris for all of his sysadmin help in rebuilding the dedi server from scratch. It’s a breath of fresh air to have a clean slate for our server infrastructure, and I look forward to the months and years ahead being made easier by Ionos!_

- We have a new application bot! Applications are now handled entirely through Discord DMs with Sethwing, taking full advantage of the new Discord button, selection menus and making for a much more snazzy experience overall. This also means we’ve been able to remove our dependency on Google Drive entirely, which has been reflected in [privacy.slabserver.org](https://privacy.slabserver.org).

- We’ve fixed several bugs with [MinecraftStats](https://github.com/pdinklag/MinecraftStats), the tool that powers [stats.slabserver.org](https://stats.slabserver.org), specifically cases where the statistics could end up in negative values.

- We now have a Golang bot that automatically polls the Mojang API for new snapshots or releases, and upon detecting a new release, will restart our Snapshot and Spawn servers automagically. The Snapshot server world even gets deleted and recreated each time! This bot currently runs as part of some Go HTTP experiments (and is affectionately named Er*Go*bot), and while not likely to have a presence in Discord for the foreseeable future, will hopefully automate even more behaviour for our dedicated server in the months ahead.

- We’ve begun preparing for our servers to upgrade to 1.18! Our Gamenight Server Installer already supports 1.18 (save for the UHC option), and we’re doing what we can to prepare for the other major servers to update, ahead of Paper having stable support for Minecraft 1.18. Keep an eye on #announcements for our progress updating the Survival server!

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>