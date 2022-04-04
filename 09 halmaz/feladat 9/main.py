from typing import *
import random
import time
import os

halmaz: List[int] = []
elemSzam: int = 0
eredmenySzotar: Dict[str, List[int]] = []

def elemekSzama() -> int:
    eredmeny: int = 0
    temp: str = ""

    while(eredmeny == 0):
        temp = input("Kérem adja meg az elemek számát: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
            return eredmeny
        else:
            print("Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

def listaFeltoltese(elemekSzam: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, elemekSzam, 1):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def elemekSzetvalasztasa(feldolgozandoHalamz: List[int]) -> Dict[str, List[int]]:
    szotar: Dict[str, Dict[int]] = {
        "pozitivSzamokHalmaza" : [],
        "negativSzamokhalmaza" : []
        }

    for szam in feldolgozandoHalamz:
        if(szam < 0):
            szotar["negativSzamokhalmaza"].append(szam)
        else:
            szotar["pozitivSzamokHalmaza"].append(szam)

    return szotar

elemSzam = elemekSzama()
halmaz = listaFeltoltese(elemSzam)
print("Az eredeti halmaz: ")
print(halmaz)

eredmenySzotar = elemekSzetvalasztasa(halmaz)
print("Pozitív számok halmaza: ")
print(eredmenySzotar["pozitivSzamokHalmaza"])

print("Negatív számok halmaza")
print(eredmenySzotar["negativSzamokhalmaza"])