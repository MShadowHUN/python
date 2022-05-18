import imp
from typing import *
from diak import Diak
from osztaly import Osztaly
from diakio import DiakIO


diakok:List[Diak]=DiakIO.read("adatok.txt")

print("A diakok adatai: \n")
for diak in diakok:
    print(f"{diak}\n")

print (f"Az osztályba {len(diakok)} diák jár.\n")

atlag:float=Osztaly.atlag(diakok)
print(f"Az osztály átlaga:{atlag:1.2f}")

joDiakok:List[Diak]=Osztaly.legjobbak(diakok)
print(f"Az osztály legjobb diákjai:")
for diak in joDiakok:
    print(f"{diak}\n")

Osztaly.atlagfelett(diakok, atlag)
print("Az osztályba átlag feletti diákok exportja megtörtént")