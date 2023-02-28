from manim import *
import random

class VectorArrow(Scene):
    def construct(self):
    
        num = VGroup()
        i = 0
        for k in range(10):

            n = DecimalNumber().shift(RIGHT * i).scale(0.5)
            num.add(n)
            i += 0.5

            for m in range(10):

                def randomize_numbers(num):

                    for n in num:
                        value = random.uniform(0, 1)
                        n.set_value(value)
                        if value > 0.5:
                            n.set_color(BLUE)
                        else:
                            n.set_color(RED)

                        self.play(Write(num))
                        self.play(FadeOut(n))

                randomize_numbers(num)