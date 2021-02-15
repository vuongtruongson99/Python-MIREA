import math

def f11(x, y):
    first = float(math.sqrt((97*(y**7) + 80*(y**3)) / (y**3 + x**8)))
    second = math.sin(x) - math.sin(y)
    third = (x**4 - 34*x**5) / (x**7 + y**6)
    return "{:.2e}".format(first - second + third)
