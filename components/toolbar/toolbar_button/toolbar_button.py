from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

Builder.load_file("./components/toolbar/toolbar_button/toolbar_button.kv")


class ToolbarButton(MDIconButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected = False

    def change_screen(self):
        if not self.selected:
            app = MDApp.get_running_app()
            buttons = self.parent.children

            # print("changing")

            for item in buttons:
                item.selected = False
                if "outline" not in item.icon:
                    # print(f"changing {item.icon}")
                    item.icon = f"{item.icon}-outline"
                    item.opacity = .3
                    item.text_color = [1, 1, 1, 1]
            self.icon = self.icon[:~7]
            self.opacity = 1
            self.selected = True

            tabs_manager = app.root.ids.main_page.ids.tabs_manager
            # print(self.tab)
            tabs_manager.current = self.tab

