class Jatekos:
    def __init__(self,vezeteknev:str,keresztnev:str,mezszam:int,poszt:str ,pontszam:int):
        super(). __init__()
        self.vezeteknev:str=vezeteknev
        self.keresztnev:str=keresztnev
        self.mezszam:int=mezszam
        self.poszt:str=poszt
        self.pontszam:int=pontszam
    
    def __str__(self):
        return f"{self.vezeteknev} { self.keresztnev} {self.mezszam} {self.poszt} Szerzett pontok:{self.pontszam}"