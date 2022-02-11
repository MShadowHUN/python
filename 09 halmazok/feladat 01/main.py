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


elemekSzama=elemSzamBekerese()