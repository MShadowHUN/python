from szekhely import Szekhely
from jatekos import Jatekos
from csapat import Csapat
from typing import *

elsojatekos:Jatekos=Jatekos("Hetfo","Helga",7,"fogado")
masodikjatekos:Jatekos=Jatekos("Kedd","Kinga",38,"libero")
harmadikjatekos:Jatekos=Jatekos("Szerda","Szilvia",40,"center")
negyedikjatekos:Jatekos=Jatekos("Csütörtök","Csilla",62,"négyesutő")
otodikatekos:Jatekos=Jatekos("Péntek","Patrícia",7,"szélsőütő")
hatodikjatekos:Jatekos=Jatekos("Vasárnap","Viktória",117,"fogado")
szekhely:Szekhely=Szekhely("Szeged",6720,"Csongrád-Csanád","Alma utca", 7)

jatekosok:List[Jatekos]=[]

jatekosok.append(elsojatekos)
jatekosok.append(masodikjatekos)
jatekosok.append(harmadikjatekos)
jatekosok.append(negyedikjatekos)
jatekosok.append(otodikatekos)
jatekosok.append(hatodikjatekos)

csapat:Csapat=Csapat("Vasvári Csanádok",jatekosok,szekhely)
print(csapat)