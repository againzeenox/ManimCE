from manim import *

class BOOK1Defs(Scene):
    def construct(self):

        # tex = Tex("There are a total of 23 Definition in BOOK 1 from Euclid's Elements").scale(0.7)
        # def1 = Tex("Definition 1:").scale(0.8).to_corner(UL)
        # def2  = Tex("Definition 2:").scale(0.8).next_to(def1, DOWN*3)
        # def3  = Tex("Definition 3:").scale(0.8).next_to(def2, DOWN*3)
        # def4  = Tex("Definition 4:").scale(0.8).next_to(def3, DOWN*3)
        # def5  = Tex("Definition 5:").scale(0.8).next_to(def4, DOWN*3)
        # def6 = Tex("Definition 6:").scale(0.8).next_to(def5, DOWN*3)
        # defat1grp = VGroup(def1, def2, def3, def4, def5, def6).set_color(RED)
        # def1c = Tex("A point is that which has no part").scale(0.8).next_to(def1, DOWN + RIGHT * 0.01)
        # def2c = Tex("A line is breadthless length").scale(0.8).next_to(def2, DOWN + RIGHT * 0.01)
        # def3c = Tex("The ends of a line are points").scale(0.8).next_to(def3, DOWN + RIGHT * 0.01)
        # def4c = Tex("A straight line is a line which lies evenly with the points on itself.").scale(0.8).next_to(def4, DOWN + RIGHT * 0.01)
        # def5c = Tex("A surface is that which has length and breadth only").scale(0.8).next_to(def5, DOWN + RIGHT * 0.01)
        # def6c = Tex("The edges of a surface are lines.").scale(0.8).next_to(def6, DOWN + RIGHT * 0.01)
        # defcat1grp = VGroup(def1c, def2c, def3c, def4c, def5c, def6c).set_color(TEAL_C)


        def7 = Tex("Definition 7:").scale(0.8).to_corner(UL)
        def8  = Tex("Definition 8:").scale(0.8).next_to(def7, DOWN*3)
        def9  = Tex("Definition 9:").scale(0.8).next_to(def8, DOWN*5)
        def10  = Tex("Definition 10:").scale(0.8).next_to(def9, DOWN*5)
        # def11  = Tex("Definition 11:").scale(0.8).next_to(def10, DOWN*3)
        # def12 = Tex("Definition 12:").scale(0.8).next_to(def11, DOWN*3)
        # defat2grp = VGroup(def7, def8, def9, def10, def11, def12).set_color(RED)
        def7c = Tex("A plane surface is a surface which lies evenly with the straight lines on itself").scale(0.8).next_to(def7, DOWN + RIGHT * 0.01)
        def8c1 = Tex("A plane angle is the inclination to one another of two lines in a ").scale(0.8).next_to(def8, DOWN + RIGHT * 0.01)
        def8c2 = Tex("plane which meet one another and do not lie in a straight line").scale(0.8).next_to(def8, DOWN*2.5 + RIGHT * 0.01)
        def9c1 = Tex("And when the lines containing the angle are straight, the angle is").scale(0.8).next_to(def9, DOWN + RIGHT * 0.01)
        def9c2 = Tex("called rectilinear").scale(0.8).next_to(def9, DOWN*2.5 + RIGHT * 0.01)
        def10c = Tex("When a straight line standing on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to that on which it stands").scale(0.8).next_to(def10, DOWN + RIGHT * 0.01)
        defcat2grp = VGroup(def7c, def8c1, def8c2, def9c1, def9c2, def10c).set_color(TEAL_C)




        # self.add(defat1grp, defcat1grp)
        self.add(def7, def8,def9, defcat2grp)