from practice.random_walk import RandomWalk
import matplotlib.pyplot as plot

rw = RandomWalk(50000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))

# 隐藏坐标轴
axes = plot.axes()
axes.xaxis.set_visible(False)
axes.yaxis.set_visible(False)

plot.scatter(rw.x, rw.y, c=point_numbers,
             edgecolor='none', s=1)

# 凸显起点和终点
plot.scatter(0, 0, c="green", edgecolor='none', s=100)
plot.scatter(rw.x[-1], rw.y[-1], c="red", edgecolor='none', s=100)
plot.show()
