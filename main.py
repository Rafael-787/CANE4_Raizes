import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcoes as fc
#from tools.intervalo import intervalo_func

st.title("Raízes")

exp = st.text_input("insira a expressão")

col1 , col2 = st.columns(2)

if  col1.button("Visualizar") and exp != '':
    st.latex(sp.latex(sp.simplify(exp)))
    st.pyplot(fc.grafico(exp))

if col2.button("calcular") and exp != '':
    st.latex(sp.latex(sp.simplify(exp)))
    st.table(fc.calcular(exp))
