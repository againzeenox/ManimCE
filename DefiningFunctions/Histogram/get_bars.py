def get_bars(histogram, data):
    portions=np.array(data).astype(float)
    total=portions.sum()
    if total ==0:
        portions[:]=0
    else:
        portions/=total

    bars = VGroup()
            
    for x,prop in enumerate(portions):
        p1=VectorizedPoint().move_to(histogram[0].c2p(x, 0))
        p2=VectorizedPoint().move_to(histogram[0].c2p(x+1, 0))
        p3=VectorizedPoint().move_to(histogram[0].c2p(x+1,prop))
        p4=VectorizedPoint().move_to(histogram[0].c2p(x, prop))
        points=VGroup(p1,p2,p3,p4)
        bar=Rectangle().replace(points, stretch=True)
        bar.set_style(
            fill_color=[YELLOW,GREEN],
            fill_opacity=0.8,
            stroke_color=[YELLOW,GREEN]
        )
        bars.add(bar)
    return bars