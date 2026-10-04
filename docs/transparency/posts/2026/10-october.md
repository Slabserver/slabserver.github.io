---
date: 2026-10-04
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# October 2026
<!-- more -->
### Donation Breakdown
**Breakdown Between 1st Of September - 31st Of September:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $92.23
Monthly Patreon Donations¹| $3.53
Total Donations (Month)| $95.76
Existing Rollover Donations| $961.22
---|---
Dedicated Hetzner Server Cost² | -$132.62
---|---
**Remaining Donation Funds**³   |  **$924.36**

[Backblaze](./../../../documentation/minecraft/server-architecture.md#backups) costs in September were $8.45. This cost is not currently paid for via the donation funds.

---

### State of the Slab

**Current staff tasks being tracked as of 3rd October 2026⁴⁵:**

![Image title](../../../assets/images/kanban/2026/October-light.png#only-light)
![Image title](../../../assets/images/kanban/2026/October-dark.png#only-dark)

**Here's a recap of the staff team actions throughout the last month:**

- We updated Slabserver to Minecraft 26.3, and upgraded the majority of our plugins and datapacks to be compatible with this version. You can find the full patchnotes in our [#announcements](https://discord.com/channels/146701388234227712/146702455487463424/1555982130180526184) channel.

- We updated The Passage to Minecraft 26.3, along with several important bugfixes. You can find the full patchnotes in our [#s4-puzzle](https://discord.com/channels/146701388234227712/614586586104987671/1555981317492048053) channel.
    - This includes a workaround for a bug Mojang introduced in 26.3, which completely broke part of the puzzle. If you have a Mojira account, we'd really appreciate you voting for [MC-31227](https://bugs.mojang.com/browse/MC-312277).

- We updated this website to use [Zensical](https://zensical.org), a new static site generator replacing [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Zensical is made by the same team, due to their need to [move away from the MkDocs framework](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/#whats-changing-in-mkdocs-20).
    - As part of this upgrade, we've also made several changes to the website, including:
        - Adopting a refreshed look to the website using modern UI elements from Zensical, while adapting these elements to align with our previous design.
        - Adding function and utility to pages, such as our [Building Guidelines](../../../documentation/minecraft/building-guidelines.md) now featuring an interactive [Nether Tunnel calculator](../../../documentation/minecraft/building-guidelines.md#nether-tunnels) to use.
        - Updating the [Server Architecture](../../../documentation/minecraft/server-architecture.md) page to use the open-source [Mermaid diagrams](https://mermaid.ai/open-source/) software, instead of [Diagrams by Mingrammer](https://diagrams.mingrammer.com).
        - Rewording a number of pages, in an effort to keep the site's content concise and succinct.
        - Improving the formatting of the website homepage and documentation overview.

- We fixed a bug where Ender Pearls  would persist between Resource World resets, which affected a number of players who were using stasis chanbers.

- We have been in touch with the other Hermit staff teams about another another cross-community event, which we hope to share more details about soon!

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
