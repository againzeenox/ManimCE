"""againzeenox 
19 May 2022
11:34:25"""


#WELCOME


"""Through this animation, I've tried to visualize the Amplitude and Period of a Wave through a Sinusoid.
I've also visualized that increasing or decreasing the value of one of them doesn't affect the length of the other phase."""

#These animations are coded in ManimCE(community maintained version) and probably won't work in any other version

#Link for the official Manim community page :
#https://www.manim.community/

#code starts here:

from manim import *

class PeriodAndAmplitude(Scene):
    def construct(self):

######################################################
################# Outro Assets #######################
######################################################

        home = "D:" #My directory from which I'll import SVGs
        black_rectangle = Rectangle().scale(10).set_color(BLACK).set_opacity(1) #This Rectangle will fill into the entire screen
        YT = SVGMobject(f"{home}\\icons8-youtube.svg").shift(6 * LEFT) #YouTube SVG
        IG = SVGMobject(f"{home}\\icons8-instagram-old.svg").shift(2 * LEFT) #Instagram SVG
        RD = SVGMobject(f"{home}\\reddit-logo-2436.svg").shift(2 * RIGHT) #Reddit SVG
        DS = SVGMobject(f"{home}\\discord-icon-svgrepo-com").shift(6 * RIGHT) #Discord SVG
        YT_name = Tex("againzeenox").shift(6 * LEFT + 1.5 * DOWN) #YouTube Channel name
        IG_name = Tex("@againzeenox").shift(2 * LEFT + 1.5 * DOWN) #Instagram handle name
        RD_name = Tex("u/againzeenox").shift(2 * RIGHT + 1.5 * DOWN) #Reddit username
        DS_name = Tex("againzeenox 5274").shift(6 * RIGHT + 1.5 * DOWN) #Discord num

######################################################
################### Main Stuff #######################
######################################################

        axis = Axes(
            x_range=[-50, 50, 1], 
            x_length=101, 
            y_range=[-50, 50, 1], 
            y_length=101
        ).add_coordinates() #We need a big axis

        Amplitude = ValueTracker(-2) #ValueOfAmplitude

        Period = ValueTracker(-3) #ValueOfPeriod

        func = always_redraw(lambda : axis.plot(
            lambda x : Amplitude.get_value() * np.cos((2 * PI * x) / Period.get_value())
        ).set_color(RED)) #This function will create a Sinusoid that will be dependent on the value of Amplitude and Period

        equation = Tex(
            "f(x) = Amplitude * cos($\\frac{2 \\pi x}{\\operatorname{Period}}$)"
        ).to_corner(UL).set_color(YELLOW) #This is just the label of the above equation

        AmplitudeLine = always_redraw(lambda : Line(
            start = axis.c2p(0, Amplitude.get_value()), 
            end = axis.c2p(Period.get_value(), Amplitude.get_value())
        ).set_color(BLUE)) #This line will start from (0, Amplitude(x)) and will end at (Period(x), Amplitude(x))

        AmplitudeEqual = Tex("Amplitude = ").to_corner(UR).shift(1.2 * LEFT).set_color(TEAL)

        PeriodLine = always_redraw(lambda : Line(
            start = axis.c2p(Period.get_value(), Amplitude.get_value()), 
            end = axis.c2p(Period.get_value(), 0)
            ).set_color(GREEN_C)) #This line will start from (Period(x), Amplitude(x)) and will end at (Period(x), 0)

        AmplitudeValue = always_redraw(lambda : DecimalNumber(num_decimal_places = 2)
        .set_value(Amplitude.get_value()).set_color(PINK).to_corner(UR)
        ) #This will convert the value of Amplitude to Decimal number so that we can treat it like a mobject

        PeriodEqual = Tex("Period = ").to_corner(UR).shift(DOWN + 1.2 * LEFT).set_color(PINK)

        PeriodValue = always_redraw(lambda : DecimalNumber(num_decimal_places = 2)
        .set_value(Period.get_value()).set_color(TEAL).to_corner(UR).shift(DOWN)
        ) #This will convert the value of Period to Decimal number so that we can treat it like a mobject

        AmplitudeBrace = always_redraw(lambda : BraceBetweenPoints(
            AmplitudeLine.get_end(), AmplitudeLine.get_start()
        )) #This is a brace around the Amplitude Line

        AmplitudeTex = always_redraw(lambda : AmplitudeBrace.get_text("Period").set_color(TEAL)) #Text for AmplitudeBrace

        PeriodBrace = always_redraw(lambda : BraceBetweenPoints(
                PeriodLine.get_end(), PeriodLine.get_start()
        )) #This is a brace around the PeriodLine

        PeriodTex = always_redraw(lambda : PeriodBrace.get_text("Amplitude").set_color(PINK)) #Text for PeriodBrace

        IndependentAmplitude = Tex(
            "Changing Period doesn't affect the lengh of Amplitude"
        ).to_edge(DOWN).set_color_by_gradient(RED, BLUE, PURPLE_C, GREEN_B).shift(DOWN) #It's just the text about Amplitude

        IndependentPeriod = Tex(
            "Changing Amplitude doesn't affect the lengh of Period"
        ).to_edge(DOWN).set_color_by_gradient(RED, BLUE, PURPLE_C, GREEN_B).shift(DOWN) #It's just the text about Period

        SurroundingRectangleForAmplitude = SurroundingRectangle(AmplitudeValue)
        SurroundingRectangleForPeriod = SurroundingRectangle(PeriodValue)

######################################################
##################### Scenes #########################
######################################################

        self.play(Create(axis), run_time = 2)
        self.play(Create(func), run_time = 3)
        self.wait()
        self.play(Write(VGroup(equation, AmplitudeEqual, AmplitudeValue, PeriodEqual, PeriodValue)))
        self.play(Create(VGroup(AmplitudeLine, PeriodLine)))
        self.wait()
        self.play(DrawBorderThenFill(VGroup(AmplitudeBrace, PeriodBrace)))
        self.play(Write(VGroup(AmplitudeTex, PeriodTex)))
        self.play(
            Amplitude.animate.set_value(-10), 
            Period.animate.set_value(-10), 
            axis.animate.scale(1/5), 
            lag_ratio = 0
            )
        self.play(
            Amplitude.animate.set_value(-3), 
            Period.animate.set_value(-2), 
            axis.animate.scale(5), 
            lag_ratio = 0
            )
        self.wait()
        self.play(
            Write(IndependentPeriod), 
            Indicate(PeriodLine),
            Flash(PeriodLine), 
            Create(SurroundingRectangleForPeriod)
            )
        self.wait()
        self.play(FadeOut(SurroundingRectangleForPeriod))
        self.play(axis.animate.scale(1/1.5))
        self.play(Amplitude.animate.set_value(5), run_time = 5)
        self.wait()
        self.play(TransformMatchingShapes(IndependentPeriod, IndependentAmplitude),  
        Indicate(AmplitudeLine), 
        Flash(AmplitudeLine), 
        Create(SurroundingRectangleForAmplitude))
        self.wait()
        self.play(FadeOut(SurroundingRectangleForAmplitude))
        self.play(Period.animate.set_value(4), run_time = 5)
        self.wait()
        #check in GitHub
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

#This video is inspired by Desmos.
#Link for the Desmos file :
#https://www.desmos.com/calculator/kihjluohq9

#Thanks for coming here

#Much love <3