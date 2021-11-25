from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

from data import EVENTS

Builder.load_file("./components/box/box.kv")


class Box(MDCard, ButtonBehavior):
    """
    Home Box elements to call in the Home Tab

    *to be called only in python code
    """
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
        self.price = f'{event["tickets"][3]["price"]}'
        self.color = self.color_map[event["color"]]
        self.code = code

        super().__init__(**kwargs)

    def on_release(self):
        print(self.code)
