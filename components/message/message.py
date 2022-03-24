from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import RiseInTransition, FallOutTransition
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard, MDSeparator

from components.black_button.black_button import BlackButton
from components.rater.rater import Rater
from components.ticket.ticket import Ticket1
from data import MESSAGES

Builder.load_file("./components/message/message.kv")


class Message(MDCard, ButtonBehavior):
    def __init__(self, code, **kwargs):
        self.code = code
        self.data = MESSAGES[code]

        self.title = self.data["title"]
        self.abstract = self.data["abstract"]
        self.date = self.data["date"]
        self.hour = self.data["hour"]
        self.read = self.data["read"]

        super().__init__(**kwargs)

    def on_release(self):
        MESSAGES[self.code]["read"] = True
        self.read = True
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
            opener.add_widget(MessageOpener(self.code, self.data, self))


class MessageOpener(MDBoxLayout):
    def __init__(self, code, data, current, **kwargs):
        self.code = code
        self.data = data
        self.sender = self.data["sender"]
        self.abstract = self.data["abstract"]
        self.title = self.data["title"]
        self.date = self.data["date"]
        self.hour = self.data["hour"]
        self.body = self.data["body"]
        self.type = self.data["type"]
        self.current = current

        super().__init__(**kwargs)

        if self.type == "rating":
            self.event = "33A-41C-25C"
            self.ids.receiver.add_widget(Rater(self.event))
            self.ids.receiver.add_widget(MDSeparator())
            self.ids.receiver.add_widget(BlackButton(text="envoyer", on_press=lambda x: self.send()))

        elif self.type == "ticket":
            self.ids.receiver.add_widget(Ticket1())

    def send(self):
        rater = self.ids.receiver.children[2].children[1].children[1]
        rate = rater.get_rate()
        comment = self.ids.receiver.children[2].children[0].text

        a = {
            self.event: {
                "rate": rate,
                "comment": comment
            }
        }

        print(a)

        MESSAGES.pop(self.code)

        parent = self.current.parent
        parent.remove_widget(self.current)

    def go_back(self, dt):
        app = MDApp.get_running_app()
        manager = app.root.ids.main_page.ids.tabs_manager

        manager.transition = FallOutTransition()
        manager.current = "MessagesTab"

