from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from components.box.box import Box
from components.category.category import Category
from components.event.event import Event
from components.treize_tickets.treize_tickets import TreizeTickets
from data import CATEGORIES, EVENTS

Builder.load_file("./main_page/main_page_tabs/events_tab/events_tab.kv")


class EventsTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        pass

    def on_kv_post(self, base_widget):
        boxes = []
        categories = [i for i in CATEGORIES.keys()]

        for i in categories:

            cat = CATEGORIES[i]
            elements = [i for i in cat["elements"].keys()][:4]
            elements = [EVENTS[i] for i in elements]

            category = Category(name=cat["name"],
                                events=cat["events"],
                                images=[j["image"] for j in elements],
                                code=i,
                                color=elements[0]["color"]
                                )
            boxes.append(category)

        self.ids.first_scroll.add_widget(
            TreizeTickets(
                header="catégories",
                boxes=boxes
            )
        )

        events = [i for i in EVENTS.keys()][:25]

        for i in events:
            event = EVENTS[i]
            self.ids.first_scroll.add_widget(Event(
                name=event["name"],
                date=event["date"],
                location=event["location"],
                color=event["color"],
                image=event["image"],
                code=i,
                price=f'à partir de {event["tickets"][3]["price"]}',
            ))
