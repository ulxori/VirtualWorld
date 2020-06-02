from .Zwierze import Zwierze
from PIL import Image, ImageTk
from .kierunki import *


class Owca(Zwierze):
    __texturaSciezka = "owca.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _getNazwa(self):
        return "Owca"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm, Owca)

    def _zwrocKopie(self, x, y):
        return Owca(self._swiat, self._getSila(), self._getInicjatywa(), x, y)