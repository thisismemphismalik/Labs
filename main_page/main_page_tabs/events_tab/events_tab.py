from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

from components.category.category import Category
from components.event.event import Event
from components.treize_tickets.treize_tickets import TreizeTickets
from data import CATEGORIES, EVENTS

Builder.load_file("./main_page/main_page_tabs/events_tab/events_tab.kv")


class EventsTab(MDScreen):

    def __init__(self, **kw):
        self.add_counter = 0
        self.add_limit = 5
        self.license_dialog = None
        self.license_dialog_opened = False

        super().__init__(**kw)

    def on_kv_post(self, base_widget):
        # add categories_frame
        boxes = []
        categories = [i for i in CATEGORIES.keys()]

        for i in categories:

            cat = CATEGORIES[i]
            elements = [i for i in cat["elements"].keys()][:4]
            elements = [EVENTS[i] for i in elements]

            category = Category(code=i)
            boxes.append(category)

        self.ids.first_scroll.add_widget(
            TreizeTickets(
                header="catégories",
                boxes=boxes
            )
        )

        # add first 13 events
        self.see_more(13, True)

    def see_more(self, quantity, first):

        number_children = len(self.ids.second_scroll.children) - 1

        events = [i for i in EVENTS.keys()][number_children:number_children+quantity]

        for i in events:
            self.ids.second_scroll.add_widget(Event(code=i))

        first_child = self.ids.second_scroll.children[quantity - 1]

        if self.add_counter >= self.add_limit:

            see_more = self.ids.see_more

            self.ids.all_container.remove_widget(see_more)

        if not first:
            Clock.schedule_once(lambda *dt: self.ids.scroller.scroll_to(first_child), 1)

        self.add_counter += 1

    def change_screen(self):
        app = MDApp.get_running_app()
        buttons = app.root.ids.main_page.ids.toolbar.children[0].children

        for item in buttons:
            item.selected = False
            if "outline" not in item.icon:
                item.icon = f"{item.icon}-outline"
                item.opacity = .3

        ticket_button = buttons[1]

        ticket_button.icon = ticket_button.icon[:~7]
        ticket_button.opacity = 1
        ticket_button.selected = True
        Clock.schedule_once(self.switch, .20)

    @staticmethod
    def switch(dt):
        app = MDApp.get_running_app()
        tabs_manager = app.root.ids.main_page.ids.tabs_manager
        buttons = app.root.ids.main_page.ids.toolbar.children[0].children
        ticket_button = buttons[1]
        tabs_manager.current = ticket_button.tab

    def close_it(self):
        self.license_dialog_opened = False

    def copyright(self, scroller):
        a = 0.07
        a = a/self.add_counter

        if not - a < scroller.scroll_y < 1.00 + a:
            if not self.license_dialog:
                self.license_dialog = MDDialog(md_bg_color=[0, 0, 0, 1],
                                               title="[color=#ffffff][size=35]13.[/color][/size]",
                                               text="[color=#ffffff][size=35]from Memphis Laboratories[/color][/size]"
                                                    "\n \n \n[color=#ffffff][size=17]version 1.0[/size][/color]",
                                               on_pre_dismiss=lambda x: self.close_it(),)

            if not self.license_dialog_opened:
                self.license_dialog.open()
                self.license_dialog_opened = True
