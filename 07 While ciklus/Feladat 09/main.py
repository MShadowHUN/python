import time
import os

szam:int=None
data:str=""

while(szam==None or szam<99 or szam>999):
    data=input("Kérem adjon meg egy 3 jegyű pozitív számot")
    if(data.isnumeric):
        szam=int(data)
        if(szam<99 or szam>999):
            print("Nem 3 jegyű számot adott meg")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")

if(szam%7==0):
    print(f"A {szam} osztható 7-tel")
else:
    print(f"A {szam} nem oszhtató 7-tel")