import time
import os
import random

penz:float=0
visszaJaro:float=0

while(penz<300):
    erme:int=random.randint(0,200)
    penz+=erme
    print(f"Eddig {penz} Ft-ot dobott be.")

udito:int=None
uditoData:str=""
while(udito==None or udito <1 or udito>5):
    uditoData=input("Nyomja meg a menü előtti számot a kívánt üdítőért: \n1- Ice tea, \n2 – Limunáde, \n3 – Epres Jégkása, \n4 – Almalé, \n5 – Szénsavmentes víz: ")
    if(uditoData.isnumeric):
        udito=int(uditoData)
        if(udito==1):
            print("Ön Ice teat választotta. Egészségere!")
        elif(udito==2):
            print("Ön Limunádé választotta. Egészségere!")
        elif(udito==3):
            print("Ön Epres Jégkását választotta. Egészségere!")
        elif(udito==4):
            print("Ön Almalét választotta. Egészségere!")
        elif(udito==5):
            print("Ön Szénsavmentes vizet választotta. Egészségere!")
        else:
            print("Ön nem 1 és 5 között adott meg számot")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system("cls")

visszaJaro=penz-300
print(f"Önnek jár visszajárandó {visszaJaro} HUF! Kérem, vegye el a visszajárót")
