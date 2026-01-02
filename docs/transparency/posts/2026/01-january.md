---
date: 2026-01-01
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# January 2026
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of December - 31st Of December:**

N.B. that due to Hetzner changing our invoice billing date to the 25th of each month in [October 2025](../2025/10-october.md), the previously used Transparency Report window of 5th -> 5th each month no longer applies. 

Hetzner and Patreon payments could also vary if their payment dates (25th and 5th, respectively) were during a weekend, and so it is much easier to just calculate the breakdown for the entirity of a previous month.

The Transparency Reports will now run from the 1st to the 31st of each month - though due to this month being used to adjust that by having a shorter timeframe, there has therefore not been a Patreon payment since the 5th December 2025.

The next Patreon donation will appear as normal in Febuary's Transparency Report.

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $75.27
Monthly Patreon Donations¹| N/A
Total Donations (Month)| $75.27
Existing Rollover Donations| $829.51
---|---
Dedicated Hetzner Server Cost² | -$124.00
---|---
**Remaining Donation Funds**³   |  **$780.78**

---

### State of the Slab

**Current staff tasks being tracked as of 1st January 2026⁴⁵:**

![State of the Slab January 2026](./../../../assets/images/kanban/2026/January.png "State of the Slab January 2026")

**Here's a recap of the staff team actions throughout the last month:**

- We've updated Slabserver to 1.21.11, and have continued to iterate upon and improve our workflow for doing so. This update was the smoothest upgrade process we've had to date since using the [Staging server](https://slabserver.org/documentation/minecraft/server-architecture/#staging-network) and [SlabCLI tool](https://github.com/Slabserver/slabcli), and we hope to find even more improvements with the Minecraft updates throughout 2026.
- We've made a number of [minor additions, fixes, and tweaks](https://github.com/Slabserver/slabserver.github.io/commits/main) to the [slabserver.org](https://slabserver.org) website, most notably to move all the legacy Transparency Reports over to the site, ensure that our Server Plugins page is up-to-date, and to simplify our Architecture diagram page on the off-chance that anyone accidentally opens it.
- We've created a small plugin called [SimpleServerSender](https://github.com/Slabserver/SimpleServerSender) that allows for players to quickly transfer between servers using `/survival`, `/creative`, and `/nexus`.
  - This was requested quite some time ago in our #feedback channel, and despite the length of time taken to complete it, hopefully goes to show how seriously we do take the feedback in that channel!
- We made a long overdue update to our #welcome banner for the first time in five years, removing the outdated servers referenced and updating it to fit with Discord's latest theme colours.
- We've released [The Great Slabserver Poll 2026](https://forms.gle/mGkGsjjGxJaQufcX8), our annual tradition of gathering feedback on various parts of our Discord and Minecraft servers.
    - We really do care about and read through every single piece of feedback, even from those who are inactive, so if you're reading this, please do take the time to complete the poll. 
        - This is also a good time to mention that some of the most negative comments we can recieve often comes with no username attached - we really, _really_ do care, and we would much rather be able to address these with you - or be approached directly about them - than to have no meaningful way of resolving the issue without further communication. Thanks in advance!

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
