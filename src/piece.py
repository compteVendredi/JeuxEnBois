# -*- coding: utf-8 -*-


from .exception import *


class Piece:
    def __init__(self, location, orientation):
        """
        Instancie une pièce 

        Args:
            location: Contient la location de la pièce (la case) 
        """
        self.location = location
        self.orientation = orientation
        self.estMort = False
        self.serieEnCours = False


    def se_deplacer(self, mouvement):
        """
        Remarque un mouvement se décompose de cette manière : (location, action)
        action qui est en général la pièce qui va se faire manger
        """     
        if(self.estMort):
            raise PieceMorteException("Une pièce morte essaye de se déplacer par elle-même")
        if(mouvement not in self.mouvement_possible()):
            raise MouvementIllegalException("MouvementIllegal.")

        self.location.contenu = None
        self.location = mouvement[0]
        self.location.contenu = self

        if mouvement[1] != None:
            self.serieEnCours = True
            mouvement[1].mourir()


    def mourir(self):
        self.estMort = True
        self.location.contenu = None


    def mouvement_possible(self):
        return []