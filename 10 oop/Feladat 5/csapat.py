from jatekos import Jatekos
from szekhely import Szekhely
from typing import *

class Csapat:
    def __init__(self, csapatnev:str, jatekosok:List[Jatekos], szekhely:Szekhely):
        super(). __init__()
        self.csapatnev:str=csapatnev
        self.jatekosok:List[Jatekos]=jatekosok
        self.szekhely:Szekhely=szekhely
    def __str__(self):
        output=f"{self.csapatnev}\n{self.szekhely}\n"
        for jatekos in self.jatekosok:
            output +=f"\t - {str(jatekos)}\n"

        return output
    
    def legjobbJatekos(self)->Jatekos:
        max:Jatekos=self.jatekosok[0]

        for i in range(1,len(self.jatekosok)):
            if(self.jatekosok[i].pontszam > max.pontszam):
                max=self.jatekosok[i]
        
        return max

    def novekvoSorrend(self)->None:
        temp=self.jatekosok.copy()
        for i in range(0, len(self.jatekosok)-1,1):
            for j in range(i+1, len(self.jatekosok), 1):
                if(self.jatekosok[j].mezszam <self.jatekosok[i].mezszam):
                    temp=self.jatekosok[i]
                    self.jatekosok[i]=self.jatekosok[j]
                    self.jatekosok[j]
        return self