# -*- coding: utf-8 -*-


from .case import *


class Plateau:
    def __init__(self, height, width):
        self.plateau = [[]]
        self.height = height
        self.width = width

        for i in range(height):
            for j in range(width):
                self.plateau[i].append(Case(i, j, self))
            self.plateau.append([])


    def get_plateau(self):
        return self.plateau
    

    def coord_valide(self, y, x):
        if y >= 0 and x >= 0 and y < self.height and x < self.width:
            return True
        else:
            return False
