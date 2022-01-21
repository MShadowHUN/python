import os
import time
import random

kissebb:int=None
nagyobb:int=None
kdata:str=""
ndata:str=""
osszeg:int=0
szamokszama:int=0
atlag:int=0
szam4:int=0
ktav:int=0
ntav:int=0

while(kissebb==None or kissebb%2!=0):
    kdata=input("kérem adja meg az első szám értékét")
    if(kdata.replace("-","").isnumeric):
        kissebb=int(kdata)
        if(kissebb%2!=0):
            print("Nem páros számot adott meg")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")

while(nagyobb==None or nagyobb<=kissebb or nagyobb%2==0):
    ndata=input("kérem adja meg a második szám értékét")
    if(ndata.replace("-","").isnumeric):
        nagyobb=int(ndata)
        if(nagyobb%2==0):
            print("Nem páratlan számot adott meg")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")
szam:int=random.randint(kissebb,nagyobb)
tav:int

for i in range(kissebb, nagyobb+1, 1):
    osszeg+=i
    szamokszama+=1
    if(i%4==0):
    szam4+=1
atlag=osszeg/szamokszama
     
for j in range(kissebb,szam+1,1 ):
    ktav+=1

for k in range(szam, nagyobb+1,1):
    ntav+=1

if(ktav>ntav):
    print("Kissebb van messzebb")
elif(ktav<ntav):
    print("Nagyobb van messzebb")
else:
    print("Egyenlő távolságra vannak")
       
print(f"A két szám közti átlag {atlag}")
print(f"4-gyel osztható számok száma: {szam4}")