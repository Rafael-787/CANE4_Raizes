import streamlit as st
import pandas as pd
import numpy as np


x = x_old
a = np.zeros((x,x))

st.data_editor(a)

if st.button("Add row"):
    x = x_old + 1