import os
import time

penz:float=None
honapSzam:int=0
data:str=" "

while(penz==None or penz<100000):
    data=input("Mennyi a megtakarított pénze?")
    if(data.isnumeric):
        penz=float(data)
        if(penz<10000 or penz>50000):
            print("Nem 10.000 és 50.000 között adott meg értéket")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")
    penz= penz*1,02
    honapSzam+=1

print(f"{honapSzam} hónap alatt éri el a 100.000Ft-ot")