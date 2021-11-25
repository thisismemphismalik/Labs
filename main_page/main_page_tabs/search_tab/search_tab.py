from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from components.black_button.black_button import BlackButton
from components.event.event import Event
from components.svg_image.svg_image import SvgImage
from data import TAGS

Builder.load_file("./main_page/main_page_tabs/search_tab/search_tab.kv")


class SearchTab(MDScreen):
    see = None

    results = None
    add_counter = 1

    old_scroll = None

    last_search = None

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

        print(f"a --- {len(a)}")

        if len(a) > 0:
            print("searching")
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

            print(f"sorted_score --- {sorted_score}")

            if len(sorted_score) > 0:
                print("parsing")

                if self.last_search != sorted_score:
                    self.last_search = sorted_score
                    self.parser(sorted_score)
                else:
                    toast(text="les resultats sont déja affichés")
            else:
                toast(text="aucun event ne correspond")

        else:
            toast(text="Veuillez saisir un recherche")

    def parser(self, events):
        results_box = self.ids.results

        results_box.clear_widgets()

        results_box.padding = [0, 30]
        results_box.spacing = 25

        if len(events) <= 13:
            for i in events:
                results_box.add_widget(Event(i))
            self.see = See()
            results_box.add_widget(self.see)
        else:
            for i in events[:13]:
                results_box.add_widget(Event(i))
            self.see = See()
            results_box.add_widget(self.see)

        self.results = events

        self.empty = False
        print(len(results_box.children))

    def see_more(self):

        if self.results is not None:
            if len(self.results) > 13:
                results_box = self.ids.results
                un_added = self.results[13:]

                results_box.remove_widget(self.see)

                if len(un_added) <= 13:
                    for i in un_added:
                        results_box.add_widget(Event(i))
                        first_child = results_box.children[len(un_added)-1]

                else:
                    for i in un_added[:13]:
                        results_box.add_widget(Event(i))
                        first_child = results_box.children[12]

                results_box.add_widget(self.see)

                Clock.schedule_once(lambda *dt: self.ids.scroller.scroll_to(first_child), 1)

                self.results = un_added

            else:
                toast(text="tous les résultats sont affichés")
        else:
            toast(text="tous les résultats sont affichés")


class See(BlackButton):
    def on_release(self):
        search_tab = self.parent.parent.parent.parent.parent
        search_tab.see_more()
