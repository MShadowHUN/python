from multiprocessing.sharedctypes import Value
from typing import *
from xmlrpc.client import boolean
from jatekos import Jatekos
from jatekosio import JatekosIO

class Csapat:
    @staticmethod
    def utok(jatekosok:List[Jatekos])->None:
        uto:List[Jatekos]=[]
        for jatekos in jatekosok:
            if(jatekos.poszt=="ütő"):
                uto.append(jatekos)
        
        JatekosIO.write("utok.txt", uto)
    
    @staticmethod
    def csapatok(jatekosok:List[Jatekos])->None:
        csapatok:Dict[str,List[str]]={}
        hozzadandoszoveg:str=""
        csapatnev:str=""
        for jatekos in jatekosok:
            csapatnev=jatekos.csapat
            if(csapatnev in csapatok.keys()):
                csapatok[csapatnev].append(jatekos)

        JatekosIO.write("csapattagok.txt", csapatok)

    @staticmethod
    def atlagmagassag(jatekosok:List[Jatekos])->None:
        atlag:float=0
        osszeg:int=0
        atlagfelettiek:List[Jatekos]=[]
        for jatekos in jatekosok:
            osszeg+=int(jatekos.magassag)
        
        atlag=osszeg/len(jatekosok)
        for jatekos in jatekosok:
            if(int(jatekos.magassag) > atlag):
                atlagfelettiek.append(jatekos)
        JatekosIO.write("atlagnalmagasabbak.txt", atlagfelettiek)

    @staticmethod
    def atlagmagassagalatt(jatekosok:List[Jatekos])->None:
        atlag:float=0
        osszeg:int=0
        atlagalattiak:List[Jatekos]=[]
        for jatekos in jatekosok:
            jatekos.magassag+=osszeg
        
        atlag=osszeg/len(jatekosok)
        for jatekos in jatekosok:
            if(jatekos.magassag < atlag):
                atlagalattiak.append(jatekos)
        JatekosIO.writea("atlagnalmagasabbak.txt", atlagalattiak,atlag)
        
    

      