from .Zwierze import Zwierze
from PIL import Image, ImageTk
from .kierunki import *


class Lis(Zwierze):
    __texturaSciezka = "lis.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def move(self,kierunek):
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
                if tmp._getSila()<self._getSila():
                    tmp._kolizja(self)
                    if self._zywy == True:
                        self._swiat._przesunOrganizm(x, y, self)

    def _getNazwa(self):
        return "Lis"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm, Lis)

    def _zwrocKopie(self, x, y):
        return Lis(self._swiat, self._getSila(), self._getInicjatywa(), x, y)