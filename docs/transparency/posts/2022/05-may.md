---
date: 2022-05-23
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# May 2022
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of April - 5th Of May:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $19.82
Monthly Patreon Donations¹| $56.66
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $76.48
Existing Rollover Donations| $541.48
---|---
Dedicated Server Cost²| -$82.90
---|---
**Remaining Donation Funds**³   |  **$535.06**

---

### State of the Slab
**Current staff tasks being tracked as of 23rd of May 2022⁴:**

![State of the Slab May 2022](./../../../assets/images/kanban/2022/May.png "State of the Slab May 2022")

**Here's a recap of the staff team actions throughout the last couple months:**

- We’ve fixed shruggie! Our existing implementation has had a long standing bug somewhere between DiscordSRV and VentureChat’s interaction with one another, which has now been replaced with a very simple plugin of our own instead that leverages the chat method in the Bukkit API. 

- We have a [new template on our GitHub](https://github.com/DaMarine/Slabserver-Bugs/issues/new/choose) for reporting bugs, that should be a lot more user friendly to complete!

- We also have a nifty new automation in Ergobot that raises server update checklists on our staff board when Mojang releases new versions, to make sure we’re even more thorough with our testing and upgrade processes. Was this necessary? No. Was this fun? …No, not really, GitHub’s API is a bit crap.

- We’ve made some network changes to our servers to cancel all attempts to connect to our SMP servers except through our proxy. This has no bearing on normal players, but was done to prevent offline UUIDs attempting to connect to our servers and spoof messages in-game.

- We updated our Snacker/Inactivity bot to the latest JDA, and now have support for tracking messages in threads! No more avoiding the Robot Overlords, the Robot Overlords see all.

- We've... taken breaks. Several of the staff team have reduced their presence the past couple months, in order to better focus on their energy, and mental health. Running this community day in day out can be a lot of work, with so much still that doesn't get covered in these transparency reports - rule infringements, bans, appeals, infrastructure issues, debugging, proof of concept ideas, seecret projects - the list goes on. While our team actions may be a little fewer and farther between, we really appreciate people being patient with us as we try to take care of the community as well as ourselves.

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>