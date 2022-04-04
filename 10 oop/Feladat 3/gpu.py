class Videokartya:
    def __init__(self, gyarto:str, tipus:str, teljesitmeny:int, videomemoria:int, led:str, venti:int,):
        super(). __init__() 
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.teljesitmeny:int=teljesitmeny
        self.videomemoria:int=videomemoria
        self.led:str=led
        self.venti:int=venti

    def __str__(self):
        return f"{self.gyarto} {self.tipus} teljesítmény:{self.teljesitmeny}W Videómemória: {self.videomemoria}GB, led:{self.led} ventillátorszám:{self.venti}db"