from kivy.lang import Builder
from kivymd.effects.stiffscroll import StiffScrollEffect
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from components.list_item.list_item import ListItem

Builder.load_file("./main_page/main_page_tabs/messages_tab/messages_tab.kv")


class MessagesTab(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.license_dialog = None

    def copyright(self, scroller):
        if not - 0.5 < scroller.scroll_y < 1.5:
            if not self.license_dialog:
                self.license_dialog = MDDialog(md_bg_color=[0, 0, 0, 1],
                                               title="[color=#ffffff][size=35]13.[/color][/size]",
                                               text="[color=#ffffff][size=35]from Memphis Laboratories[/color][/size]"
                                                    "\n \n \n[color=#ffffff][size=17]version 1.0[/size][/color]")

            self.license_dialog.open()

    def on_kv_post(self, base_widget):
        for i in range(25):
            self.ids.first_scroll.add_widget(ListItem())

