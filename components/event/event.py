from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from data import EVENTS, COLORMAP

Builder.load_file("./components/event/event.kv")


class Event(MDCard, ButtonBehavior):
    def __init__(self, code, **kwargs):

        self.color_map = COLORMAP

        self.code = code
        self.data = EVENTS[self.code]

        self.image = self.data["image"]
        self.name = self.data["name"]
        self.price = f'à partir de {self.data["tickets"][3]["price"]} FCFA'
        self.location = self.data["location"]
        self.date = self.data["date"]
        self.color = self.color_map[self.data["color"]]

        super().__init__(**kwargs)

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)
