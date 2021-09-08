import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        string = str(self.x) + " " + str(self.y) + "\n"
        return string


def cmp(p):
    return p.x, -p.y


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


f = open("IO/2.in", "r")
g = open("IO/2.out", "w")
poligon = []
n = int(f.readline()[0])
for _ in range(n):
    point = list(map(int, f.readline().split()))
    poligon.append(Point(point[0], point[1]))


top_left = min(poligon, key=cmp)
pos = poligon.index(top_left)

aux = poligon[pos:]
aux.extend(poligon[:pos])
aux.append(aux[0])
L = [aux[0], aux[1]]

for i in range(2, n+1):
    L.append(aux[i])
    while len(L) > 2 and turn(L[-3], L[-2], L[-1]) != "stanga":
        L.pop(-2)
L.pop()

for i in L:
    g.write(str(i))

f.close()
g.close()
