from pilota import Pilota
from pilotaio import PilotaIO
from typing import *
from pilotak import Pilotak

pilotak:List[Pilota] = []

pilotak = PilotaIO.read("pilotak.csv")

PilotaIO.kiiras(pilotak)

Pilotak.hanySoros(pilotak)

Pilotak.utolsoSorbanPilota(pilotak)

Pilotak.tizenkilencedikSzazadbanSzuletett(pilotak)

Pilotak.legkissebbRajtszam(pilotak)

Pilotak.tobbszoriRajtszamok(pilotak)