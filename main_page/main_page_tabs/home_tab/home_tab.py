from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen

from components.box.box import Box
from components.toolbar.toolbar_button.toolbar_button import ToolbarButton
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

        # self.ids.first_scroll.add_widget(MDIconButton(icon="ticket-confirmation-outline"))