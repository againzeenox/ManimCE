def get_epsilon_lines(x, dx, graph, axes, line_length = 20, color = WHITE):
    result = VGroup()
    line1 = DashedLine(
        start = ORIGIN, end = line_length * RIGHT
    ).move_to(axes.c2p(x + dx, graph.underlying_function(x + dx))).set_color(color = color)

    dot1 = Circle(radius=0.07).set_color(color=color).move_to(axes.c2p(x + dx, graph.underlying_function(x + dx)))

    line2 = DashedLine(start=ORIGIN, end=line_length * RIGHT).move_to(axes.c2p(x - dx, graph.underlying_function(x - dx))).set_color(color = color)

    dot2 = Circle(radius=0.07).set_color(color=color).move_to(axes.c2p(x - dx, graph.underlying_function(x - dx)))
    result.add(line1, line2, dot1, dot2)

    return result