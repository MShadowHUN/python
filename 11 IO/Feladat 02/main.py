import imp
from typing import *
from könyv import Konyv
from könyvtar import Konyvtar
from könyvio import KonyvIO

konyvek:List[Konyv]=KonyvIO.read("adatok.txt")

print("Könyvek adatai: \n")
for konyv in konyvek:
    print(f"{konyv}\n")

Konyvtar.informatika(konyvek)
print("A könyvtárban lévő informatika témájú könyvek exportja megtörtént")

Konyvtar.huszadikszazad(konyvek)
print("A huszadik században kiadott könyvek exportja megtörtént")