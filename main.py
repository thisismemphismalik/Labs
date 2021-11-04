from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

Builder.load_file("./main.kv")


class Manager(ScreenManager):
    pass


class Labs(MDApp):
    def build(self):
        Window.size = (350, 600)
        Window.top = 0
        Window.left = 0
        manager = Manager()
        return manager


Labs().run()
