class Egyenloszar:
    def __init__(self, alap: float, szar: float) -> None:
        super().__init__()
        
        self.alap = alap
        self.szar = szar

    def __str__(self) -> str:
        return f"alap = {self.alap}\nszélesség = {self.szar}\nT = {self.terulet()}\nK = {self.kerulet()}"

    def terulet(self) -> float:
        return self.alap * (((self.szar * self.szar)-((2/self.alap)*(2/self.alap)))**(0.5))
    
    def kerulet(self) -> float:
        return 2 *self.szar + self.alap