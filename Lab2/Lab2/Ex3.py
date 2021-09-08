import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        string = str(self.x) + " " + str(self.y) + "\n"
        return string


def turn(p, q, r):
    matrix = np.array([[1, 1, 1], [p.x, q.x, r.x], [p.y, q.y, r.y]])
    det = np.linalg.det(matrix)
    epsilon = 0.000001

    if -epsilon <= det <= epsilon:
        return "coliniare"
    elif det < -epsilon:
        return "dreapta"
    else:
        return "stanga"


def position(p):
    a, b, c = triangle[0], triangle[1], triangle[2]
    turn_triangle = turn(a, b, c)
    if turn_triangle == "coliniare":
        return "Cele 3 puncte sunt coliniare !"
    elif turn_triangle == "dreapta":
        a, c = c, a

    matrix = np.array([[a.x, a.y, a.x**2+a.y**2, 1],
                       [b.x, b.y, b.x**2+b.y**2, 1],
                       [c.x, c.y, c.x**2+c.y**2, 1],
                       [p.x, p.y, p.x**2+p.y**2, 1]])
    det = np.linalg.det(matrix)
    epsilon = 0.000001

    if -epsilon <= det <= epsilon:
        return "conciclic"
    elif det < -epsilon:
        return "exterior"
    else:
        return "interior"


f = open("IO/Input3.txt", "r")
# g = open("IO/Output3.txt", "w")
triangle = []
points = []
for _ in range(3):
    point = list(map(int, f.readline().split()))
    triangle.append(Point(point[0], point[1]))
np_nr = int(f.readline())
for _ in range(np_nr):
    point = list(map(int, f.readline().split()))
    points.append(Point(point[0], point[1]))

for point in points:
    print(position(point))
    # g.write(position(point))

f.close()
# g.close()
