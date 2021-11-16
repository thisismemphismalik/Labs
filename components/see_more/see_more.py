from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

Builder.load_file("./components/see_more/see_more.kv")


class SeeMore(MDCard, ButtonBehavior):
    pass
