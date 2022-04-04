class Ram:
    def __init__(self, gyarto:str, tipus:str,foglalat:str, kapacitas:int, frekvencia:int):
        super(). __init__() 
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.foglalat=foglalat
        self.kapacitas:int=kapacitas
        self.frekencia:int=frekvencia

    def __str__(self):
        return f"{self.gyarto} {self.tipus} Kapacitás:2x{self.kapacitas}GB Frekvencia:{self.frekencia}MHz Foglalat:{self.foglalat}"