from manim import *
class Creditsee(Scene):
    def construct(self):
        credittext = MarkupText("<u>CREDITS</u>").move_to(UP*2).set_color(RED)
        wikitex = Text("WikiPedia")
        alephtex = Text("aleph0.clarku.edu").next_to(wikitex, DOWN, buff=0.5)
        self.add(credittext, wikitex, alephtex)