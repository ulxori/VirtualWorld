from enum import Enum

class Id(Enum):
    Wilk=1
    Owca=2
    Lis=3
    Zolw=4
    Antylopa=5
    Trawa=6
    Mlecz=7
    Guarana=8
    WilczeJagody=9
    BarszczSosnowskiego=10
    CyberOwca=11
    Czlowiek=12


class Sila(Enum):
    Wilk = 9
    Owca = 4
    Lis = 3
    Zolw = 2
    Antylopa = 4
    Trawa = 0
    Mlecz = 0
    Guarana = 0
    WilczeJagody = 99
    BarszczSosnowskiego = 10
    Czlowiek = 5

class Inicjatywa(Enum):
    Wilk = 5
    Owca = 4
    Lis = 7
    Zolw = 1
    Antylopa = 4
    Czlowiek = 5
    Roslina = 0

class Kierunki(Enum):
    gora='w'
    dol='s'
    prawo='d'
    lewo='a'
