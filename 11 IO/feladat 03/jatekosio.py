from asyncore import write
from fileinput import filename
from importlib.resources import path
from multiprocessing.sharedctypes import Value
from statistics import mode
from jatekos import Jatekos
from typing import *
import io
import os

class JatekosIO:
    def __init__(self) -> None:
        super().__init__()
        
    @staticmethod
    def read(fileName: str) -> List[Jatekos]:
        oneLine:str = None
        allLines:List[str]=[]
        
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path,encoding='latin-1', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")

        jatekosok: List[Jatekos] = []
        jatekos: Jatekos = None

        adatok: List[str] = []

        nev: str = None
        magas: int = None
        poszt: str = None
        nemzetiseg: str = None
        csapat: str = None
        orszag: str = None

        for line in allLines:
            adatok = line.split('\t')

            nev = adatok[0]
            magas = adatok[1]
            poszt = adatok[2]
            nemzetiseg = adatok[3]
            csapat = adatok[4]
            orszag = adatok[5]

            jatekos = Jatekos(nev,magas,poszt,nemzetiseg,csapat,orszag)
            jatekosok.append(jatekos)

        return jatekosok

    @staticmethod
    def write(fileName:str,jatekosok:List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path,encoding='latin-1', mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.nev}, {jatekos.magas}, {jatekos.poszt}, {jatekos.nemzetiseg}, {jatekos.orszag}, {jatekos.orszag}")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")


    @staticmethod
    def csapattagokIras(fileName:str,csapattagok:Dict[str,List[str]]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path,encoding='latin-1', mode="w") as file:
                for (key,value) in csapattagok.items():
                    file.write(f"{key}\n")
                    for nev in value:
                      file.write(f"\t-{nev}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")

    @staticmethod
    def magassagKiiras(fileName:str,jatekosok:List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path,encoding='latin-1', mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.nev}, {jatekos.magas}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
            
    @staticmethod
    def nemzetisegKiiras(fileName:str,nemzetisegek:Dict[str,int]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)
            with open(path,encoding='latin-1', mode="w") as file:
                for key,value in nemzetisegek.items():
                    file.writelines(f"{key} - {value}\n")
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
            
    @staticmethod
    def atlagnalMagasabbakKiirasa(fileName:str,atlagnalMagasabb:List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str =os.path.join(here, fileName)
            with open(path,encoding="latin-1",mode="w") as file:
                for jatekos in atlagnalMagasabb:
                    file.write(f"{jatekos.nev} - {jatekos.magas}\n")
        except FileNotFoundError as ex:
            print(f"{ex.fileName} nem található")

    @staticmethod
    def atlagnalAlacsonyabbakKiirasa(fileName:str,atlagnalAlacsonyabb:Dict[Jatekos,float]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str =os.path.join(here, fileName)
            with open(path,encoding="latin-1",mode="w") as file:
                for (key,value) in atlagnalAlacsonyabb.items():
                    file.write(f"{key.nev}, {key.magas} - Az átlagtól {value:1.2f}-al alacsonyabb\n")
        except FileNotFoundError as ex:
            print(f"{ex.fileName} nem található")