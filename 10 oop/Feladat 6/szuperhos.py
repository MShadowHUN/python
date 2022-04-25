import random

class Szuperhos:
    def __init__(self, nev:str):
        super(). __init__()
        self.nev:str=nev
        self.ero:int=random.randint(50,100)
        self.hp:int=random.randint(60,90)
    
    def __str__(self):
        return f"Szuperhő neve:{self.nev} ereje:{self.ero} életpontja:{self.hp}"
    
    def tamad (self, ellenseg:"Szuperhos")->bool:
        return self.ero > ellenseg.hp