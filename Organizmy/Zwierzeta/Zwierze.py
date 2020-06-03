from ..Organizm import *

import random
class Zwierze(Organizm):
    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        super().__init__(swiat,sila,inicjatywa,id,x,y)


    @abstractmethod
    def _czyTenSamGatunek(self, organizm): pass

    def _akcja(self):
        kierunek=random.randint(0,3)
        self._move(kierunek)

    def _move(self,kierunek):
        x, y = self._getPozycja()
        if kierunek == 0:
            y += 1
        elif kierunek == 1:
            y -= 1
        elif kierunek == 2:
            x += 1
        elif kierunek == 3:
            x -= 1
        if self._swiat._walidujPunkt(x, y):
            tmp = self._swiat._getZawartoscPunktu(x, y)
            if tmp == None:
                self._swiat._przesunOrganizm(x, y, self)
            else:
                tmp._kolizja(self)


    def _kolizja(self,atakujacy):

        if self._czyTenSamGatunek(atakujacy):
            self._rozmnazajSie()
        else:
            if self._getSila()>atakujacy._getSila():
                atakujacy._umrzyj()
            else:
                x,y=self._getPozycja()
                self._umrzyj()
                atakujacy._swiat._przesunOrganizm(x, y, atakujacy)






