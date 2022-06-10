
from sqlite3 import adapters
from pilota import Pilota
import os
import time
from typing import *

class PilotaIO:
    
    @staticmethod
    def read (fileName:str) -> List[Pilota]:
        oneLine: str = None
        allLines:List[str] = []
        try:
            here:str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here,fileName)
            with open(path, encoding="utf-8",mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található")
        
        pilota:Pilota = None
        pilotak:List[Pilota] = []

        nev:str = None
        szuletesiDatum:str = None
        nemzetiseg:str = None
        rajtszam:int = None



        for line in allLines:
            adat = line.split(";")
            
            if(adat.__contains__("születési_dátum")):
                pass
            else:
                nev = adat[0]
                szuletesiDatum = adat[1]
                nemzetiseg = adat[2]
                rajtszam = adat[3]


                pilota = Pilota(nev,szuletesiDatum,nemzetiseg,rajtszam)
                pilotak.append(pilota)

        return pilotak

    @staticmethod
    def kiiras (pilotak:List[Pilota]) -> None:
        for pilota in pilotak:
            print(f"{pilota}\n")
    
    @staticmethod
    def sorokSzamaKiiras (sorokSzama:int) -> None:
        print(f"3. feladat: {sorokSzama}")

    @staticmethod
    def utolsoPilotaKiiras (utolsoPilota:Pilota) -> None:
        print(f"4. feladat: {utolsoPilota.nev}")

    @staticmethod
    def tizenkilencedikSzazadbanSzuletettPilotakKiirasa (tizenkilencedikSzazadbanSzuletettPilotak:List[Pilota]) -> None:
        print(f"5.feladat:")
        for pilota in tizenkilencedikSzazadbanSzuletettPilotak:
            print(f"\t{pilota.nev} ({pilota.szuletesiDatum})\n") 
    
    @staticmethod
    def legkissebbRajtszamuPilotaKiiras(legkissebbRajtszamu:Pilota) -> None:
        print(f"6.feladat: {legkissebbRajtszamu}")
    
    @staticmethod
    def tobbszoriRajtszamokKiiras(TobbszorEloforduloRajtszamok:List[int]) -> None:
        print(f"7.feladat:")
        for szamok in TobbszorEloforduloRajtszamok:
            print(f"{szamok}")