---
date: 2024-08-18
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# August 2024
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of July - 5th Of August:**


Costs/Donations |      $
---|---
Monthly Patreon Donations¹| $80.28
Monthly Paypal Donations¹| $528.89 (yes, this is not a typo)
Total Donations (Month)| $608.57
Existing Rollover Donations| $242.48
---|---
Dedicated Server Cost²| -$85.14
Hetzner VPS Speedtest Cost| -$3.39
---|---
**Remaining Donation Funds**³   |  **$763.12**

---

### State of the Slab

**Current staff tasks being tracked as of 18th August 2024⁴:**

![State of the Slab August 2024](./../../../assets/images/kanban/2024/August.png "State of the Slab August 2024")

**Here's a recap of the staff team actions throughout the last two months:**

#### The small stuff:
- We continued the Decked Out community crossover event, welcoming the VintageBeef and Scar communities onto custom server instances of the Decked Out map. We were relieved to get this wrapped up ahead of the Season 4 launch, and a huge shoutout to Dex, Mens, and Twist for their hard work in making these crossover events happen, they've been really well received by all communities involved.

- We delegated all responsibility of the hotly-requested Slabserver Wiki to the slightly regretful requestee, GamingTwist. Rising to his new responsibilities, he has already setup Discord OAuth, spent an entire week battling MediaWiki formatting, and is now working on ways to improve ease of community collaboration, which should enable more people to help contribute to the project.

