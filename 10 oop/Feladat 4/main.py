from tanulok import Tanulo
from csoport import Csoport
from typing import *

elsotanulo:Tanulo=Tanulo("Hétfő","Henrik","1997.07.14")
masodiktanulo:Tanulo=Tanulo("Kedd","Kevin","1997.06.24")
harmadiktanulo:Tanulo=Tanulo("Szerda","Szilárd","1997.07.04")
tanulok:List[Tanulo]=[]
tanulok.append(elsotanulo)
tanulok.append(masodiktanulo)
tanulok.append(harmadiktanulo)

csoport:Csoport=Csoport("10.b info", tanulok)
print(csoport)