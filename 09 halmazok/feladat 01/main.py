from typing import *
import random
import time
import os

halmaz:List[int]=[]
elemekSzama:int=None
osszeg:int=None
ketjegyuSzamok:int=None
paratlanSzamokOsszege:int=None
nullaraVegzodoSzamok=None
max:int=None
minIndex:int=None

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

def sum(osszeadandoHalmaz:List[int])-> int:
    eredmeny:int=0
    for item in osszeadandoHalmaz:
        eredmeny+=item

    return eredmeny

def parosKiirasa(kiirandoHalmaz:List[int])->None:
    for item in kiirandoHalmaz:
        if(item%2==0):
            print(f"{item}", end="\t")

def ketjegyuSzamokSzama(keresesHalmaza:List[int])->int:
    eredmeny:int=0
    for item in keresesHalmaza:
        if(abs(item)>9 and abs(item)<100):
            eredmeny +=1

    return eredmeny    

def egyjegyuSzamok(keresesHalmaza:List[int])->int:
    for item in keresesHalmaza:
        if(abs(item)<10):
            print(f"{item}", end="\t")

def paratlanSzamok(keresesHalamz:List[int])->int:
    eredmeny:int=0
    for item in keresesHalamz:
        if(item%2==1):
            eredmeny+=item
    return eredmeny
 
def nullaraVegzodoSzamokSzama(keresesHalmaz:List[int])->int:
    eredmeny:int=0
    for item in keresesHalmaz:
        if(item %10==0):
            eredmeny+=1
    return eredmeny

def novekvoSorrend(keresesHalmaz:List[int])->List[int]: 
    temp:int=None
    for i in range(0, len(keresesHalmaz)-1,1):
        for j in range(i +1, len(keresesHalmaz), 1):
            if(keresesHalmaz[j] < keresesHalmaz[i]):
                temp=keresesHalmaz[i]
                keresesHalmaz[i]=keresesHalmaz[j]
                keresesHalmaz[j]=temp
    return keresesHalmaz

def legnagyobbErtek(keresesHalmaz:List[int])->int:
    maximum:int=keresesHalmaz[0]
    for index in range(1, len(keresesHalmaz)):
        if(keresesHalmaz[index] > maximum):
            maximum=keresesHalmaz[index]
    
    return maximum

def legkisebbErtekIndexe(keresesHalmaz:List[int])->int:
    index:int=0
    minimum:int=keresesHalmaz[index]

    for i in range(1, len(keresesHalmaz)):
        if(keresesHalmaz[index] < minimum):
            minimum=keresesHalmaz[i]
            index=i
    
    return index
elemekSzama=elemSzamBekerese()
halmaz=listaFelotleseRandomSzamokkal(elemekSzama)

os.system("cls")
print("A halmaz elemei: \n")
halmazKiirasa(halmaz)

#írassuk ki a tartalmát fordított sorrendbe
print("\nA halmaz elemei fordított sorrendbe: \n")
halmazKiirasaFordítva(halmaz)

#adjuk osssze a halmaz elemeit
osszeg=sum(halmaz)
print(f"\nA halmaz elemeinek osszege: {osszeg}")

#atlag
print(f"\nA halmaz elemeinek átlaga: {osszeg / elemekSzama}")

#páros elemek kiirasa
print("\nPáros elemek:")
parosKiirasa(halmaz)

#ketjegyu szamok szama
ketjegyuSzamok=ketjegyuSzamokSzama(halmaz)
print(f"\nA halmazban lévő ketjegyű számok száma: {ketjegyuSzamok}")

#egyejegyu szamok szama
print(f"\nA halmazban lévő egyjegyű számok:")
egyjegyuSzamok(halmaz)
 

paratlanSzamokOsszege=paratlanSzamok(halmaz)
print(f"\nA halmaz elemeinek osszege: {paratlanSzamokOsszege}")

nullaraVegzodoSzamok = nullaraVegzodoSzamokSzama(halmaz)
print(f"\nA halmazban {nullaraVegzodoSzamok} db nullára végződő szám van.")

rendezettHalmaz:List[int]=novekvoSorrend(halmaz)
print(rendezettHalmaz)

max=legnagyobbErtek(halmaz)
print(f"\nA halmaz legnagyobb értéke: {max}")

minIndex=legkisebbErtekIndexe(halmaz)
print(f"\nA halmaz legkisebb értékének helye: {minIndex}")