from sympy import *
import matplotlib.pyplot as plt
from tools import intervalo_func
from tools import raizes_func

def grafico(exp):
    data,_ = intervalo_func(exp)
    
    fig, ax = plt.subplots()
    fig.suptitle("Gráfico da expressão")
    ax.plot(data[0,:],data[1,:])
    ax.grid(true)
    ax.set_ylim(data[0,0],data[0,-1])

    return fig

def calcular(exp1):
    _,intervalo = intervalo_func(exp1)

    dic = raizes_func(intervalo,exp1)

    return dic

def matrix_x(ordem):

    x = []
    for i in range(ordem):
        x.append(f"x{i+1}")

    return " ".join((r'\begin{bmatrix}',r"\\".join(x),r'\end{bmatrix}'))

if __name__ == "__main__":
    # Área para testes
    print(matrix_x(3))