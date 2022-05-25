import imp
from typing import *
from jatekos import Jatekos
from csapat import Csapat
from jatekosio import JatekosIO

jatekosok:List[Jatekos]=JatekosIO.read("adatok.txt")

print("Játékosok adatai: \n")
for jatekos in jatekosok:
    print(f"{jatekos}\n")

Csapat.utok(jatekosok)
print("Az ütő játékosok exportja megtörtént")

Csapat.csapatok(jatekosok)
print("Csapatok szerinti export megtörtént")

Csapat.atlagmagassag(jatekosok)
print("Átlagnál magasabbak exportja megtörtént")

Csapat.atlagmagassagalatt(jatekosok)
print("Átlagnál alacsonyabbak kigyűjtése megtörtént")

Csapat.magassagnov(jatekosok)
print("Játékosok magasság szerinti növekvő sorrendbe való kiírása megtörtént")

Csapat.nemzetisegek(jatekosok)
print("Nemzetiség szerinti képviselet exprojta megtörtént")

Csapat.posztok(jatekosok)
print("Játéksok összmagasságának poszt szerinti rendezés exportja megtörtént")