from manim import *

class AboutElements(Scene):
    def construct(self):



        mark = Tex("Mayankk20007").scale(0.3).set_opacity(0.2).to_corner(DR)
        self.add(mark)
        #MAIN DEFINITION:


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




        #########################
        #Comments

        drive = "D:\\ManimCE\\Projects\\euclid_elements\\Introduction\\page\\Euclid's Elements - Wikipedia_files"
        scholars = Text("Scholars believe that the Elements is largely a compilation of \n  propositions based on books by earlier Greek mathematicians").scale(0.5).move_to(DOWN*2)
        fragment = ImageMobject(f"{drive}\\P._Oxy._I_29.jpg").scale(2).move_to(UP)
        fragmentdscrp = Text("A fragment of Euclid's Elements on part of the Oxyrhynchus papyri").scale(0.5).next_to(fragment, DOWN)
        scholartextgrp = VGroup(scholars, fragmentdscrp)
        self.play(FadeIn(fragment))
        self.play(Write(scholartextgrp))
        self.wait(2)
        self.play(FadeOut(fragment, scholartextgrp))
        self.wait()


        ###########################
        #Announcement
        tex1 = Text("I am going to be making videos on postulates and propositions").scale(0.7).move_to(UP) 
        tex2 = Text("mentioned in Euclid's Elements. I would try to explain them visually").scale(0.7).move_to(UP*0.5)
        tex3 = Text("through videos. We'll go through every single postulate as well as").scale(0.7)
        tex4 = Text("propositition from all 13 books. Videos will be uploaded in").scale(0.7).move_to(DOWN*0.5)
        tex5 = Text("upcoming days").scale(0.7).move_to(DOWN)
        texgrp = VGroup(tex1, tex2, tex3, tex4, tex5)
        self.play(Write(texgrp))
        self.wait(3)
        self.play(FadeOut(texgrp))
        self.wait()

        ##########################
        #Credits
        credittext = MarkupText("<u>CREDITS</u>").move_to(UP*2).set_color(RED)
        wikitex = Text("WikiPedia")
        alephtex = Text("aleph0.clarku.edu").next_to(wikitex, DOWN, buff=0.5)
        credgrp = VGroup(credittext, wikitex, alephtex)
        self.play(Write(credgrp))
        self.wait(2)
        self.play(Uncreate(credgrp))
        self.wait(2)