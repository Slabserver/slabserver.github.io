# diagram.py
from urllib.request import urlretrieve

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MariaDB
from diagrams.saas.chat import Discord
from diagrams.generic.blank import Blank
from diagrams.custom import Custom

#Pterodactyl
pterodactyl_url = "https://avatars.githubusercontent.com/u/16179146"
pterodactyl_icon = "pterodactyl.png"
urlretrieve(pterodactyl_url, pterodactyl_icon)

#phpMyAdmin
phpmyadmin_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/PhpMyAdmin_logo.svg/2560px-PhpMyAdmin_logo.svg.png"
phpmyadmin_icon = "phpmyadmin.png"
urlretrieve(phpmyadmin_url, phpmyadmin_icon)

#Pl3xMap
Pl3xMap_url = "https://camarosa.xyz/img/dynmap.png"
Pl3xMap_icon = "Pl3xMap.png"
urlretrieve(Pl3xMap_url, Pl3xMap_icon)

with Diagram(filename="main_network", show=True, direction="LR"):

    # applications = Discord("#applications")
    ingamechat = Discord("#ingamechat")

    with Cluster("Dedicated Ubuntu Server"):

        # applicationbot = Docker("Application Bot")

        Pl3xMap = Custom("Pl3xMap", Pl3xMap_icon)
        paddingPl3xMap = Blank("") 

        with Cluster("Bungee Network 1"):
            proxy1 = Docker("Proxy 1")
            padding1 = Blank("")
            resource = Docker("Resource")
            survival = Docker("Survival")
            padding2 = Blank("")

            proxy1 - Edge(penwidth="0.0") -  padding1
            proxy1 >> Edge(color="darkgreen") << survival
            proxy1 >> Edge(color="darkgreen") << resource
            proxy1 - Edge(penwidth="0.0") -  padding2

        with Cluster("MySQL / MariaDB"):  
            maindb = MariaDB("Databases")
            phpmyadmin = Custom("phpMyAdmin", phpmyadmin_icon)

    # applications >> Edge(color="#7289DA") >> applicationbot
    # applicationbot >> proxy1

    survival >> Edge() << maindb
    resource >> Edge() << maindb
    maindb << phpmyadmin
    survival >> Edge(color="#7289DA") >> ingamechat
    resource  - Edge(penwidth="0.0") - paddingPl3xMap
    survival >> Pl3xMap