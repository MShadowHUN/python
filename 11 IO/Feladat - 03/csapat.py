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
            osszeg+=int(jatekos.magassag)
        
        atlag=osszeg/len(jatekosok)
        for jatekos in jatekosok:
            if(int(jatekos.magassag) < atlag):
                atlagalattiak.append(jatekos)
        JatekosIO.writea("atlagnalmagasabbak.txt", atlagalattiak,atlag)

    @staticmethod
    def magassagnov(jatekosok:List[Jatekos])->None:
        temp:int=None

        for i in range(0, len(jatekosok)-1,1):
            for j in range(i+1,len(jatekosok),1):
                if(jatekosok[j].magassag>jatekosok[i].magassag):
                    temp=jatekosok[i].magassag
                    jatekosok[i].magassag=jatekosok[j].magassag
                    jatekosok[j].magassag=temp
        JatekosIO.write("magaslatok.txt", jatekosok)


    @staticmethod
    def nemzetisegek(jatekosok:List[Jatekos])->None:
        nemzetiseg:Dict[str,int]={}
        hozzadandoszoveg:str=""
        nemzetisegnev:str=""
        for jatekos in jatekosok:
            nemzetisegnev=jatekos.nemzetiseg
            if(nemzetisegnev in nemzetiseg.keys()):
                nemzetiseg[nemzetisegnev]+=1
        JatekosIO.write("nemzetiseg.txt", nemzetiseg)

    @staticmethod
    def posztok(jatekosok:List[Jatekos])->None:
        posztok:Dict[str,int]={}
        hozzadandoszoveg:str=""
        poszt:str=""
        for jatekos in jatekosok:
            poszt=jatekos.poszt
            if(poszt in posztok.keys()):
                posztok[poszt]+=int(jatekos.magassag)
        JatekosIO.write("posztok.txt", posztok)
      