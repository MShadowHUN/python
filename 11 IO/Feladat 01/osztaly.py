from typing import *
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
        
        DiakIO.write("atlagfelettiek.txt", diakok)