from champion import PogChamp
import random

class Worrior(PogChamp):
    def __init__(self, nev: str, faj: str):
        PogChamp.__init__(self,nev,faj)
    def GetRage(self):
        self.power+=random.randint(30,60)
        self.hp+=120
        self.mana-=200
        self.armor+=50