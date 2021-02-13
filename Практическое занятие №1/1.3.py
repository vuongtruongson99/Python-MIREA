import math

def f(n, m):
    first = 0
    second = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            first += j**4 - math.tan(j) + 91
            second += 21*(i**5) - j**2

    return first / 87 + second

print("f(37, 53) = {:.2E}".format(f(37, 53)))
print("f(35, 93) = {:.2E}".format(f(35, 93)))
