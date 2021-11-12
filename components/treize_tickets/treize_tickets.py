from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("./components/treize_tickets/treize_tickets.kv")


class TreizeTickets(MDBoxLayout):
    def __init__(self, header, boxes, **kwargs):
        self.header = header.capitalize()
        self.boxes = boxes

        super().__init__(**kwargs)

        for item in boxes:
            self.ids.boxes_container.add_widget(item)
