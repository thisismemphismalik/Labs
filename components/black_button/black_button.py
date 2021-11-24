from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

Builder.load_file("./components/black_button/black_button.kv")


class BlackButton(MDCard, ButtonBehavior):
    pass
