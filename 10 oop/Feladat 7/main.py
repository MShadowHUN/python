from jatekos import Jatekos
from typing import *
import time
import random


def kihuzottSzamok()->Set[int]:
    szet:Set[int]={random.randint(1,99)}
    randomszam:int=None
    while(len(szet)<5):
        randomszam=random.randint(1,99)
        szet.add(randomszam)

    return szet

kihuzottszamok:Set[int]=kihuzottSzamok()
print(kihuzottszamok)
time.sleep(1)
tippek:Set[int]=kihuzottSzamok()
print(tippek)
jatekos:Jatekos=Jatekos("Kolosszális Koppány", tippek)
print(jatekos)

talalatok:Set[int]=jatekos.talalatokSzama(kihuzottszamok)
if(len(talalatok)==0):
    print("Sajnos egy számot sem talált el")
else:
    print(f"Az eltalált számok: {talalatok}")