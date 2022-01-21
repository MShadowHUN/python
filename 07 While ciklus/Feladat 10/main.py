import os
import time

n:int=None
data:str=""
szamokszam:int=0
osszeg:int=0

while(n==None or n<0 or n>99):
    data=input("Kérem a számot")
    if(data.isnumeric):
        n=int(data)
        if(n<0 or n>99):
            print("A szám nincs 0 és 99 között")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")
for i in range(0,n+1,1):
    if(i%2==0):
        print(i, end=" ")
    if(i%5==0):
        osszeg+=i
    if(i%11==0):
        szamokszam+=1

print(f"\nAz 5-tel osztható számok összege:{osszeg}")
print(f"A 11-gyel osztható számok száma:{szamokszam}")

for j in range(0,n+1,1):
    if(j%7==3):
        print(j, end=" ")