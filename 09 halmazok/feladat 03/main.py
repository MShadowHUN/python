from typing import *
import random

halmaz:List[int]=[]
osszeg:int=None
atlag:float=None
hatos:int=0
paratlan:int=0
max:Dict[int,int]=[]

def halmazFeltoltes()->List[int]:
    eredmeny:List[int]=[]
    for i in range(0,7,1):
        eredmeny.append(random.randint(1,6))

    return eredmeny

def sum(bejarandoHalmaz:List[int])->int:
    eredmeny:int=0
    for szam in bejarandoHalmaz:
        eredmeny+=szam
    
    return eredmeny

def hatosokszama(bejarandoHalmaz:List[int])->int:
    eredmeny:int=0
    for szam in bejarandoHalmaz:
        if(szam==6):
            eredmeny +=1
    
    return eredmeny

def paratlanSzamokSzama(bejarando:List[int])->int:
    eredmeny:int=0
    for szam in bejarando:
        if(szam%2==0):
            eredmeny +=1
    
    return eredmeny

def maximum(bejarando:List[int])->Dict[int,int]:
    eredmeny:Dict[int,int]=[]
    for szam in bejarando:
        if(dic.has_key(szam)):
            dic[szam]+1
        else:
            dic.add(szam, 1)

halmaz=halmazFeltoltes()
print(halmaz)
osszeg=sum(halmaz)
atlag=osszeg/7
print(f"\nDobások átlaga: {atlag}")
hatos=hatosokszama(halmaz)
print(f"\n {hatos} db-szor dobtunk hatos")
paratlan=paratlanSzamokSzama(halmaz)
print(f"\n {paratlan} db páratlan szám van")

max=maximum(halmaz)
print(max)