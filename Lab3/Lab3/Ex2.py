from math import inf


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        string = str(self.x) + " " + str(self.y) + "\n"
        return string


def intersection(point, semi_plans):
    lim_sup_y = inf
    lim_inf_y = -inf
    lim_sup_x = inf
    lim_inf_x = -inf

    for cfs in semi_plans:
        a, b, c = cfs
        if a == 0:
            if b > 0:
                lim_sup_y = min(lim_sup_y, - c / b)
            elif b < 0:
                lim_inf_y = max(lim_inf_y, - c / b)
        elif b == 0:
            if a > 0:
                lim_sup_x = min(lim_sup_x, - c / a)
            elif a < 0:
                lim_inf_x = max(lim_inf_x, - c / a)

        if lim_inf_x > lim_sup_x or lim_inf_y > lim_sup_y:
            return -1

    if lim_inf_x > -inf and lim_inf_y > -inf and lim_sup_x < inf and lim_sup_y < inf:
        if lim_inf_x <= point.x <= lim_sup_x and lim_inf_y <= point.y <= lim_sup_y:
            aria = (lim_sup_y - lim_inf_y) * (lim_sup_x - lim_inf_x)
            return aria

    return -1


f = open("IO/Input2.txt", "r")
g = open("IO/Output2.txt", "w")

tests_counter = int(f.readline())
for _ in range(tests_counter):
    f.readline()
    x, y = list(map(float, f.readline().split()))
    n = int(f.readline())
    q = Point(x, y)
    semi_plans = []
    for _ in range(n):
        coefficients = list(map(float, f.readline().split()))
        semi_plans.append(tuple(coefficients))
    result = intersection(q, semi_plans)
    if result == -1:
        g.write("Nu exista\n")
    else:
        g.write("Exista " + str(result) + '\n')

f.close()
g.close()
