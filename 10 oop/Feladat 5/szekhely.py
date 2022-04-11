class Szekhely:
    def __init__(self,telepules:str,iranyitoszam:int,megye:str,kozterulet:str,szam:int):
        super(). __init__()
        self.telepules:str=telepules
        self.iranyitoszam:int=iranyitoszam
        self.megye:str=megye
        self.kozterulet:str=kozterulet
        self.szam:int=szam

    def __str__(self):
        return f"{self.megye}megye: {self.telepules} / {self.iranyitoszam} / {self.kozterulet}, {self.szam}"