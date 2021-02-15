import math

def f12(x):
    if x < 56:
        return "{:.2e}".format(math.sin(math.exp(x)) + math.sin(x) - 34)
    elif x >= 56 and x < 91:
        return "{:.2e}".format(21*(x**3) - math.cos(x))
    else:
        return "{:.2e}".format((x**3 + x/5 - 52)**4 - math.tan(x))
