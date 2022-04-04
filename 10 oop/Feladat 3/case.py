class Gephaz:
    def __init__(self, gyarto:str, tipus:str, szelesseg:int, magassag:int, kivitel:str, venti:int,hossz:int ):
        super(). __init__() 
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.szelesseg:int=szelesseg
        self.magassag:int=magassag
        self.kivitel:str=kivitel
        self.venti:int=venti
        self.hossz:int=hossz
    
    def __str__(self):
        return f"{self.gyarto}  {self.tipus}  {self.magassag}mm x {self.szelesseg}mm x {self.hossz}mm  {self.kivitel}  gyári ventillátorok száma:{self.venti}"