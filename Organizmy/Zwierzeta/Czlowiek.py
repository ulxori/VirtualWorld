from .Zwierze import Zwierze
from abc import ABC, abstractmethod
from PIL import Image,ImageTk

class Czlowiek(Zwierze):

    __texturaSciezka="czlowiek.png"

    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        super().__init__(swiat,sila,inicjatywa,id,x,y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))

    def _getNazwa(self):
       return "Czlowiek"

    def _kolizja(self):
       pass
    def _rozmnazajSie(self):
       pass
    def _akcja(self):
       pass

    def _czyTenSamGatunek(self,organizm):
        return isinstance(organizm,Czlowiek)


