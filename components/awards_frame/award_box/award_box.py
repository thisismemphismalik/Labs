from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

Builder.load_file("./components/awards_frame/award_box/award_box.kv")


class AwardBox(MDCard, MDTabsBase, ButtonBehavior):
    pass
