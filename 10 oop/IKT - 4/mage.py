from champion import PogChamp
import random

class Mage(PogChamp):
    def __init__(self, nev: str, faj: str):
        PogChamp.__init__(self,nev,faj)
    def CastSpell(self):
        self.power+=random.randint(10,50)
        self.hp+=100
        self.mana-=50
        self.armor+=150