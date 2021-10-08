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
        
        
        
    def update(self,*dt):
        self.relacion_aspecto.update(SizeTools.set_aspecto(Window.size,25,14))
        print(self.relacion_aspecto)
        