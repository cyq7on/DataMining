import matplotlib.pyplot as plot

input_range = range(1, 10)
squares = [x * x for x in input_range]
print(squares)
print(list(input_range[:-1]))
plot.plot(input_range, squares, linewidth=5)
plot.title("square number".title(), fontsize=24)
plot.xlabel("x")
plot.ylabel("y")
plot.show()
