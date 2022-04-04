class Hdd:
    def __init__(self, gyarto:str, tipus:str,kapacitas:int, rpm:int, meret:float):
        super(). __init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kapacitas:int=kapacitas
        self.rpm:int=rpm
        self.meret:float=meret
    
    def __str__(self):
        return f"{self.gyarto}  {self.tipus} kapacitás:{self.kapacitas}TB, Fordulatszám:{self.rpm} Méret:{self.meret}Col"