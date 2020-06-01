from ..Organizm import *

class Zwierze(Organizm):
    def __init__(self):
        super.__init__()

    @abstractmethod
    def czyTenSamGatunek(self, org): pass
