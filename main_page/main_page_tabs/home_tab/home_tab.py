import random

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

from components.box.box import Box
from components.treize_tickets.treize_tickets import TreizeTickets
from data import EVENTS

Builder.load_file("./main_page/main_page_tabs/home_tab/home_tab.kv")


class HomeTab(MDScreen):
    def on_kv_post(self, base_widget):
        boxes = []
        events = [i for i in EVENTS.keys()]
        for i in range(13):
            event = random.choice(events)

            box = Box(name=EVENTS[event]["name"],
                      color=EVENTS[event]["color"],
                      code=event,
                      image=EVENTS[event]["image"],
                      price=f'à partir de {EVENTS[event]["tickets"][3]["price"]}')
            boxes.append(box)

        self.ids.first_scroll.add_widget(TreizeTickets("Cette semaine", boxes))

        boxes.clear()
        events = [i for i in EVENTS.keys()]
        for i in range(13):
            event = random.choice(events)

            box = Box(name=EVENTS[event]["name"],
                      color=EVENTS[event]["color"],
                      code=event,
                      image=EVENTS[event]["image"],
                      price=f'à partir de {EVENTS[event]["tickets"][3]["price"]}')
            boxes.append(box)

        self.ids.first_scroll.add_widget(TreizeTickets("Ce mois", boxes))

        boxes.clear()
        events = [i for i in EVENTS.keys()]
        for i in range(13):
            event = random.choice(events)

            box = Box(name=EVENTS[event]["name"],
                      color=EVENTS[event]["color"],
                      code=event,
                      image=EVENTS[event]["image"],
                      price=f'à partir de {EVENTS[event]["tickets"][3]["price"]}')
            boxes.append(box)

        self.ids.first_scroll.add_widget(TreizeTickets("Nos Tendances", boxes))

    def __init__(self, **kw):
        self.button_added = False
        self.license_dialog = None
        self.license_dialog_opened = False

        super().__init__(**kw)

    def change_screen(self):
        app = MDApp.get_running_app()
        buttons = app.root.ids.main_page.ids.toolbar.children[0].children

        for item in buttons:
            item.selected = False
            if "outline" not in item.icon:
                item.icon = f"{item.icon}-outline"

        ticket_button = buttons[2]

        ticket_button.icon = ticket_button.icon[:~7]
        ticket_button.selected = True
        Clock.schedule_once(self.switch, .25)

    def switch(self, dt):
        app = MDApp.get_running_app()
        tabs_manager = app.root.ids.main_page.ids.tabs_manager
        buttons = app.root.ids.main_page.ids.toolbar.children[0].children
        ticket_button = buttons[2]
        tabs_manager.current = ticket_button.tab

    def close_it(self):
        self.license_dialog_opened = False

    def copyright(self, scroller):
        a = 0.5

        if not - a < scroller.scroll_y < 1.00 + a:
            if not self.license_dialog:
                self.license_dialog = MDDialog(md_bg_color=[0, 0, 0, 1],
                                               title="[color=#ffffff][size=35]13.[/color][/size]",
                                               text="[color=#ffffff][size=35]from Memphis Laboratories[/color][/size]"
                                                    "\n \n \n[color=#ffffff][size=17]version 1.0[/size][/color]",
                                               on_pre_dismiss=lambda x: self.close_it(), )

            if not self.license_dialog_opened:
                self.license_dialog.open()
                self.license_dialog_opened = True

    # def on_touch_down(self, touch):
    #     app = MDApp.get_running_app()
    #     toolbar = app.root.ids.main_page.ids.toolbar
    #
    #     if toolbar.collide_point(touch.pos[0], touch.pos[1]):
    #
    #         for x in toolbar.children[0].children:
    #             x.on_touch_down(touch)
    #
    #     else:
    #         for x in self.children:
    #             x.on_touch_down(touch)
    #             for y in x.children:
    #                 y.on_touch_down(touch)
