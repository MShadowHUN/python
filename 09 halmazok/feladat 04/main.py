import random
from typing import *

#valtozok
elemekszama:int=random.randint(10,20)
halmaz:List[int]=[]
pozitivHalmaz:List[int]=[]

def halmazfeltoltese(elem:int)->List[int]:
    eredmeny:List[int]=[]

    for item in range(0, elem, 1):
        eredmeny.append(random.randint(-100,100))
    return eredmeny

def kiiras(halmaz:List[int])->None:
    for szam in halmaz:
        print(f"{szam}", end="\t")

def pozitivHalmazFeltoltese(halmaz:List[int])->List[int]:
    eredmeny:List[int]=[]

    for szam in halmaz:
        if(szam>=0):
            eredmeny.append(szam)
    return eredmeny

halmaz=halmazfeltoltese(elemekszama)
print(elemekszama)
print("\nA generált halmaz \n")
kiiras(halmaz)
pozitivHalmaz=pozitivHalmazFeltoltese(halmaz)
print("\nA generált pozitív halmaz \n")
kiiras(pozitivHalmaz)