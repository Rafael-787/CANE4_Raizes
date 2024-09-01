from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np
from .bisseccao import bisseccao_func
from .newton import newton_func

def raiz_func(intervalo,formula):
    print("Iniciando calculo de raiz")
    print(f"intervalo: {intervalo}")
    print(f"formula: {formula}")
    xk,u = bisseccao_func(intervalo,formula)
    print(f"Finalizado bissecção: {xk}")
    r,i,e = newton_func(xk,formula)
    print("Finalizado Newton")
    print(f'raiz: {r}  iteração:{i+u}  erro:{e}')
    return r, i+u, e


if __name__ == "__main__":
    intervalo = (-5,0)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz_func(intervalo,exp1)