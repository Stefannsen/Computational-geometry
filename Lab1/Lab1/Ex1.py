import numpy as np


def turn(x1, y1, x2, y2, x3, y3):
    matrix = np.array([[1, 1, 1], [x1, x2, x3], [y1, y2, y3]])
    det = np.linalg.det(matrix)
    epsilon = 0.000001

    if -epsilon <= det <= epsilon:
        return "coliniare"
    elif det < -epsilon:
        return "dreapta"
    else:
        return "stanga"


f = open("IO/1.in", "r")
g = open("IO/1.out", "w")
n = int(f.readline()[0])
arr = []
for _ in range(n):
    for _ in range(n):
        arr.extend(list(map(int, f.readline().split())))
    g.write(turn(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]) + '\n')
    arr = []

f.close()
g.close()
