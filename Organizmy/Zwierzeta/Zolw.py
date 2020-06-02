from .Zwierze import Zwierze
from PIL import Image,ImageTk
from .kierunki import *


class Zolw(Zwierze):
    __texturaSciezka = "zolw.png"

    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        super().__init__(swiat,sila,inicjatywa,id,x,y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))