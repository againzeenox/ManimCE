#February, 28, 2023
#@Mayankk20007
from manim import *
from cmath import sqrt


class prop1(Scene):
    def construct(self):
        """"
        It is required to construct an equilateral triangle on the straight line AB.

        Describe the circle BCD with center A and radius AB. Again describe the circle ACE with center B and radius BA. Join the straight lines CA and CB from the point C at which the circles cut one another to the points A and B.

        Now, since the point A is the center of the circle CDB, therefore AC equals AB. Again, since the point B is the center of the circle CAE, therefore BC equals BA.

        But AC was proved equal to AB, therefore each of the straight lines AC and BC equals AB.

        And things which equal the same thing also equal one another, therefore AC also equals BC.

        Therefore the three straight lines AC, AB, and BC equal one another.

        Therefore the triangle ABC is equilateral, and it has been constructed on the given finite straight line AB."""


        #SETUP:
        mark = Tex("Mayankk20007").scale(0.3).set_opacity(0.2).to_corner(DR)
        title = MarkupText("<u>BOOK: 1, Proposition: 1</u>").to_corner(UP)
        aim = Tex("Aim: to construct an equilateral triangle")
        aim2 = Tex(" through a finite straight line AB").next_to(aim, DOWN)




        #STEPS:
        step1 = Tex("1. Let AB be the given finite straight line.").scale(0.7).move_to(UP * 2 + LEFT *  3.5).set_color(RED)
        step2 = Tex("2. Construct a circle of radius 'AB' with 'A' as centre").scale(0.7).move_to(UP*1.5).align_to(step1, LEFT).set_color(BLUE)
        step3 = Tex("3. Repeat the same process with 'B' as reference").scale(0.7).move_to(UP).align_to(step1, LEFT).set_color(GREEN)
        step4 = Tex("4. Join 'A' and 'B' with either point of ").scale(0.7).move_to(UP *0.5).align_to(step1, LEFT).set_color(RED)
        step4_2 = Tex("intersection of the 2 circles at 'C'").scale(0.7).align_to(step1, LEFT).set_color(RED)


        
        
        #GEOMETRY:
        line = Line(color=RED)
        length = line.get_length()
        circ1 = Circle(radius=length).move_to(line.get_start()).set_color(BLUE)
        circ2 = circ1.copy().move_to(line.get_right()).set_color(GREEN)
        invisible_height = Line().rotate(PI/2).move_to(UP * length / 2 + DOWN * 0.11).set_length(length * sqrt(3) / 2).set_opacity(0)
        hyp1 = Line(color=RED, start=line.get_left(), end=invisible_height.get_top())
        hyp2 = Line(color=RED, start=line.get_right(), end=invisible_height.get_top())

        

        #LABELS:
        interlabel = always_redraw(lambda : Tex("C").scale(0.5).next_to(invisible_height.get_top(), UP, buff = 0.1))
        leftlabel = Tex("A").scale(0.5).next_to(line.get_left(), LEFT, buff = 0.1)
        rightlabel = Tex("B").scale(0.5).next_to(line.get_right(), RIGHT, buff = 0.1)
        circlabeld = always_redraw(lambda: Tex("D").scale(0.5).next_to(circ1.get_left(), LEFT, buff = 0.1))
        circlabele = always_redraw(lambda: Tex("E").scale(0.5).next_to(circ2.get_right(), RIGHT, buff=0.1))




        #OBSERVATION:
        obs1 = Tex("Now, since the point A is the center of the circle CDB").scale(0.7).shift(DOWN*1.5)
        obs2 = Tex("therefore AC=AB").scale(0.7).next_to(obs1, DOWN*0.5).set_color(BLUE)
        obs3 = Tex("Similarly, BC=BA").scale(0.7).next_to(obs2, DOWN*0.5).set_color(GREEN)
        obs4 = Tex("But, AC was proved to be AB").scale(0.7).next_to(obs3, DOWN*0.5).set_color(RED)
        transobs = Tex("That means, AB=BC=CA").scale(0.8).shift(DOWN * 1.5)
        transobs2 = Tex("In other words, ABC, by definition, is an equilateral triangle").scale(0.8).next_to(transobs, DOWN*0.5)
        transobs3 = Tex("Which completes the proposition").scale(0.8).next_to(transobs2, DOWN * 0.5)




        #GROUPS:
        aims = VGroup(aim, aim2)
        step4grp = VGroup(step4, step4_2)
        allsteps = VGroup(step1, step2, step3, step4, step4_2)
        obsgrp = VGroup(obs1, obs2, obs3, obs4)
        circlabels = VGroup(circlabeld, circlabele)
        lrlabels = VGroup(rightlabel, leftlabel)
        hypgrp = VGroup(hyp1, hyp2)
        diagramforanim = VGroup(circ1, circ2, lrlabels, interlabel, invisible_height, line, hyp1, hyp2)
        lastpart = VGroup(title, diagramforanim[0:4], transobs, transobs2, transobs3, circlabels)



        #SCENES:
        self.add(mark)
        self.play(Write(title))
        self.wait()
        self.play(Write(aims))
        self.wait(2)
        self.play(aims.animate.move_to(UP *  9))
        self.wait()
        self.play(Write(step1))
        self.play(DrawBorderThenFill(line))
        self.play(Write(lrlabels))
        self.wait()
        self.play(Write(step2))
        self.play(DrawBorderThenFill(circ1))
        self.wait()
        self.play(Write(step3))
        self.play(DrawBorderThenFill(circ2))
        self.wait()
        self.play(Write(step4grp))
        self.play(Create(hypgrp))
        self.play(Write(interlabel))
        self.wait()
        self.wait(2)
        self.play(FadeOut(allsteps))
        self.play(diagramforanim.animate.move_to(LEFT*0.5 +UP*0.8))
        self.wait(0.15)
        self.play(Write(circlabels))
        self.wait()
        self.play(Write(obs1))
        self.wait()
        self.play(Indicate(circ1))
        self.play(Write(obs2))
        self.wait()
        self.play(Write(obs3))
        self.play(Indicate(circ2))
        self.wait()
        self.play(Write(obs4))
        self.wait(2)
        self.play(ReplacementTransform(obsgrp, transobs))
        self.wait()
        self.play(Write(transobs2))
        self.wait()
        self.play(Write(transobs3))
        self.wait(5)
        self.play(FadeOut(lastpart))
        self.wait()
        self.play(Indicate(diagramforanim[5: 8]))
        self.play(Uncreate(diagramforanim[5: 8]))
        self.wait()