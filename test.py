from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.button import Button
class testapp(App):
 def build(self):
  self.layout=FloatLayout()
  self.button=Button(text='move',size_hint=(0.2,0.1),pos_hint={'x':0.4,'y':0},on_press=self.animation)
  self.layout.add_widget(self.button)
  return self.layout
 #---------animation function
 def animation(self,*args):
  ani=Animation(pos_hint={'x':0.4,'y':0.7})
  ani.start(self.button)
testapp().run()