from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

from components.box.box import Box

Builder.load_file("./components/treize_tickets/treize_tickets.kv")


class TreizeTickets(MDBoxLayout):
    def __init__(self, header="header", boxes=None, **kwargs):
        super().__init__(**kwargs)

        if boxes is None:
            boxes = [Box() for i in range(13)]
        self.header = header.capitalize()
        self.boxes = boxes

        for item in boxes:
            self.ids.boxes_container.add_widget(item)
