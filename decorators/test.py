import math

def integrate_func(func, n):
    xi = 0
    omegai = (math.pi) / n
    i = 0
    while i <= n:
        sigma = xi + xi
        xi = omegai * (math.cos((math.pi * (2 * i - 1)) / (2 * n)))
        i += 1
        print(i)
    return sigma

def one_func(x): 
    return math.sqrt(1.0 - x * x)

assert math.fabs(integrate_func(one_func, 100) - 2.0) < 1.0e-3

assert math.fabs(integrate_func(math.cos, 100) - 2.403939430634413) < 1.0e-4
