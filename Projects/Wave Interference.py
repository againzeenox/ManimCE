"""againzeenox
18 May 2022
3:29 AM"""


#WELCOME


"""Through this animation, I've tried to visualise Wave Interference
"The changing number" is the phase difference between the two curves.
The green curve is what you get by adding the two orange waves together."""

#These animations are coded in ManimCE(community maintained version) and probably won't work in any other version


#code starts here:

from manim import *
class rose(Scene):
    def construct(self):
        

        ######################################################
        ################# Outro Assets #######################
        ######################################################

        home = "D:"   #My directory from which I'lll import SVGs
        channel_name = Tex("againzeenox").to_corner(UR)  #SUBSCRIBE!!!
        black_rectangle = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1).scale(10) #This Rectangle will fill into the entire screen
        YT = SVGMobject(
            f"{home}\\icons8-youtube.svg"
        ).shift(6 * LEFT) #YouTube SVG


        IG = SVGMobject(
            f"{home}\\icons8-instagram-old.svg"
        ).shift(2 * LEFT) #Instagram SVG


        RD = SVGMobject(
            f"{home}\\reddit-logo-2436.svg").shift(2 * RIGHT) #Reddit SVG


        DS = SVGMobject(
            f"{home}\\discord-icon-svgrepo-com"
        ).shift(6 * RIGHT) #Discord SVG
        

        YT_name = Tex("againzeenox").shift(6 * LEFT + 1.5 * DOWN) #YouTube Channel name
        IG_name = Tex("@againzeenox").shift(2 * LEFT + 1.5 * DOWN) #Instagram handle name
        RD_name = Tex("u/againzeenox").shift(2 * RIGHT + 1.5 * DOWN) #Reddit username
        DS_name = Tex("againzeenox 5274").shift(6 * RIGHT + 1.5 * DOWN) #Discord num

        ######################################################
        ################### Main Stuff #######################
        ######################################################

        a = ValueTracker(-2 * PI) #value of "a"
        axis = Axes()
        sin = axis.plot(lambda x : np.sin(x)).set_color(RED) #f(x) = sin(x)
        sin2 = always_redraw(lambda : axis.plot(lambda x : np.sin(x + a.get_value())).set_color(BLUE)) #f(x) = sin(x + a)
        sin3 = always_redraw(lambda : axis.plot(lambda x : np.sin(x + a.get_value()) + np.sin(x)).set_color(GREEN)) #f(x) = sin(x + a + sin(x))
        sin_label = Tex("$f(x) = sin(x)$").set_color(RED).to_corner(UL) #label for "f(x) = sin(x)"
        sin2_label = Tex("$f(x) = sin(x +  $").set_color(BLUE).to_edge(UP) #label for "f(x) = sin(x + a)"
        sin3_label = Tex("$f(x) = sin(x + sin(x) + $").set_color(GREEN).to_edge(DOWN).shift(LEFT) #label for f(x) = sin(x + a + sin(x))
        a_value = always_redraw(
            lambda : DecimalNumber(num_decimal_places=2).set_value(a.get_value()).set_color(BLUE).next_to(sin2_label, RIGHT)
        ) #Writes the value of "a" and is constantly updating
        a_copy = always_redraw(
            lambda : DecimalNumber(num_decimal_places=2).set_value(a.get_value()).set_color(GREEN).next_to(sin3_label, RIGHT)
        ) #Writes the value of "a" and is constantly updating
        sin2_brac = Tex("$)$").next_to(a_value, RIGHT).set_color(BLUE)
        sin3_brac = Tex("$)$").next_to(a_copy, RIGHT).set_color(GREEN)


        ######################################################
        ##################### Scenes #########################
        ######################################################

        self.play(Write(channel_name),
        Create(axis),
        Write(VGroup(sin_label, sin2_label, sin3_label)),
        Write(VGroup(a_value, a_copy, sin2_brac, sin3_brac)),
        Create(VGroup(sin, sin2, sin3)))
        self.wait()
        self.play(a.animate.set_value(5 * PI), run_time=10) #Value of "a" becomes (5 * PI)
        self.wait()
        self.play(a.animate.set_value(-5 * PI), run_time=20) #Value of "a" becomes (-5 * PI)
        self.wait()
        self.play(FadeIn(black_rectangle)) #This animation will have an effect of every mobject on screen "Fading Out"
        self.wait()
        self.play(DrawBorderThenFill(VGroup(YT, IG, RD, DS))) #Outro SVGs
        self.play(Write(VGroup(YT_name, IG_name, RD_name, DS_name))) #Reach out names
        self.wait(10)

        """If you have any suggestion(s) / complaint(s) / doubt(s), you can feel free to reach out through the following links:
        Youtube : https://www.youtube.com/channel/UCk71twvi6p8i6AqYtFng95g
        Instagram : https://www.instagram.com/againzeenox/
        Reddit : https://www.reddit.com/user/againzeenox
        Discord : againzeenox#7760"""

        """Thanks you Grant Sanderson for making ManimCE, ManimGL and ManimCairo
        Thanks you developers of each library for helping and maintaining Manim"""

        """And Thanks to you for coming here"""

        #Much love <3
