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
        # self.opacity = 0
        app = MDApp.get_running_app()
        manager = app.root.ids.main_page.ids.tabs_manager

        opener = manager.get_screen("OpenerTab")

        opener.clear_widgets()

        global backward
        backward = manager.current

        manager.current = "OpenerTab"

        opener.add_widget(BoxOpener(self.code))  # "33A-41C-25C"


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
        self.add_tickets(self.tickets)

    def add_tickets(self, tickets):
        print(tickets)
        ids = [i for i in tickets.keys()]
        print(len(ids))

        self.ids.tickets.add_widget(MDBoxLayout(size_hint=[1, None], height=10))

        for j in ids:
            print(tickets[j])
            self.ids.tickets.add_widget(MDSeparator())
            self.ids.tickets.add_widget(Ticket(tickets[j]))
        self.ids.tickets.add_widget(MDSeparator())

        if len(ids) < 5:
            self.ids.box_image.height += 163 - ((len(ids) - 1) * 41)

    def go_back(self):
        app = MDApp.get_running_app()
        manager = app.root.ids.main_page.ids.tabs_manager

        self.clear_widgets()

        global backward
        manager.current = backward


class Ticket(MDBoxLayout):
    def __init__(self, info, **kwargs):
        self.info = info
        self.name = info["name"]
        self.price = info["price"]
        self.quantity = info["quantity"]
        super().__init__(**kwargs)
        print(self.info)

    def modify(self, but):
        qt = self.ids.quantity
        if but.icon == "minus" and int(qt.text) > 0:
            qt.text = str(int(qt.text) - 1)

        elif but.icon == "plus" and int(qt.text) < self.quantity:
            qt.text = str(int(qt.text) + 1)
