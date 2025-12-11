# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

with Diagram(filename="../images/architecture/backups", show=True, direction="TB"):
    
    # custom icons are relative to the filename above
    restic = Custom("Restic", "icons/restic.png")
    backblaze = Custom("Backblaze B2 Storage", "icons/backblaze.png")

    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Game Servers"):
            proxy = Docker("Proxy")
            survival = Docker("Survival")
            resource = Docker("Resource")
            creative = Docker("Creative")
            snapshot = Docker("Snapshot")
            gamenight = Docker("Gamenight")
            misc = Docker("Misc. Servers")

        servers = [misc, snapshot, gamenight, creative, resource, survival, proxy]

        servers << Edge(color="#a81c2b") >> restic
        restic << Edge(color="#a81c2b") >> backblaze
           