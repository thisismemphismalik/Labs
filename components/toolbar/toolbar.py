from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

from data import MESSAGES

Builder.load_file("./components/toolbar/toolbar.kv")


class Toolbar(MDFloatLayout):
    def on_kv_post(self, base_widget):
        Clock.schedule_interval(self.check, 1)

    def on_touch_down(self, touch):

        if self.collide_point(touch.pos[0], touch.pos[1]):

            for x in self.children[0].children:
                x.on_touch_down(touch)

        else:
            return

    def check(self, dt):
        # use to check un_read messages

        if MESSAGES:
            for i in [j for j in MESSAGES.keys()]:
                if not MESSAGES[i]["read"]:
                    self.red_alarm = [1, 0, 0, 1]
                    break

                else:
                    self.red_alarm = [0, 0, 0, 0]
