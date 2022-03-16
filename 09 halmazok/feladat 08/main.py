from typing import *
import time
import os

halmaz: List[int] = []

def szamBeolvasasa() -> int:
    eredmeny: int = None
    temp: str = ""

    while(eredmeny == None):
        temp = input("Kérema adja meg a számot: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
            return eredmeny
        else:
            print("Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

def listaFeltoltese() -> List[int]:
    eredmeny: List[int] = []
    ujElemekSzama: int = 0
    szam: int = None
    letezik: bool = None

    while(ujElemekSzama < 3):
        szam = szamBeolvasasa()
        letezik = True if(eredmeny.count(szam) == 1) else False #megvizsgáljuk, hogy a szám szerepel-e a listában (háromkomponensű üzemeltetővel)
        if(not letezik): # ha a szám nem létezik, akkor a listába kerül, az új elemek számát is meg kell növelni egyel
            eredmeny.append(szam)
            ujElemekSzama += 1
        else:
            ujElemekSzama = 0
            print(f"{szam} már szerepel a listában.")
            time.sleep(2)
            os.system("cls")

    return eredmeny


halmaz = listaFeltoltese()
print(halmaz)