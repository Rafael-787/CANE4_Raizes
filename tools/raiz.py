from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np
from bisseccao import bisseccao
from newton import newton

def raiz(intervalo,formula):
    xk,u = bisseccao(intervalo,formula)
    print(xk)
    r,i,e = newton(xk,formula)
    print(f'raiz: {r}  iteração:{i+u}  erro:{e}')


if __name__ == "__main__":
    intervalo = (-5,0)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz(intervalo,exp1)