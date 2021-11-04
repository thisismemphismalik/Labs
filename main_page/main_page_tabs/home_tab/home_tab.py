from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from main_page.main_page_tabs.home_tab.components.treize_tickets.treize_tickets import TreizeTickets

Builder.load_file("./main_page/main_page_tabs/home_tab/home_tab.kv")


class HomeTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.button_added = False

    def on_kv_post(self, base_widget):
        self.ids.first_scroll.add_widget(TreizeTickets(header="Tendances"))
        self.ids.first_scroll.add_widget(TreizeTickets(header="Près de moi"))
        self.ids.first_scroll.add_widget(TreizeTickets(header="Cette semaine"))

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
        Clock.schedule_once(self.switch, .3)

    def switch(self, dt):
        app = MDApp.get_running_app()
        tabs_manager = app.root.ids.main_page.ids.tabs_manager
        buttons = app.root.ids.main_page.ids.toolbar.children[0].children
        ticket_button = buttons[2]
        tabs_manager.current = ticket_button.tab
