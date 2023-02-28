def get_histogram(possible_outcomes):
    result = VGroup()
    ax = Axes(
        x_range=[0, possible_outcomes],
        x_length=11,
        y_range=[0, 0.5],
        y_length=5,
        tips=False
    )
    x_nums = VGroup(
        *[
            Integer()
            .scale(0.75)
            .set_value(k)
            .next_to(ax.c2p(k, 0), DR, buff=0.35)
            for k in range(possible_outcomes)
        ]
    )
    y_nums = VGroup()
    value = 0
    for i in range(6):
        num = (
            Integer(value, unit = "\\%")
            .scale(0.5)
            .next_to(ax.c2p(0, i / 10), LEFT, buff=0.1)
        )
        value += 10
        y_nums.add(num)
    result.add(ax, x_nums, y_nums)
    result.to_edge(DL)
    return result