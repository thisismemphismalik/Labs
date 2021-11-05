from kivy.lang import Builder
from kivymd.effects.stiffscroll import StiffScrollEffect
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from components.list_item.list_item import ListItem

Builder.load_file("./main_page/main_page_tabs/messages_tab/messages_tab.kv")


class MessagesTab(MDScreen):

    def on_kv_post(self, base_widget):
        for i in range(25):
            self.ids.first_scroll.add_widget(ListItem())

