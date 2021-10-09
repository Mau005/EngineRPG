#coding: utf-8
#author: mau

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.animation import Animation
from Core.Coordenadas import Coordenadas

#64x96


class Objeto(Widget,Coordenadas):
    def __init__(self,relacion_aspecto,ruta_sprite,pos,**kargs):
        Widget.__init__(self,**kargs)
        Coordenadas.__init__(self)
        self.size_hint = (None,None)
        self.size = [relacion_aspecto["cuadroX"],relacion_aspecto["cuadroY"]]
        self.pos = pos
        with self.canvas:
            self.bg_rect = Rectangle(source=ruta_sprite, pos=self.pos, size=self.size)
            
            
    
    
    
    def set_sprite(self,ruta_Sprite):
        self.bg.rect.source = ruta_Sprite
        
    def __ajustado(self, pos):
        self.size = (pos["cuadroX"],pos["cuadroY"])
        self.bg_rect.size = (pos["cuadroX"],pos["cuadroY"])
        
    def set_pos(self,pos):
        self.pos = pos
        self.bg_rect.pos = pos
        
        
    def update(self,*dt):
        self.bg_rect.pos = self.pos
        