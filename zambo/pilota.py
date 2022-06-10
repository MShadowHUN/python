class Pilota:
    def __init__ (self,nev:str,szuletesiDatum:str, nemzetiseg:str,rajtszam:int) -> None:
        self.nev:str = nev
        self.szuletesiDatum:str = szuletesiDatum
        self.nemzetiseg:str = nemzetiseg
        self.rajtszam:int = rajtszam
    def __str__(self) -> str:
        return f"{self.nev}\n -Született:{self.szuletesiDatum}\n -Nemzetiség:{self.nemzetiseg}\n -Rajtszám:{self.rajtszam}"