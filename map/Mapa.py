#coding: utf-8
#author: mau

class Mapa():
    
    def __init__(self):
        
        self.mapa = [[None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None,None,None,None],]
        
        
    def get_pos(self,x,y):
        return self.mapa[x][y]
    
    def set_pos(self,x,y,valor):
        self.mapa[x][y] = valor