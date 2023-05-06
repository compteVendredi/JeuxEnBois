# -*- coding: utf-8 -*-


from .plateau import *
from .pion import *
from tkinter import * 
from .pion import *
from .constante import *
from .dame import *
from .fenetreJeu import *


class FenetreJeu:
    def __init__(self, plateau_height, plateau_width, comportement_grille, comportement_fin_tour):
        self.fenetre = Tk()
        self.fenetre.geometry(RESOLUTION_FENETRE_JEU)
        self.fenetre.title(TITRE_FENETRE)
        self.frame_jeu = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.frame_jeu.pack(side=LEFT)
        self.frame_texte = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.frame_texte.pack(side=RIGHT)
        
        self.plateauBouton = [[]]
        
        for i in range(1,plateau_height+1):
            Label(self.frame_jeu, text=i).grid(row=i,column=0)
        for i in range(1,plateau_width+1):
            Label(self.frame_jeu, text=chr(ord("A")+i-1)).grid(row=0,column=i)

        for i in range(plateau_height):
            for j in range(plateau_width):
                btn = Button(self.frame_jeu, command=lambda i=i,j=j: comportement_grille(i,j)\
                             , bg=COULEUR_DAMIER1 if (j+(i%2))%2 else COULEUR_DAMIER2)
                btn.grid(row=i+1, column=j+1)
                self.plateauBouton[i].append(btn)
 
            self.plateauBouton.append([]) 
            
            
        self.etatPartie = Text(self.frame_texte)
        self.etatPartie.pack()
        self.btnFinTour = Button(self.frame_texte, text="Fin tour", command=comportement_fin_tour)
        self.btnFinTour.pack()  
        
        
    def setPlateauBouton(self, i, j, texte, couleur, height=2, width=2):
        self.plateauBouton[i][j].config(text=texte, fg=couleur, height=height, width=width) 
        
        
    def setEtatPartie(self, texte):
        self.etatPartie.delete("1.0", END)
        self.etatPartie.insert(END, texte)
                                  
                                  
    def lancerFenetreJeu(self):
        self.fenetre.mainloop()
        
    def fermerFenetre(self):
        self.fenetre.destroy()        