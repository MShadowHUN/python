import os
import time

kor:int=-1
data:str=""

while(kor<0 or kor>99):
    data=input("Kérem adja meg a korát: ")
    if(data.replace("-", "").isnumeric()):
        kor=int(data)
    else:
        print("Nem számot adott meg/nem jó a szám értéke")
        time.sleep(3)
        os.system("cls")
        
if(kor >=0 and kor <=6):
    print("Gyerek")
elif(kor >=7 and kor <=18):
    print("Iskolás")
elif(kor >=19 and kor <=65):
    print("Dolgozó")
elif(kor >=65):
    print("Nyugdíjas")