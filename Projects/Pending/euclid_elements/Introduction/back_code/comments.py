from manim import *

class eescene2(Scene):
    def construct(self):
        drive = "D:\\ManimCE\\Projects\\euclid_elements\\Introduction\\page\\Euclid's Elements - Wikipedia_files"
        scholars = Text("Scholars believe that the Elements is largely a compilation of \n  propositions based on books by earlier Greek mathematicians").scale(0.5).move_to(DOWN*2)
        fragment = ImageMobject(f"{drive}\\P._Oxy._I_29.jpg").scale(2).move_to(UP)
        fragmentdscrp = Text("A fragment of Euclid's Elements on part of the Oxyrhynchus papyri").scale(0.5).next_to(fragment, DOWN)
        scholartextgrp = VGroup(scholars, fragmentdscrp)
        self.play(FadeIn(fragment))
        self.play(Write(scholartextgrp))