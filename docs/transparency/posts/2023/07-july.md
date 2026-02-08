---
date: 2023-09-18
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# July 2023
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of June - 5th Of July:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹ | $6.73
Monthly Patreon Donations¹ | $61.87
Monthly Cryptocurrency Donations¹ | $0
Total Donations (Month)| $68.60
Existing Rollover Donations| $238.71
---|---
Dedicated Server Cost²| -$88.82
---|---
**Remaining Donation Funds** ³   |  **$218.49**

---

### State of the Slab
**Current staff tasks being tracked as of 11th July 2023⁴:**

![State of the Slab July 2023](./../../../assets/images/kanban/2023/July.png "State of the Slab July 2023")

Here's a recap of the staff team actions throughout the last month:
- We’ve connected our Pterodactyl API to our internal monitoring system [Nagios](https://www.nagios.com/solutions/linux-monitoring/), so that we receive internal pager notifications if any of our major servers are detected as being offline for multiple minutes straight.
  - While members can (and often will!) spot a server going down before this system alerts us, having such systems in place is a good practice for any dedicated system or infrastructure like ours.

- We’ve addressed some long-standing external backup costs, by reducing the frequency with which we prune. Each prune also re-downloads objects in order to rebuild the packs of backups. and downloading data is the most costly part of our external backup provider [Backblaze](https://www.backblaze.com).
  - Pruning backups now only occurs twice a month, with the added benefit of our incremental backups being kept slightly longer on average - between 28 and 42 days. Our [documentation on backups](../../../documentation/minecraft/server-architecture.md#backups) has been updated to reflect this change.

- We’ve sadly set our subreddit /r/slabserver to ‘restricted’, following Reddit’s API changes which killed most third party apps, and to reflect that our community has long since moved to Discord. Transparency reports will now be posted on GitHub.

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>