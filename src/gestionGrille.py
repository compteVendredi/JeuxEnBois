# -*- coding: utf-8 -*-

from .plateau import *
from .pion import *
from tkinter import * 
from .pion import *
from .constante import *
from .dame import *
from .fenetreJeu import *
from .etatFenetre import *



class GestionGrille():
    def __init__(self, plateau, fenetre, etatJeu, listePiece):
        self.plateau = plateau
        self.fenetre = fenetre
        self.etatJeu = etatJeu
        self.listePiece = listePiece
    
    
    def setFenetre(self, fenetre):
        self.fenetre = fenetre
        
    
    def piecesObligatoire(self):
        piecesAJouer = []
        for i in list(filter(lambda x: (not x.estMort) and x.orientation != self.etatJeu.tour, self.listePiece)):
            listeMouvementPossible = i.mouvement_possible()
            for j in listeMouvementPossible:
                if j[1] != None:
                    piecesAJouer += [i]
        return piecesAJouer
    
    def interaction_grille(self, i, j):

        if self.etatJeu.tourFini:
            return
        
        if self.etatJeu.etat == EtatFenetre.IDLE:

            if isinstance(self.plateau.plateau[i][j].contenu, Piece) and self.plateau.plateau[i][j].contenu.orientation == self.etatJeu.tour \
                and self.etatJeu.priseObligatoire == [] \
                    or self.etatJeu.priseObligatoire != [] and self.plateau.plateau[i][j].contenu in self.etatJeu.priseObligatoire:
                
                self.etatJeu.pieceSelectionnee = self.plateau.plateau[i][j].contenu
                self.etatJeu.mouvementPossible = self.etatJeu.pieceSelectionnee.mouvement_possible()
                for iMvt in self.etatJeu.mouvementPossible:
                    self.fenetre.setPlateauBouton(iMvt[0].y,iMvt[0].x,AFFICHAGE_MOUVEMENT_POSSIBLE, COULEUR_MOUVEMENT_POSSIBLE) 
                if len(self.etatJeu.mouvementPossible) > 0:
                    self.etatJeu.etat = EtatFenetre.SELECTION

        elif self.etatJeu.etat == EtatFenetre.SELECTION:
            for iMvt in self.etatJeu.mouvementPossible:
                if iMvt[0].y == i and iMvt[0].x == j:
                    self.etatJeu.pieceSelectionnee.se_deplacer(iMvt)
                    self.etatJeu.priseObligatoire = self.piecesObligatoire()
                    if iMvt[1] != None and len(list(filter(lambda x: x[1] != None, self.etatJeu.pieceSelectionnee.mouvement_possible())))>0:
                        self.etatJeu.serieEnCours = True   
                        self.etatJeu.etat = EtatFenetre.SELECTION  
                        if self.etatJeu.tour == OrientationPiece.NORD:
                            self.etatJeu.nbSud -= 1
                        else:
                            self.etatJeu.nbNord -= 1
                    else:
                        self.etatJeu.serieEnCours = False
                        self.etatJeu.tourFini = True  
                    break
            self.actualiserPlateau()

            if self.etatJeu.serieEnCours:
                self.etatJeu.mouvementPossible = self.etatJeu.pieceSelectionnee.mouvement_possible()
                for iMvt in self.etatJeu.mouvementPossible:
                    self.fenetre.setPlateauBouton(iMvt[0].y,iMvt[0].x,AFFICHAGE_MOUVEMENT_POSSIBLE, COULEUR_MOUVEMENT_POSSIBLE) 
            else:
                self.etatJeu.etat = EtatFenetre.IDLE


    def actualiserPlateau(self):
            for i in range(self.plateau.height):
                for j in range(self.plateau.width):
                    if isinstance(self.plateau.plateau[i][j].contenu, Piece):
                        if self.plateau.plateau[i][j].contenu.orientation == OrientationPiece.NORD:
                            couleur = COULEUR_SUD
                        else:
                            couleur = COULEUR_NORD    

                        if isinstance(self.plateau.plateau[i][j].contenu, Pion):
                            texte = AFFICHAGE_PION
                        else:
                            texte = AFFICHAGE_DAME
                    else:
                        texte = AFFICHAGE_VIDE
                        couleur = COULEUR_DEFAUT
                        
                    self.fenetre.setPlateauBouton(i,j,texte,couleur)    