from kivy.graphics.svg import Svg
from kivy.uix.scatter import Scatter


class SvgImage(Scatter):
    def __init__(self, source, **kwargs):

        super().__init__(**kwargs)

        with self.canvas:
            svg = Svg(source)
            self.size_hint = [None, None]
            self.size = [svg.width*self.scale, svg.height*self.scale]
            self.pos_hint = {"center_x": .5, "center": .5}
