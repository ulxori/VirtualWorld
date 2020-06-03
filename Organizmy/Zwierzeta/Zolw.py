from .Zwierze import Zwierze
from PIL import Image,ImageTk
import random
from .kierunki import *
#stale
szansaRuchu=4

class Zolw(Zwierze):
    __texturaSciezka = "zolw.png"

    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        super().__init__(swiat,sila,inicjatywa,id,x,y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _akcja(self):
        szansaRuchu=random.randint(0,4)
        if szansaRuchu<1:
            kierunek = random.randint(0,3)
            self._move(kierunek)

    def _getNazwa(self):
        return "Zolw"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm, Zolw)

    def _zwrocKopie(self, x, y):
        return Zolw(self._swiat, self._getSila(), self._getInicjatywa(),self._getId(), x, y)


    def _kolizja(self,atakujacy):
        if self._czyTenSamGatunek(atakujacy):
            self._rozmnazajSie()
        else:
            if atakujacy._getSila()<5:
                atakujacy._umrzyj()
            else:
                x, y = self._getPozycja()
                self._umrzyj()
                atakujacy._swiat._przesunOrganizm(x, y, atakujacy)
