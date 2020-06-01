import tkinter as tk
from .Stale import *
from Organizmy import *
import random
#stałe
szerokoscSwiata=720
wysokoscSwiata=480
nowaGra='n'
wczytajgre='l'
liczbaTypowOrganizmow=12
wiadomoscStartowa="Witaj, aby zacząc naciśnij:\nn - Nowa gra \nl - Wczytaj gre"
z=None

class Swiat(tk.Canvas):

    def __init__(self):
        super().__init__(width=szerokoscSwiata,height=wysokoscSwiata,background="black",highlightthickness=0)
        self.create_text(200,70,text=wiadomoscStartowa,fill="#fff",font=("TkDeaufultFont",24))
        self.bind_all("<Key>",self._inicjujRozgrywke)
        self._plansza=[[z for i in range(20)] for j in range(20)]
        self._kolejkaOrganizmow=[]
        self._wysokosc=20
        self._szerokosc=20
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
                self._dodajOrganizm(i,x,y)
        self._rozgrywka()

    def _rozgrywka(self):
        self.bind("<Button-1>",self._wykonajTure)
        self.bind_all("<Key>",self._rysujPlansze)

    def _wykonajTure(self,e):
        print(1)
    def _rysujPlansze(self,e):
        print(2)

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
        tmp=Czlowiek(self,Sila.Czlowiek,Inicjatywa.Czlowiek,Id.Czlowiek,x,y)
        self._kolejkaOrganizmow.append(tmp)
        self._plansza[y][x]=tmp
    def _dodajOrganizm(self,id,x,y):
        if id ==Id.Wilk:
            print(1)






