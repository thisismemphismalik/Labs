from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("./components/chip_chooser/chip_chooser.kv")


class ChipChooser(MDBoxLayout):
    def on_kv_post(self, base_widget):
        last = self.children[~0]
        last.on_press()

    def check(self, chip):
        print(self.children[~0].text)
        # print(chip.touch)