#### The medium stuff:
- We've overhauled our main Proxy network for Season 4, moving from Bungeecord to Velocity due to the former being deprecated. We've also managed to remove the second Proxy network, documented [here](https://github.com/Slabserver/Slabserver-Documentation/wiki/Architecture) for those not familiar with our previous setup.
  - Our architecture pages will be updated shortly, once Ionos is fully cancelled and decommissioned within the next month.

- We polled for the Season 4 tweaks, to investigate whether we should adjust the Phantom spawning behaviour, and support invisible item frames within Survival. These poll results helped to inform us that nearly 75% of people wanted each of those things, so:
  - We've written a custom plugin called InvisItemFrames. that makes Item Frames invisible with Splash or Lingering Potions of Invisibility. We're very satisfied with the implementation, which you can read the details of [here](https://discord.com/channels/146701388234227712/146702455487463424/1271588913378627585), and hope that it strikes a good balance between the custom functionality, while still feeling somewhat vanilla-adjacent.
  - We've increased the time it takes for Phantoms to spawn, from 3 in-game days to 9 in-game days. Happy bad sleep schedules!
  - We've updated [our Season 4 tweaks page](https://slabserver.org/tweaks) with this information.


#### The big stuff:
- We ended Season 3 of Slabserver, after a wonderful five years of the server being live. Our farewell events included our prestigious awards show The Slabbys, and a finale tour of the server, both of which aimed to recognise the huge amount of creativity and time that people have put into this server during those five years. To end the season, a heartfelt speech was prepared for you all, which can be read [here](https://discord.com/channels/146701388234227712/596920517643206656/1264855382149566534), and the Season 3 world download can be found [here](../../../documentation/general/downloads.md)

- We setup and ran an extensive community-wide speedtest to our current datacentre, and a potential new server host, in order to further investigate and understand the widespread connection issues that members have experienced in terms of speed and stability. This speedtest was completed in two stages, and provided us with a huge amount of quantitive data to understand what benefits a potential server move for Season 4 would have. And so...

- We provided notice to cancel our server with the current host Ionos, and ordered a new dedicated server from [Hetzner](https://www.hetzner.com/)! We ordered the [AX42](https://www.hetzner.com/dedicated-rootserver/ax42/configurator/#/) config, with an additional 1TB SSD and a 22TB HDD, which should also help to mitigate any of the storage issues we've experienced in the past couple years. This server move also brings a neat bump in server hardware for us once again, and with the results of the speedtest we're confident that this move should prove to be a much more stable connection for the majority of members.
  - Moving server hosts is no small feat for us to pull off, and certainly not an easy one, but we'll get no better opportunity to pull this off than during our S3->S4 downtime. Keep your fingers crossed for us having a smooth transfer over to the new server, and we'll share in #announcements when the server move is scheduled/completed!

- We... had an absolute nightmare of an experience trying to get hold of our server from Hetzner. Due to the custom server configuration we ordered by including the additional hard drives, our order took far longer than we anticipated to be physically provisioned in their datacentre, and ended up exceeding Hetzner's own estimates listed on their site, or provided by their support team on multiple occasions.
  - Over the course of the two weeks between Season 3 and Season 4, we contacted Hetzner's support and datacentre teams almost every single day, attempting to get any further information, accurate estimates for the server, or have it be expedited, given the rapidly approaching launch date of Season 4.
  - This dragged on for long enough that we had to revert our cancellation of our old Ionos server, just to ensure that we had our old server to launch on for Season 4, should Hetzner not arrive in time. This ended up being a very wise move, given that our breakthrough with Hetzner came barely two days before Season 4 began.
  - Through our persistence and rapport with Hetzner's support team, or from them simply hoping to never hear from me ever again, they were able to help approve us a new AX42 server with no custom configuration that had just become available, and then lodge a support ticket with the datacentre to add the new drives. This proved to be significantly quicker, presumably due to the fact that this didn't require anything new to be physically built in the Hetzner datacentre, and not even two hours later, our Hetzner server was finally online.
    - A huge thanks to their sales and support teams pulling through for us on this one!

- We've done far more technical setup behind-the-scenes for Season 4 than I can ever reasonably do justice in these Transparency Reports. Deprecating old plugins, configuring new plugins, reconfiguring our various Proxy plugins around the new Velocity setup. Transferring every gameserver and community bot over from Ionos to Hetzner, reconfiguring settings and databases in each server as a result, all while trying to minimise downtime for each. I cannot state enough just how much work has gone into the double-whammy of Season 4 and our server migration.
  - It is a huge testament to my peers in the staff team, particularly Chris, that this was pulled off anywhere near as successfully as it has been - and for the most part been barely visible to the community. During the S4 launch, many of our databases were still running on the Ionos server while the Survival world ran on Hetzner, resulting in a crazy "silly string and superglue" style setup to get the launch working in time. But it all came together in the end, by the skin of our teeth, and so...

- We launched Season 4, finally, after six months of it being announced, and well over a year of internal planning and preparation for an eventual reset. As mentioned above, due to all the delays and hurdles we had getting hold of the new Hetzner server, getting the new Survival network online really came down to the wire, and I am incredibly proud of how well the launch went with all that considered.
  - We also developed a plugin for launch, simply named "Buster", that let us dynamically adjust settings such as render distance, simulation distance, and mobcap limits. This was the result of the internal stress testing we mentioned in our [June 2024](06-june.md) Transparency Report, and made a huge difference to our server stability and performance on launch. To those who bet against Finey's promises of 20tps at launch, never bet against a bald man.

#### The other stuff
- We received a significant number of Paypal donations this month, in response to the Survival reset and dedicated server move. Several people noted that their contributions were to help cover the additional month of Ionos cost we've incurred due to the Hetzner delays, and two individuals contributed an astronomical amount of the total donations this month. From the bottom of our hearts, thank you to everyone for your incredibly generous donations.

- We hosted the Season 4 Ender Dragon fight... and have a missing Dragon Egg. After the Ender Dragon was first defeated, four candles appeared where the Dragon Egg should have been, along with a [mysterious book](https://github.com/user-attachments/assets/355ba211-0b64-46f3-bdb1-756ef015f038).
  - In addition to the Dragon Wings, the Ender Dragon now also drops an [Initiation Candle](https://github.com/user-attachments/assets/ac714d77-f258-427e-b3bf-6079701b67e9)...


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