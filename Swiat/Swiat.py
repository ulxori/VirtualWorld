import tkinter as tk
from .Stale import *
from Organizmy import *
import random


#stałe
szerokoscSwiata=600
wysokoscSwiata=600
nowaGra='n'
wczytajgre='l'
liczbaTypowOrganizmow=12
wiadomoscStartowa="Witaj, aby zacząc naciśnij:\nn - Nowa gra \nl - Wczytaj gre"
szerokoscPostaci=30
wysokoscPostaci=30
wysokoscPlanszy=20
szerokoscPlanszy=20
niezdefiniowana=0
w=0
h=0
z=None
##############
class Swiat(tk.Canvas):

    def __init__(self):
        super().__init__(width=szerokoscSwiata,height=wysokoscSwiata,background="black",highlightthickness=0)
        self.create_text(200,70,text=wiadomoscStartowa,fill="#fff",font=("TkDeaufultFont",24))
        self.bind_all("<Key>",self._inicjujRozgrywke)
        self._plansza=[[z for i in range(20)] for j in range(20)]
        self._kolejkaOrganizmow=[]
        self._wysokosc=wysokoscPlanszy
        self._szerokosc=szerokoscPlanszy
        self._kierunek=None

    def _inicjujRozgrywke(self,event):
        if event.keysym==nowaGra:
            self.unbind_all("<Key>")
            self._nowaGra()
        elif event.keysym==wczytajgre:
            self.unbind_all("<Key>")


    def _nowaGra(self):
        print('sss')
        x,y=self._losowyPunkt()
        self._dodajCzlowiek(x,y)
        for i in range(1,liczbaTypowOrganizmow-1):
            for j in range(2):
                x,y=self._losowyPunkt()
                self._dodajOrganizm(i,x,y,niezdefiniowana)
        self.delete("all")
        self._rozgrywka()

    def _rozgrywka(self):
        self._rysujPlansze()
        self.bind_all("<Key>",self._wykonajTure)

    def _wykonajTure(self,e):
        self.delete("all")
        self._setKierunke(e.keysym)
        for org in self._kolejkaOrganizmow:
            org._akcja()
        self._rysujPlansze()


    def _rysujPlansze(self):
        for row in self._plansza:
            for el in row:
                if not el==None:
                    x,y=el._getPozycja()
                    self.create_image(x*szerokoscPostaci+15,y*wysokoscPostaci+15,image=el._getTextura())


                   

    def _losowyPunkt(self):
        znaleziony=False
        while not znaleziony:
            x=random.randint(0,self._szerokosc-1)
            y=random.randint(0,self._wysokosc-1)
            if self._plansza[y][x]==None:
                znaleziony=True
        return x,y

    def _setKierunke(self,kierunek):
        self._kierunek=kierunek

    def _getKierunek(self):
        return self._kierunek

    def _dodajCzlowiek(self,x,y):
        tmp=Czlowiek(self,Sila.Czlowiek.value,Inicjatywa.Czlowiek.value,Id.Czlowiek.value,x,y)
        self._kolejkaOrganizmow.append(tmp)
        self._plansza[y][x]=tmp
    def _dodajOrganizm(self,id,x,y,sila):
        if id ==Id.Trawa.value:
            self._kolejkaOrganizmow.append(Trawa(self,Sila.Trawa.value,Inicjatywa.Roslina.value,Id.Trawa.value,x,y))
            self._plansza[y][x] = self._kolejkaOrganizmow[-1]

        if id==Id.WilczeJagody.value:
            self._kolejkaOrganizmow.append(WilczeJagody(self,Sila.WilczeJagody.value,Inicjatywa.Roslina.value,Id.WilczeJagody.value,x,y))
            self._plansza[y][x] = self._kolejkaOrganizmow[-1]



    def _getKierunek(self):
        return self._kierunek

    def _walidujPunkt(self,x,y):
        if x>=0 and x<szerokoscPlanszy and y>=0 and y<wysokoscPlanszy:
            return True
        else:
            return False

    def _getSasiedniePola(self,x,y):
        sasiedniePola=[]
        for i in range(3):
            posY=y-1+i
            for j in range(3):
                posX=x-1+j
                if self._walidujPunkt(posX,posY):
                    if i==1 and j==1:
                        continue
                    else:
                        sasiedniePola.append((posX,posY))
        return sasiedniePola

    def _getZawartoscPunktu(self,x,y):
        return self._plansza[y][x]


    def _umiescNaPlanszy(self,organizm):

        x,y=organizm._getPozycja()
        self._plansza[y][x]=organizm
        self._kolejkaOrganizmow.append(organizm)


    def _usunOrganizm(self,organizm):

        x,y=organizm._getPozycja()
        self._plansza[y][x]=None
        self._kolejkaOrganizmow.remove(organizm)


    def _przesunOrganizm(self,x,y,organizm):

        xPoprzadnie, yPoprzednie=organizm._getPozycja()
        self._plansza[yPoprzednie][xPoprzadnie]=None
        self._plansza[y][x]=organizm
        organizm._setPozycja(x,y)





