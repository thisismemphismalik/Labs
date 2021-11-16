from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("./main_page/main_page_tabs/search_tab/search_tab.kv")


class SearchTab(MDScreen):
    def correction(self, field):
        if field.focused:
            field.hint_text = ""
        else:
            field.hint_text = "    tapez votre recherche"
