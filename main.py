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
    try:
        st.latex(sp.latex(sp.simplify(exp)))
        st.pyplot(fc.grafico(exp))
    except:
        if 'x' not in exp:
            st.error("Não há variável x na expressão.")
        else:
            st.error("Verifique a expressão.")

if col2.button("calcular") and exp != '':
    st.latex(sp.latex(sp.simplify(exp)))
    dic = fc.calcular(exp)
    print(dic)
    aviso = dic.pop("aviso")
    if dic != {}:
        if aviso != []:
            st.warning(aviso[1])
        st.table(dic)
    else:
        st.warning("Não foram encontradas raízes reais no intervalo [-100,100]")
