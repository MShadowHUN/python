class Motorkerekpar:
    def __init__(self, gyarto:str="", tipus:str="", kivitel:str="", teljesitmeny:int=0, hengerurtartalom:int=0, suly:int=0 ):
        super(). __init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kivitel:str=kivitel
        self.teljesitmeny:int=gyarto
        self.hengerurtartalom:int=hengerurtartalom
        self.suly:int=suly
    
    def __str__(self):
        return f"{self.gyarto} {self.tipus} {self.kivitel} ({self.teljesitmeny}kW {self.hengerurtartalom})cm^3"

