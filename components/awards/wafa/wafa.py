from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

from data import ACCOUNT

Builder.load_file("./components/awards/wafa/wafa.kv")


class Wafa(MDCard, ButtonBehavior):

    def __init__(self, **kwargs):
        local_code = [i for i in ACCOUNT.keys()][0]
        supernova = ACCOUNT[local_code]["awards"]["wafa'"]
        print(supernova)
        self.name = "wafa'".upper()
        self.challenge = supernova["challenge"]
        self.score = supernova["score"]
        self.image = supernova["image"]
        super().__init__(**kwargs)

    def evolution(self):
        progress = self.ids.percent

        if progress.current_percent < progress.max_percent:
            progress.current_percent += 1

        else:
            print("ended")
