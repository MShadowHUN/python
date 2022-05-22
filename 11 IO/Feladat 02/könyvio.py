from typing import *
from encodings import utf_8
from statistics import mode
from könyv import Konyv
import io
import os

class KonyvIO:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read(fileName:str)->List[Konyv]:
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
        
        konyvek:List[Konyv]=[]
        konyv:Konyv=None
        adatok:List[str]=[]
        veznev:str=None
        kernev:str=None
        szulev:str=None
        cim:str=None
        isbn:int=None
        kiado:str=None
        kiadasiev:int=None
        ar:int=None
        tema:str=None
        oldal:int=None
        honor:int=None

        for line in allLines:
            adatok=line.split('\t')

            veznev=adatok[0]
            kernev=adatok[1]
            szulev=adatok[2]
            cim=adatok[3]
            isbn=adatok[4]
            kiado=adatok[5]
            kiadasiev=adatok[6]
            ar=adatok[7]
            tema=adatok[8]
            oldal=adatok[9]
            honor=adatok[10]

            konyv=Konyv(veznev,kernev, szulev, cim, isbn, kiado, kiadasiev, ar, tema, oldal, honor,) 
            konyvek.append(konyv)   


        return konyvek

    @staticmethod
    def write(fileName:str, konyvek:List[Konyv])->None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open (fileName,encoding='latin-1', mode="w") as file:
                for konyv in konyvek:    
                    file.write(f"{konyv.veznev}\t{konyv.kernev}\t{konyv.szulev}\t{konyv.cim}\t{konyv.isbn}\t{konyv.kiado}\t{konyv.kiadasiev}\t{konyv.ar}Ft\t{konyv.tema}\t{konyv.oldal}\t{konyv.honor}Ft\n")
        except Exception as ex:
            print(f"{ex}")