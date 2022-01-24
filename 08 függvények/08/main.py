import time
import os

pont:int=None
jegy:int=None

def hiba(szoveg:str)->None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def pontBekeres()-> int:
    eredmeny:int=None

    while(eredmeny==None):
        data=input("Kérem adja meg a pontszámát:")
        if(data.isdigit):
            if(int(data)>=0 or int(data)<=100):
                eredmeny=int(data)
                return eredmeny
            else:
                hiba("A szám nem 0 és 100 között van")
        else:
            hiba("Nem számot adott meg")

def vizsgalat(pontszam:int)->int:
    if(pontszam <50):
        return 1
    elif(pontszam >=50 and pontszam <60):
        return 2
    elif(pontszam >=60 and pontszam <70):
        return 3
    elif(pontszam >=70 and pontszam <85):
        return 4
    else:
        return 5

def kiiras(pontszam:int, erdemjegy:int)->None:
    print(f"Ön {pontszam} pontot ért el ezért az érdejegye: {erdemjegy}")

pont:int=pontBekeres()
jegy=vizsgalat(pont)
kiiras(pont, jegy)

