from multiprocessing.sharedctypes import Value
from typing import *
from xmlrpc.client import boolean
from diak import Diak
from diakio import DiakIO

class Osztaly:
    @staticmethod
    def atlag(diakok:List[Diak])->float:
        osszeg:float=0
        atlag:float=0

        for diak in diakok:
            osszeg +=diak.atlag

        atlag=osszeg/len(diakok)


        return atlag
    @staticmethod
    def legjobbak(diakok:List[Diak])->List[Diak]:
        joDiakok:List[Diak]=[diakok[0]]

        for i in range(1,len(diakok),1):
            if(diakok[i].atlag == joDiakok[0].atlag):
                joDiakok.append(diakok[i])
                joDiakok[0]=diakok[i]
            elif(diakok[i].atlag > joDiakok[0].atlag):
                joDiakok.clear()
                joDiakok.append(diakok[i])

        return joDiakok

    @staticmethod
    def atlagfelett(diakok:List[Diak],atlag:float)->None:
        atlagFelettiek:List[Diak]=[]
        for diak in diakok:
            if(diak.atlag > atlag):
                atlagFelettiek.append(diak)
        
        DiakIO.write("atlagfelettiek.txt", atlagFelettiek)

    @staticmethod
    def vanEkitunoTanulo(diakok:List[Diak])->boolean:
        vanE:boolean=False

        for diak in diakok:
            if(diak.atlag==5.00):
                vanE=True
                break
        return vanE
    

    @staticmethod
    def jegyek(diakok:List[Diak])->Dict[str, int]:
        eredmeny:Dict[str,int]={
            "elégtelen":0,
            "elégséges":0,
            "közepes":0,
            "jó":0,
            "kitűnő":0
        }
        
        for diak in diakok:
            if(diak.atlag < 2):
                eredmeny["elégtelen"]+=1
            elif(diak.atlag < 3):
                eredmeny["elégséges"]+=1
            elif(diak.atlag < 4):
                eredmeny["közepes"]+=1
            elif(diak.atlag < 5):
                eredmeny["jó"]+=1
            else:
                eredmeny["kitűnő"]+=1
        return eredmeny
    
    
    @staticmethod
    def masikjegyek(diakok:List[Diak])->Dict[str, int]:
        eredmeny:Dict[str,int]={}
        alsoHatarertek:int=0
        hatarertekek:Dict[str, int]={
        "elégtelen":2,
        "elégséges":3,
        "közepes":4,
        "jó":5,
        "kitűnő":6,
        }

        for (key, value) in hatarertekek.items():
            darab:int=0

            for diak in diakok:
                if(diak.atlag >= alsoHatarertek and diak.atlag < value):
                    darab+=1
            eredmeny[key]=darab    
            alsoHatarertek= value        
    
        return eredmeny
    