from typing import *
import random
import time
import os

halmaz:List[int]=[]
elemekSzama:int=None

def hiba(szoveg)->None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def elemSzamBekerese()-> int:
    eredmeny:int=None
    while(eredmeny==None or eredmeny<2):
        temp:str=input("Kérem adja meg a halmaz elemeinek a számát:")
        if(temp.isdigit()):
            eredmeny=int(temp)
            if(eredmeny<2):
                hiba("A halmaz elemeinek száma legalább 2-nek kell lennie")
        else:
            hiba("Nem számot adot meg")
        
    return eredmeny

def listaFelotleseRandomSzamokkal(elem:int)->List[int]:

    eredmeny:List[int] = []
    for i in range(elem):
        eredmeny.append(random.randint(-10,10))
        time.sleep(0.005)
    
    return eredmeny

def halmazKiirasa(kiirandoHalmaz:List[int])->None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def halmazKiirasaFordítva(kiirandoHalmaz:List[int])->None:
    max:int=len(kiirandoHalmaz)-1
    for index in range(max, -1, -1):
         print(f"{kiirandoHalmaz[index]}", end="\t")

elemekSzama=elemSzamBekerese()
halmaz=listaFelotleseRandomSzamokkal(elemekSzama)

os.system("cls")
print("A halmaz elemei: \n")
halmazKiirasa(halmaz)

#írassuk ki a tartalmát fordított sorrendbe
print("A halmaz elemei fordított sorrendbe: \n")
halmazKiirasaFordítva(halmaz)