from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

Builder.load_file("./components/chip_chooser/search_chip/search_chip.kv")


class SearchChip(MDCard, ButtonBehavior):
    pass
