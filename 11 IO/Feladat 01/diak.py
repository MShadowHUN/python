class Diak:
    def __init__(self, nev:str, atlag:float) ->None :
        super().__init__()
        self.nev:str=nev
        self.atlag:float=atlag

    def __str__(self)->str:
        return f"{self.nev}:{self.atlag}"

    