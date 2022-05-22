import random

class PogChamp:
    def __init__(self, nev:str, faj:str):
        super(). __init__()
        self.nev:str=nev
        self.faj:str=faj
        self.power:int=random.randint(1000,2000)
        self.hp:int=random.randint(500,800)
        self.mana:int=random.randint(600,750)
        self.armor:int=random.randint(400,800)
    def __str__(self):
        return f"Karakter neve:{self.nev} faja:{self.faj} ereje:{self.power} életpontja:{self.hp} manája:{self.mana} páncélja:{self.armor}"
    
    def tamad (self, ellenseg:"PogChamp")->bool:
        return self.power > ellenseg.armor