from multiprocessing.sharedctypes import Value
from typing import *
from xmlrpc.client import boolean
from könyv import Konyv
from könyvio import KonyvIO

class Konyvtar:
    @staticmethod
    def informatika(konyvek:List[Konyv])->None:
        info:List[Konyv]=[]
        for konyv in konyvek:
            if(konyv.tema=="informatika"):
                info.append(konyv)
        
        KonyvIO.write("informatika.txt", info)

    @staticmethod
    def huszadikszazad(konyvek:List[Konyv])->None:
        ezerkilenc:List[Konyv]=[]
        for konyv in konyvek:
            if(int(konyv.kiadasiev)>=1900 and int(konyv.kiadasiev)<2000):
                ezerkilenc.append(konyv)
        
        KonyvIO.write("1900.txt", ezerkilenc)