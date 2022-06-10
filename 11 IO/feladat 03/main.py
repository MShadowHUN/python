from jatekos import Jatekos
from jatekosio import JatekosIO
from typing import *
from csapat import Csapat


jatekosok: List[Jatekos] = JatekosIO.read("roplabda.txt")

Csapat.kiiras(jatekosok)

Csapat.posztKereses("ütõ",jatekosok)

Csapat.csapatJatekosa(jatekosok)

Csapat.magassagSorrend(jatekosok)

Csapat.nemzetisegek(jatekosok)

Csapat.atlagnalMagasabb(jatekosok)

Csapat.posztokOsszMagassag(jatekosok)

Csapat.alacsonyak(jatekosok)