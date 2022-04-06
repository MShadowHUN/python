from tanulok import Tanulo

class Csoport:
    def __init__(self, csoportnev:str, tanulok:List[Tanulo]):
        super() __init__()
        self.csoportnev:str=csoportnev
        self.tanulok:List[Tanulo]=tanulok
    
    def __str__(self):
        return f"{self.csoportnev}\n{self.tanulok}"