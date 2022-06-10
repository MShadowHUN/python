from audioop import add
from sqlite3 import DatabaseError
from jatekos import Jatekos
from jatekosio import JatekosIO
from typing import *


class Csapat:

    @staticmethod
    def kiiras(jatekosok:List[Jatekos]) -> None:
        print("A játékosok:")
        for jatekos in jatekosok:
            print(f"\n- {jatekos}")
        print(f"\n")

    @staticmethod
    def posztKereses (poszt:str,jatekosok:List[Jatekos]) -> None:
        adottPoszt: List[Jatekos] = []
        for jatekos in jatekosok:
            if(jatekos.poszt == poszt):
                adottPoszt.append(jatekos)

        JatekosIO.write("utok.txt",adottPoszt)

    @staticmethod
    def csapatJatekosa (jatekosok:List[Jatekos]) -> None:
        
        #kikeressük a kulcsokat
        csapatok:set[str] = set()
        for jatekos in jatekosok:
            csapatok.add(jatekos.csapat)
        
        csapattagok: Dict[str,List[str]] = {}

        #minden kulcshoz a szótárban csinálnuk egy üres listát
        #mivel memóriát kell a listának lefoglalni
        #enek célje, h a következő ciklusban az új elemet
        #a játékost listába tudjuk tenni
        for csapat in csapatok:
            csapattagok[csapat] = []

        #játékos kikeresése ami az éppen soronlévő csapathoz tartozik 
        #majd hozzáadása
        for csapat in csapatok:
            for jatekos in jatekosok:
                if(csapat == jatekos.csapat):                  
                    csapattagok[csapat].append(jatekos.nev)

        JatekosIO.csapattagokIras("csapattagok.txt",csapattagok)

    @staticmethod
    def magassagSorrend (jatekosok:List[Jatekos]) -> None:
        data:Jatekos = None

        for i in range(0, len(jatekosok),1):
            for j in range(i+1, len(jatekosok),1):
                if(jatekosok[i].magas > jatekosok[j].magas):
                    data = jatekosok[i]
                    jatekosok[i] = jatekosok[j]
                    jatekosok[j] = data
        
        JatekosIO.magassagKiiras("magaslatok.txt",jatekosok)
        
    @staticmethod
    def nemzetisegek(jatekosok:List[Jatekos]) -> None:
        nemzetiseg:set[str] = set()
        for jatekos in jatekosok:
            nemzetiseg.add(jatekos.nemzetiseg)
            
        nemzetisegek: Dict[str,int] = {}
        
        for nemzetiseg in nemzetiseg:
            nemzetisegek[nemzetiseg] = 0
        
        data:int = 0
        
        for nemzetiseg in nemzetisegek:
            for jatekos in jatekosok:
                if(jatekos.nemzetiseg == nemzetiseg):
                    data += 1
                nemzetisegek[nemzetiseg] = (data)     
                                   
                
                     
        JatekosIO.nemzetisegKiiras("nemzetisegek.txt",nemzetisegek)

    @staticmethod
    def atlagMagassagKiszamitas(jatekosok:list[Jatekos]) -> float:
        atlagMagassag: int = 0
        
        for jatekos in jatekosok:
            atlagMagassag += int(jatekos.magas)
        
        atlagMagassag:float = atlagMagassag / len(jatekosok)
        return atlagMagassag

    @staticmethod
    def atlagnalMagasabb(jatekosok:List[Jatekos]) -> None:
        atlagMagassag = Csapat.atlagMagassagKiszamitas(jatekosok)
        atlagnalMagasabb:List[Jatekos] = []

        for jatekos in jatekosok:
            if(float(jatekos.magas) > atlagMagassag):
                atlagnalMagasabb.append(jatekos)
        
        JatekosIO.atlagnalMagasabbakKiirasa("magaslatok.txt", atlagnalMagasabb)
        
    @staticmethod
    def posztokOsszMagassag(jatekosok:List[Jatekos]) -> None:
        posztokMagassag:Dict[str,int] = {}
        posztok:set[str] = set()
        
        for jatekos in jatekosok:
            posztok.add(jatekos.poszt)
            
        for poszt in posztok:
            posztokMagassag[poszt] = 0
        
        for poszt in posztok:
            for jatekos in jatekosok:
                if(poszt == jatekos.poszt):
                    posztokMagassag[poszt] = posztokMagassag[poszt] + int(jatekos.magas)

        for (key,value) in posztokMagassag.items():
            print(f"{key} - {value}\n")
            
            
            
    @staticmethod
    def alacsonyak(jatekosok:List[Jatekos]) -> None:
        atlagmagassag = Csapat.atlagMagassagKiszamitas(jatekosok)
        
        atlagnalAlacsonyabb:Dict[Jatekos,float] = {}
        alacsonyabb: List[Jatekos] = []

        for jatekos in jatekosok:
            if(float(jatekos.magas) < atlagmagassag):
                alacsonyabb.append(jatekos)
            
        for jatekos in alacsonyabb:
            atlagnalAlacsonyabb[jatekos] = atlagmagassag - float(jatekos.magas)
        
        JatekosIO.atlagnalAlacsonyabbakKiirasa("alacsonyak.txt", atlagnalAlacsonyabb)