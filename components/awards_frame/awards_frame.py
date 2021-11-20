from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

from components.awards_frame.award_box.award_box import AwardBox

Builder.load_file("./components/awards_frame/awards_frame.kv")


class AwardsFrame(MDBoxLayout):
    def on_kv_post(self, base_widget):
        self.ids.awards_box.add_widget(AwardBox(md_bg_color=[0,1,0,.3]))
        self.ids.awards_box.add_widget(AwardBox())
