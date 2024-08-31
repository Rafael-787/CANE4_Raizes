from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np
from bisseccao import bisseccao
from newton import newton

def raiz(intervalo,formula):
    print("Iniciando calculo de raiz")
    print(f"intervalo: {intervalo}")
    print(f"formula: {formula}")
    xk,u = bisseccao(intervalo,formula)
    print(f"Finalizado bissecção: {xk}")
    r,i,e = newton(xk,formula)
    print("Finalizado Newton")
    print(f'raiz: {r}  iteração:{i+u}  erro:{e}')
    return r, i+u, e


if __name__ == "__main__":
    intervalo = (-5,0)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz(intervalo,exp1)