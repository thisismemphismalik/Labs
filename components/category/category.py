from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

Builder.load_file("./components/category/category.kv")


class Category(MDCard, ButtonBehavior):
    def __init__(self, box_image="./lnx.png", name="Memphis Malik", events=13,
                 code="abcdefgh", color="red", **kwargs):
        super().__init__(**kwargs)

        self.color_map = {
            "black": [0,0,0,.3],
            "blue": [0,0,1,.3],
            "green": [0,1,0,.3],
            "red": [1,0,0,.3],
            "sky-blue": [0,1,1,.3],
            "violet": [1,0,1,.3],
            "yellow": [1,1,0,.3],
            "white": [1,1,1,.3]
        }

        self.box_image = box_image
        self.name = name
        self.events = events
        self.color = self.color_map[color]
        self.code = code

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)
