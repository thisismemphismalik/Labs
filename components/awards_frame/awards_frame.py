from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd_extensions.akivymd.uix.progresswidget import AKCircularProgress

from components.awards.caesare.caesare import Caesare
from components.awards.motheresa.motheresa import Motheresa
from components.awards.supernova.supernova import Supernova
from components.awards.wafa.wafa import Wafa

Builder.load_file("./components/awards_frame/awards_frame.kv")


class AwardsFrame(MDBoxLayout):
    def on_kv_post(self, base_widget):
        self.ids.awards_box.add_widget(Supernova())
        self.ids.awards_box.add_widget(Motheresa())
        self.ids.awards_box.add_widget(Caesare())
        self.ids.awards_box.add_widget(Wafa())


        # pass

AKCircularProgress