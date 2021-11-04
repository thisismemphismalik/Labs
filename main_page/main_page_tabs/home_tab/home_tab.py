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
        self.ids.first_scroll.add_widget(TreizeTickets(header="tendances"))
        self.ids.first_scroll.add_widget(TreizeTickets(header="cette semaine"))
        self.ids.first_scroll.add_widget(TreizeTickets(header="abordables"))

    @staticmethod
    def change_screen():
        app = MDApp.get_running_app()
        tabs_manager = app.root.ids.main_page.ids.tabs_manager
        buttons = app.root.ids.main_page.ids.toolbar.children[0].children

        for item in buttons:
            item.selected = False
            if "outline" not in item.icon:
                item.icon = f"{item.icon}-outline"

        ticket_button = buttons[2]

        ticket_button.icon = ticket_button.icon[:~7]
        ticket_button.selected = True

        tabs_manager.current = ticket_button.tab
