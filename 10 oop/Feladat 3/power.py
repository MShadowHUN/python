class Tap:
    def __init__(self, gyarto:str, tipus:str, teljesitmeny:int, besorolas:str, modalitas:bool, kivitel:str):
        super(). __init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.teljesitmeny:int=teljesitmeny
        self.besorolas:str=besorolas
        self.modalitas:bool=modalitas
        self.kivitel:str=kivitel 
    
    def __str__(self):
        return f"{self.gyarto} {self.tipus} teljesítmény:{self.teljesitmeny}W Besorolás:{self.besorolas} Moduláris?:{self.modalitas} {self.kivitel}"