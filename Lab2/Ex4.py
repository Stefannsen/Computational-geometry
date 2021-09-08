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


def legal_test():
    a, b, c, d = polygon[0], polygon[1], polygon[2], polygon[3]
    turn_triangle = turn(a, b, c)
    if turn_triangle == "coliniare":
        return "Cele 3 puncte sunt coliniare !"
    elif turn_triangle == "dreapta":
        a, c = c, a

    matrix = np.array([[a.x, a.y, a.x**2+a.y**2, 1],
                       [b.x, b.y, b.x**2+b.y**2, 1],
                       [c.x, c.y, c.x**2+c.y**2, 1],
                       [d.x, d.y, d.x**2+d.y**2, 1]])
    det = np.linalg.det(matrix)
    epsilon = 0.000001

    if -epsilon <= det <= epsilon:
        return "both legal"
    elif det < -epsilon:
        return "BD illegal"
    else:
        return "AC illegal"


f = open("IO/Input4.txt", "r")
# g = open("IO/Output3.txt", "w")
polygon = []
for _ in range(4):
    point = list(map(int, f.readline().split()))
    polygon.append(Point(point[0], point[1]))

print(legal_test())
f.close()
# g.close()
