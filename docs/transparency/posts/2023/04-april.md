---
date: 2023-05-01
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# April 2023
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of March - 5th Of April:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $6.08
Monthly Patreon Donations¹| $56.25
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $62.33
Existing Rollover Donations| $290.51
---|---
Dedicated Server Cost²| -$85.44
---|---
**Remaining Donation Funds** ³   |  **$267.40**

---

### State of the Slab
**Current staff tasks being tracked as of 30th April 2023⁴:**

![State of the Slab April 2023](./../../../assets/images/kanban/2023/April.png "State of the Slab April 2023")

**Here's a recap of the staff team actions throughout the last month:**

- We hosted an April Fools server event, parodying Fortnite’s Season 2 by overhauling the visuals of our many areas around spawn. We've also released a world download for the April Fools changes, which can be found here: [link!](https://drive.google.com/file/d/1sgVcn6oNWd_7rEhTjIE75CTDyZcIPdXP/view?usp=share_link)

- We updated all of our servers to 1.19.4. In doing so, we felt a great disturbance in the Force, as if millions of Slabber mods suddenly cried out in terror and were suddenly silenced.

- We fixed advancement messages made in the survival and resource world not displaying in the other server (hopefully for the last time!) thanks to relying on the Paper API instead of packet listening, which can change between versions.

- We’ve spent several months monitoring some unexpected costs with our Backblaze and Restic backup system. This turned out to be from pruning the restic backups each day, causing much of the backup cache data to be redownloaded from Backblaze. We’re continuing to monitor what the best balance of backup history versus avoiding excessive pruning costs is.

- We migrated our kanban board to GitHub Projects, after ZenHub decided to try and charge a lot of money. Our State of the Slab screenshots will look a little different, but the new board is a little simpler, a little cleaner, and now integrated in the main Slabserver organization on GitHub. We’re _so_ professional.

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>