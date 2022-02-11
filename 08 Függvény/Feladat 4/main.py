import time
import os
import datetime

felhasznaloNev:str=None
szuletesiEv:int=None
kor:int=None

def nevBeolvasasa()-> str:
    eredmeny:str=None

    while (eredmeny==None):
        data:str=input("Kérem adja meg a nevét:")
        if(len(data) > 3):
            eredmeny=data
            return eredmeny
        else:
            print("Túl rövid nevet adott meg!")
            time.sleep(3)
            os.system("cls")

def szuletesiEvBekerese() ->int:
    eredmeny:int=None
    ma:datetime=datetime.datetime.now()     #a mai dátumot adja vissza
    jelenlegiEv:int=int(ma.strftime("%Y")) #visszadja a jelenlegi évet a dátumból #
    while(eredmeny==None):
        data:str=input("Kérem adja meg a születési évét:")
        if(data.isnumeric()):
            eredmeny=int(data)
            if(eredmeny>= jelenlegiEv):
                eredmeny=None
                print("A születési év nem lehet név mint a jelenlegi év!")
                time.sleep(3)
                os.system("cls")
            else:
                return eredmeny

        else:
            print("Nem számot adott meg")
            time.sleep(3)
            os.system("cls")

def eletkorKiszamitasa(ev:int)->int:
    ma:datetime=datetime.datetime.now()    
    jelenlegiEv:int=int(ma.strftime("%Y"))

    return jelenlegiEv - ev

def kiiratas(nev:str, ev:int)-> None:
    print(f"{nev} ön az idén {ev} éves.")

felhasznaloNev=nevBeolvasasa()
szuletesiEv= szuletesiEvBekerese()
kor= eletkorKiszamitasa(szuletesiEv)

kiiratas(felhasznaloNev, kor)
        