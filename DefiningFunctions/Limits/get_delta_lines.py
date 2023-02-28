def get_delta_lines(x, dx, graph, axes, line_length = 20, color = WHITE):
    result = VGroup()
    line1 = DashedLine(
        start = ORIGIN, end = line_length * UP
    ).move_to(axes.c2p(x + dx, 0)).set_color(color = color)
    line2 = DashedLine(start=ORIGIN, end=line_length * UP).move_to(axes.c2p(x - dx, 0)).set_color(color = color)
    result.add(line1, line2)
    return result