---
date: 2024-01-19
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# January 2024
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of December - 5th Of January:**

Costs/Donations |      $
---|---
Monthly Patreon Donations¹| $65.12
Monthly Paypal Donations¹| $6.62
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $71.20
Existing Rollover Donations| $192.95
---|---
Dedicated Server Cost²| -$88.28
---|---
**Remaining Donation Funds**³   |  **$176.41**

---

### State of the Slab

**Current staff tasks being tracked as of 18th January 2024⁴:**

![State of the Slab January 2024](./../../../assets/images/kanban/2024/January.png "State of the Slab January 2024")


**Here's a recap of the staff team actions throughout the last month:**

#### The small stuff:
- We released The Great Slabserver Poll of 2024, gathering demographics, suggestions, and feedback from the community. In less than 24 hours, we've already received more responses than last year, and we can't wait to see what the final total ends up being.
    - It'll take us a couple of weeks after the poll closes to sort through and discuss the results in depth, but we'll aim to publish any major decisions from the poll in #announcements as soon as we can!

- We fixed an exploit with Lite2Edit involving falling block entities - thank you to the community member that flagged this to us!

- We fixed an issue with [Ergobot](https://discord.com/channels/146701388234227712/147017948912025601/1166833906461450280) where the snapshot server was not correctly restarting after a new Minecraft release. This was a result of the [mojang version manifest](https://piston-meta.mojang.com/mc/game/version_manifest.json) inconsistently returning etags, and we've updated the bot to handle this accordingly.

- We updated Modbot with a small quality of life improvement to [inform muted members how long before their mute expires](https://i.imgur.com/QoI0kww.png).

- We updated [slabserver.org/macros](https://macros.slabserver.org) based on the discussion and input from the [#suggestions topic](https://discord.com/channels/146701388234227712/549320896590905344/1171904397048041494).
    - We now explicitly allow macros for repeated actions on a delay, due to it being possible via some OS settings for quite some time and falling in a grey area of our ruleset.
    - We now also allow macros that work when unfocused and/or AFK, due to this already being possible for those with secondary PCs/Laptops or VMs. Mods that emulate this behaviour are now also allowed.
    - We also moved away from the ancient reddit link for this, to our nice swanky GitHub pages. Cool.
    - During this discussion, we also updated our rules to explicitly ban entity radars within our [client mod](https://github.com/Slabserver/Slabserver-Documentation/wiki/Client-Mods) rules.
    - As a final note, this set of changes was made back in November, but did not happen in time to be included in November's State of the Slab.

- We fixed a bug where the Dragon Egg would be briefly obtainable in the Resource World.

- We did some small research into Custom World Generation and custom structures, mainly as a hobby project and to better understand what may be possible for future resource worlds or spinoff servers. At the time of writing, we have no active plans to use this research, but after my many petitions for Mojang to re-add the functionality, it was nice to finally understand what is possible to achieve.

#### The medium stuff:
- We've started to (try and) organise a Decked Out crossover event with the other Hermitcraft communities, and invite them to come and tour a copy of our amazing Decked Out project from the Survival server.
    - We've received a huge amount of interest on this, and Tango himself did express interest in joining too. Sadly, planning that particular crossover with him has been rather tricky, and very limited in communication from him and his team - we shall remain hopeful, but at the very least will continue to focus on sharing this amazing project with many members across the various HC communities.
    - This is all still in the early stages of planning, and will require a significant amount of preparation in terms of staffing and infrastructure - watch this space!


#### The big stuff:
- We've started to address a number of the actionable items from the roundtable conclusions regarding moderation, as referenced in [November's transparency report](https://github.com/Slabserver/Transparency-Reports/wiki/November-2023): 
    - We're implementing a more formal reporting system, aimed at shifting agency and responsibility for punishments and bans toward the community. Conceptually, this would be integrated into Chester like modmail, but filled out similar to our [whitelist application UI](https://i.imgur.com/Y86ENhy.png). On our end, it'll be flagged as a 'Member Report' to acknowledge, address, and provide some form of outcome.
        - We will compliment this with a revised internal system for tracking the number of reports and outcomes for any given member, giving us a better 'at a glance' view of their standing in the community. Once this system is fully implemented, we will share more details on this system and our process.
 - We're also reassessing our internal staff team structure, roles, and permissions.
    - While the staff team aims to operate on a flat hierarchy internally, over time small deviations had occurred with the permissions staff members had available within our Discord, server panel, and dedicated server. This has largely been standardised now, with the exception of SSH access to our dedicated server - staff members with this access have made valid use cases, and a consensus of requiring access from the rest of the team.
    - This is also to try and consider the best balance of:
        - **a)** better reflecting this style of internal flat hierarchy to the community
        - **b)** better reflecting the modular responsibilities that each staff member feels uniquely placed to provide
        - **c)** better reflecting community members own perception of each staff member, and what they are best suited towards
   - This has been and remains a longer term topic and goal for us to refine. The topic has been slowed due to several staff taking a hiatus in the past few months, but we hope to make some more progress or proposals on this internally within the next month or so.

- We've held extensive investigations and discussions around the widespread use of client mods which had been explicitly banned on our survival server.
  - This conversation has been covered at length within our Discord channels, and has been better explained in our community bulletin channels than State of the Slab can concisely describe. You can find links to the respective bulletin posts here: [#1](https://discord.com/channels/146701388234227712/597097924991647774/1191799624768426054) [#2](https://discord.com/channels/146701388234227712/597097924991647774/1191799688324714557) [#3](https://discord.com/channels/146701388234227712/597097924991647774/1194833849117589576) [#4](https://discord.com/channels/146701388234227712/597097924991647774/1198258566465847317)

- We're looking for feedback on how the format of these Transparency Reports and State of the Slab moving forward. If you enjoy these reports and roundups, we'd really appreciate your input on the #suggestions topic [here](https://discord.com/channels/146701388234227712/549320896590905344/1198001515470786661)!

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>