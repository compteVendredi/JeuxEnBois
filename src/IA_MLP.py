# -*- coding: utf-8 -*-


import random


class IA_MLP():
    def __init__(self, plateau, listePiece, campIA):
        self.plateau = plateau
        self.campIA = campIA
        self.listePiece = listePiece
    
    
    def calculerScore(self, piece, mouvement):
        if mouvement[1] != None:
            return 10
        else:
            anciennePos = piece.location
            piece.se_deplacer(mouvement)
            listePieceEnnemie = list(filter(lambda x: (not x.estMort) and x.orientation != self.campIA, self.listePiece))
            for i in listePieceEnnemie:
                listeMouvementEnnemiPossible = i.mouvement_possible()
                for j in listeMouvementEnnemiPossible:
                    if j[1] != None and j[1] == piece:
                        piece.location.contenu = None
                        piece.location = anciennePos
                        anciennePos.contenu = piece
                        return -10 
            piece.location.contenu = None  
            piece.location = anciennePos  
            anciennePos.contenu = piece            
            return 0
    
    def listeActionPossible(self):
        listePiece = list(filter(lambda x: (not x.estMort) and x.orientation == self.campIA, self.listePiece))
        res = []
        for i in listePiece:
            listeMouvementPossible = i.mouvement_possible()
            for j in listeMouvementPossible:
                score = self.calculerScore(i, j)
                res.append((i,j,score))
        
        return res
    
    
    def jouer(self):
        listeActionPossible = self.listeActionPossible()
        #action = random.choice(listeActionPossible)
        action = max(listeActionPossible, key=lambda x: x[2])
        action[0].se_deplacer(action[1])
        serie = action[1]
        while serie[1] != None:
            mouvementRestant = list(map(lambda x: (x,self.calculerScore(action[0],x))\
                , list(filter(lambda x: x[1] != None, action[0].mouvement_possible()))))
            if mouvementRestant != []:
                serie = max(mouvementRestant, key=lambda x: x[1])
                action[0].se_deplacer(serie[0])
            else:
                break
                