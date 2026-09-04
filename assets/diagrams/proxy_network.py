# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MariaDB
from diagrams.saas.chat import Discord
from diagrams.generic.blank import Blank
from diagrams.custom import Custom

with Diagram(filename="../images/architecture/proxy_network", show=True):

    # custom icons are relative to the filename above
    # ingamechat = Discord("#ingamechat")
    # paddingPl3xMap = Blank("") 

    with Cluster("Dedicated Ubuntu Server"):

        phpmyadmin = Custom("phpMyAdmin", "icons/phpmyadmin.png")
        # pl3xmap = Custom("Pl3xMap", "icons/pl3xmap.png")

        with Cluster("Bungee Network 1"):
            # padding1 = Blank("")
            proxy1 = Docker("Proxy")
            passage = Docker("Passage")
            resource = Docker("Resource")
            survival = Docker("Survival")
            # padding2 = Blank("")

            # proxy1 - Edge(penwidth="0.0") -  padding1
            proxy1 >> Edge(color="darkgreen") << resource
            proxy1 >> Edge() << passage
            proxy1 >> Edge(color="darkgreen") << survival
            # survival > Edge(minlen="0") < passage
            # survival >> Edge(color="darkgreen") << passage

            # proxy1 - Edge(penwidth="0.0") -  padding2

        with Cluster("MySQL / MariaDB"):  
            maindb = MariaDB("Databases")
            phpmyadmin

    survival >> Edge() << maindb
    resource >> Edge() << maindb
    passage >> Edge() << maindb
    maindb << phpmyadmin
    # survival >> Edge(color="#7289DA") >> ingamechat
    # resource  - Edge(penwidth="0.0") - paddingPl3xMap
    # survival >> pl3xmap