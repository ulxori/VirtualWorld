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
    def akcja(self): pass
    @abstractmethod
    def kolizja(self): pass
    @abstractmethod
    def getNazwa(self): pass
    @abstractmethod
    def rozmnazajSie(self): pass
    def getSila(self):
        return self._sila
    def getInicjatywa(self):
        return self._inicjatywa
    def czyZywy(self):
        return self._zywy
    def getId(self):
        return self._id
    def setSila(self,sila):
        self._sila=sila
    def doZapisu(self):
        x,y=*self._pozycja



