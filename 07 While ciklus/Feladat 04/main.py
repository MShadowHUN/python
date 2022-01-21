import os
import time

osszeg:int=0
proba:int=0
hozzadando:int=None
data:str=""

while(osszeg<100):
    data=input("Kérem adjon meg egy számot.")
    if(data.isnumeric()):
        hozzadando=int(data)
        osszeg=osszeg+hozzadando
        print(osszeg)
        proba+=1
        print(proba)
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system('cls')
print(osszeg)