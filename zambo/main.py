from pilota import Pilota
from pilotaio import PilotaIO
from typing import *

pilotak:List[Pilota] = []

pilotak = PilotaIO.read("pilotak.csv")

PilotaIO.kiiras(pilotak)