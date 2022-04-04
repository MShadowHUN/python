class Proci:
    def __init__(self, gyarto:str, tipus:str, teljesitmeny:int, alaporajel:float, frekvencia:int, magszam:int,):
        super(). __init__() 
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.teljesitmeny:int=teljesitmeny
        self.alaporajel:float=alaporajel
        self.frekvencia:int=frekvencia
        self.magszam:int=magszam

    def __str__(self):
        return f"{self.gyarto} {self.tipus} teljesítmény:{self.teljesitmeny}W Gyári órajel:{self.alaporajel}GHz, Frekvencia:{self.frekvencia}MHz, {self.magszam} magos"