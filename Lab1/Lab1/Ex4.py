import math
import numpy as np


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        string = str(self.x) + " " + str(self.y) + "  "
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


def convex_cover(points):
    def cmp(p):
        return p.x, p.y

    def parse(points):
        L = [points[0], points[1]]
        for i in range(2, len(points)):
            L.append(points[i])
            while len(L) > 2 and turn(L[-3], L[-2], L[-1]) != "stanga":
                L.pop(-2)
        L.pop()
        return L

    points.sort(key=cmp)
    L = parse(points)
    points.reverse()
    L.extend(parse(points))
    return L


def distance(p, q):
    return math.sqrt((p.x-q.x) ** 2 + (p.y-q.y) ** 2)


def compare(p):
    return p[2], p[0].x, p[0].y


f = open("IO/4.in", "r")
g = open("IO/4.out", "w")
polygon = []

n = int(f.readline()[0])
for _ in range(n):
    point = list(map(int, f.readline().split()))
    polygon.append(Point(point[0], point[1]))

convex = convex_cover(polygon)
convex.append(convex[0])
not_in_cover = []
for x in polygon:
    if x not in convex:
        not_in_cover.append(x)

while len(not_in_cover) > 0:
    pts = []
    for p in not_in_cover:
        mini = math.inf
        pos = -1
        for i in range(len(convex)-1):
            dist = distance(p, convex[i]) + distance(p, convex[i+1])\
                   - distance(convex[i], convex[i+1])
            if mini > dist:
                mini = dist
                pos = i
        r = (distance(convex[pos], p) + distance(p, convex[pos+1])) / distance(convex[pos], convex[pos+1])
        pts.append((p, pos+1, r))

    t = min(pts, key=compare)
    not_in_cover.remove(t[0])
    convex.insert(t[1], t[0])

for i in convex:
    print(i)
f.close()
g.close()
