from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("./components/header/header.kv")


class Header(MDFloatLayout):
    def __init__(self, current_page="current_tab", **kwargs):
        super().__init__(**kwargs)

        self.current_tab = current_page
