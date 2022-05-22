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

vanE:bool=Osztaly.vanEkitunoTanulo(diakok)
if(vanE):
    print("Van kitűnő tanuló")
else:
    print("Nincs kitűnő tanuló ")


eredmenyek:Dict[str,int]=Osztaly.jegyek(diakok)

print(f"{eredmenyek}")

eredmenyek2:Dict[str,int]=Osztaly.masikjegyek(diakok)
for (key,value) in eredmenyek2.items():
    print(f"\t-{key} : {value}")
