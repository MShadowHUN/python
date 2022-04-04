import time
import os
import random
from typing import *

kaloria:List[int]=[]
osszege:int=None
maxÉrték:int=None
atlag:float=None
szazEsEzerKozott:int=None
csokkenoSorrend:List[int]=[]

def hiba(szoveg:str)->None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

"""feldat 1 """
def kaloriaBevitel()->List[int]:
    eredmeny:List[int]=[]
    temp:str=None

    while(temp==None):
        temp=input("Kérem adja meg az étel kalóriaértékét:")
        if(temp.isdigit()):
            if(int(temp)>=0 and int(temp)<=100000):
                eredmeny.append(int(temp))
                temp=None
            else:
                hiba("Nem 0 és 100.000 között adott meg értéket")
        elif(temp== "#"):
            break
        else:
            hiba("Nem számot adott meg")
    return eredmeny

def osszeg(bejarando:List[int])->int:
    eredmeny:int=0
    for item in bejarando:
        eredmeny+=item
    
    return eredmeny

"""feldat 2 """
def maximum(bejarando:List[int])->int:
    eredmeny:int=0
    for item in bejarando:
        if(item>eredmeny):
            eredmeny=item
    return eredmeny
"""feladat 3"""
def atlagSzamitas(bejarando:List[int], osszeg:int)->float:
    eredmeny:float=osszeg/len(bejarando)

    return eredmeny

"""feladat 4"""
def szazEsEzerKozottSzamokSzama(bejarando:List[int])->int:
    eredmeny:int=0
    for item in bejarando:
        if(item>=10 and item<=100):
            eredmeny+=1
    return eredmeny

"""feladat 5"""
def csokkeno(bejarando:List[int])->List[int]:
    temp:int=None
    for i in range(0, len(bejarando)-1,1):
        for j in range(0, len(bejarando),1):
            if(bejarando[j]>bejarando[i]):
                temp=bejarando[j]
                bejarando[j]=bejarando[i]
                bejarando[i]=temp
    return bejarando           

"""feldat 1 """
kaloria=kaloriaBevitel()
print(kaloria)

osszege=osszeg(kaloria)
print(f"A termékek össz kalóriája: {osszege}")

"""feldat 2 """
maxÉrték=maximum(kaloria)
print(f"A legtöbb kalóriájja a sorban lévő termékeknek: {maxÉrték}")

"""feladat 3"""
atlag=atlagSzamitas(kaloria, osszege)
print(f"A termékekátlag  kalóriájja: {atlag}")

"""feladat 4"""
szazEsEzerKozott=szazEsEzerKozottSzamokSzama(kaloria)
print(f"100 – 1000 közti kalóriaértéke száma:{szazEsEzerKozott}")

"""feladat 5"""
print("Kalória értékek csökkenő sorrendben:")
print( csokkeno(kaloria), end="\n")