class Konyv:
    def __init__(self, veznev:str, kernev:str,szulev:str,cim:str,isbn:int,kiado:str,kiadasiev:int,ar:int,tema:str,oldal:int,honor:int ) ->None :
        super().__init__()
        self.veznev:str=veznev
        self.kernev:str=kernev
        self.szulev:str=szulev
        self.cim:str=cim
        self.isbn:int=isbn
        self.kiado:str=kiado
        self.kiadasiev:int=kiadasiev
        self.ar:int=ar
        self.tema:str=tema
        self.oldal:int=oldal
        self.honor:int=honor

    def __str__(self)->str:
        return f"{self.veznev}:{self.kernev}:{self.szulev}:{self.cim}:{self.isbn}:{self.kiado}:{self.kiadasiev}:{self.ar}:{self.tema}:{self.oldal}:{self.honor}"
