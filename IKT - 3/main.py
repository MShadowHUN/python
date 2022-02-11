import re
import time
import os
from typing import Dict

regex = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
jelszoKinézet= re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
letezik:bool=None

def emailBekérése()->str:
    eredmeny:str=None
    while(eredmeny==None):
        data:str=input("Kérem adja meg az email címét:")
        if re.fullmatch(regex, data):
            print("Az email címe hiteles")
            eredmeny=str(data)
            return eredmeny
        else:
            print("Nem hiteles email címet adott meg")
            time.sleep(3)
            os.system("cls")

def jelszoBekeres()->str:
    eredmeny:str=None
    while(eredmeny==None):
        data:str=input("Kérem adja meg a jelszavát:")
        if re.fullmatch(jelszoKinézet, data):
            print("Az jelszava hiteles")
            eredmeny=str(data)
            return eredmeny
        else:
            print("Nem hiteles jelszót adott meg")
            time.sleep(3)
            os.system("cls")

def isUserExists(email: str, password: str) -> bool:
    users: Dict[str, str] = {
        'hetfo@test.com': 'Testjelszo1',
        'kedd@test.com': 'Testjelszo2',
        'szerda@test.com': 'Testjelszo3',
        'csutortok@test.com': 'Testjelszo4',
        'pentek@test.com': 'Testjelszo5',
        'szombat@test.com': 'Testjelszo6',
        'vasarnap@test.com': 'Testjelszo7'
    }

    isExists: bool = ((email, password) in users.items())
    return isExists

email:str=emailBekérése()
jelszo:str=jelszoBekeres()
letezik= isUserExists(email, jelszo)

if(letezik==True):
    print("Sikeres bejelentkezés a rendszerbe!")
else:
    print("A rendszerhez való hozzáférés megtagadva!")