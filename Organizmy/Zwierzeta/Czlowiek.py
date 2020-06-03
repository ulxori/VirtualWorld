from .Zwierze import Zwierze
from abc import ABC, abstractmethod
from PIL import Image,ImageTk
from .kierunki import *


class Czlowiek(Zwierze):

    __texturaSciezka="czlowiek.png"

    def __init__(self,swiat,sila,inicjatywa,id,x,y,czyAktywna,pozostaleTury):
        super().__init__(swiat,sila,inicjatywa,id,x,y)
        self._textura = ImageTk.PhotoImage((Image.open(self.__texturaSciezka)))
        self._aktywnaUmiejetnosc=czyAktywna
        self._pozostaleTuryUmiejetnosci=pozostaleTury


    def _getNazwa(self):
       return "Czlowiek"

    def _czyAktywna(self):
        return self._aktywnaUmiejetnosc

    def _regenerujUmiejetnosc(self):
        self._pozostaleTuryUmiejetnosci=self._getPozostaleTuryUmiejetnosci()+1

    def _aktywujUmiejetnosc(self):
        self._aktywnaUmiejetnosc=True

    def _dezaktywujUmiejetnosc(self):
        self._aktywnaUmiejetnosc=False
    def _getPozostaleTuryUmiejetnosci(self):
        return self._pozostaleTuryUmiejetnosci

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
            tmp=self._swiat._getZawartoscPunktu(x,y)
            if tmp==None:
                self._swiat._przesunOrganizm(x,y,self)
            else:
                if self._aktywnaUmiejetnosc==False:
                    tmp._kolizja(self)
                    if self._zywy==True:
                        self._swiat._przesunOrganizm(x, y, self)

    def _czyTenSamGatunek(self,organizm):
        return isinstance(organizm,Czlowiek)

    def _zwrocKopie(self): pass



