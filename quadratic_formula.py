import math
import cmath

def quad_solve(a,b,c):

    #Discriminant
    D = b*b - 4*a*c

    #If c = 0 -- One Real and One Zero Root
    if c == 0:
        print((-b+b) / (2*a))
        print((-b-b) / (2*a))

    #Positive Discriminant -- Real and Distinct Roots
    elif D > 0:
        SD = D**0.5; #Square Root of the Discriminant
        print((2*c) / (-b - SD))
        print((2*c) / (-b + SD))

    #Discriminant is Zero -- Real and Equal Roots
    elif D == 0:
        print(-b / (2*a))
        print(-b / (2*a))

    #Discriminant is Negative -- Complex and Distinct Roots
    else:
        print((-b - cmath.sqrt(D)) / (2*a))
        print((-b + cmath.sqrt(D)) / (2*a))

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a == 0:
    print('Not a Quadratic')

else:
    quad_solve(a,b,c)
