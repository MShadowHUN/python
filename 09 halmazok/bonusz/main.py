from typing import *
import time
import os
import webbrowser

nevek:List[str]=[]
szabadnapok:List[int]=[]

def hiba(szoveg:str):
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def nevbekeres()->str:
    eredmeny:str=None
    while(eredmeny==None or eredmeny.isspace() or len(eredmeny)<3 ):
        eredmeny=input("Kérem adja meg a nevét:")
        if(eredmeny.isspace()):
            hiba("Kérem ne csak SPACE karakterből álljon a név.")
        elif(len(eredmeny)<3):
            hiba("Kérem legalább 3 karakterből álljon a név")
    return eredmeny

def szabadnapBekeres(nev:str)->int:
    eredmeny:int=None
    while(eredmeny==None or eredmeny<0 or eredmeny>365):
        data:str=input(f"Kérem adha meg {nev} szabadnapjainak számát")
        if(data.replace("-", "").isnumeric()):
            eredmeny=int(data)
            if(eredmeny<0):
                hiba("Nem lehet negatív")
            elif(eredmeny>365):
                hiba("Keress munkát")
        else:
            hiba("Nem számot adott meg")
    return eredmeny

def nevFeltoltes(lista:List[str]):
    eredmeny:str=""
    for i in range(0,10,1):
        eredmeny=nevbekeres()
        lista.append(eredmeny)

def szabadnapokFeltoltese(lista:List[int], nev:List[str]):
    eredmeny:int=None
    for i in range(0,10,1):
        eredmeny=szabadnapBekeres(nev[i])
        lista.append(eredmeny)

def kiiras(nev:List[str], szabadnap:List[int]):
    szam:int=None
    neve:str=""
    for i in range(0,10,1):
        szam=szabadnap[i]
        neve=nev[i]
        print(f"{neve}-nek {szam} db szabadnapja van")
        time.sleep(0.5)

def csokkenosorrend(nev:List[str], szabadnap:List[int]):
    nevtemp:str=""
    szamtemp:int=None
    for i in range(0, len(nev)-1,1):
        for j in range(i+1, len(nev),1):
            if(szabadnap[i]<szabadnap[j]):
                szamtemp=szabadnap[i]
                szabadnap[i]=szabadnap[j]
                szabadnap[j]=szamtemp
                nevtemp=nev[i]
                nev[i]=nev[j]
                nev[j]=nevtemp

nevFeltoltes(nevek)
szabadnapokFeltoltese(szabadnapok, nevek)
print("Az eredeti beolvasás szerint:")
kiiras(nevek, szabadnapok)
csokkenosorrend(nevek, szabadnapok)
print("\nA szabadnapok szerint csökkenő sorrendbe rendezve:")
kiiras(nevek,szabadnapok)























time.sleep(5)
webbrowser.open("https://www.youtube.com/watch?v=lpiB2wMc49g")