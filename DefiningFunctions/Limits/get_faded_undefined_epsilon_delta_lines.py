def get_faded_undefined_epsilon_delta_lines(
    x, graph, axes, line_length = 20, color = WHITE, opacity = 0.5
):
    result = VGroup()
    epsilon_line = DashedLine(start = ORIGIN, end = line_length * RIGHT).set_color(color).move_to(axes.c2p(x + 0.0000001, graph.underlying_function(x + 0.0000001))).set_opacity(opacity)
    delta_line = DashedLine(start = ORIGIN, end = line_length * UP).set_color(color).move_to(axes.c2p(x, 0)).set_opacity(opacity)
    result.add(epsilon_line, delta_line)