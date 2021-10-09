from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from Core.Lista_Objetos import Lista_Objetos
from kivy.core.window import Window
from Core.Tools import SizeTools

from Render.Objeto import Objeto
Builder.load_file("Ventanas/game.kv")

class Game(Screen):
    ventana = ObjectProperty()
    
    def __init__(self,**kargs):
        Screen.__init__(self,**kargs)
        self.name = "game"
        self.relacion_aspecto ={"cuadroX":64,"cuadroY":96}
        self.lista_objetos = Lista_Objetos()
        
        temporalX = self.relacion_aspecto["cuadroX"] /2
        temporalY = self.relacion_aspecto["cuadroY"] / 3
        
        guiaX = 0
        guiaY = 0
        guia = 0
        
        for y in range(0,30):
            for x in range(0,20):
                self.ventana.add_widget(self.lista_objetos.get_objeto(1,self.relacion_aspecto,[guiaX,guiaY]))
                guiaX +=temporalX
                guiaY += temporalY
            guiaX = y*temporalX
            guia = 0
            guia -= y*temporalY
            guiaY = guia
                
        
    def update(self,*dt):
        self.relacion_aspecto.update(SizeTools.set_aspecto(Window.size,25,14))
        