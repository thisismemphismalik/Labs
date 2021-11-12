from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from components.category.category import Category
from components.event.event import Event
from components.treize_tickets.treize_tickets import TreizeTickets

Builder.load_file("./main_page/main_page_tabs/events_tab/events_tab.kv")


class EventsTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        pass

    def on_kv_post(self, base_widget):
        self.ids.first_scroll.add_widget(
            TreizeTickets(
                header="catégories",
                boxes=[Category(color="blue",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="yellow",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="red",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="violet",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="green",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="sky-blue",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="black",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       Category(color="white",name="name",
                                events=113,code="00000",
                                images=["./hie.jpg",
                                        "./lnx.png",
                                        "./vin.jpg",
                                        "./mem.jpg"]),
                       ]
            )
        )

        # pass
