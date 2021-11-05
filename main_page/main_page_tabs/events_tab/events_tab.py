from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from components.event.event import Event

Builder.load_file("./main_page/main_page_tabs/events_tab/events_tab.kv")


class EventsTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        pass

    def on_kv_post(self, base_widget):
        # for i in range(25):
        #     self.ids.first_scroll.add_widget(Event())

        pass
