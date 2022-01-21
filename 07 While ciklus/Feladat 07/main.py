import os
import time

kissebb:int=None
nagyobb:int=None
kdata:str=""
ndata:str=""

while(kissebb==None):
    kdata=input("kérem adja meg az első szám értékét")
    if(kdata.replace("-","").isnumeric):
        kissebb=int(kdata)
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")

while(nagyobb==None or nagyobb<=kissebb):
    ndata=input("kérem adja meg a második szám értékét")
    if(ndata.replace("-","").isnumeric):
        nagyobb=int(ndata)
    else:
        ("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")

for i in range(nagyobb,kissebb,-1):
    print(i, end=" ")
print()