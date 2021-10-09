#coding: utf-8
#author: mau

import kivy

from Core.Lista_Objetos import Lista_Objetos

kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from Game import Game

class Space(App):
    
    def __init__(self,**kargs):
        App.__init__(self,**kargs)
        self.manejador = ScreenManager()
        self.game = Game()
        self.asignar_ventanas()
        
    def asignar_ventanas(self):
        self.manejador.add_widget(self.game)
        
    def update(self,*dt):
        
        self.game.update(dt)
        
    def build(self):
        Clock.schedule_interval(self.update,(1/60))
        return self.manejador

    
if __name__ == '__main__':
    Space().run()