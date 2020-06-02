from ..Organizm import *
import random

#stale
liczbaProbRozmazania=3
szansaRozmnozenia=50


class Roslina(Organizm):
    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        super().__init__(swiat,sila,inicjatywa,id,x,y)

    def _akcja(self):
        for i in range(liczbaProbRozmazania):
            szansa=random.randint(0,szansaRozmnozenia)
            if szansa<1:
                self._rozmnazajSie()
                break



    def _kolizja(self,atakujacy):
        self._umrzyj()

