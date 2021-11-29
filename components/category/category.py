import random

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import RiseInTransition, FallOutTransition
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

from components.box.box import Box
from data import CATEGORIES, COLORMAP, EVENTS

Builder.load_file("./components/category/category.kv")


class Category(MDCard, ButtonBehavior):
    """
    Category Box to call in the Events Tab

    *to be called only in python code
    """

    def __init__(self, code, **kwargs):
        self.code = code
        self.data = CATEGORIES[self.code]
        self.color_map = COLORMAP
        self.name = self.data["name"]
        self.events = f'{self.data["events"]} Events'

        self.elements = [i for i in self.data["elements"].keys()]
        self.four_elements = [EVENTS[self.elements[i]] for i in range(4)]

        self.images = [self.four_elements[i]["image"] for i in range(4)]
        self.color = self.color_map[random.choice(self.four_elements)["color"]]

        super().__init__(**kwargs)

    def on_release(self):
        self.open()

    def open(self):
        app = MDApp.get_running_app()
        current = app.root.ids.main_page.ids.tabs_manager.current

        if current != "OpenerTab":
            print(current)
            opener = app.root.ids.main_page.ids.tabs_manager.get_screen("OpenerTab")
            opener = opener.ids.opener_manager.get_screen("TabOne")
            # print(opener)
            opener.clear_widgets()
            #
            manager = app.root.ids.main_page.ids.tabs_manager
            manager.transition = RiseInTransition()
            manager.current = "OpenerTab"
            #
            opener.add_widget(CategoryOpener(self.code, self.name, self.elements, self.images))  # "33A-41C-25C"


class CategoryOpener(MDBoxLayout):
    step = 0
    round = 0

    def __init__(self, code, name, elements, images,  **kwargs):
        self.code = code
        self.elements = elements
        self.images = images
        self.name = name.upper()
        super().__init__(**kwargs)
        Clock.schedule_interval(self.image_animation, 3)

    def on_kv_post(self, base_widget):
        self.add_boxes()

    def image_animation(self, dt):
        # images = self.images

        self.ids.image_box.source = self.images[self.step]
        if self.step < 3:
            self.step += 1
        else:
            self.step = 0

    def add_boxes(self):
        if len(self.elements) >= 13:
            to_add = self.elements[:13]

            for i in to_add[:7]:
                self.ids.box_container1.add_widget(Box(i))

            for j in to_add[7:13]:
                self.ids.box_container2.add_widget(Box(j))
        else:
            to_add = self.elements

            if len(to_add) % 2 == 0:
                half = len(to_add) // 2
                for i in to_add[:half]:
                    self.ids.box_container1.add_widget(Box(i))
                for i in to_add[half:]:
                    self.ids.box_container2.add_widget(Box(i))

            else:
                half = (len(to_add) // 2) + 1
                for i in to_add[:half]:
                    self.ids.box_container1.add_widget(Box(i))
                for i in to_add[half:]:
                    self.ids.box_container2.add_widget(Box(i))

    def go_back(self, dt):
        app = MDApp.get_running_app()
        manager = app.root.ids.main_page.ids.tabs_manager

        manager.transition = FallOutTransition()
        manager.current = "TicketsTab"
