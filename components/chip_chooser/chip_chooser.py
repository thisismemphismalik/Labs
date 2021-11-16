from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("./components/chip_chooser/chip_chooser.kv")


class ChipChooser(MDFloatLayout):
    def search(self, chip):
        self.ids.marker.x = chip.x
        self.ids.marker.owner = chip.text
        print(self.ids.marker.owner)
