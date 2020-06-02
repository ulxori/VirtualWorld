from .Zwierze import Zwierze
from abc import ABC, abstractmethod
from PIL import Image,ImageTk
from .kierunki import *


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
       x,y=self._getPozycja()
       kierunek=self._swiat._getKierunek()
       if kierunek==Kierunek.dol.value:
           y+=1
       elif kierunek==Kierunek.gora.value:
           y-=1
       elif kierunek==Kierunek.prawo.value:
           x+=1
       elif kierunek==Kierunek.lewo.value:
           x-=1
       if self._swiat._walidujPunkt(x,y):
           self._setPozycja(x,y)


    def _czyTenSamGatunek(self,organizm):
        return isinstance(organizm,Czlowiek)


