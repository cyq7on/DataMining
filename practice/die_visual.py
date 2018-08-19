import pygal

from practice.die import Die

die1 = Die()
die2 = Die(8)
result = []
for i in range(1000):
    result.append(die1.roll() + die2.roll())

freq = []
r = range(2, die1.num_sides + die2.num_sides + 1)
for roll in r:
    freq.append(result.count(roll))
print(freq)

bar = pygal.Bar()
# bar.x_labels = [str(x) for x in r]
bar.x_labels = map(str, r)
print(bar.x_labels)
bar.add("D6 + D6", freq)
bar.render_in_browser()

