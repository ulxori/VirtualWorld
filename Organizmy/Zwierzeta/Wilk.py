from .Zwierze import Zwierze
from PIL import Image, ImageTk
import random
from .kierunki import *


class Wilk(Zwierze):
    __texturaSciezka = "wilk.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _getNazwa(self):
        return "Wilk"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm, Wilk)

    def _zwrocKopie(self, x, y):
        return Wilk(self._swiat, self._getSila(), self._getInicjatywa(), x, y)
