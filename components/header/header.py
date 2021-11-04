from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("./components/header/header.kv")


class Header(MDFloatLayout):
    pass
