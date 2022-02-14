#!/usr/bin/pyhton3
print('Solve Quadratic Equation:')

import math
import cmath
def quad_solve(a,b,c):
    D = b*b - 4*a*c
    SD = D**0.5

    if (D>0):
        x1 = (-b + SD / (2*a)
        x2 = (2*c) / (-b+SD)
    return x1, x2
print(quad_solve(1,1e10,4))
