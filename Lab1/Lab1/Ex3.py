import numpy as np


class Point:
    def __init__(self, x = 0, y = 0):
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

def preprocessing(pol):
    def cmp_left(p):
        return p.x, -p.y

    def cmp_right(p):
        return -p.x, -p.y

    leftest_point, rightest_point = min(pol, key=cmp_left), min(pol, key=cmp_right)

    l_index = pol.index(leftest_point)
    r_index = pol.index(rightest_point)
    print("------")
    print(l_index, r_index)
    if r_index > l_index:
        lower_frontier = pol[l_index:r_index+1]
        upper_frontier = pol[r_index:]
        upper_frontier.extend(pol[:l_index+1])
    else:
        upper_frontier = pol[r_index:l_index+1]
        lower_frontier = pol[l_index:]
        lower_frontier.extend(pol[:r_index+1])

    return lower_frontier, upper_frontier


def position(pt):
    global lower_fr, upper_fr

    def binary_search(arr, start, end, pt):
        if end >= start:
            mid = start + (end - start) // 2
            if mid + 1 > len(arr) - 1:
                return -1
            if arr[mid].x <= pt.x <= arr[mid + 1].x:
                if arr[mid].x < pt.x < arr[mid + 1].x:
                    return mid
                if arr[mid].x == pt.x == arr[mid + 1].x:
                    if arr[mid].y > pt.y > arr[mid+1].y or arr[mid].y < pt.y < arr[mid+1].y:
                        return mid
                    elif pt.y > arr[mid].y > arr[mid+1].y or pt.y < arr[mid].y < arr[mid+1].y:
                        return binary_search(arr, start, mid - 1, pt)
                    else:
                        return binary_search(arr, mid + 1, end, pt)
                elif arr[mid].x == pt.x:
                    if mid-1 > 0 and arr[mid-1].x == arr[mid].x:
                        return binary_search(arr, start, mid - 1, pt)
                    else:
                        return mid
                else:
                    if mid + 2 <= len(arr) - 1 and arr[mid + 2].x == arr[mid + 1].x:
                        print("aici")
                        return binary_search(arr, mid + 1, end, pt)
                    else:
                        return mid
            elif arr[mid].x >= pt.x:
                return binary_search(arr, start, mid - 1, pt)
            else:
                return binary_search(arr, mid + 1, end, pt)
        else:
            print("aaaaa")
            return -1

    print(pt.x, pt.y)
    l_index = binary_search(lower_fr, 0, len(lower_fr)-1, pt)

    if l_index == -1:
        return "outside"
    else:
        turn_io = turn(lower_fr[l_index], lower_fr[l_index+1], pt)
        turn_col = turn(lower_fr[l_index], pt, lower_fr[l_index+1])
        if turn_io == "dreapta":
            return "outside"
        elif turn_col == "coliniare":
            return "on edge"
        else:
            upper_fr.reverse()
            r_index = binary_search(upper_fr, 0, len(upper_fr) - 1, pt)
            turn_io = turn(upper_fr[r_index], upper_fr[r_index + 1], pt)
            turn_col = turn(upper_fr[r_index], pt, upper_fr[r_index + 1])
            if turn_io == "stanga":     # stanga pt upper_fr.reverse() == dreapta pt upper_fr
                return "outside"
            elif turn_col == "coliniare":
                return "on edge"
            else:
                return "inside"


f = open("IO/3.in", "r")
g = open("IO/3.out", "w")
polygon = []
points = []


n = int(f.readline()[0])
for _ in range(n):
    point = list(map(int, f.readline().split()))
    polygon.append(Point(point[0], point[1]))
lower_fr, upper_fr = preprocessing(polygon)
for i in lower_fr:
    print(i)
print()
for i in upper_fr:
    print(i)
m = int(f.readline()[0])
for _ in range(m):
    point = list(map(int, f.readline().split()))
    points.append(Point(point[0], point[1]))

for point in points:
    print("==")
    g.write(position(point) + "\n")

f.close()
g.close()
