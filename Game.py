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
        self.relacion_aspecto ={"cuadroX":64*1.2,"cuadroY":96*1.2}
        self.lista_objetos = Lista_Objetos()
        self.escena = []
        self.__perspective("isometricx64")
        

    def __perspective(self,perspectiva):
        if perspectiva == "isometricx64":
            temporalX = self.relacion_aspecto["cuadroX"] /2
            temporalY = self.relacion_aspecto["cuadroY"] / 3
            
            guiaX = 0
            guiaY = 0
            guia = 0
            
            for y in range(-5,30):
                for x in range(-5,30):
                    obj = self.lista_objetos.get_objeto(1,self.relacion_aspecto,[guiaX,guiaY])
                    self.ventana.add_widget(obj)
                    self.escena.append(obj)
                    guiaX +=temporalX
                    guiaY += temporalY
                guiaX = y*temporalX
                guia = 0
                guia -= y*temporalY
                guiaY = guia
                
        
    def update(self,*dt):
        self.relacion_aspecto.update(SizeTools.set_aspecto(Window.size,25,14))
        