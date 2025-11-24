---
date: 2022-12-30
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# November 2022
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of October - 5th Of November:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $6.08
Monthly Patreon Donations¹| $48.34
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $54.42
Existing Rollover Donations| $421.49
---|---
Dedicated Server Cost²| -$85.62
---|---
**Remaining Donation Funds** ³   |  **$390.29**

---

### State of the Slab

**Here's a recap of the staff team actions throughout November:**

- We've... done a lot of work with our Coreprotect data. We had a long term goal to move our Coreprotect data from Sqlite to MySQL/MariaDB, as a proper SQL solution that best fits our use case. This was largely successful, but in the move had some mapping issues with some of the block IDs used internally by Coreprotect. Our cleanest solution to fix this was start a fresh database for Coreprotect, and keep the old data purely for reference purposes.
  - We introduced a new plugin, Mineprotect, to access this old Coreprotect data ingame alongside our new data. This was an amazing QOL plugin by MC that helps to differentiate the data from the two plugins, and in cases of the aforementioned mapping issues where block IDs aren't tracked properly, shows the possible block/item IDs that Coreprotect could be referring to.
  - We will, eventually, move this old data to a form of external 'glacier' cloud storage to free up some well needed space while still allowing us to access it, but the estimated costs for this were higher than anticipated and as of right now, we are no further on moving this.
  - While very little of this work was done in November, I promised in Octobers Transparency Report this'd be covered in November's, so here you are!

- We announced the Hermitfan UHC, taking place on January 22nd! We've put a lot of work into helping make this happen, and will be setting up and hosting the event ourselves on Slab's dedicated hardware. Joehills and VintageBeef themselves will be participating, and as of the time of writing, we have all four members of our team selected! We're still figuring out what the best way is of allowing spectators and/or streams of the event, so watch this space!

- We introduced `/back` on the Creative server, to return you to your plot after visiting spawn, or another person's plot.

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>