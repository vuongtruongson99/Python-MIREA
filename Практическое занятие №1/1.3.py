import math

def f13(n, m):
    first = 0
    second = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            first += j**4 - math.tan(j) + 91
            second += 21*(i**5) - j**2

    return "{:.2e}".format(first / 87 + second)
