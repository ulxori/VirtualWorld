import tkinter as tk
from .Stale import *
from Organizmy import *
import random
from PIL import Image, ImageTk

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
textura="Swiat.png"


class Swiat(tk.Canvas):


    def __init__(self):

        super().__init__(width=szerokoscSwiata,height=wysokoscSwiata,background="black",highlightthickness=0)
        self.create_text(200,70,text=wiadomoscStartowa,fill="#fff",font=("TkDeaufultFont",24))
        self.bind_all("<Key>",self._inicjujRozgrywke)
        self._plansza=[[z for i in range(20)] for j in range(20)]
        self._kolejkaOrganizmow=[]
        self._punktDlaNowegoOrganizmu=()
        self._menuSwiata=ImageTk.PhotoImage((Image.open(textura)))
        self._wysokosc=wysokoscPlanszy
        self._szerokosc=szerokoscPlanszy
        self._kierunek=None


    def _inicjujRozgrywke(self,event):

        if event.keysym==nowaGra:
            self.unbind_all("<Key>")
            self._nowaGra()

        elif event.keysym==wczytajgre:
            self.unbind_all("<Key>")
            self._wczytajGre()
            self._rozgrywka()

    def _wczytajGre(self):
        zapis=open("save.txt","r")

        for line in zapis:
            line=line.split()
            id=int(line[0])
            x=int(line[1])
            y=int(line[2])
            sila=int(line[3])
            if id==Id.Czlowiek.value:
                czyAktywna=line[4]
                pozostaleTury=int(line[5])
                self._dodajCzlowiek(sila,x,y,czyAktywna,pozostaleTury)
            else:
                self._dodajOrganizm(id, x, y, niezdefiniowana)
        zapis.close()
        self.delete("all")



    def _nowaGra(self):

        x,y=self._losowyPunkt()
        self._dodajCzlowiek(x,y,Sila.Czlowiek.value,False,5)
        for i in range(1,liczbaTypowOrganizmow):
            for j in range(2):
                x,y=self._losowyPunkt()
                self._dodajOrganizm(i,x,y,niezdefiniowana)

        self.delete("all")
        self._rozgrywka()


    def _rozgrywka(self):
        self._rysujPlansze()
        self.bind_all("<Button-1>", self._przechwycPole)
        self.bind_all("<Key>",self._wykonajTure)
        self.bind_all("<Tab>",self._zapiszGre)

    def _przechwycPole(self,event):
        self.delete("all")
        self.create_image(165, 15, image=self._getMenuSwiat())

        posX=int(event.x/szerokoscPostaci)
        posY=int(event.y/wysokoscPostaci)
        if self._getZawartoscPunktu(x=posX,y=posY)==None:
            self.setPunktDlaNowegoOrganizmu(posX,posY)
            self.bind_all("<Button-3>",self._wstawOrganizm)



    def setPunktDlaNowegoOrganizmu(self,x,y):
        self._punktDlaNowegoOrganizmu=(x,y)

    def _wstawOrganizm(self,event):
       id=int((event.x/szerokoscPostaci)+1)
       self._dodajOrganizm(id,*self._punktDlaNowegoOrganizmu,niezdefiniowana)
       self.unbind_all("<Button-3>")
       self.delete("all")
       self._rysujPlansze()



    def _getMenuSwiat(self):
        return self._menuSwiata


    def _getPunktDlaNowego(self):
        return self._punktDlaNowegoOrganizmu()


    def _wykonajTure(self,e):
        self.delete("all")
        self._setKierunke(e.keysym)
        liczbaOrganizmow=len(self._kolejkaOrganizmow)
        counter=0
        for org in self._kolejkaOrganizmow:
            org._akcja()
            if counter==liczbaOrganizmow:
                break
            counter+=1
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

    def _dodajCzlowiek(self,sila,x,y,czyAktywna,pozostaleTury):
        tmp=Czlowiek(self,sila,Inicjatywa.Czlowiek.value,Id.Czlowiek.value,x,y,czyAktywna,pozostaleTury)
        self._kolejkaOrganizmow.append(tmp)
        self._plansza[y][x]=tmp
    def _dodajOrganizm(self,id,x,y,sila):
        if id ==Id.Trawa.value:
            self._kolejkaOrganizmow.append(Trawa(self,Sila.Trawa.value,Inicjatywa.Roslina.value,Id.Trawa.value,x,y))


        if id==Id.WilczeJagody.value:
            self._kolejkaOrganizmow.append(WilczeJagody(self,Sila.WilczeJagody.value,Inicjatywa.Roslina.value,Id.WilczeJagody.value,x,y))


        if id==Id.Mlecz.value:
            self._kolejkaOrganizmow.append(Mlecz(self,Sila.Mlecz.value,Inicjatywa.Roslina.value,Id.Mlecz.value,x,y))

        if id==Id.Guarana.value:
            self._kolejkaOrganizmow.append(Guarana(self,Sila.Guarana.value,Inicjatywa.Roslina.value,Id.Guarana.value,x,y))

        if id==Id.BarszczSosnowskiego.value:
            self._kolejkaOrganizmow.append(BarszczSosnowskiego(self,Sila.BarszczSosnowskiego.value,Inicjatywa.Roslina.value,Id.BarszczSosnowskiego.value,x,y))

        if id==Id.Antylopa.value:
            if sila<Sila.Antylopa.value:
                sila=Sila.Antylopa.value
            self._kolejkaOrganizmow.append(Antylopa(self,sila,Inicjatywa.Antylopa.value,Id.Antylopa.value,x,y))

        if id==Id.CyberOwca.value:
            if sila<Sila.CyberOwca.value:
                sila=Sila.CyberOwca.value
            self._kolejkaOrganizmow.append(CyberOwca(self,sila,Inicjatywa.CyberOwca.value,Id.CyberOwca.value,x,y))

        if id==Id.Lis.value:
            if sila<Sila.Lis.value:
                sila=Sila.Lis.value
            self._kolejkaOrganizmow.append(Lis(self,sila,Inicjatywa.Lis.value,Id.Lis.value,x,y))
        if id==Id.Owca.value:
            if sila<Sila.Owca.value:
                sila=Sila.Owca.value
            self._kolejkaOrganizmow.append(Owca(self,sila,Inicjatywa.Owca.value,Id.Owca.value,x,y))
        if id==Id.Wilk.value:
            if sila<Sila.Wilk.value:
                sila=Sila.Wilk.value
            self._kolejkaOrganizmow.append(Wilk(self,sila,Inicjatywa.Lis.value,Id.Lis.value,x,y))
        if id==Id.Zolw.value:
            if sila<Sila.Zolw.value:
                sila=Sila.Zolw.value
            self._kolejkaOrganizmow.append(Zolw(self,sila,Inicjatywa.Zolw.value,Id.Zolw.value,x,y))


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

        if not organizm in self._kolejkaOrganizmow:
            print(1)

        x,y=organizm._getPozycja()
        self._plansza[y][x]=None
        self._kolejkaOrganizmow.remove(organizm)


    def _przesunOrganizm(self,x,y,organizm):

        xPoprzadnie, yPoprzednie=organizm._getPozycja()
        self._plansza[yPoprzednie][xPoprzadnie]=None
        self._plansza[y][x]=organizm
        organizm._setPozycja(x,y)

    def _zapiszGre(self,event):
        zapisGry=open("save.txt",'w')
        for el in self._kolejkaOrganizmow:
            str=el._doZapisu()
            zapisGry.write(str)
        zapisGry.close()






