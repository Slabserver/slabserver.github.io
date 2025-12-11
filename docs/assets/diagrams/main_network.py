# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MariaDB
from diagrams.saas.chat import Discord
from diagrams.generic.blank import Blank
from diagrams.custom import Custom

with Diagram(filename="../images/architecture/main_network", show=True, direction="LR"):

    # custom icons are relative to the filename above
    phpmyadmin = Custom("phpMyAdmin", "icons/phpmyadmin.png")
    pl3xmap = Custom("Pl3xMap", "icons/pl3xmap.png")
    ingamechat = Discord("#ingamechat")
    paddingPl3xMap = Blank("") 

    with Cluster("Dedicated Ubuntu Server"):

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
            phpmyadmin

    survival >> Edge() << maindb
    resource >> Edge() << maindb
    maindb << phpmyadmin
    survival >> Edge(color="#7289DA") >> ingamechat
    resource  - Edge(penwidth="0.0") - paddingPl3xMap
    survival >> pl3xmap