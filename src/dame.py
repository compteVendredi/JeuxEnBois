# -*- coding: utf-8 -*-


from .piece import *
from .exception import *


class Dame(Piece):
    def __init__(self, location, orientation):
        super().__init__(location)
        self.orientation = orientation


    def se_deplacer(self, mouvement):
        if(mouvement[0].contenu != None):
            raise CaseOccupeeException("La case de destination contient déjà une pièce.")

        super().se_deplacer(mouvement)


    def mouvement_possible(self):
        res = []
        mouvement_theorique = [(-1,-1),(-1,1),(1,-1),(1,1)]
        terminaison =         [False, False, False, False]

        k = 1
        while not(terminaison[0] and terminaison[1] and terminaison[2] and terminaison[3]):
            for indice in range(len(mouvement_theorique)):
                if terminaison[indice]:
                    continue
                (i,j) = mouvement_theorique[indice]
                destY = self.location.y+i*k
                destX = self.location.x+j*k
                

                if self.location.plateau.coord_valide(destY, destX):
                    if self.location.plateau.plateau[destY][destX].contenu == None:
                        res.append((self.location.plateau.plateau[destY][destX], None))
                    elif self.location.plateau.plateau[destY][destX].contenu.orientation != self.orientation:
                        if self.location.plateau.coord_valide(destY+i, destX+j) and self.location.plateau.plateau[destY+i][destX+j].contenu == None:
                            res.append((self.location.plateau.plateau[destY+i][destX+j], self.location.plateau.plateau[destY][destX].contenu))
                            terminaison[indice] = True  
                    else:
                        terminaison[indice] = True
                else:
                    terminaison[indice] = True                              
            k += 1

        return res    