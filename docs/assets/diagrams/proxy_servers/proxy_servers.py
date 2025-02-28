# diagram.py
from urllib.request import urlretrieve

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MariaDB
from diagrams.saas.chat import Discord
from diagrams.custom import Custom

#phpMyAdmin
phpmyadmin_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/PhpMyAdmin_logo.svg/2560px-PhpMyAdmin_logo.svg.png"
phpmyadmin_icon = "phpmyadmin.png"
urlretrieve(phpmyadmin_url, phpmyadmin_icon)

with Diagram(filename="proxy_servers", show=True):
    
    applications = Discord("#applications")

    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Bots"): 
            applicationbot = Docker("Application Bot")

        with Cluster("Game Servers - Bungee Network 2"):
            proxy2 = Docker("Proxy 2")

        with Cluster("Game Servers - Bungee Network 1"):
            proxy1 = Docker("Proxy 1")

        with Cluster("MySQL / MariaDB"):  
            maindb = MariaDB("Databases")
            phpmyadmin = Custom("phpMyAdmin", phpmyadmin_icon)

    applications >> Edge(color="#7289DA") >> applicationbot
    applicationbot >> proxy1
    applicationbot >> proxy2
    
    proxy1 >> Edge() << maindb
    proxy2 >> Edge() << maindb
    maindb << phpmyadmin