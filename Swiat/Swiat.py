import tkinter as tk
from .Stale import *
#stałe
szerokoscSwiata=720
wysokoscSwiata=480
nowaGra='n'
wczytajgre='l'
wiadomoscStartowa="Witaj, aby zacząc naciśnij:\nn - Nowa gra \nl - Wczytaj gre"
class Swiat(tk.Canvas):

    def __init__(self):
        super().__init__(width=szerokoscSwiata,height=wysokoscSwiata,background="black",highlightthickness=0)
        self.create_text(200,70,text=wiadomoscStartowa,fill="#fff",font=("TkDeaufultFont",24))
        self.bind_all("<Key>",self._inicjujRozgrywke)
        self._organizmy=[]
        self._wysokosc=20
        self._szerokosc=20

    def _inicjujRozgrywke(self,event):
        if event.keysym==nowaGra:
            self.unbind_all("<Key>")
            self._nowaGra()
        elif event.keysym==wczytajgre:
            self.unbind_all("<Key>")


    def _nowaGra(self):
        print('sss')


    def _dodajOrganizm(self,id):
        if id ==Id.Wilk:
            print(1)






