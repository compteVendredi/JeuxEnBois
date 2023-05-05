# -*- coding: utf-8 -*-



from tkinter import messagebox
from .plateau import *
from .pion import *
from enum import Enum
from tkinter import * 
from .pion import *
from .constante import *
from .dame import *



class Etat(Enum):
    IDLE = 0
    SELECTION = 1


class Jeu_dame:

    def __init__(self):
        self.etat = Etat.IDLE
        self.plateau = Plateau(10,10)
        self.mouvementPossible = []
        self.pieceSelectionnee = None
        self.tour = Orientation.NORD
        self.serieEnCours = False
        self.nbNord = 0
        self.nbSud = 0
        self.tourFini = False

        for j in range(0,self.plateau.width,2):
            self.plateau.plateau[0][j+1].contenu = Pion(self.plateau.plateau[0][j+1], Orientation.SUD)
            self.plateau.plateau[1][j].contenu = Pion(self.plateau.plateau[1][j], Orientation.SUD)
            self.nbNord += 2

            self.plateau.plateau[self.plateau.height-2][j+1].contenu = Pion(self.plateau.plateau[self.plateau.height-2][j+1], Orientation.NORD)
            self.plateau.plateau[self.plateau.height-1][j].contenu = Pion(self.plateau.plateau[self.plateau.height-1][j], Orientation.NORD)
            self.nbSud += 2 


        self.fenetre = Tk()
        self.fenetre.title("Jeu de dames")
        self.frame_jeu = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.frame_jeu.pack(side=LEFT)
        self.frame_texte = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.frame_texte.pack(side=RIGHT)

        self.plateauBouton = [[]]

        for i in range(self.plateau.height):
            for j in range(self.plateau.width):
                btn = Button(self.frame_jeu, command=lambda i=i,j=j: self.interaction_grille(i,j)\
                             , bg=COULEUR_DAMIER1 if (j+(i%2))%2 else COULEUR_DAMIER2)
                btn.grid(row=i, column=j)
                self.plateauBouton[i].append(btn)
 
            self.plateauBouton.append([])

        self.etatPartie = Label(self.frame_texte)
        self.etatPartie.pack()
        self.btnFinTour = Button(self.frame_texte, text="Fin tour", command=self.fin_tour)
        self.btnFinTour.pack()

        self.actualiserPlateau()

        self.tourFini = True
        self.fin_tour()


    def actualiserPlateau(self):
        for i in range(self.plateau.height):
            for j in range(self.plateau.width):
                btn = self.plateauBouton[i][j]
                if isinstance(self.plateau.plateau[i][j].contenu, Piece):
                    if self.plateau.plateau[i][j].contenu.orientation == Orientation.NORD:
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
                    
                btn.config(text=texte, fg=couleur, height=2, width=2)        



    def interaction_grille(self, i, j):

        if self.tourFini:
            return
        
        if self.etat == Etat.IDLE:

            if isinstance(self.plateau.plateau[i][j].contenu, Piece) and self.plateau.plateau[i][j].contenu.orientation == self.tour:
                
                self.pieceSelectionnee = self.plateau.plateau[i][j].contenu
                self.mouvementPossible = self.pieceSelectionnee.mouvement_possible()
                for iMvt in self.mouvementPossible:
                    self.plateauBouton[iMvt[0].y][iMvt[0].x].config(text=AFFICHAGE_MOUVEMENT_POSSIBLE, fg=COULEUR_MOUVEMENT_POSSIBLE) 
                if len(self.mouvementPossible) > 0:
                    self.etat = Etat.SELECTION

        elif self.etat == Etat.SELECTION:
            for iMvt in self.mouvementPossible:
                if iMvt[0].y == i and iMvt[0].x == j:
                    self.pieceSelectionnee.se_deplacer(iMvt)
                    if iMvt[1] != None and len(list(filter(lambda x: x[1] != None, self.pieceSelectionnee.mouvement_possible())))>0:
                        self.serieEnCours = True   
                        self.etat = Etat.SELECTION  
                        if self.tour == Orientation.NORD:
                            self.nbSud -= 1
                        else:
                            self.nbNord -= 1
                    else:
                        self.serieEnCours = False
                        self.tourFini = True  
                    break
            self.actualiserPlateau()

            if self.serieEnCours:
                self.mouvementPossible = list(filter(lambda x: x[1] != None, self.pieceSelectionnee.mouvement_possible()))
                for iMvt in self.mouvementPossible:
                    self.plateauBouton[iMvt[0].y][iMvt[0].x].config(text=AFFICHAGE_MOUVEMENT_POSSIBLE, fg=COULEUR_MOUVEMENT_POSSIBLE) 
            else:
                self.etat = Etat.IDLE


    def verifierVictoire(self):
        if self.nbSud == 0:
            messagebox.showinfo("Fin du jeu", "Bravo au nord")
        elif self.nbNord == 0:
            messagebox.showinfo("Fin du jeu", "Bravo au sud")


    def fin_tour(self):
        if(self.tourFini):
            self.tourFini = False
            if self.tour == Orientation.NORD:
                self.tour = Orientation.SUD
                self.etatPartie.config(text="Tour au NORD")
            else:
                self.tour = Orientation.NORD
                self.etatPartie.config(text="Tour au SUD")
        self.verifierVictoire()

    def lancer(self):
        self.fenetre.mainloop()