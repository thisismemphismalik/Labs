from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import RiseInTransition
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from components.box.box import BoxOpener
from data import EVENTS, COLORMAP

Builder.load_file("./components/event/event.kv")


class Event(MDCard, ButtonBehavior):
    def __init__(self, code, **kwargs):

        self.color_map = COLORMAP

        self.code = code
        self.data = EVENTS[self.code]

        self.image = self.data["image"]
        self.name = self.data["name"]
        self.price = f'à partir de {self.data["tickets"][3]["price"]} FCFA'
        self.location = self.data["location"]
        self.date = self.data["date"]
        self.color = self.color_map[self.data["color"]]

        super().__init__(**kwargs)

    def on_release(self):
        self.open()

    def open(self):
        app = MDApp.get_running_app()
        current = app.root.ids.main_page.ids.tabs_manager.current

        if current != "OpenerTab":
            print(current)
            opener = app.root.ids.main_page.ids.tabs_manager.get_screen("OpenerTab")
            opener = opener.ids.opener_manager.get_screen("TabOne")
            # print(opener)
            opener.clear_widgets()
            #
            manager = app.root.ids.main_page.ids.tabs_manager
            manager.transition = RiseInTransition()
            manager.current = "OpenerTab"
            #
            opener.add_widget(BoxOpener(self.code, self.data, current))
