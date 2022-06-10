from operator import contains
from tempfile import tempdir
from pilota import Pilota
import os
import time
from typing import *
from pilotaio import PilotaIO


class Pilotak:
    @staticmethod
    def hanySoros(pilotak:List[Pilota]) -> None:
        sorokSzama:int = 0
        for pilota in pilotak:
            sorokSzama+=1

        PilotaIO.sorokSzamaKiiras(sorokSzama)

    @staticmethod
    def utolsoSorbanPilota(pilotak:List[Pilota]) ->None:
        utolsoPilota:Pilota = None
        for pilota in pilotak:
            utolsoPilota = pilota
        
        PilotaIO.utolsoPilotaKiiras(utolsoPilota)
    
    @staticmethod
    def tizenkilencedikSzazadbanSzuletett (pilotak:List[Pilota]) -> None:
        tizenKilencedikSzazadbanSzuletettPilotak:List[Pilota] = []
        szuletesiev:int = None


        for pilota in pilotak:
            adat = pilota.szuletesiDatum.split(".")

            szuletesiev = int(adat[0])
            if(szuletesiev < 1901):
                tizenKilencedikSzazadbanSzuletettPilotak.append(pilota)
        
        PilotaIO.tizenkilencedikSzazadbanSzuletettPilotakKiirasa(tizenKilencedikSzazadbanSzuletettPilotak)
    
        
    @staticmethod    
    def legkissebbRajtszam (pilotak:List[Pilota]) -> None:
        legkissebbRajtszamu:Pilota = None
        rajtszamok:set(int) = set()
        legkissebbRajtszam: int= None
        temp:int = None

        for pilota in pilotak:
            rajtszamok.add(pilota.rajtszam)

        for rajtszam in rajtszamok:
            temp = rajtszam
            if(rajtszam < temp):
                legkissebbRajtszam = rajtszam

        for rajtszam in rajtszamok:
            temp = rajtszam
            for pilota in pilotak:
                if(rajtszam < temp):
                    legkissebbRajtszam = rajtszam 
                    if(pilota.rajtszam == legkissebbRajtszam):
                        legkissebbRajtszamu = pilota
        
        PilotaIO.legkissebbRajtszamuPilotaKiiras(legkissebbRajtszamu)

    @staticmethod
    def tobbszoriRajtszamok(pilotak:List[Pilota]) -> None:
        TobbszorEloforduloRajtszamok:List[int] = []
        temp:List[Pilota] = []

        rajtszamok:set(int) = set()
        for pilota in pilotak:
            rajtszamok.add(pilota.rajtszam)
        
        for rajtszam in rajtszamok:
            if (pilota.rajtszam == rajtszam):
                temp.append(pilota.rajtszam)
                if(int(temp.__len__()) > 1):
                    TobbszorEloforduloRajtszamok.append(pilota.rajtszam)

        PilotaIO.tobbszoriRajtszamokKiiras(TobbszorEloforduloRajtszamok)