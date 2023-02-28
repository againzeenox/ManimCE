from manim import *

class announcement(Scene):
    def construct(self):
        tex1 = Text("I am going to be making videos on postulates and propositions").scale(0.7).move_to(UP) 
        tex2 = Text("mentioned in Euclid's Elements. I would try to explain them visually").scale(0.7).move_to(UP*0.5)
        tex3 = Text("through videos. We'll go through every single postulate as well as").scale(0.7)
        tex4 = Text("propositition from all 13 books. Videos will be uploaded in").scale(0.7).move_to(DOWN*0.5)
        tex5 = Text("upcoming days").scale(0.7).move_to(DOWN)
        texgrp = VGroup(tex1, tex2, tex3, tex4, tex5)
        self.play(Write(texgrp))