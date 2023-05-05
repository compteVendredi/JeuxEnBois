# -*- coding: utf-8 -*-



from tkinter import messagebox
from .plateau import *
from .pion import *
from tkinter import * 
from .pion import *
from .constante import *
from .dame import *
from .fenetreJeu import *
from .gestionGrille import *
from .etatFenetre import *
from .etatJeu import *
from .fenetreMenu import *


class GestionJeu:

    def __init__(self):
        self.fenetre = FenetreMenu(self.modeJcJ, self.modeJcJ)  


    def modeJcJ(self):
        
        self.fenetre.fermerFenetre()
        
        self.plateau = Plateau(10,10)
        self.etatJeu  = EtatJeu()             

        self.creer_plateau()
        
        self.gestionGrille = GestionGrille(self.plateau, None, self.etatJeu)
        
        self.fenetre = FenetreJeu(self.plateau.height, self.plateau.width, self.gestionGrille.interaction_grille, self.fin_tour)

        self.gestionGrille.setFenetre(self.fenetre)

        self.gestionGrille.actualiserPlateau()

        self.etatJeu.tourFini = True
        self.fin_tour() 
        self.fenetre.lancerFenetreJeu()
        

    def creer_plateau(self):
        for j in range(0,self.plateau.width,2):
            self.plateau.plateau[0][j+1].contenu = Pion(self.plateau.plateau[0][j+1], OrientationPiece.SUD)
            self.plateau.plateau[1][j].contenu = Pion(self.plateau.plateau[1][j], OrientationPiece.SUD)
            self.etatJeu.nbNord += 2

            self.plateau.plateau[self.plateau.height-2][j+1].contenu = Pion(self.plateau.plateau[self.plateau.height-2][j+1], OrientationPiece.NORD)
            self.plateau.plateau[self.plateau.height-1][j].contenu = Pion(self.plateau.plateau[self.plateau.height-1][j], OrientationPiece.NORD)
            self.etatJeu.nbSud += 2 





    def verifierVictoire(self):
        if self.etatJeu.nbSud == 0:
            messagebox.showinfo("Fin du jeu", "Bravo au nord")
        elif self.etatJeu.nbNord == 0:
            messagebox.showinfo("Fin du jeu", "Bravo au sud")


    def fin_tour(self):
        if(self.etatJeu.tourFini):
            self.etatJeu.tourFini = False
            if self.etatJeu.tour == OrientationPiece.NORD:
                self.etatJeu.tour = OrientationPiece.SUD
                self.fenetre.setEtatPartie("Tour au NORD")
            else:
                self.etatJeu.tour = OrientationPiece.NORD
                self.fenetre.setEtatPartie("Tour au SUD")
        self.verifierVictoire()


    def lancer(self):
        self.fenetre.lancerFenetreMenu()