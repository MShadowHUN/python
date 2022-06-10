
from varos import Varos
from varosio import Varosio
from typing import *
from varosok import Varosok

varosok: List[Varos] = Varosio.read("adatok.txt")

Varosio.kiiras(varosok)

Varosok.megyeiJoguVarosok(varosok)

Varosok.nepesseg(varosok)

Varosok.nagyTeruletuTelepules(varosok)

Varosok.bekesmegye(varosok)

Varosok.megyeteruletekkiszamitasa(varosok)