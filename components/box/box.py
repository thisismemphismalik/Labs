from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import FallOutTransition, RiseInTransition
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard, MDSeparator

from data import EVENTS, COLORMAP

Builder.load_file("./components/box/box.kv")


class Box(MDCard, ButtonBehavior):
    """
    Home Box elements to call in the Home Tab

    *to be called only in python code
    """

    def __init__(self, code, **kwargs):
        self.code = code
        self.data = EVENTS[code]

        self.image = self.data["image"]
        self.name = self.data["name"]
        self.price = f'{self.data["tickets"][3]["price"]}'
        self.color = COLORMAP[self.data["color"]]

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
            opener.add_widget(BoxOpener(self.code, self.data, current))  # "33A-41C-25C"


class BoxOpener(MDBoxLayout):
    view = 1

    def __init__(self, code, data, backward, **kwargs):
        self.code = code
        self.data = data
        self.backward = backward

        self.name = self.data["name"]
        self.image = self.data["image"]
        self.category = self.data["category"]
        self.about = self.data["about"]
        self.location = self.data["location"]
        self.date = self.data["date"]
        self.hour = self.data["hour"]
        self.tickets = self.data["tickets"]
        self.infos = f"{self.location}\n \n le    {self.date}    à    {self.hour}\n \n {self.code}"

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
            self.ids.tickets.add_widget(Ticket(tickets[j], self.backward))
        self.ids.tickets.add_widget(MDSeparator())

        self.ids.tickets.add_widget(MDBoxLayout(size_hint=[1, None], height=10))

        if len(ids) < 5:
            self.ids.box_image.height += 163 - ((len(ids) - 1) * 41)

    def go_back(self, dt):
        app = MDApp.get_running_app()
        if self.backward != "OpenerTab":
            manager = app.root.ids.main_page.ids.tabs_manager
            manager.transition = FallOutTransition()
            manager.current = self.backward

    def info(self):
        header = self.ids.header
        info_box_1 = self.ids.info_box_1
        info_box_2 = self.ids.info_box_2

        if self.view == 1:
            header.opacity = 0
            self.ids.back.disabled = True

            info_box_1.opacity = 1
            self.view = 2

        elif self.view == 2:
            info_box_1.opacity = 0
            info_box_2.opacity = 1
            self.view = 3
        else:
            info_box_2.opacity = 0
            header.opacity = 1
            self.ids.back.disabled = False
            self.view = 1

    def buy(self):
        print(self.ids.totals.text)


class Ticket(MDBoxLayout):
    def __init__(self, info, back, **kwargs):
        self.backward = back
        self.info = info
        self.name = info["name"]
        self.price = info["price"]
        self.quantity = info["quantity"]
        super().__init__(**kwargs)
        # print(self.info)
        # print(self.parent)

    def modify(self, but):
        qt = self.ids.quantity
        if but.icon == "minus" and int(qt.text) > 0:
            qt.text = str(int(qt.text) - 1)
            self.check_total("-", self.price)

        elif but.icon == "plus" and int(qt.text) < self.quantity:
            qt.text = str(int(qt.text) + 1)
            self.check_total("+", self.price)

    def check_total(self, sign, value):
        app = MDApp.get_running_app()
        opener = None
        if self.backward != "OpenerTab":
            opener = app.root.ids.main_page.ids.tabs_manager.get_screen("OpenerTab")
            opener = opener.ids.opener_manager.get_screen("TabOne")
        res = None

        total = opener.children[0].ids.totals

        # total corrector
        old = self.value_decoder(total.text)

        # value corrector
        val = self.value_decoder(value)
        if sign == "-":
            res = old - val
        if sign == "+":
            res = old + val

        total.text = self.value_encoder(res)

    def value_decoder(self, value):
        a = value.split(" ")
        if "FCFA" in a:
            a.pop(~0)

        b = ""
        for i in a:
            b = b + i

        b = int(b)

        return b

    def value_encoder(self, value):
        b = []
        c = []
        d = ""

        if type(value) == int:
            a = str(value)

            for i in range(len(a)//3):
                e = a[~2:]
                a = a[:~2]
                b.append(e)

            if len(a) > 0:
                b.append(a)

            for i in range(len(b)):
                c.append(b[~i])

            for i in c:
                d = d + f"{i} "

            d = d + "FCFA"

        return d

