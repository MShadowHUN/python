from tulajdonos import Tulajdonos

class Motorkerekpar:
    def __init__(self, gyarto:str, tipus:str, kivitel:str, teljesitmeny:int, hengerurtartalom:int, suly:int, tulajdonos:Tulajdonos):
        super(). __init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kivitel:str=kivitel
        self.teljesitmeny:int=teljesitmeny
        self.hengerurtartalom:int=hengerurtartalom
        self.suly:int=suly
        self.tulajdonos:Tulajdonos=tulajdonos

    def __str__(self):
        return f"{self.gyarto} {self.tipus} {self.kivitel} ({self.teljesitmeny}kW {self.hengerurtartalom})cm^3\n Száraz Tömege:{self.suly}kg"

