from .Roslina import Roslina
from PIL import Image, ImageTk



class Mlecz(Roslina):
    __texturaSciezka = "mlecz.png"

    def __init__(self, swiat, sila, inicjatywa, id, x, y):
        super().__init__(swiat, sila, inicjatywa, id, x, y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))


    def _zwrocKopie(self,x,y):
        return Mlecz(self._swiat,self._sila,self._inicjatywa,self._id,x,y)


    def _getNazwa(self):
        return "Mlecz"