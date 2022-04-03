class Egyenlooldal:

    def __init__(self, oldal: float,) -> None:
        super().__init__()
        

        self.oldal = oldal

    def __str__(self) -> str:
        return f"oldal = {self.oldal}\n T = {self.terulet()}\nK = {self.kerulet()}"

    def terulet(self) -> float:
        return (self.oldal * (((self.oldal*self.oldal)-(2/self.oldal)*(2/self.oldal))**(0.5)))
    
    def kerulet(self) -> float:
        return 3 *self.oldal
