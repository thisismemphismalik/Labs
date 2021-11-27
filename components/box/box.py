from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard, MDSeparator

from data import EVENTS

Builder.load_file("./components/box/box.kv")

backward = None


class Box(MDCard, ButtonBehavior):
    """
    Home Box elements to call in the Home Tab

    *to be called only in python code
    """
    def __init__(self, code, **kwargs):
        event = EVENTS[code]
        self.color_map = {
            "black": [0, 0, 0, .3],
            "blue": [0, 0, 1, .3],
            "green": [0, 1, 0, .3],
            "red": [1, 0, 0, .3],
            "sky-blue": [0, 1, 1, .3],
            "violet": [1, 0, 1, .3],
            "yellow": [1, 1, 0, .3],
            "white": [1, 1, 1, .3],
        }

        self.image = event["image"]
        self.name = event["name"]
        self.price = f'{event["tickets"][3]["price"]}'
        self.color = self.color_map[event["color"]]
        self.code = code

        super().__init__(**kwargs)

    def on_release(self):
        self.open()

    def open(self):
        app = MDApp.get_running_app()
        manager = app.root.ids.main_page.ids.tabs_manager

        opener = manager.get_screen("OpenerTab")

        opener.clear_widgets()
        opener.add_widget(BoxOpener(self.code))

        global backward
        backward = manager.current

        manager.current = "OpenerTab"


class BoxOpener(MDBoxLayout):
    def __init__(self, code, **kwargs):
        self.color_map = {
            "black": [0, 0, 0, .3],
            "blue": [0, 0, 1, .3],
            "green": [0, 1, 0, .3],
            "red": [1, 0, 0, .3],
            "sky-blue": [0, 1, 1, .3],
            "violet": [1, 0, 1, .3],
            "yellow": [1, 1, 0, .3],
            "white": [1, 1, 1, .3],
        }

        self.code = code
        self.title = EVENTS[code]["name"]
        self.image = EVENTS[code]["image"]

        self.tickets = EVENTS[code]["tickets"]

        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        for i in [j for j in self.tickets.keys()]:
            self.ids.tickets.add_widget(Ticket())
            self.ids.tickets.add_widget(MDSeparator())

    def go_back(self):
        app = MDApp.get_running_app()
        manager = app.root.ids.main_page.ids.tabs_manager

        self.clear_widgets()

        global backward
        manager.current = backward


class Ticket(MDBoxLayout):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
