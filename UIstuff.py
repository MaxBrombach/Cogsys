import streamlit as st
import numpy as np
from numpy.core._multiarray_umath import dtype


class UIInsertionsort:

    def __init__(self):
        pass

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]
        if 'buttonarray' not in st.session_state:
            st.session_state['buttonarray'] = np.zeros(6, dtype=bool)

        mystate = st.session_state['buttonarray']
        buttonvalues = np.zeros(6, dtype=bool)

        for i in range(1, 6):
            buttonvalues[i-1] = (columnlist[i-1].button("⠀" + str(i) + "⠀"))

        newarray = np.logical_or(mystate, buttonvalues)
        st.write(newarray)

