from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np
import math
from .raiz import raiz_func

def raizes_func(intervalos,exp):
    dic = {}
    for n,i in enumerate(intervalos):
        r,it,e = raiz_func(i,exp)
        dic[n+1] = {
                "raiz":r,
                "intervalo":i,
                "interações":it,
                "erro":"{:.2e}".format(e)
                }
        print(f" raiz {n+1} ok")
    return dic

if __name__ == "__main__":
    from intervalo import intervalo

    x = symbols('x')
    exp1 = x**3 - 9*x +3
    _,intervalos = intervalo(exp1)
    dict = raizes_func(intervalos,exp1)
    print(dict)