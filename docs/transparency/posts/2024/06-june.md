---
date: 2024-06-11
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# June 2024
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of May - 5th Of June:**

Costs/Donations |      $
---|---
Monthly Patreon Donations¹| $83.54
Monthly Paypal Donations¹| $11.68
Total Donations (Month)| $95.22
Existing Rollover Donations| $228.72
---|---
Dedicated Server Cost²| -$85.65
---|---
**Remaining Donation Funds**³   |  **$238.29**

---

### State of the Slab

**Current staff tasks being tracked as of 11th June 2024⁴⁵:**

![State of the Slab June 2024](./../../../assets/images/kanban/2024/June.png "State of the Slab June 2024")

**Here's a recap of the staff team actions throughout the last month:**
- We've finally decided on the Season 4 seed, after weeks upon weeks of deliberation. We've searched countless seeds using the amazing [Cubiomes](https://github.com/Cubitect/cubiomes-viewer) tool, slowly whittling down our selection from discussions back and forth within the team. The seed was first found by JadeLake, and slowly but surely became our top choice through a very lengthy process of elimination. We're really pleased with the final pick, and we can't wait for you to see it live on the server.
- We've assembled Spawn and Nether Hub design teams, that are hard at work to help design the form and functionality of these areas ahead of launch. There's some truly amazing plans going on within these groups, and if you keep your eye on the voice channels you might even catch them doing some of the designing live! 
  - Please note that **anyone** can help to build these designs once Season 4 goes live, or contribute further to the projects. This is just to get our initial approach and functionality in place for these areas.
- We've welcomed GamingTwist as a Technical Assistant to the team, where he will be helping out on the techy side of our community work a little more officially.
- We added 1.20.6+ support for Gamenight Servers, and added Java 21 support to any Gamenight servers created for Minecraft 1.19 and above.
  - As part of this, we also fixed an issue where Gamenight servers created for Minecraft 1.17.x would use an incompatible version of Java.
- We've conducted some Season 4 stress testing, to better understand what optimisation steps we are able to take on the server, both prior to and during the launch. We're fairly confident that the server will perform much better than any Survival launch so far!
- We've updated all of our datapacks for Season 4, refactoring our files around the significant and sweeping (and often stupid) changes that Mojang has made in 1.20.6 and [1.21](https://github.com/Slabserver/Transparency-Reports/assets/10583568/e6d9efd3-de1f-4023-a33b-6243114a335a).
  - Of particular note, we've removed The Tunnel and Etho's Wrench files, as well as the custom coral crafting recipes. We've now added a shapeless undyed shulker box crafting recipe for consistency with the other custom shulker recipes.
    - Please pray for no more breaking changes before 1.21 releases, this has all been a massive pain to update.
  - Please also note that Slabserver advancements will not be added for launch, as most of the Season 3 ones will eventually carry over once we have new coordinates for the location-based triggers.
- We began the long-awaited Decked Out community crossover event, welcoming the Iskall, Rendog, and Xisuma communities onto custom server instances of the Decked Out map. The events have been received incredibly well by all the communities, and this event wouldn't have been possible without Twist's invaluable work. While Tango and his staff team have now declined to join in, we hope to welcome the GoodTimesWithScar and VintageBeef communities within this month as well, who have been far more enthusiastic about exploring our DO dungeon.
- We rewrote Etho's Wrench as a plugin, to move the more complex logic away from datapack jank and to make it more maintainable in the future.
  - This task has existed in some form or other on the staff board for 3.5 years, and we finally got there in the end!
-  We've significantly refined our internal Kanban board as you likely saw in the screenshot above, moving most of our 'In Draft' issues that weren't previously visible within State of the Slab into fully refined issues.  As part of this, the label system has been overhauled too, now showing a Priority and Size estimate for each issue, and a Milestone label to categorise related issues.
  - These Priority and Size labels are purely informational, intended to provide the community with more context about the issue. They will always be a rough estimate for the amount of work involved... though quite honestly are just based on vibes.
    - A neat thing to note is the date that the issue on the sidebar was created, just to highlight the timeframes for some of our work! The 'Begin Season 4 of Slabserver' was initially drafted after the 2023 Great Slabserver Poll, as we started to refine the technical and infrastructure improvements we'd need for a new Season. It's rare that we can share the more detailed view of these issues, but hopefully this is a fun little bit of proof for just how far in advance some things start to be worked on.

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