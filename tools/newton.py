from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np

def newton(xk,exp):
    x = symbols('x')
    f = lambdify(x,exp,'numpy')
    derivada = diff(exp,x)
    f_dif = lambdify(x,derivada,'numpy')
    print(derivada)
    e = 1
    xk_old = xk
    u = 0


    while e >= 10e-4 or u >= 90:
        xk = xk - f(xk)/f_dif(xk)
        e = abs((xk)-xk_old)/abs(xk)
        xk_old = xk
        u += 1
        
    #print(f'raiz: {xk}  iteração:{u}  erro:{e}')
    return xk,u,e

if __name__ == "__main__":
    intervalo = (-5,0)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz,iterações,erro = newton(-5,exp1)
    print(f'raiz: {raiz}  iteração:{iterações}  erro:{erro}')