from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

from data import MESSAGES

Builder.load_file("./components/list_item/list_item.kv")


class ListItem(MDCard, ButtonBehavior):
    def __init__(self, code, **kwargs):
        message = MESSAGES[code]
        self.title = message["title"]
        self.subject = message["subject"]
        self.date = message["date"]
        self.code = code

        super().__init__(**kwargs)

    def on_release(self):
        MESSAGES[self.code]["read"] = True
