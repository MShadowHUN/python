import time
import os

def nevBekeres()->str:
    nev:str=None

    while(nev==None):
        data:str=input("Kérem a nevét:")
        if(len(data)<3):
            print("Túl rövid a név, min 3 karakter")
            time.slepp(3)
            os.system("cls")
        else:
            nev=data
    return nev

def udvozles(nev:str)->None:
    print(f"Üdvözlöm {nev}.")

felhasznalo:str=nevBekeres
udvozles(felhasznalo)