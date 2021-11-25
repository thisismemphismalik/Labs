from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from components.svg_image.svg_image import SvgImage
from data import TAGS

Builder.load_file("./main_page/main_page_tabs/search_tab/search_tab.kv")


class SearchTab(MDScreen):
    empty = True
    empty_results_widgets = None
    empty_results_padding = [0, 150, 0, 0]
    empty_results_spacing = 30

    def on_kv_post(self, base_widget):
        self.empty_results_widgets = [SvgImage("SVG.svg"),
                                      MDLabel(theme_text_color="Secondary",
                                      halign="center",
                                      font_style="Subtitle2",
                                      text="les résultats de votre recherche vont apparaître ici")]
        for i in self.empty_results_widgets:
            self.ids.results.add_widget(i)
        self.ids.results.padding = self.empty_results_padding
        self.ids.results.spacing = self.empty_results_spacing
        print("done")

    def correction(self, field):
        if field.focused or field.text != "":
            field.hint_text = ""
        else:
            field.hint_text = "    tapez votre recherche"

        # self.tags_to_find = field.text.split(" ")

    def prepare(self, tags):
        tags_list = list(tags.split(" "))

        empty = tags_list.count("")

        if empty > 0:
            for i in range(empty):
                tags_list.remove("")

        new_text = ""
        for i in tags_list:
            new_text = f"{new_text}{i} "

        self.ids.field.text = new_text

        return tags_list

    def research(self, tags):
        a = self.prepare(tags)
        val = []
        score = {}

        for i in a:
            try:
                val += TAGS[i]
            except KeyError:
                pass

        print(val)

        for i in val:
            a = i
            if i not in [i for i in score.keys()]:
                score[a] = 1
            else:
                score[a] += 1

        sorted_score = [key[0] for key in sorted(score.items(), key=lambda x: x[1], reverse=True)]

        print(sorted_score)
        self.parser(sorted_score)
        return sorted_score

    def parser(self, events):
        results_box = self.ids.results
        if len(events) > 0:
            for i in self.empty_results_widgets:
                print(i)
                results_box.remove_widget(i)

            results_box.padding = [0, 30]
            results_box.spacing = 100

        for i in events:
            results_box.add_widget(MDLabel(text=f"{i}"))

        self.empty = False
