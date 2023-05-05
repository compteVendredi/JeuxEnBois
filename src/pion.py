# -*- coding: utf-8 -*-


from .piece import *
from enum import Enum
from .dame import *


class Orientation(Enum):
    NORD = 1
    SUD = 0


class Pion(Piece):
    def __init__(self, location, orientation):
        super().__init__(location)
        self.orientation = orientation


    def se_deplacer(self, mouvement):
        if(mouvement[0].contenu != None):
            raise CaseOccupeeException("La case de destination contient déjà une pièce.")

        super().se_deplacer(mouvement)

        if(self.orientation == Orientation.NORD and self.location.y == 0 \
           or self.orientation == Orientation.SUD and self.location.y == self.location.plateau.height-1):
            self.mourir()
            self.location.contenu = Dame(self.location, self.orientation)


    def mouvement_possible(self):
        res = []
        mouvement_theorique = [(-1,-1),(-1,1),(1,-1),(1,1)]

        for (i,j) in mouvement_theorique:
            destY = self.location.y+i
            destX = self.location.x+j

            if self.location.plateau.coord_valide(destY, destX):
                if self.location.plateau.plateau[destY][destX].contenu == None:
                    if self.orientation == Orientation.NORD and i < 0 or self.orientation == Orientation.SUD and i > 0:
                        res.append((self.location.plateau.plateau[destY][destX], None))
                elif self.location.plateau.plateau[destY][destX].contenu.orientation != self.orientation:
                    if self.location.plateau.coord_valide(destY+i, destX+j) and self.location.plateau.plateau[destY+i][destX+j].contenu == None:
                        res.append((self.location.plateau.plateau[destY+i][destX+j], self.location.plateau.plateau[destY][destX].contenu))                                


        return res       

