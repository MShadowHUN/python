from typing import *
import random

halmaz:List[int]=[]
osszeg:int=None
atlag:float=None
elemszam:int=random.randint(10,20)
otszazFelettiSzamokSzama:int=0

#halmaz generalasa
def halmazFeltoltes(elem:int)->List[int]:
    eredmeny:List[int]=[]
    szorzo:int=1
    szam:int=None
    for i in range(0, elem, 1):
        szam=random.randint(100,999)
        eredmeny.append(szam * szorzo)
        szorzo *=-1

    return eredmeny

def halmazKiirasa(kiirandoHalmaz:List[int])->None:
    for szam in kiirandoHalmaz:
        print(f"{szam}", end="\t")

def sum(bejarandoHalmaz:List[int])->int:
    eredmeny:int=0
    for szam in bejarandoHalmaz:
        eredmeny +=szam

    return eredmeny

def otszazFelettiSzamokSzamanakMeghatarozasa(bejarandoHalmaz:List[int])->int:
    eredmeny:int=0
    for szam in bejarandoHalmaz:
        if(szam>500):
            eredmeny +=1

    return eredmeny

#főprogram
halmaz=halmazFeltoltes(elemszam)
halmazKiirasa(halmaz)
osszeg=sum(halmaz)
atlag=osszeg/elemszam
print(f"\nA halmaz elemeinek összege:  {osszeg}")
print(f"\nA halmaz elemeinek átlaga: {atlag}")
otszazFelettiSzamokSzama=otszazFelettiSzamokSzamanakMeghatarozasa(halmaz)
print(f"\nA halmazban {otszazFelettiSzamokSzama} db 500 feletti szám van")