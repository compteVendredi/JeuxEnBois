# -*- coding: utf-8 -*-


import random


class IA_random():
    def __init__(self, plateau, listePiece, campIA):
        self.plateau = plateau
        self.campIA = campIA
        self.listePiece = listePiece
    
    def listeActionPossible(self):
        listePiece = list(filter(lambda x: (not x.estMort) and x.orientation == self.campIA, self.listePiece))
        res = []
        for i in listePiece:
            listeMouvementPossible = i.mouvement_possible()
            for j in listeMouvementPossible:
                res.append((i,j))
        
        return res
    
    
    def jouer(self):
        listeActionPossible = self.listeActionPossible()
        action = random.choice(listeActionPossible)
        action[0].se_deplacer(action[1])