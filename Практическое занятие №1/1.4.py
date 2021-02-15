import math

def f14(n):
    if n == 0:
        return 6
    else:
        return "{:.2e}".format(math.cos(float(f14(n-1))) - math.sin(float(f14(n-1))))