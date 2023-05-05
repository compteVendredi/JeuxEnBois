# -*- coding: utf-8 -*-


from tkinter import * 
from .constante import *


class FenetreMenu():
    def __init__(self, modeJcJ, modeJcO):
        self.fenetre = Tk()
        self.fenetre.title(TITRE_FENETRE)
        self.frame_jeu = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.frame_jeu.pack(side=LEFT)
        self.frame_texte = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.frame_texte.pack(side=RIGHT)
        
        Label(self.fenetre, text="Choisir un mode de jeu", font=("Arial", 18)).pack(pady=20)
        
        Button(self.fenetre, text="Joueur contre joueur", command=modeJcJ).pack(pady=10)
        
        Button(self.fenetre, text="Joueur contre ordinateur", command=modeJcO).pack(pady=10)
                
                                  
                                  
    def lancerFenetreMenu(self):
        self.fenetre.mainloop()
        
        
    def fermerFenetre(self):
        self.fenetre.destroy()