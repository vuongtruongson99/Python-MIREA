import math

def f(n):
    if n == 0:
        return 6
    else:
        return math.cos(f(n-1)) - math.sin(f(n-1))

print("f(3) = {:.2E}".format(f(3)))
print("f(9) = {:.2E}".format(f(9)))
