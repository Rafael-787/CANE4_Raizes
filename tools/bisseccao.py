from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np

def bisseccao (intervalo,exp):
    a,b = intervalo
    i_old = b
    u = 0
    e = 1
    f = lambdify(x,exp,'numpy')

    while u < 3 or e < 10e-4:
        global c
        #global u
        i = (a+b)/2
        c = f(i)
        #print(f"f({i} = {c})")
        if c * f(b) <0 : 
            a = i
        else:
            b = i

        e = abs((i)-i_old)/abs(i)
        i_old = i
        #print(u)
        u += 1

    #print(f"Raiz: {i}  iterações:{u}")
    return i,u

if __name__ == "__main__":
    
    intervalo = (-5,0)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz, iterações = bisseccao(intervalo,exp1)
    print(f"Raiz: {raiz}  iterações:{iterações}")