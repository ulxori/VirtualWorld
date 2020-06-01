from abc import ABC,abstractmethod

class Organizm(ABC):
    def __init__(self,swiat,sila,inicjatywa,id,x,y):
        self._swiat=swiat
        self._sila=sila
        self._inicjatywa=inicjatywa
        self._id=id
        self._zywy=True
        self._pozycja=(x,y)
    @abstractmethod
    def _akcja(self): pass
    @abstractmethod
    def _kolizja(self): pass
    @abstractmethod
    def _getNazwa(self): pass
    @abstractmethod
    def _rozmnazajSie(self): pass
    def _getSila(self):
        return self._sila
    def _getInicjatywa(self):
        return self._inicjatywa
    def _czyZywy(self):
        return self._zywy
    def _getId(self):
        return self._id
    def _setSila(self,sila):
        self._sila=sila
    def _doZapisu(self):
        id=self._id
        sila=self._sila
        x,y=self._pozycja
        str=f"{id} {x} {y} {sila}"
        return str




