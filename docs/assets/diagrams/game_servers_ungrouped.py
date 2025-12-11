# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

with Diagram(filename="../images/architecture/game_servers_ungrouped", show=True, direction="TB"):

    # custom icons are relative to the filename above
    pterodactyl = Custom("Pterodactyl", "icons/pterodactyl.png")
    
    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Game Servers"):
            proxy = Docker("Proxy")
            survival = Docker("Survival")
            resource = Docker("Resource")
            creative = Docker("Creative")
            gamenight = Docker("Gamenight")
            snapshot = Docker("Snapshot")
            misc = Docker("Misc. Servers")

            servers = [proxy, survival, resource, creative, snapshot, gamenight, misc]

            pterodactyl >> Edge(color="#004da4") >> servers
           