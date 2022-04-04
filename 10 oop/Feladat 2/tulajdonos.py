class Tulajdonos:
    def __init__(self, nev:str="", szuletesiDatum:str="", nem :str="", szuletesihely:str=""):
        super(). __init__()

        self.nev:str=nev 
        self.szuletsiDatum:str=szuletesiDatum
        self.nem:str=nem 
        self.szuletsihley:str=szuletesihely

    def __str__(self):
        return f"Tulajdonos: {self.nev}\n {self.szuletsiDatum}\n {self.nem}\n {self.szuletsihley}"
