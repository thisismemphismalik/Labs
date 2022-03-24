from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from components.message.message import Message
from data import MESSAGES

Builder.load_file("./main_page/main_page_tabs/messages_tab/messages_tab.kv")


class MessagesTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        Clock.schedule_interval(self.check, 1)

    def on_kv_post(self, base_widget):
        for i in [j for j in MESSAGES.keys()]:
            a = Message(i)

            if a.read:
                self.ids.read.add_widget(a)
            else:
                self.ids.unread.add_widget(a)

    def check(self, dt):
        messages = self.ids.unread.children

        for i in messages:
            print(i.read)
            if i.read:
                a = i
                self.ids.unread.remove_widget(a)
                self.ids.read.add_widget(a)
