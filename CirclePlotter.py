import math
pi = math.pi


def circle_coords(radius, points, centre):
    return [((math.cos(2 * pi / points * x) * radius)+centre[0], (math.sin(2 * pi / points * x) * radius)+centre[1]) for x in range(0, points)]


if __name__ == "__main__":
    print(circle_coords(10, 36, (10.05476, 6.09875)))
