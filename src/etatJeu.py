# -*- coding: utf-8 -*-


from .orientationPiece import *
from .etatFenetre import *


class EtatJeu():
    def __init__(self):
        self.etat = EtatFenetre.IDLE
        self.mouvementPossible = []
        self.pieceSelectionnee = None
        self.serieEnCours = False
        self.tourFini = False
        self.tour = OrientationPiece.NORD
        self.nbNord = 0
        self.nbSud = 0       
        self.priseObligatoire = []   