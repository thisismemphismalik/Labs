from kivy.lang import Builder
from kivymd.app import MDApp


KV = Builder.load_string("""
MDFloatLayout:
    MDLabel:
        text: "azerty"
""")

class Mein(MDApp):
    def build(self):
        return KV