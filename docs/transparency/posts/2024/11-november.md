---
date: 2024-12-08
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# November 2024
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of October - 5th Of November:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $6.08
Monthly Patreon Donations¹| $74.62
Total Donations (Month)| $80.70
Existing Rollover Donations| $535.80
---|---
Dedicated Hetzner Server Cost² | -$114.61
---|---
**Remaining Donation Funds**³   |  **$501.89**

---

### State of the Slab

**Current staff tasks being tracked as of 5th November 2024⁴⁵:**

![State of the Slab November 2024](./../../../assets/images/kanban/2024/October.png "State of the Slab November 2024")

**Here's a recap of the staff team actions throughout the month:**

- We’ve written an approval process and guidelines for using Chunkloaders on the Survival server, by popular request. You can find these guidelines [here](https://discord.com/channels/146701388234227712/146702455487463424/1294198592352817184).
- We introduced a ‘Member Report’ feature into Chester, aimed at providing our community with a clearer, consistent way of flagging member behaviour to staff, and indicating whether they feel it warrants further action.
    - This feature was first mentioned in the January 2024 Transparency Report, though has taken us some time to fully complete, and Season 4’s preparation and launch naturally took priority for us.
    - We highly recommend reading the full [announcement post](https://discord.com/channels/146701388234227712/146702455487463424/1294733545108930611) and [#feedback thread](https://discord.com/channels/146701388234227712/1294712190238068806) for far more detail on the How and Why of this feature, as it’s been incredibly important to us that we get this one right.
      - If you have any further thoughts or questions to share about it, we’d welcome your input on the thread or via Modmail.
- We reverted our attempt to move our server proxy network to [Velocity](https://papermc.io/software/velocity), and are once again using [Bungeecord](https://github.com/SpigotMC/BungeeCord). While our tests with Velocity prior to Season 4 proved promising, our main reason for moving away from Bungeecord was due to confusion that it was being deprecated alongside [Waterfall](https://papermc.io/software/waterfall) - which later turned out to be incorrect.
    - Velocity plugins also proved to not be as feature-complete or as stable in production as our Bungeecord setup had been, particularly for the Resource World functionality. With reassurances from the Spigot developers that they had no plans to deprecate Bungeecord, we switched our setup back.
    - This change was made several months ago in August, but was missed in the Transparency Reports at the time due to the amount of changes and technical work during Season 4’s launch.
- We addressed even more issues on Survival that have been occurring on Survival since the launch of Season 4:
    - Fixed respawn locations being forgotten when players disconnecting from the Main World
    - Fixed several inconsistencies with respawn locations when dying in the Resource World
    - Fixed `/r` timeouts and chat colours not working by reverting our chat plugin back to VentureChat, having switched to FairyChat in our attempt to move to Velocity
- We launched the Season 4 directory for the [Nether Hub](https://slabserver.org/hub) and [Shopping District](https://slabserver.org/shops), which aims to improve the discoverability of various destinations in each of these locations.
- We shared a status update on the Season 4 puzzle, which continues to be worked on tirelessly behind-the-scenes almost every single day. The puzzle is now expected to release in the first half of 2025, and we are hopeful that timings will coincide for it to launch around our ten year anniversary in April.

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