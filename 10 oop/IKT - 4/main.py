from champion import PogChamp
from worrior import Worrior
from mage import Mage
from bruiser import Bruiser
from typing import *

anwen:Mage=Mage("Anwen", "elf")
galadriel:Mage=Mage("Galadriel", "elf")
tauriel:Worrior=Worrior("Tauriel","elf")
eowyn:Worrior=Worrior("Eowyn","ember")
lurtz:Bruiser=Bruiser("Lurtz", "Ork")

Mage.CastSpell(anwen)
Mage.CastSpell(galadriel)
Worrior.GetRage(tauriel)
Worrior.GetRage(eowyn)
Bruiser.LetsMakeTrouble(lurtz)

print(f"{anwen}\n")
print(f"{galadriel}\n")
print(f"{tauriel}\n")
print(f"{eowyn}\n")
print(f"{lurtz}\n")

hosok:List[PogChamp]=[anwen, galadriel, tauriel, eowyn]

for PogChamp in hosok:
    if(PogChamp.tamad(lurtz)):
        print(f"{PogChamp.nev} legyőzi Lurtzot\n")
    else:
        print(f"{PogChamp.nev} nem győzi le Lurtzot\n")