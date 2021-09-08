from math import inf


def intersection(semi_plans):
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
            return "Intersectie vida"

    if lim_inf_x > -inf and lim_inf_y > -inf and lim_sup_x < inf and lim_sup_y < inf:
        return "Intersectie nevida marginita"
    else:
        return "Intersectie nevida nemarginita"


f = open("IO/Input1.txt", "r")
g = open("IO/Output1.txt", "w")

tests_counter = int(f.readline())
for _ in range(tests_counter):
    n = int(f.readline())
    semi_plans = []
    for _ in range(n):
        coefficients = list(map(float, f.readline().split()))
        semi_plans.append(tuple(coefficients))
    g.write(intersection(semi_plans) + '\n')

f.close()
g.close()
