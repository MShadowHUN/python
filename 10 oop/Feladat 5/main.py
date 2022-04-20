from szekhely import Szekhely
from jatekos import Jatekos
from csapat import Csapat
from typing import *

elsojatekos:Jatekos=Jatekos("Hetfo","Helga",7,"fogado",52)
masodikjatekos:Jatekos=Jatekos("Kedd","Kinga",38,"libero",38)
harmadikjatekos:Jatekos=Jatekos("Szerda","Szilvia",40,"center",7)
negyedikjatekos:Jatekos=Jatekos("Csütörtök","Csilla",62,"négyesutő",40)
otodikatekos:Jatekos=Jatekos("Péntek","Patrícia",7,"szélsőütő",62)
hatodikjatekos:Jatekos=Jatekos("Vasárnap","Viktória",117,"fogado",2)
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

print("A legtöbb pontszammal rendelkező játékos:\n")
print(csapat.legjobbJatekos())

novekvoSorrend:List[Jatekos]=jatekosok.copy
print("Mezszám szerint növekvő sorrendbe:")
