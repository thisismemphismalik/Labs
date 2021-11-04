from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

Builder.load_file("./components/box/box.kv")


class Box(MDCard, ButtonBehavior):
    def __init__(self, box_image=None, text_one=None, text_two=None, code=None, **kwargs):
        super().__init__(**kwargs)

        self.box_image = box_image
        self.text_one = text_one
        self.text_two = text_two
        self.code = code

    def on_release(self):
        print(self.code)
