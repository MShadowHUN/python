from typing import *
import random

honapok:Tuple[str]=(
    "Január",
    "Február",
    "Március",
    "Április",
    "Május",
    "Június",
    "Július",
    "Augusztus",
    "Szeptember",
    "Október",
    "November",
    "December"
)
fizetesek:List[int]=[]
szjaErteke:float=None
tbErteke:float=None
nyugdijErteke:float=None

def fizetesekGeneralasa()->List[int]:
    eredmeny:List[int]=[]
    for i in range(0,12,1):
        eredmeny.append(random.randint(300,10000))
    
    return eredmeny

def fizetesekOsszege(berek:List[int])->int:
    eredmeny:int=0
    for ber in berek:
        eredmeny+=ber
    return eredmeny

def SZJA(berek:List[int])->float:
    osszeg:int=fizetesekOsszege(berek)
    return osszeg * 0.335

def tb(szja:float)->float:
    return szja* 0.45

def nyugdij(szja:float)->float:
    return szja* 0.55

def fizetesekKiirasa(berek:List[int], honap:Tuple[str])->None:
    for index in range(0,12,1):
        print(f"{honap[index]}-{berek[index]} EUR")

fizetesek=fizetesekGeneralasa()
fizetesekKiirasa(fizetesek, honapok)
szjaErteke=SZJA(fizetesek)
tbErteke=tb(szjaErteke)

print(f"SZJA: {szjaErteke} EUR")
print(f"TB hozzajarulas: {tbErteke} EUR")