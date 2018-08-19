from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x = [0]
        self.y = [0]

    def get_next_step(self):
        dis_list = list(range(1, 5))

        direction = choice([-1, 1])
        distance = choice(dis_list)
        next_x = self.x[-1] + direction * distance

        direction = choice([-1, 1])
        distance = choice(dis_list)
        next_y = self.y[-1] + direction * distance
        return next_x, next_y

    def fill_walk(self):
        while len(self.x) < self.num_points:
            next_x, next_y = self.get_next_step()
            if next_x == self.x[-1] and next_y == self.y[-1]:
                continue
            self.x.append(next_x)
            self.y.append(next_y)
