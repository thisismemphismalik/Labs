from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("./components/list_item/list_item.kv")


class ListItem(MDCard, ButtonBehavior):
    def __init__(self, title="Recption de tickets", subject="Issa Doumbia vous a offert un ticket", date="12 mai",
                 code="87654321", **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.subject = subject
        self.date = date
        self.code = code

    def on_release(self):
        print(self.code)
