class Varos:
    def __init__(self,nev:str,tipus:str,megyeNeve:str,jaras:str,kisterseg:str,nepesseg:int,terulet:float) -> None:
        super().__init__()
        self.nev:str = nev
        self.tipus:str = tipus
        self.megyeNeve:str = megyeNeve
        self.jaras:str =jaras
        self.kisterseg:str =kisterseg
        self.nepesseg:int =nepesseg
        self.terulet:float =terulet
    def __str__(self) -> str:
        return f"{self.nev}:\n -{self.tipus}\n -{self.megyeNeve} megye\n -{self.jaras}\n -{self.kisterseg}\n -{self.nepesseg} fő\n -{self.terulet}\n"