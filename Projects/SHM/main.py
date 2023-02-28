from manim import *
config.background_color = BLUE
class UCMvsSHM(Scene):
    def construct(self):
        circle = Circle(color=RED, fill_opacity=0.3)
        self.add(circle)
        self.add(Square(color=PURPLE, fill_opacity=0.3))