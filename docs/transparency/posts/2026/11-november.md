---
date: 2026-11-02
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# November 2026
<!-- more -->
### Donation Breakdown
**Breakdown Between 1st Of October - 31st Of October:**

Costs/Donations |      $
---|---
Monthly Paypal Donations [^1]| $8.02
Monthly Patreon Donations [^1]| $109.53
Total Donations (Month)| $117.55
Existing Rollover Donations| $924.36
---|---
Dedicated Hetzner Server Cost [^2] | -$131.79
---|---
**Remaining Donation Funds** [^3]   |  **$910.12**

[Backblaze](./../../../documentation/minecraft/server-architecture.md#backups) costs in October were $10.34. This expense is currently not paid for via the server donation funds.

---

### State of the Slab

**Current staff tasks being tracked as of 1st November 2026:** [^4] [^5]

![State of the Slab November 2026](../../../assets/images/kanban/2026/November-light.png#only-light "State of the Slab November 2026")
![State of the Slab November 2026](../../../assets/images/kanban/2026/November-dark.png#only-dark "State of the Slab November 2026")

**Here's a recap of the staff team actions throughout the last month:**

- We helped Mumbo's staff team host a Hermitfan 'Advancement Race' cross-community event on our server hardware, attended by five other Hermitcraft communities.
    - Admittedly, interest in this event within Slabserver was lower than we expected - so we'd appreciate any feedback on what part(s) didn't appeal to our community.
- We announced our own 'Wish Life' event, a new twist on the Life Series format coinciding with the Hermits' own 'Final Life' series.
    - Wish Life starts this weekend, so be sure to read the [announcement](https://discord.com/channels/146701388234227712/146702455487463424/1565835017500762252) for more information about the event, and how you can take part.
- We've made some improvements to HuskSync when saving player data during server shutdown, in the hope of fixing the inventory duplication and rollback issues when the server restarts.
- We patched our dedicated server to address the infamous [PHP vulnerabilities](https://www.php.net/archive/2026.php#2026-10-21-5) that were made public last month, which affected a significant number of internet-facing systems.
- We've made several accessibility, performance and UX improvements to [slabserver.org](https://slabserver.org), including a dialog for the 'Join our servers' button on the homepage, and support for [Tags](https://zensical.org/docs/setup/tags/) to filter searches.
    - You should also find that our homepage and documentation pages load faster after following several [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) audit recommendations. Notably, we've optimised a number of images to use the `.webp` format, and are no longer using Google Fonts.
    - As part of this work, we've raised a couple of bugs with Zensical, to address some issues we've found and help improve this framework for other users of this open-source project. Huge thanks to the Zensical team for having both issues fixed within 24 hours of reporting!

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

[^1]: Donation amounts shown reflect the amounts received after transaction fees charged by [PayPal](https://www.paypal.com/webapps/mpp/paypal-fees) and [Patreon](https://www.patreon.com/pricing).
[^2]: The dedicated server hosts our game servers, databases, and bots. See [Server Architecture](../../../documentation/minecraft/server-architecture.md) for more details.
[^3]: Unless otherwise disclosed, this will always be put forward towards next months server costs, and displayed in `Existing Rollover Donations` within the Transparency Report.
[^4]: We will not show items from the kanban board that contain sensitive tasks and information, or are [draft issues](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues).
[^5]: The [Priority](../../../assets/images/kanban/Priority.png) and [Size](../../../assets/images/kanban/Size.png) labels are a rough estimate of the work involved, and are purely assigned based on vibes.
