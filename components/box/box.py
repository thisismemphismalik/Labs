from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

Builder.load_file("./components/box/box.kv")


class Box(MDCard, ButtonBehavior):
    def __init__(self, box_image="./lnx.png", text_one="Lil Nas", text_two="7 500 FCFA", code="12345678", **kwargs):
        super().__init__(**kwargs)

        self.box_image = box_image
        self.text_one = text_one
        self.text_two = text_two
        self.code = code

    def on_release(self):
        app = MDApp.get_running_app()
        toolbar = app.root.ids.main_page.ids.toolbar

        if not toolbar.collide_point(self.last_touch.pos[0], self.last_touch.pos[1]):
            print(self.code)

