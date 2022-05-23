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
        csapatok:Dict[str,List[str]]={
            "Imoco Volley":[],
            "AGIL Volley":[],
            "Linemár Békéscsaba":[],
            "Fatum Nyíregyháza"[],
            "Partizan":[],
            "Crvena Zvezda":[],
            "Telekom Baku":[],
            "Rabita Baku":[],
            "Fenerbahçe Acibadem":[],
            "Asystel Novara":[],
            "Besiktas":[],
        }
        for jatekos in jatekosok:
            if(str(jatekos.csapat)==csapatok[key]):
                csapatok[key]=jatekos.nev

        JatekosIO.write("csapattagok.txt", csapatok)
