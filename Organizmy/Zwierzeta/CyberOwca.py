from .Zwierze import Zwierze
from PIL import Image, ImageTk
from .kierunki import *


class CyberOwca(Zwierze):
    __texturaSciezka = "cyberOwca.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))
    def _akcja(self):
        barszcz=self._swiat._szukajNajblizszegoBarszczu(*self._getPozycja())
        if barszcz!=None:
            xB,yB=barszcz._getPozycja()
            xA,yA=self._getPozycja()
            if xB>xA:
                xA+=1
            elif xB<xA:
                xA-=1
            elif yB>yA:
                yA+=1
            elif yB<yA:
                yA-=1
        if self._swiat._walidujPunkt(xA, yA):
            tmp = self._swiat._getZawartoscPunktu(xA, yA)
            if tmp == None:
                self._swiat._przesunOrganizm(xA, yA, self)
            else:
                tmp._kolizja(self)





    def _getNazwa(self):
        return "Cyber owca"

    def _czyTenSamGatunek(self, organizm):
        return isinstance(organizm, CyberOwca)

    def _zwrocKopie(self, x, y):
        return CyberOwca(self._swiat, self._getSila(), self._getInicjatywa(),self._getId(), x, y)