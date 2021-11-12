from kivy.lang import Builder
from kivymd.effects.stiffscroll import StiffScrollEffect
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

from components.event.event import Event
from components.list_item.list_item import ListItem
from data import EVENTS

Builder.load_file("./main_page/main_page_tabs/messages_tab/messages_tab.kv")


class MessagesTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_kv_post(self, base_widget):
        for i in range(25):
            self.ids.first_scroll.add_widget(ListItem())

