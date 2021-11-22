from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd_extensions.akivymd.uix.progresswidget import AKCircularProgress

from components.awards_frame.award_box.award_box import AwardBox

Builder.load_file("./components/awards_frame/awards_frame.kv")


class AwardsFrame(MDBoxLayout):
    def on_kv_post(self, base_widget):
        for i in range(5):
            self.ids.awards_box.add_widget(AwardBox())


        # pass

AKCircularProgress