import os
import time

eu:float=None
atvaltasMertekegysege:str=None
atvaltottMennyiseg:float=None

def hiba(szoveg:str)-> None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def euroBekerese()->float:
    eredmeny:float=None

    while(eredmeny==None):
        data:str=input("Kérem adja meg a pénzét euróban:")
        if(data.replace(".", "").isdigit()):
            eredmeny=float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemenő adat")

def valtasValasztas ()->str:
    eredmeny:str=None

    while(eredmeny==None):
        data:str=input("Kérem a váltás módját [JPY vagy USD vagy CHF]:")
        if(data.upper()== "JPY"or data.upper()=="USD" or data.upper()=="CHF"):
            eredmeny=data.capitalize()
            return eredmeny
        else:
            hiba("Ilyen opció nincs!")

def atvaltas(euro:float, mire:str)->float:
    if(mire=="JPY"):
        return euro * 0.75
    elif(mire=="USD"):
        return euro*0.8
    elif(mire=="CHF"):
        return euro*0.55

def kiiras (euro:float, atvaltottPenz:float, mertekegyseg:str)-> None:
    print(f"{euro}Euro= {atvaltottPenz} {mertekegyseg}.")

eu= euroBekerese()
atvaltasMertekegysege= valtasValasztas()
atvaltottMennyiseg=atvaltas(eu, atvaltasMertekegysege)
kiiras(eu, atvaltottMennyiseg, atvaltasMertekegysege)