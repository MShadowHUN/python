from tanulok import Tanulo
from typing import *

class Csoport:
    def __init__(self, csoportnev:str, tanulok:List[Tanulo]):
        super(). __init__()
        self.csoportnev:str=csoportnev
        self.tanulok:List[Tanulo]=tanulok
    
    def __str__(self):
        output=f"{self.csoportnev}\n"
        for tanulo in self.tanulok:
            output +=f"\t - {str(tanulo)}\n"

        return output