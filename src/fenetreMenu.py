# -*- coding: utf-8 -*-


from tkinter import * 
from .constante import *


class FenetreMenu():
    def __init__(self, jouer):
        self.fenetre = Tk()
        self.fenetre.title(TITRE_FENETRE)
        self.fenetre.grid()
        self.label_mode = Label(self.fenetre, text="Choisissez le mode de jeu :")
        self.label_mode.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.var_mode = StringVar()
        self.radio_jcj = Radiobutton(self.fenetre, text="Joueur contre joueur", variable=self.var_mode, value="JcJ")
        self.radio_jcj.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.radio_jco = Radiobutton(self.fenetre, text="Joueur contre ordinateur", variable=self.var_mode, value="JcO")
        self.radio_jco.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.label_ia = Label(self.fenetre, text="Choisissez l'IA :")
        self.label_ia.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.var_ia = StringVar()
        self.radio_ia1 = Radiobutton(self.fenetre, text="IA BFS (traditionnel)", variable=self.var_ia, value="IA_BFS")
        self.radio_ia1.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        self.radio_ia2 = Radiobutton(self.fenetre, text="IA MLP (réseau de neurones)", variable=self.var_ia, value="IA_MLP")
        self.radio_ia2.grid(row=5, column=0, padx=20, pady=5, sticky="w")
        self.button_jouer = Button(self.fenetre, text="Jouer", command=lambda var_mode=self.var_mode,var_ia=self.var_ia: jouer(var_mode, var_ia))
        self.button_jouer.grid(row=6, column=0, padx=5, pady=5, sticky="w")

                
                                  
                                  
    def lancerFenetreMenu(self):
        self.fenetre.mainloop()
        
        
    def fermerFenetre(self):
        self.fenetre.destroy()