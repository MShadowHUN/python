from typing import *

class Jatekos:
    def __init__(self, nev:str, tippek:Set[int]):
        super(). __init__()
        self.nev:str=nev
        self.tippek:Set[int]=tippek
    
    def __str__(self)->str:
        return f"{self.nev}\ttippjei:{self.tippek}"

    def talalatokSzama(self, kihuzottSzamok:Set[int])->int:
        return self.tippek.intersection(kihuzottSzamok)