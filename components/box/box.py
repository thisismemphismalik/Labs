from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

Builder.load_file("./components/box/box.kv")


class Box(MDCard, ButtonBehavior):
    """
    Home Box elements to call in the Home Tab

    *to be called only in python code
    """
    def __init__(self, image, name, price, color, code, **kwargs):

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

        self.image = image
        self.name = name
        self.price = price
        self.color = self.color_map[color]
        self.code = code

        super().__init__(**kwargs)

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)
