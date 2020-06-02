from ..Organizm import *

class Zwierze(Organizm):
    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        super().__init__(swiat,sila,inicjatywa,id,x,y)


    @abstractmethod
    def _czyTenSamGatunek(self, organizm): pass
