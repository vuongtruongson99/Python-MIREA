import math

def f11(x, y):
    first = float(math.sqrt((97*(y**7) + 80*(y**3)) / (y**3 + x**8)))
    second = math.sin(x) - math.sin(y)
    third = (x**4 - 34*x**5) / (x**7 + y**6)
    return first - second + third

def f12(x):
    if x < 56:
        return math.sin(math.exp(x)) + math.sin(x) - 34
    elif x >= 56 and x < 91:
        return 21*(x**3) - math.cos(x)
    else:
        return (x**3 + x/5 - 52)**4 - math.tan(x)

def f13(n, m):
    first = 0
    second = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            first += j**4 - math.tan(j) + 91
            second += 21*(i**5) - j**2

    return first / 87 + second

def f14(n):
    if n == 0:
        return 6
    else:
        return math.cos(float(f14(n-1))) - math.sin(float(f14(n-1)))
