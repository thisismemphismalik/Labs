from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

from components.box.box import Box
from components.treize_tickets.treize_tickets import TreizeTickets

Builder.load_file("./main_page/main_page_tabs/home_tab/home_tab.kv")


class HomeTab(MDScreen):
    def on_kv_post(self, base_widget):
        for i in range(15):
            self.ids.first_scroll.add_widget(Box(name="KO", color="black",
                                             code="azerty",box_image="./lnx.png",
                                             price="1425"))
    def __init__(self, **kw):
        super().__init__(**kw)

        self.button_added = False
        self.license_dialog = None

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

    def copyright(self, scroller):
        if not - 0.5 < scroller.scroll_y < 1.5:
            if not self.license_dialog:
                self.license_dialog = MDDialog(md_bg_color=[0, 0, 0, 1],
                                               title="[color=#ffffff][size=35]13.[/color][/size]",
                                               text="[color=#ffffff][size=35]from Memphis Laboratories[/color][/size]"
                                                    "\n \n \n[color=#ffffff][size=17]version 1.0[/size][/color]")

            self.license_dialog.open()
