---
date: 2024-10-05
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# October 2024

### Donation Breakdown
**Breakdown Between 5th Of September - 5th Of October:**

<!-- more -->

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $31.85
Monthly Patreon Donations¹| $69.95
Total Donations (Month)| $101.80
Existing Rollover Donations| $586.21
---|---
Dedicated Ionos Server Cost (Final Two Weeks)²| -$36.99
Dedicated Hetzner Server Cost² | -$115.92
---|---
**Remaining Donation Funds**³   |  **$535.80**

---

### State of the Slab

**Current staff tasks being tracked as of 5th October 2024⁴:**

![State of the Slab October 2024](./../../../assets/images/kanban/2024/October.png "State of the Slab October 2024")

**Here's a recap of the staff team actions throughout the last two months:**

- We re-established our [Restic and Backblaze backup solution](https://github.com/Slabserver/Slabserver-Documentation/wiki/Architecture#backups) on our new host, Hetzner. This ensures that our critical server data is securely stored in multiple locations, and our [disaster recovery](https://aws.amazon.com/what-is/disaster-recovery) solutions remain functional in case of any unforeseen incidents.
- We expanded the worldborder in The Nether from 1000 to 2000 blocks, to give players more room to build in this dimension of the main world.
- We added the Etho’s Wrench plugin to S4, which offers a convenient way to rotate blocks in Survival mode. This version comes with some adjustments from S3: 
    - To obtain a basic "Rotate" wrench, drop a Carrot on a Stick into Soul Fire.
    - For the advanced wrenches:
        - Flip Wrench: Drop a Carrot on a Stick + Copper Ingot into Soul Fire.
        - Face Wrench: Drop a Carrot on a Stick + Gold Ingot into Soul Fire.
- We fixed a number of bugs on Survival that were identified since the launch of Season 4:
    - Fixed players appearing at coordinates 0, 0 in The Nether after logging out
    - Fixed Resource World enderporters not teleporting players when activated.
    - Fixed The Nether and The End dimensions in the Resource World having their difficulty set to Easy instead of Hard.
    - Fixed `/alpha` not functioning correctly due to a missing command alias
    - Fixed Etho’s Wrench not being obtainable on the Creative Server, and not respecting other players' plot permissions or boundaries.
    - Fixed Modbot’s `!ip` command not correctly returning the Survival server version.

- We released the S4 LOD data for use with the Distant Horizons mod, allowing players to preload the raw world data for the entire map without having to generate it themselves.
    - Note that this is only the raw world data - builds will still have to be rendered manually once within render distance.
- We’ve started collecting submissions for the S4 directory, namely submissions of shop listings and Nether tunnel locations. If you’d like to help by contributing information for your shop or tunnel, please see the [#community-bulletin](https://discord.com/channels/146701388234227712/1279485910450307082/1279485910450307082) post. 

- We updated several of our servers to Minecraft 1.21.1, to support the latest versions of plugins like Axiom and FAWE.
- We officially announced, at long last, the upcoming Season 4 puzzle for Slabserver—a project that has been in development for over four and a half years.
    - We can’t wait to share more with you soon, but we’re taking a little more time to playtest, polish, and perfect it, to make sure it’s the best experience possible for you all. Look out for a more detailed status update on the puzzle in the next six weeks, as we get closer to revealing more…
---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>

<sup>⁵ The [Priority](../../../assets/images/kanban/Priority.png) and [Size](../../../assets/images/kanban/Size.png) labels for our State of the Slab Board are a rough estimate of the amount of work involved, and quite honestly are just assigned based on vibes.</sup>