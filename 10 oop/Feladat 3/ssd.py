class Ssd:
    def __init__(self, gyarto:str, tipus:str,kapacitas:int, iras:int, olvasas:int):
        super(). __init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kapacitas:int=kapacitas
        self.iras:int=iras
        self.olvasas:int=olvasas

    def __str__(self):
        return f"{self.gyarto}  {self.tipus} kapacitás:{self.kapacitas}GB Olvasási sebesség:{self.olvasas}MB/s Írási sebesség:{self.iras}MB/s"