from .Zwierze import Zwierze
from PIL import Image, ImageTk
from .kierunki import *


class CyberOwca(Zwierze):
    __texturaSciezka = "cyberOwca.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _getNazwa(self):
        return "Cyber owca"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm, CyberOwca)

    def _zwrocKopie(self, x, y):
        return CyberOwca(self._swiat, self._getSila(), self._getInicjatywa(),self._getId(), x, y)