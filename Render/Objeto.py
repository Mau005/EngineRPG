#coding: utf-8
#author: mau

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.animation import Animation
from Core.Coordenadas import Coordenadas

#64x96


class Objeto(Widget,Coordenadas):
    def __init__(self,ruta_sprite,**kargs):
        Widget.__init__(self,**kargs)
        Coordenadas.__init__(self)
        with self.canvas:
            self.bg_rect = Rectangle(source=ruta_sprite, pos=self.pos, size=self.size)
    
    
    
    def set_sprite(self,ruta_Sprite):
        self.bg.rect.source = ruta_Sprite
        
    def __ajustado(self, pos):
        self.size = (pos["cuadroX"],pos["cuadroY"])
        self.bg_rect.size = (pos["cuadroX"],pos["cuadroY"])
        
        
    def update(self,relacion_aspecto,*dt):
        self.__ajustado(relacion_aspecto)
        