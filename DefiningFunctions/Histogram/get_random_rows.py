def get_random_row(s=0.2, n=10):
    values = np.random.random(n)
    nums = VGroup()
    syms = VGroup()
    for x, value in enumerate(values):
        num = DecimalNumber(value)
        num.set(height=0.25)
        num.move_to(x*RIGHT)
        num.positive = num.get_value()<s
        if num.positive:
            num.set_color(GREEN)
            sym = Tex("TRUE").scale(2).set_color(GREEN)
        else:
            num.set_color(RED)
            sym = Tex("FALSE").scale(2).set_color(RED)
        sym.match_color(num)
        sym.match_height(num)
        sym.positive=num.positive
        sym.next_to(num, DOWN, buff=0.25)

        nums.add(num)
        syms.add(sym)

    row = VGroup(nums,syms)
    row.nums= nums
    row.syms=syms
    row.n_positive=sum([m.positive for m in nums])

    row.center().to_edge(UP, buff=0)
    return row