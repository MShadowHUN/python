import random
import os
import time

start:int=None #kitalálandó szám kezdőértéke
end:int=None #kitalálandó szám végértéke
titkos:int=None #kitalálandó szám

def hiba(uzenet:str)->None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")

def szamBeolvasasa(kezdoErtek:int, vegertek:int,)->int:
    eredmeny:int=None

    while(eredmeny==None):
        data=input(f"Kérem adjon meg egy egész számot [{kezdoErtek} - {vegertek}]:")
        if(data.isdigit() and int(data)>=kezdoErtek and int(data) <=vegertek):
            eredmeny=data
        elif(data.isdigit()and (int(data)<kezdoErtek or int(data)>vegertek)):
            hiba("A megadott szám nincs a határértékek között ")

        else:
            hiba("Nem pozitív")

def kitalalandoSzam(kezdoErtek:int, vegertek:int)->int:
    return random.randint(kezdoErtek,vegertek)

def tipBeolvasasa()->int:
    eredmeny:int=None

    while(eredmeny==None):
        data=input(f"Kérem tippet:")
        if(data.isdigit()):
            eredmeny=int(data)
        else:
            hiba("Nem számot adott meg") 

def sikeresTipp(probalkozasokSzama:int, szam:int)->None:
    print(f"Próbálkozások száma:{probalkozasokSzama}.")
    print(f"A kitalálandó szám:{szam}.")

def sikertelenTipp(tipp:int, szam:int)->None:
   if(tipp>szam):
        print("A kitalálandó szam kisebb")
   else:
        print("A kitalálandó szam nagyobb")

def jatek(tipp:int)->None:
    probalkozasokSzama:int=0
    ertek:int=0

    while(ertek!=tipp):
        tipBeolvasasa
        probalkozasokSzama+=1


start=szamBeolvasasa(0,9)
end=szamBeolvasasa(40,50)
titkos=kitalalandoSzam(start, end+1)

jatek(titkos)