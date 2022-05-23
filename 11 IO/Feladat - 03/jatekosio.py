from typing import *
from encodings import utf_8
from statistics import mode
from jatekos import Jatekos
import io
import os

class JatekosIO:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read(fileName:str)->List[Jatekos]:
        oneLine:str=None
        allLines:List[str]=[]
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path,encoding='latin-1', mode="r") as file:
                for line in file:
                    oneLine=line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
        
        jatekosok:List[Jatekos]=[]
        jatekos:Jatekos=None
        adatok:List[str]=[]

        for line in allLines:
            adatok=line.split('\t')
        
            nev=adatok[0]
            magassag=adatok[1]
            poszt=adatok[2]
            nemzetiseg=adatok[3]
            csapat=adatok[4]
            orszag=adatok[5]

            jatekos=Jatekos(nev,magassag,poszt,nemzetiseg,csapat,orszag)
            jatekosok.append(jatekos)
        return jatekosok
    
    @staticmethod
    def write(fileName:str, jatekosok:List[Jatekos])->None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open (fileName,encoding='latin-1', mode="w") as file:
                for jatekos in jatekosok:    
                    file.write(f"{jatekos.nev}\t{jatekos.magassag}\t{jatekos.poszt}\t{jatekos.nemzetiseg}\t{jatekos.csapat}\t{jatekos.orszag}\n")
        except Exception as ex:
            print(f"{ex}")