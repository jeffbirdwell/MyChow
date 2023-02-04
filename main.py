
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

Config.set('graphics', 'resizable', True)
Builder.load_file("MyChow.kv")

class MyChow(App):
    def build(self):
        self.window = FloatLayout()
        return self.window



if __name__=="__main__":
    MyChow().run()