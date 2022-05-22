from champion import PogChamp
import random

class Bruiser(PogChamp):
    def __init__(self, nev: str, faj: str):
        PogChamp.__init__(self,nev,faj)
    def LetsMakeTrouble(self):
        self.power+=random.randint(20,50)
        self.hp+=200
        self.mana-=150
        self.armor+=40