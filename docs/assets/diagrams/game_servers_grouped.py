# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker

with Diagram(filename="../images/architecture/game_servers_grouped", show=True, direction="TB"):

    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Game Servers - Bungee Network 1"):
            proxy = Docker("Proxy")
            survival = Docker("Survival")
            resource = Docker("Resource")
            proxy >> Edge(color="darkgreen") << survival
            proxy >> Edge(color="darkgreen") << resource

        with Cluster("Game Servers - Other servers"):
            creative = Docker("Creative")
            snapshot = Docker("Snapshot")
            gamenight = Docker("Gamenight")
            misc = Docker("Misc. Servers")
            nonbungee = [creative, snapshot, gamenight, misc]
