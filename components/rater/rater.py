from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

from data import EVENTS

Builder.load_file("./components/rater/rater.kv")


class Rater(MDBoxLayout):
    def __init__(self, event_code, **kwargs):
        self.code = event_code
        self.data = EVENTS[self.code]

        self.name = self.data["name"]
        self.date = self.data["date"]
        super().__init__(**kwargs)

    def check(self, field):
        if field.text == "Laissez un commentaire":
            field.text = ""
        elif field.text == "":
            field.text = "Laissez un commentaire"

    def valuer(self, rater):
        a = {
            1: "Médiocre !",
            2: "Passable !",
            3: "Assez Bien !",
            4: "Bien !",
            5: "Très Bien !"
        }

        a = a[rater.get_rate()]

        self.ids.translater.text = a