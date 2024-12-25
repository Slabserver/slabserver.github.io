# Lag Guidelines

### **Villagers & Trading halls**



Villagers are consistently terrible for server performance. For trading halls, best practices are:

<img align="right" width="40%" src="https://github.com/Slabserver/Slabserver-Documentation/assets/72826160/ac587f82-c4a2-4dca-86fc-7fa029043280"/>

* To share them with other players where possible, or keep the villagers to the needed minimum if you're using them solo.

* To ensure they are loaded only when intended to be used, and are built 9+ chunks away from your base - particularly so for larger trading halls.

* To ensure sure your Villagers aren't perpetually scared by Zombies, as it'll **a)** cause small calculation bursts and **b)** spawn golems that cost even more performance in the long run.
    *  Breaking line of sight between the mobs should prevent this from happening.



### **Automatic Farms**

For automatic farms in general (private or public), best practices are:

<img align="right" width="40%" src="https://github.com/Slabserver/Slabserver-Documentation/assets/72826160/7fe4f901-852f-4ba7-b724-164ab848a011"/>

* To consider whether you really need the farm. We have a wide variety of effective and efficient community farms for most essential items.

* To have an overflow protection, so that items don't get bunched up anywhere when overproducing.

* To have the farm shut off completely, as soon as it reaches full storage capacity.

* To ensure that they are only loaded when intended to be used - particularly so for larger farms that require a lot of mob spawning or item dropping,.

### **Bunched Up Mobs**

For animal farms, killing chamber, or any other similar situation, best practices are:

<img align="right" width="40%" src="https://github.com/Slabserver/Slabserver-Documentation/assets/72826160/0872376a-191b-43f6-81a3-3dc4f335456c"/>

* To ensure mobs are not bunched up in small areas, 1x1 holes or water streams, as mobs colliding is also notoriously terrible for server performance!

* To cull any colliding mobs to as few entities as possible, particularly so where mobs are bunched up for a prolongued amount of time. 
    * For longer AFK sessions, please make sure to use wither roses or similar to kill mobs as efficiently as possible, and prevent them from bunching up. For animal farms, simply breed them again whenever required.

* To use vines (any vine should work) to reduce collisions, when you simply cannot avoid keeping multiple mobs in a smaller chamber.

