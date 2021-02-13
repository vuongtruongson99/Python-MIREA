import math

def f(x):
    if x < 56:
        return math.sin(math.exp(x)) + math.sin(x) - 34
    elif x >= 56 and x < 91:
        return 21*(x**3) - math.cos(x)
    else:
        return (x**3 + x/5 - 52)**4 - math.tan(x)

print("f(59) = {:.2E}".format(f(59)))
print("f(86) = {:.2E}".format(f(86)))
