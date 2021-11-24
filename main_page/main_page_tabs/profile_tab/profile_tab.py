from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from components.awards_frame.awards_frame import AwardsFrame
from data import ACCOUNT as User
from frames.profile_buttons_frame.profile_buttons_frame import ProfileButtonsFrame

Builder.load_file("./main_page/main_page_tabs/profile_tab/profile_tab.kv")


class ProfileTab(MDScreen):
    names = None
    ACCOUNT = None

    def on_kv_post(self, base_widget):
        # labo
        self.ids.racine.add_widget(AwardsFrame())

        self.ids.racine.add_widget(ProfileButtonsFrame())

    def on_pre_enter(self, *args):
        # mapping the data
        self.ACCOUNT = User

        # parsing names
        names = self.ids.names_box.children
        local_code = [i for i in self.ACCOUNT.keys()][0]
        local_names = self.ACCOUNT[local_code]["infos"]["names"]
        local_names_keys = [i for i in local_names.keys()]
        local_names_values = [local_names[i] for i in local_names_keys]
        # print(local_names_values)
        for i in range(len(local_names_values)):
            names[~i].text = local_names_values[i].lower()

        # parsing image
        image = self.ids.image
        local_image = self.ACCOUNT[local_code]["infos"]["image"]
        image.source = local_image
        # print(local_image)

    def on_enter(self, *args):
        self.names = self.ids.names_box.children
        # print(self.names)
        if not self.check(self.names):
            print("repaining")
            Clock.schedule_interval(self.repair, 1/60)

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
