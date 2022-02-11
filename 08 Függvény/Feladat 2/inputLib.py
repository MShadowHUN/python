import time
import os


def tizedesSzamBeolvasas() ->float:
    data=input(f"Kérem adjon meg egy számot")
    if(data.replace("-","").replace(".","").isnumeric()):
        return float(data)
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system('cls')

def egeszSzamBeolvasas() ->int:
    data=input(f"Kérem adjon meg egy számot")
    if(data.replace("-","").isnumeric()):
        return int(data)
    else:
        print("Nem számot adott meg")
        time.sleep(3)
        os.system('cls')