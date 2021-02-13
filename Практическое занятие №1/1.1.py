import math

def f(x, y):
    first = float(math.sqrt((97*(y**7) + 80*(y**3)) / (y**3 + x**8)))
    second = math.sin(x) - math.sin(y)
    third = (x**4 - 34*x**5) / (x**7 + y**6)
    return first - second + third

print("f(-68, 19) = {:.2E}".format(f(-68, 19)))
print("f(-72, 19) = {:.2E}".format(f(-72, 19)))
