class Jatekos:
    def __init__(self,vezeteknev:str,keresztnev:str,mezszam:int,poszt:str):
        super(). __init__()
        self.vezeteknev:str=vezeteknev
        self.keresztnev:str=keresztnev
        self.mezszam:int=mezszam
        self.poszt:str=poszt
    
    def __str__(self):
        return f"{self.vezeteknev} { self.keresztnev} {self.mezszam} {self.poszt}"