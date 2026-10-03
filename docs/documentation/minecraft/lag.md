# Lag Guidelines

### **Villagers & Trading Halls**

Villagers are consistently terrible for server performance. Best practices are:

<img align="right" width="40%" src="/assets/images/lag/1.png"/>

* Share trading halls with other players where possible, or keep villagers to a minimum if you're using them solo.

* Ensure trading halls are loaded only when in use, and are built 9+ chunks away from your base.

* Ensure villagers aren't perpetually scared by zombies, as it **a)** causes small calculation bursts and **b)** spawns iron golems that will lag the server even more.
    *  Breaking line of sight between villagers and zombies will prevent them from being perpetually scared.



### **Automatic Farms**

For automatic farms in general (private or public), best practices are:

<img align="right" width="40%" src="/assets/images/lag/2.png"/>

* Use community farms instead -  there are a variety of effective and efficient farms for most essential items.

* Use overflow protection in the farm design, so items don't get bunched up anywhere when overproducing.

* Make the farm shut down as soon as its storage is full.

* Make sure the farm is only loaded when in use, especially farms with a lot of mob spawns or item drops.

### **Colliding Mobs**

For animal farms, killing chamber, or any other similar situation, best practices are:

<img align="right" width="40%" src="/assets/images/lag/3.png"/>

* Ensure mobs are not crammed in small areas, 1x1 holes or water streams, as mob collisions are terrible for server performance and one of the main sources of lag.

* Cull any colliding mobs to as few entities as possible, particularly where mobs are bunched up for a long amounts of time. 
    * For longer AFK sessions, use wither roses or similar mechanics to kill mobs as efficiently as possible.
    * For animal farms, simply breed them when required.

* Use vines to reduce collisions if you cannot avoid having multiple mobs in a smaller chamber.
