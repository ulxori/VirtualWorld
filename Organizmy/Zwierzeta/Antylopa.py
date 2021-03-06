from .Zwierze import Zwierze
from PIL import Image, ImageTk
import random
from .kierunki import *
#stale
szansaUcieczki=50


class Antylopa(Zwierze):
    __texturaSciezka = "antylopa.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _akcja(self):
        kierunek = random.randint(0,3)
        self._move(kierunek)
        if self._czyZywy():
            self._move(kierunek)

    def _kolizja(self,atakujacy):
        wolnePola = self._swiat._getSasiedniePola(*self._getPozycja())
        szansa=random.randint(0,100)
        if szansa<szansaUcieczki and wolnePola:
            x,y= wolnePola[0]
            self._swiat._przesunOrganizm(x,y,self)
        else:
            if self._getSila()> atakujacy._getSila():
                atakujacy._umrzyj()
            else:
                x, y = self._getPozycja()
                self._umrzyj()
                atakujacy._swiat._przesunOrganizm(x, y, atakujacy)

    def _getNazwa(self):
        return "Antylopa"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm,Antylopa)

    def _zwrocKopie(self,x,y):
        return Antylopa(self._swiat,self._getSila(),self._getInicjatywa(),self._getId(),x,y)

