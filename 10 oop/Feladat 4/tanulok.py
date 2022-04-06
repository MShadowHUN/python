class Tanulo:
    def __init__(self,vezeteknev:str,keresztnev:str,szuletesiDatum:str):
        super(). __init__()
        self.vezeteknev:str=vezeteknev
        self.keresztnev:str=keresztnev
        self.szuletesiDatum:str=szuletesiDatum
    
    def __str__(self):
        return f"Név:{self.vezeteknev} {self.keresztnev} Született:{self.szuletesiDatum}\n"