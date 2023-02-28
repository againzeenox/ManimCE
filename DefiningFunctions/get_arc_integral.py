from __future__ import annotations
from manim import *


__all__ = [
    "CoordinateSystem",
    "Axes",
    "ThreeDAxes",
    "NumberPlane",
    "PolarPlane",
    "ComplexPlane",
]

import fractions as fr
import numbers
from typing import TYPE_CHECKING, Any, Callable, Iterable, Sequence

import numpy as np
from colour import Color

from manim import config
from manim.constants import *
from manim.mobject.geometry.arc import Circle, Dot
from manim.mobject.geometry.line import Arrow, DashedLine, Line
from manim.mobject.geometry.polygram import Polygon, Rectangle, RegularPolygon
from manim.mobject.graphing.functions import ImplicitFunction, ParametricFunction
from manim.mobject.graphing.number_line import NumberLine
from manim.mobject.graphing.scale import LinearBase
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.text.tex_mobject import MathTex
from manim.mobject.types.vectorized_mobject import (
    VDict,
    VectorizedPoint,
    VGroup,
    VMobject,
)
from manim.utils.color import *
from manim.utils.config_ops import merge_dicts_recursively, update_dict_recursively
from manim.utils.simple_functions import binary_search
from manim.utils.space_ops import angle_of_vector

if TYPE_CHECKING:
    from manim.mobject.mobject import Mobject
    
    
    
    
    
    
    
    
##########################################################################
############################# Function ###################################
##########################################################################


def get_arc_integral(
    Axes,
    function,
    line_width = 5,
    line_opacity = 1,
    line_color: Color = RED,
    dot_color = TEAL_B,
    dot_opacity = 0.8,
    scale_factor_for_dots = 0.7,
    dx = None,
    x_min = None,
    x_max = None
    ):

        """Creates dots on equal intervals on the X-Axis of the function
        Then Creates a line between every 2 consecutive Dots
        Hence, giving us an integral for measuring the length of an arc
        
        Required Arguments
        ------------------
        Axes
            Axis on which Arc integral has to be called

        Function
            Function on which Arc integral has to be called
        
        dx
            each interval is denoted as "dx"
        
        x_min
            Value of x from where the arc lines has to be started
            
        x_max
            Value of x at which the arc lines has to end

        Customizations
        --------------
        line_width
            Width of lines going from Dot to Dot
            default width = 5

        line_opacity
            opacity of lines going from Dot to Dot
            default opacity = 1

        line_color
            color of lines going from Dot to Dot
            you can use a gradient too
            default color = RED

        dot_color
            color of Dots at an encrement of "dx"
            default color = TEAL_B

        dot_opacity
            opacity of Dots at an encrement of "dx"
            default opacity = 0.8

        scale_factor_for_dots
            the value by which dots will be scaled
            default value = 0.7

        Returns
        -------
        :class:`~VGroup` containing the Dots and Lines

        Example
        -------
        from manim import *
        class GetArcIntegralExample(Scene):
            def construct(self):

                Axis = Axes().shift(2 * DOWN)
                Plot = Axis.plot(lambda x : x**2)

                Arc_Integral = Axis.get_arc_integral(function=Plot,
                dx=1,
                x_min=-5,
                x_max=5,
                line_color=BLUE,
                line_opacity=1,
                line_width=6,
                dot_color=RED,
                dot_opacity=1,
                scale_factor_for_dots=1)

                self.play(Create(VGroup(Axis, Plot)))

                self.wait()

                self.play(Create(Arc_Integral))

                self.wait()

created on:

1 July 2022

10:35 PM

againzeenox

        """
        dots = VGroup(

        )
        
        lines = VGroup(

        )
        
        result = VGroup(
            dots, 
            lines
        )
        
        x_range = np.arange(
            x_min, 
            x_max, 
            dx
        )

        colors = color_gradient(
            
            [             ######################################################
                GRAY,     ######################################################
            YELLOW        ############# This section has no effect #############
            ], len(       ######################################################
                x_range   ######################################################
            )
        )

        for x, color in zip(
            x_range, 
            colors
        ):

            p1 = Dot(

            ).scale(
                scale_factor_for_dots
            ).move_to(
                Axes.input_to_graph_point(
                    x, 
                    function
                )
            )

            p2 = Dot(

            ).scale(
                scale_factor_for_dots
            ).move_to(
                Axes.input_to_graph_point(
                    x + dx, function
                )
            )

            dots.add(
                p1, 
                p2
            )

            dots.set_fill(
                dot_color, 
                opacity = dot_opacity
            )

            line = Line(
                p1.get_center(

                ), p2.get_center(

                ), stroke_color = line_color, stroke_width = line_width
            ).set_opacity(
                line_opacity
            )

            lines.add(
                line
            )

        return result