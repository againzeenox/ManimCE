def update(dummy,n_added_data_points=0):
    new_row=get_random_row()
    row.become(new_row)
    count=sum([m.positive for m in new_row.nums])
    data[count]+=1
    if n_added_data_points:
        values=np.random.random((n_added_data_points, 10))
        counts=(values<0.2).sum(1)
        for i in range(len(data)):
            data[i]+=(counts==i).sum()
    bars.become(get_bars(histogram=histogram,data=data))
    arrow.next_to(bars[count], UP, buff=0.1)
    bars[2].set_style(
        fill_color=[BLUE_B, BLUE_D], fill_opacity=0.8, stroke_color=BLUE
    )