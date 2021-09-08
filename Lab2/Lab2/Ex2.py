class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        string = str(self.x) + " " + str(self.y) + "\n"
        return string


def monotony(pol):
    # x-monotony
    leftest_point = min(pol, key=lambda p: p.x)
    left_index = pol.index(leftest_point)
    x_polygon = pol[left_index:]
    x_polygon.extend(pol[:left_index+1])
    x_mon = True
    x_decrease = False
    print(*x_polygon)
    for i in range(len(x_polygon)-1):
        if x_polygon[i].x > x_polygon[i+1].x:
            x_decrease = True
        if (x_decrease and x_polygon[i].x < x_polygon[i+1].x) or x_polygon[i].x == x_polygon[i+1].x:
            x_mon = False
            break
    # y-monotony
    lowest_point = min(pol, key=lambda p: p.y)
    lowest_index = pol.index(lowest_point)
    y_polygon = pol[lowest_index:]
    y_polygon.extend(pol[:lowest_index+1])
    y_mon = True
    y_decrease = False
    print()
    print(*y_polygon)
    for i in range(len(y_polygon)-1):
        if y_polygon[i].y > y_polygon[i+1].y:
            y_decrease = True
        if (y_decrease and y_polygon[i].y < y_polygon[i+1].y) or y_polygon[i].y == y_polygon[i+1].y:
            y_mon = False
            break

    print(x_mon, y_mon)
    x_word = "" if x_mon else "nu "
    y_word = "" if y_mon else "nu "
    g.write("Poligonul {}este x-monoton\n".format(x_word))
    g.write("Poligonul {}este y-monoton\n".format(y_word))


f = open("IO/Input22.txt", "r") # f = open("IO/Input2.txt", "r")
g = open("IO/Output2.txt", "w")
polygon = []
n = int(f.readline())
for _ in range(n):
    point = list(map(int, f.readline().split()))
    polygon.append(Point(point[0], point[1]))

monotony(polygon)
f.close()
g.close()
