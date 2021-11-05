from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

Builder.load_file("./components/category/category.kv")


class Category(MDCard, ButtonBehavior):
    def __init__(self, box_image="./lnx.png", name="Memphis Malik", events=13,
                 code="abcdefgh", color="red", **kwargs):
        super().__init__(**kwargs)

        self.box_image = box_image
        self.name = name
        self.events = events
        self.color = color
        self.code = code

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)
