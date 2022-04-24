import random

class Szuperhos:
    def __init__(self, nev:str):
        super(). __init__()
        self.nev:str=nev

        ero:int=random.randint(50,100)
        hp:int=random.randint(60,90)
    
    def __str__(self):
        self.ero:int=random.randint(50,100)
        self.hp:int=random.randint(60,90)
        return f"Szuperhő neve:{self.nev} ereje:{ero} életpontja:{hp}"
    
    def tamad(self,hos:"Szuperhos", ellenseg:"Szuperhos")->bool:
        if(self.hos.ero > self.ellenseg.hp):
            legyozi:bool=True
        else:
            legyozi:bool=False
        return legyozi