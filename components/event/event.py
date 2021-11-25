from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from data import EVENTS

Builder.load_file("./components/event/event.kv")


class Event(MDCard, ButtonBehavior):
    def __init__(self, code, **kwargs):
        event = EVENTS[code]
        self.color_map = {
            "black": [0, 0, 0, .3],
            "blue": [0, 0, 1, .3],
            "green": [0, 1, 0, .3],
            "red": [1, 0, 0, .3],
            "sky-blue": [0, 1, 1, .3],
            "violet": [1, 0, 1, .3],
            "yellow": [1, 1, 0, .3],
            "white": [1, 1, 1, .3],
        }

        self.image = event["image"]
        self.name = event["name"]
        self.price = f'à partir de {event["tickets"][3]["price"]} FCFA'
        self.location = event["location"]
        self.date = event["date"]
        self.color = self.color_map[event["color"]]
        self.code = code

        super().__init__(**kwargs)

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)
