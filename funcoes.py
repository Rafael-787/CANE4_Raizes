from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np
from tools import intervalo_func
from tools import raizes_func

def grafico(exp):
    data,_ = intervalo_func(exp)
    
    fig, ax = plt.subplots()
    fig.suptitle("Gráfico da expressão")
    ax.plot(data[0,:],data[1,:])
    ax.grid(true)
    ax.set_ylim(data[0,0],data[0,-1])
    #ax.set_xlabel('Tempo [s]')
    #ax.set_ylabel('Fator N [G]')


    return fig

def calcular(exp1):
    _,intervalo = intervalo_func(exp1)

    dic = raizes_func(intervalo,exp1)

    return dic

if __name__ == "__main__":
    # Área para testes
    x = symbols('x')
    exp1 = x**3 - 9*x +3
    print(calcular(exp1))