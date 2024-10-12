import streamlit as st
import numpy as np
import funcoes as fc
from tools import met_gauss


if 'shape' not in st.session_state:
    st.session_state.shape = 2

shape = st.session_state.shape
ma = np.zeros((shape,shape))
mb = np.zeros((shape,1))

st.title("Sistema Linear")
with st.container():
    col1, col2, col3 = st.columns(3,vertical_alignment='center')

    col1.data_editor(ma)

    matrix_x = fc.matrix_x(shape)
    col2.latex(f"X {matrix_x} = ")

    col3.data_editor(mb)

with st.container():
    col1, col2, col3 = st.columns(3,gap="small")
    if col1.button("Add row"):
        st.session_state.shape = shape + 1
        st.rerun()

    if col1.button("Clear"):
        st.session_state.shape = 2
        st.rerun()

    if col3.button("Calcular"):
        dic = met_gauss(ma,mb)
        if dic["aviso"] != "":
            st.warning(dic["aviso"])
        else:
            st.divider()
            with st.container():
                st.subheader("Solução")
                latex_solucao = fc.array_matrix(np.array(dic["resolução"]).reshape(-1, 1))
                st.latex(f"{matrix_x} = {latex_solucao}")
                
                
                with st.expander("Detalhes"):
                    st.markdown(f"""
                            **Ordem**: {dic["ordem"]} \n
                            **Número de trocas**: {dic["n_trocas"]} \n
                            **Matrix escalonada**: \n
                                """)
                    st.latex(fc.array_matrix(dic["escalonada"]))

