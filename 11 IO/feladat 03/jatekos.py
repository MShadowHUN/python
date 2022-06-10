class Jatekos:
        def __init__(self, nev:str, magas:int, poszt:str, nemzetiseg:str, csapat:str, orszag:str,) -> None:
            super().__init__()
            self.nev:str = nev
            self.magas:int = magas
            self.poszt:str = poszt
            self.nemzetiseg:str = nemzetiseg
            self.csapat:str = csapat
            self.orszag:str = orszag
        
        def __str__(self) -> str:
            return f"{self.nev}, {self.magas}, {self.poszt}, {self.nemzetiseg}, {self.csapat}, {self.orszag}"
