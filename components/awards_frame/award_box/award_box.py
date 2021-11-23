from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard

Builder.load_file("./components/awards_frame/award_box/award_box.kv")


class AwardBox(MDCard, ButtonBehavior):
    # pass
    def __init__(self, name="SUPERNOVA", image="./lnx.png", challenge=5, score=3, **kwargs):

        self.name = name.lower()
        self.challenge = challenge
        self.score = score
        self.image = image
        super().__init__(**kwargs)

    def evolution(self):
        progress = self.ids.percent

        if progress.current_percent < progress.max_percent:
            progress.current_percent += 1

        else:
            print("ended")
