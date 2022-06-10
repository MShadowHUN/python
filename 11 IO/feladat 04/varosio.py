
from multiprocessing.sharedctypes import Value
from varos import Varos
from typing import *
import io
import os

class Varosio:
    @staticmethod
    def read(fileName:str) -> None:
        oneLine:str=None
        allLines:List[str]=[]
        try:
            here:str = os.path.dirname(os.path.abspath(__file__))
            path:str = os.path.join(here,fileName)
            with open (path, mode="r", encoding="latin-1") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print (f"{ex.filename} nem található")
        
        varos:Varos = None
        varosok:List[Varos] = []

        nev:str = None
        tipus:str = None
        jaras: str = None
        megyeNeve:str = None
        kisterseg: str= None
        nepesseg: int = None
        terulet: float = None


        for line in allLines:
            adatok = line.split("\t")

            nev = adatok[0]
            tipus = adatok[1]
            jaras=adatok[2]
            megyeNeve = adatok[3]
            kisterseg=adatok[4]
            nepesseg=int(adatok[5])
            terulet=float(adatok[6])

            varos = Varos(nev,tipus,jaras,megyeNeve,kisterseg,nepesseg,terulet)
            varosok.append(varos)
        
        return varosok

    def kiiras(varosok:List[Varos]) -> None:
        for varos in varosok:
            print(f"-{varos}\n")

    @staticmethod
    def megyeiJoguVarosokKiirasa (fileName:str,varosok:List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path, encoding="utf-8", mode="w")as file:
                for varos in varosok:
                    file.write(f"- {varos.nev}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található")

    @staticmethod
    def nepessegKiirasa (fileName:str,varosok:List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path, encoding="utf-8", mode="w")as file:
                for key,value in varosok.items():
                    file.write(f"- {key}, {value}fő \n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található")
            
    @staticmethod
    def nagyTeruletuTelepulesKiiras (fileName:str,varosok:List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path, encoding="utf-8", mode="w")as file:
                for varos in varosok:
                    file.write(f"- {varos.nev}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található")
            
    @staticmethod
    def bekesmegyeKiiras (fileName:str,bekesmegyeitelepulesek:List[str]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path, encoding="utf-8", mode="w")as file:
                for telepules in bekesmegyeitelepulesek:
                    file.write(f"- {telepules}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található")       
        
    @staticmethod
    def megyeteruletKiiras (fileName:str,megyekEsTeruleteik:Dict[str,int]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path, encoding="utf-8", mode="w")as file:
                for key,value in megyekEsTeruleteik.items():
                    file.write(f"- {key}, {value}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található")       
