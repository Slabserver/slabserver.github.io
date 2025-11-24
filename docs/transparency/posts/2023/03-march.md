---
date: 2023-03-17
authors: [DaUltraMarine]
description: >
  Our monthly Transparency Reports, containing our monthly donations and summarising the progress our staff team has made recently.
search:
  boost: 0.5

---

# March 2023
<!-- more -->
### Donation Breakdown
**Breakdown Between 5th Of February - 5th Of March:**

Costs/Donations |      $
---|---
Monthly Paypal Donations¹| $6.08
Monthly Patreon Donations¹| $61.83
Monthly Cryptocurrency Donations¹| $0
Total Donations (Month)| $67.91
Existing Rollover Donations| $308.94
---|---
Dedicated Server Cost²| -$86.34
---|---
**Remaining Donation Funds** ³   |  **$290.51**

---

### State of the Slab
**Current staff tasks being tracked as of 17th March 2023⁴:**

![State of the Slab March 2023](./../../../assets/images/kanban/2023/March.png "State of the Slab March 2023")

Here's a recap of the staff team actions throughout the last month:

- We fixed two bugs related to synchronising advancement and death messages between our Survival and Resource worlds. This fix unfortunately had a bug where advancement and death messages would be duplicated when both worlds were occupied, so we fixed that one too.

- We did some internal work to streamline the process of creating new long-term game servers, such as Chainworld and Third Life. Specifically:
    - We streamlined our firewall policies to require minimal maintenance long-term.
    - We created a new (staff-only) Discord command to create and configure new servers, without the auto-deletion features that `/gamenight` uses. We’ve been getting increasing amounts of requests for this as more long-term game servers get suggested, so for those of you keen to host longer term servers on Slab, there’s never been a better time!

- We’ve been taking important privacy measures to protect exposure of IP addresses in our temporary gamenight servers’ logs. Please read our #suggestions topic [here](https://discord.com/channels/146701388234227712/549320896590905344/1086287847230812211) for more details.

- We fixed an issue where Gamenight servers created for versions 1.7 - 1.18 were not correctly patching the infamous [Log4j vulnerability](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition).

---

### Server Donation Links
Paypal: [https://slabserver.org/paypal](https://slabserver.org/paypal)

Patreon: [https://slabserver.org/patreon](https://slabserver.org/patreon)

---

<sup>¹ Donation amount listed is after transaction fees have taken place.</sup>

<sup>² The dedicated server hosts all of our game servers, databases, as well as our various Discord bots. You can find more detail on this [in our documentation](../../../documentation/minecraft/server-architecture.md).</sup>

<sup>³ Unless disclosed otherwise, this will always be put forward towards next months server costs, and will be displayed in ‘rollover donations’ within the transparency report.</sup>

<sup>⁴ There will be occasions that certain items on the board are redacted, should they still be in [draft](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#creating-draft-issues), or contain sensitive tasks or information.</sup>