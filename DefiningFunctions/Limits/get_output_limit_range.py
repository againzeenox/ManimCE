def get_output_limit_range(x, graph, dx, range, axes):
    result = VGroup()
    dot = Circle(radius=0.07).set_color(YELLOW).move_to(axes.c2p(x + 0.00000001, graph.underlying_function(x + 0.0000001)))
    result.add(dot)
    for x in np.arange(x - range, x + range, dx):
        if 0 - dx < x < 0 + dx:
            line = VectorizedPoint
        else:
            line = Line(
                start = axes.c2p(x, graph.underlying_function(x)),
                end=axes.c2p(x + dx, graph.underlying_function(x + dx))
            ).set_color(YELLOW)
            result.add(line)
    return result