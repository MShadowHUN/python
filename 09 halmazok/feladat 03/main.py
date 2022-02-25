from typing import *
import random

halmaz:List[int]=[]
osszeg:int=None
atlag:float=None
hatos:int=0
paratlan:int=0

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

def legnagyobbKulcsErteke(szotar:Dict[int, int])->List[int]:
    kulcs:int=None
    ertek:int=0
    eredmeny:List[int]=[]

    #a legnagyobb ertek kikeresese a szotarbol ertek alapjan
    for key, value in szotar.items(): #vegiglepkedunk a szotar ossz elemen a kulcs-ertek parokkal
        if(szotar[key] > ertek):
            kulcs=key
            ertek=szotar[key]

    for key,value in szotar.items: #kikeressuk azokat a kulcsokat melyeknek az erteke egyenlo az ertek valtozoval, mivel azok a kulcsok (dobasok) szama fordul elo a legtobbszor
        if(szotar[key]==ertek):
            eredmeny.append(key)
    return eredmeny

def legtobbetEloforduloSzam(bejarando:List[int])->List[int]:
    szotar:Dict[int,int]={} #Dict[kulcs->szam, value->szam elofordulasi szama]
    #meghatarozzuk az elofordulasi szamoket
    for szam in bejarando:
        if(szam in szotar):
            szotar[szam] +=1 #szotar[szam]-> a kulcshoz tartozo erteket adja vissza
        else:
            szotar[szam]=1
    #lista =[2,4,1,1,6,3,5]
    #szotar={1:2, 2:1, 3:1, 4:1, 5:1, 6:1}
    eredmeny:List[int]=legnagyobbKulcsErteke(szotar)
    return eredmeny

halmaz=halmazFeltoltes()
print(halmaz)
osszeg=sum(halmaz)
atlag=osszeg/7
print(f"\nDobások átlaga: {atlag}")
hatos=hatosokszama(halmaz)
print(f"\n {hatos} db-szor dobtunk hatos")
paratlan=paratlanSzamokSzama(halmaz)
print(f"\n {paratlan} db páratlan szám van")

legtobbetEloforduloSzamok:List[int]=legtobbetEloforduloSzam(halmaz)
print(f"\n A legtobbet elofordulo szam(ok): {legtobbetEloforduloSzamok}")