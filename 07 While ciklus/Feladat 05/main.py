import os
import time

proba:int=0
hatarErtek:int=None
hozzadando:int=0
data:str=""
osszeg:int=0
hatarErtekInput:str=""

while(hatarErtek==None or hatarErtek<100):
    hatarErtekInput=input("Határérték:")
    if(hatarErtekInput.replace("-", "").isnumeric()):
        hatarErtek=int(hatarErtekInput)
        if(hatarErtek<100):
            print("A számnak minimum 100-nak kell lennie")
    else:
        print("Nem számot adott meg")
        time.sleep(4)
        os.system("cls")

while(osszeg <hatarErtek):
    data=input("Szám:")
    if(data.replace("-", "").isnumeric()):
        hozzadando=int(data)
        osszeg+=hozzadando
        proba+=1
        print(f"{proba}-szor/szer olvasott be számot, összegük {osszeg}")
    else:
        print("Nem számot adott meg")
print(f"A végső szám {osszeg}")