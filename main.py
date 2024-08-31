import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def latex_print(formula:str):
    st.latex(latex())


st.title("Raízes")

formula = st.text_input("insira a fórmula")
print(type(formula))

exp = sp.simplify(formula)

intervalo = (-100,100)
x = sp.symbols('x')
f = sp.lambdify(x,exp,'numpy')
#sp.nsolve(exp,x,[-5,10])

x_values = np.linspace(intervalo[0], intervalo[1], 10000)
y_values = f(x_values)
data = np.hstack((x_values,y_values))

if st.button("Visualizar"):
    st.latex(sp.latex(exp))
    

    fig, ax = plt.subplots()
    ax.plot(x_values,y_values)
    fig.suptitle(sp.latex(exp))
    ax.set_ylim(intervalo[0],intervalo[1])
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Fator N [G]')
    st.pyplot(fig)
