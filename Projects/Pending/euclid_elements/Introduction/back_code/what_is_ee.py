from manim import *
class head(Scene):
    def construct(self):
        def1 = Text("Euclid's Elements is a mathematical treatise consisting of 13 books attributed to the").scale(0.5).move_to(2*UP)
        head = MarkupText("<u> What is Euclid's Elements?</u>").next_to(def1, UP, buff=0.5).set_color(BLUE)
        def2 = Text("ancient Greek mathematician Euclid in Alexandria, Ptolemaic Egypt. It is a collection of ").scale(0.5).move_to(UP*1.5)
        def3 = Text("definitions, postulates, propositions, and mathematical proofs of the propositions. ").scale(0.5).move_to(UP)
        def4 = Text("The books cover plane and solid Euclidean geometry, elementary number theory,").scale(0.5).move_to(UP*0.5)
        def5 = Text("and incommensurable lines. Elements is the oldest extant large-scale deductive").scale(0.5)
        def6 = Text("treatment of mathematics. It has proven instrumental in the development of logic,").scale(0.5).move_to(DOWN*0.5)
        def7 = Text("and its logical rigor was not surpassed until the 19th century.").scale(0.5).move_to(DOWN)
        wiki = Text("-WikiPedia(The free Encyclopedia)").scale(0.7).move_to(DOWN*2 + RIGHT*2.5)
        defgrp = VGroup(def1, def2, def3, def4, def5, def6, def7)
        maingrp = VGroup(head, def1, def2, def3, def4, def5, def6, def7, wiki)
        self.play(Create(head))
        self.wait()
        for k in defgrp:
            self.play(Write(k))
        self.play(Write(wiki))
        self.wait(5)
        self.play(FadeOut(maingrp))
        self.wait()