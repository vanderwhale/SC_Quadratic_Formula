import math
import cmath

def quad_solve(a,b,c):

    D = b*b - 4*a*c

    if D>0:
        SD = D**0.5;
        if b > 0: SD = -SD
        print((-b + SD) / (2*a))
        print((2*c) / (-b + SD))

    elif D == 0:
        print(-b / (2*a))
        print(-b / (2*a))

    else:
        print((-b - cmath.sqrt(D)) / (2*a))
        print((-b + cmath.sqrt(D)) / (2*a))

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a == 0:
    print('idiot')

else:
    quad_solve(a,b,c)
