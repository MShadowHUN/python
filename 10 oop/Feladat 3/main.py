from case import Gephaz
from cfan import Procihuto
from gpu import Videokartya
from power import Tap
from cpu import Proci
from ram import Ram
from mother import Alaplap
from hdd import Hdd
from ssd import Ssd
from pc import Pc

gephaz:Gephaz=Gephaz("Deep Cool","Matrexx 55 MESH", 440, 210, "E-ATX",4, 480)
procihuto:Procihuto=Procihuto("Noctua","NH-U12S",125,158,"Intel/AMD",12,45 )
videokartya:Videokartya=Videokartya("Gigabyte","1660 Super", 125,6,"RGB",3)
tap:Tap=Tap("Riotoro","Enigma 850 G2",850,"Gold",True,"ATX")
proci:Proci=Proci("AMD","Ryzen 5 3600",65,3.6,3200,6)
ram:Ram=Ram("Kingston","HyperX Fury","DDR4",8,3000)
alaplap:Alaplap=Alaplap("MSI","MPG B550 GAMING PLUS","B550","AMD", "DDR4")
hdd:Hdd=Hdd("Seagate","BarraCuda",2,7200,3.5)
ssd:Ssd=Ssd("Seagate", "MP510",240,1050,3)
pc:Pc=Pc(videokartya,proci,tap,ram,alaplap,gephaz,procihuto,ssd,hdd)
print(pc)