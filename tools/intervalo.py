from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np

def intervalo(exp):
    interval = (-100,100) # Intervalo maior
    x = symbols('x')
    f = lambdify(x,exp,'numpy')
    
    # Cria uma lista com 10000 x entre o intervalo maior
    x_values = np.linspace(interval[0], interval[1], 10000)
    
    # Calcula o valor de Y para cada x
    y_values = f(x_values)
    
    # Cria uma matriz numpy com os valores xy
    data = np.vstack((x_values,y_values))
    
    # Faz a multiplicação dos elementos
    produto = y_values[1:] * y_values[:-1]

    # Cria uma lista com tuplas dos intervalos das raízes
    intervalos = [(lambda i: (data[0,i],data[0,i+1]))(i) for i in np.where(produto < 0)[0]] 

    #print(intervalos)
    return data,intervalos


if __name__ == "__main__":
    x = symbols('x')
    exp1 = x**3 - 9*x +3
    data, intervalo_r = intervalo(exp1)

    print(intervalo_r)