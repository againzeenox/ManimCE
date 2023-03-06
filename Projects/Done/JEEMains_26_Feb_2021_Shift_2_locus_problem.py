from manim import * 

class Locus(Scene):
    def construct(self):

        mark = Tex("Mayankk20007").scale(0.4).set_opacity(0.4).to_corner(DR)
        self.add(mark)
        # self.add_sound(f"bg.mp3")
        photo = ImageMobject(f"D:\\ManimCE\\experiments\\locus\\media\\images\\locus1\\Screenshot 2023-03-02 160907.png").scale(3)
        self.play(FadeIn(photo))
        self.wait(3)
        self.play(FadeOut(photo))
        self.wait(2)
        


        axis = NumberPlane(x_range=[-10, 10, 1], y_range=[-4, 6, 1]).shift(LEFT*2)
        numberplane = axis.copy()
        circ = Circle(radius=1).move_to(axis.c2p(0, 0))
        circ_rotate = always_rotate(Circle(radius=1).move_to(axis.c2p(0, 0)), rate=1.5)
        dot = always_redraw(lambda :Dot().move_to(circ_rotate.get_start()))

        point = Dot(point=axis.c2p(3, 2))
        circtex = Tex("$x^2 + y^2 = 1$").next_to(circ, DOWN).set_color_by_gradient(PINK)
        pointtex = Tex("$(3, 2)$").scale(0.5).next_to(point, UP, buff=0.1).set_color(ORANGE)
        whattex = Tex("Which path does $(h, k)$ follow \n as $(x, y)$ moves on the circle?").set_color_by_gradient(TEAL_B, TEAL_D).to_edge(UP)




        line = always_redraw(lambda : Line(start=axis.c2p(3, 2), end=dot.get_center()).set_color_by_gradient(RED, PURPLE))
        circdot = always_redraw(lambda: Dot().move_to(line.get_end()))
        xy = always_redraw(lambda : Tex("$(x, y)$").next_to(line.get_end(), UP, buff=0.1).scale(0.5).set_color(GREEN_D))
        locus_dot = always_redraw(lambda: Dot().move_to(line.get_midpoint()))
        hk = always_redraw(lambda: Tex("$(h, k)$").next_to(locus_dot.get_center(), UP, buff=0.1).scale(0.5).set_color(YELLOW_C))

        trace = TracedPath(locus_dot.get_center)
        
        # self.add(point, circ, circtex, pointtex)

        self.wait()
        # self.play(Create(axis))
        self.play(DrawBorderThenFill(circ))
        self.wait()
        self.play(Create(VGroup(point, line, locus_dot, circdot)))
        self.wait()
        self.play(Write(VGroup(circtex, pointtex, xy, hk)))
        self.wait()
        self.play(Write(whattex), run_time=2)
        self.wait()
        self.play(Uncreate(whattex))
        self.wait()
        self.add(circ_rotate, dot)
        self.wait(7)
        self.add(trace)
        self.wait(10)
        self.play(DrawBorderThenFill(numberplane))
        self.wait(7)
        self.play(FadeOut(VGroup(circ, point, line, locus_dot, circdot, circtex, pointtex, xy, hk, circ_rotate, dot, trace, numberplane)))
        self.wait(2)
        # self.add(circ, axis, dot, line, locus_dot, trace)
        # self.wait()
        # self.add(circ_rotate)
        # self.wait(10)
