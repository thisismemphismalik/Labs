import random

from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from data import CATEGORIES, EVENTS

Builder.load_file("./components/category/category.kv")


class Category(MDCard, ButtonBehavior):
    """
    Category Box to call in the Events Tab

    *to be called only in python code
    """
    def __init__(self, code, **kwargs):
        category = CATEGORIES[code]
        self.color_map = {
            "black": [0, 0, 0, .3],
            "blue": [0, 0, 1, .3],
            "green": [0, 1, 0, .3],
            "red": [1, 0, 0, .3],
            "sky-blue": [0, 1, 1, .3],
            "violet": [1, 0, 1, .3],
            "yellow": [1, 1, 0, .3],
            "white": [1, 1, 1, .3]
        }
        elements = [i for i in category["elements"].keys()]
        elements = [random.choice(elements) for i in range(4)]
        self.images = [EVENTS[i]["image"] for i in elements]

        self.name = category["name"]
        self.events = f'{category["events"]} Events'
        self.color = self.color_map[EVENTS[random.choice(elements)]["color"]]
        self.code = code

        super().__init__(**kwargs)

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)
