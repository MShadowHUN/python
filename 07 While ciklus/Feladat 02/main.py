#név nem lehet üres string
#szóközök(1 vagy több)
#név hossza (min: 3)

import os
import time

nev:str=""
nevHossza: int = 0

while(nev=="" or nev.isspace() or nevHossza<3):
    nev:str=str(input("Kérem a nevét:"))
    nevHossza = len(nev)

    if(nev==""):
        print("Nem adott meg egyetlen karaktert sem")
        time.sleep(3)
        os.system("cls")
    elif(nev.isspace()):
        print("Csak szóközt adott meg")
        time.sleep(3)
        os.system("cls")
    elif(nevHossza<3):
        print("Név nem elég hosszú")
        time.sleep(3)
        os.system("cls")
print(f"Üdvözlöm {nev}")
