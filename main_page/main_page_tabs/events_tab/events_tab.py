from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("./main_page/main_page_tabs/events_tab/events_tab.kv")


class EventsTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        pass