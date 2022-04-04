import math
class Kor:
    def __init__(self, sugar: float) -> None:
        super().__init__()

        self.sugar = sugar

    def __str__(self) -> str:
        return f"A Kör kerülete: {self.kerulet()}\nA Területe{self.terulet()}"

    def kerulet(self) -> float:
        return 2 * self.sugar * math.pi
    def terulet(self) -> float:
        return self.sugar * self.sugar * math.pi
