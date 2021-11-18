from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("./main_page/main_page_tabs/profile_tab/profile_tab.kv")


class ProfileTab(MDScreen):
    names = None

    def on_pre_enter(self, *args):
        self.names = self.ids.names_box.children
        print(self.names)
        if not self.check(self.names):
            print("repaining")
            Clock.schedule_interval(self.repair, 1/1)

    @staticmethod
    def check(labels):
        checker = None
        for i in labels:
            print(i.text)
            print(i.height)

            if not i.height <= 40:
                checker = False
                break
            else:
                checker = True

        return checker

    def repair(self, dt):
        labels = self.names
        a = labels[0].font_size
        print(a)
        for i in labels:
            i.font_size = a - 1

        if self.check(labels):
            Clock.unschedule(self.repair)
