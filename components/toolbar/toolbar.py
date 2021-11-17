from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("./components/toolbar/toolbar.kv")


class Toolbar(MDFloatLayout):

    def on_touch_down(self, touch):

        if self.collide_point(touch.pos[0], touch.pos[1]):

            for x in self.children[0].children:
                x.on_touch_down(touch)

        else:
            return
