from .Zwierze import Zwierze
from abc import ABC, abstractmethod
class Czlowiek(Zwierze):

   def _getNazwa(self):
       return "Czlowiek"
   def _czyTenSamGatunek(self,organizm):
        pass
