from typing import *
import random
import time
import os

halmazA: List[int] = []
halmazB: List[int] = []
ujHalmaz: List[int] = []
elemekSzama: int = None

def elemSzambekerese() -> int:
    eredmeny: int = None
    temp: str = ""

    while(eredmeny == None):
        temp = input("Kérem adja meg az elemek számát: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
            return eredmeny
        else:
            print("Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

def halmazFeltoltese(elemSzam: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, elemSzam, 1):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def kiiras(halmaz: List[int]) -> None:
    for szam in halmaz:
        print(f"{szam}", end=" ")

def halmazUj(halmaz1: List[int], halmaz2: List[int], elemek: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(elemek):
        eredmeny.append(halmaz1[i])
        eredmeny.append(halmaz2[i])

    return eredmeny

elemekSzama = elemSzambekerese()
halmazA = halmazFeltoltese(elemekSzama)
kiiras (halmazA)
print("\n")

elemekSzama = elemSzambekerese()
halmazB = halmazFeltoltese(elemekSzama)
kiiras(halmazB)
print("\n")

ujHalmaz = halmazUj(halmazA, halmazB, elemekSzama)
kiiras(ujHalmaz)
