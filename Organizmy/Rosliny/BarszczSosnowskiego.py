from .Roslina import Roslina
from PIL import Image, ImageTk



class BarszczSosnowskiego(Roslina):
    __texturaSciezka = "barszcz.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))