# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

with Diagram(filename="../images/architecture/game_servers", show=True, direction="TB"):

    # custom icons are relative to the filename above
    pterodactyl = Custom("Pterodactyl", "icons/pterodactyl.png")
    
    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Game Servers"):
            proxy = Docker("Proxy")
            survival = Docker("Survival")
            resource = Docker("Resource")
            passage = Docker("Passage")
            creative = Docker("Creative")
            snapshot = Docker("Snapshot")
            misc = Docker("Misc. Servers")

            servers = [proxy, survival, resource, passage, creative, snapshot, misc]

            pterodactyl >> Edge(color="#004da4") >> servers
           