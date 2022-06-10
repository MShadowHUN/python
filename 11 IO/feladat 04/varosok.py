from varos import Varos
from varosio import Varosio
from typing import *

class Varosok: 
    
    @staticmethod
    def megyeiJoguVarosok(varosok:List[Varos]) -> None:
        megyeiJoguVarosok:List[Varos] = []
        for varos in varosok:
            if(varos.tipus == "megyeszékhely megyei jogú város"):
                megyeiJoguVarosok.append(varos)
            
        Varosio.megyeiJoguVarosokKiirasa("megyejoguvarosok.txt",megyeiJoguVarosok)
        
    @staticmethod
    def nepesseg(varosok:List[Varos]) -> None:
        varosokNepessege:Dict[str,int] = {}

        
        for varos in varosok:
            if(varos.nepesseg > 50000 and varos.nepesseg < 100000):
                varosokNepessege[varos.nev] = (varos.nepesseg)
                
        Varosio.nepessegKiirasa("nepesseg.txt",varosokNepessege)
        
    @staticmethod
    def nagyTeruletuTelepules(varosok:List[Varos]) -> None:
        nagyteruletu:List[Varos] = []
        
        for varos in varosok:
            if(varos.terulet > 200):
                nagyteruletu.append(varos)
            
        Varosio.nagyTeruletuTelepulesKiiras("nagyteruletek.txt",nagyteruletu)
        
    @staticmethod
    def bekesmegye (varosok:List[Varos]) -> None:
        bekesmegyeitelepulesek: List[str] = []
        for varos in varosok:
            if(varos.megyeNeve == "Békés"):
                bekesmegyeitelepulesek.append(varos.nev)
            
        Varosio.bekesmegyeKiiras("bekes.txt",bekesmegyeitelepulesek)        
                
    @staticmethod
    def megyeteruletekkiszamitasa (varosok:List[Varos]) -> None:
        megyekEsTeruleteik:Dict[str,float] = {}
        megyek: set[str] = set()
        for varos in varosok:
            megyek.add(varos.megyeNeve)
            
        for megye in megyek:
            megyekEsTeruleteik[megye] = 0    
            
        for megye in megyek:
            for varos in varosok:
                if (varos.megyeNeve == megye):
                    megyekEsTeruleteik[megye] += varos.terulet
        
        Varosio.megyeteruletKiiras("megyeterületek.txt", megyekEsTeruleteik)