# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

with Diagram(filename="../images/architecture/bots", show=True, direction="TB"):

    # custom icons are relative to the filename above
    pterodactyl = Custom("Pterodactyl", "icons/pterodactyl.png")

    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Bots"):
            emojirolesbot = Docker("Emoji Roles Bot")
            modbot = Docker("Modbot")
            applicationbot = Docker("Application Bot")
            playerlistbot = Docker("Playerlist Bot")    
            snackerinactivitybot = Docker("Snacker/Inactvity Bot")
            musicbot = Docker("Music Bot")
            chester = Docker("Chester")
            ergobot = Docker("ErGoBot")

        bots = [ergobot, musicbot, playerlistbot, emojirolesbot, snackerinactivitybot, chester, modbot, applicationbot]
        pterodactyl >> Edge(color="#004da4") >> bots