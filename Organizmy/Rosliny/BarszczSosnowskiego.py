from .Roslina import Roslina
from ..Zwierzeta import CyberOwca
from PIL import Image, ImageTk
import random
#stale
szansaRozmnozenia=50
liczbaProbRozmazania=1


class BarszczSosnowskiego(Roslina):
    __texturaSciezka = "barszcz.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _zwrocKopie(self, x, y):
        return BarszczSosnowskiego(self._swiat, self._sila, self._inicjatywa, self._id, x, y)

    def _getNazwa(self):
        return "Barszcz Sosnowskeigo"

    def _akcja(self):
        for i in range(liczbaProbRozmazania):
            szansa = random.randint(0, szansaRozmnozenia)
            if szansa < 1:
                self._rozmnazajSie()
                break
        sasiedniePola = self._swiat._getSasiedniePola(*self._getPozycja())
        for x, y in sasiedniePola:
            tmp=self._swiat._getZawartoscPunktu(x, y)
            if not tmp==None:
                tmp._umrzyj()
    def _kolizja(self,atakujacy):
        if isinstance(atakujacy,CyberOwca):
            self._umrzyj()
        else:
            atakujacy._umrzyj()



