class Alaplap:
    def __init__(self, gyarto:str, tipus:str,kivitel:str, cpufoglalat:str, ramfoglalat:str):
        super(). __init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kivitel:str=kivitel
        self.cpufoglalat:str=cpufoglalat
        self.ramfoglalat:str=ramfoglalat
    def __str__(self):
        return f"{self.gyarto} {self.tipus} {self.kivitel} CPU foglalat:{self.cpufoglalat} RAM foglalat:{self.ramfoglalat}"