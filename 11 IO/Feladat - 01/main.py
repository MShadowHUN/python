from diak import Diak
from typing import *
from diakio import DiakIO

diakok: List[Diak] = DiakIO.read("adatok.txt")

print("A diakok adatai: \n")
for diak in diakok:
    print(f"{diak}\n")