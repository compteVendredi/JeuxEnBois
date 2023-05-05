# -*- coding: utf-8 -*-


class Case:
    def __init__(self, y, x, plateau):
        self.y = y 
        self.x = x
        self.contenu = None
        self.plateau = plateau


    def get_contenu(self):
        return self.contenu


    def set_contenu(self, contenu):
        self.contenu = contenu
