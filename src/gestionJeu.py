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
from .IA_BFS import *
from .typeJeu import *
from .IA_MLP import *


class GestionJeu:

    def __init__(self):
        self.fenetre = FenetreMenu(self.jouer)  
        self.IA = None
        self.joueContreIA = False
        self.campIA = OrientationPiece.NORD
        self.listePiece = []
        self.typeJeu = TypeJeu.DAME   
        self.plateau = None
        self.etatJeu = None  
        
    
    def relancer(self):
        self.__init__()            
    

    def modeGenerique(self):
        self.fenetre.fermerFenetre()
        
        self.plateau = Plateau(10,10)
        self.etatJeu  = EtatJeu()  

        self.creer_plateau()
    
        self.gestionGrille = GestionGrille(self.plateau, None, self.etatJeu, self.listePiece, self.actualiserStatutJeu)
        
        self.fenetre = FenetreJeu(self.plateau.height, self.plateau.width, self.gestionGrille.interaction_grille, self.fin_tour)

        self.gestionGrille.setFenetre(self.fenetre)

        self.gestionGrille.actualiserPlateau()

        self.etatJeu.tourFini = False
        self.changement_joueur() 
        self.actualiserStatutJeu()
        self.fenetre.lancerFenetreJeu()   


    def jouer(self, modeJeu, modeIA):
        if modeJeu.get() == "JcJ":
            self.modeJcJ()
        elif modeJeu.get() == "JcO":
            if modeIA.get() == "IA_BFS":
                self.IA = IA_BFS(self.plateau, self.listePiece, self.campIA)
                self.modeJcO()
            elif modeIA.get() == "IA_MLP":
                self.IA = IA_MLP(self.plateau, self.listePiece, self.campIA)
                self.modeJcO()

    def modeJcJ(self):
        self.modeGenerique()
        
        
    def modeJcO(self):
        self.joueContreIA = True
        self.modeGenerique()     
        

    def creer_plateau(self):
        for j in range(0,self.plateau.width,2):
            for i in range(0, self.plateau.height, 1):
                camp = None
                if i < 4:
                    self.etatJeu.nbNord += 1
                    camp = OrientationPiece.SUD
                elif i > 5:
                    self.etatJeu.nbSud += 1 
                    camp = OrientationPiece.NORD
                else:
                    continue
                self.plateau.plateau[i][j+1-i%2].contenu = Pion(self.plateau.plateau[i][j+1-i%2], camp)
                self.listePiece += [self.plateau.plateau[i][j+1-i%2].contenu]
                                      





    def verifierVictoire(self):
        if self.etatJeu.nbSud == 0:
            messagebox.showinfo("Fin du jeu", "Bravo au nord")
            return True
        elif self.etatJeu.nbNord == 0:
            messagebox.showinfo("Fin du jeu", "Bravo au sud")
            return True
        else:
            return False


    def changement_joueur(self):
        if self.etatJeu.tour == OrientationPiece.NORD:
            self.etatJeu.tour = OrientationPiece.SUD
        else:
            self.etatJeu.tour = OrientationPiece.NORD

    def fin_tour(self):
        if(self.etatJeu.tourFini):
            self.etatJeu.tourFini = False
            self.changement_joueur()
            self.actualiserStatutJeu()                        

            if not(self.verifierVictoire()):
                if self.joueContreIA:
                    self.IA.jouer()
                    self.etatJeu.priseObligatoire = self.gestionGrille.piecesObligatoire()
                    self.gestionGrille.actualiserPlateau()
                    if not(self.verifierVictoire()):
                        self.changement_joueur()
                    self.actualiserStatutJeu()                        
            else:
                self.fenetre.fermerFenetre()
                self.relancer()
                


    def actualiserStatutJeu(self):
        if self.etatJeu.tour == OrientationPiece.NORD:
            texte_tour = "Tour au SUD"
        else:
            texte_tour = "Tour au NORD"
            
        priseObligatoire = "Les pièces obligatoires à jouer sont : \n"
        for i in self.etatJeu.priseObligatoire:
            priseObligatoire += str(chr(ord("A")+i.location.x)) + ";" + str(i.location.y+1) + "  "
            
        serieEnCours = "Serie en cours : " + str(self.etatJeu.serieEnCours)
        
        tourFini = "Tour fini : " + str(self.etatJeu.tourFini)
            
        self.fenetre.setEtatPartie(texte_tour + "\n" + priseObligatoire + "\n" + serieEnCours + "\n" + tourFini)


    def lancer(self):
        self.fenetre.lancerFenetreMenu()