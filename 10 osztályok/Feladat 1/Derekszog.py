class Derekszog:

    def __init__(self, befogo: float, hosszabbBefogo: float, atfogo:float) -> None:
        super().__init__()
        

        self.befogo =befogo
        self.hosszabbBefogo = hosszabbBefogo
        self.atfogo =atfogo

    def __str__(self) -> str:
        return f"befogo = {self.befogo}\nszélesség = {self.hosszabbBefogo}\nátfogó = {self.atfogo}\nT = {self.terulet()}\nK = {self.kerulet()}"

    def terulet(self) -> float:
        return (self.befogo * self.hosszabbBefogo)/2
    
    def kerulet(self) -> float:
        return self.befogo + self.hosszabbBefogo + self.atfogo