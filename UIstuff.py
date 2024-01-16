import streamlit as st
import numpy as np
from numpy.core._multiarray_umath import dtype


class UIInsertionsort:

    def __init__(self):
        self.startarray = [2, 4, 3, 8, 7]

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]
        if 'buttonarray' not in st.session_state:
            st.session_state['buttonarray'] = np.zeros(5, dtype=bool)


        buttonvalues = np.zeros(5, dtype=bool)
        st.write("Sessions", st.session_state['buttonarray'])

        for i in range(5):
            buttonvalues[i] = (columnlist[i].button("⠀" + str(self.startarray[i]) + "⠀"))

        st.session_state['buttonarray'] = np.logical_or(st.session_state['buttonarray'], buttonvalues)
        st.write(st.session_state['buttonarray'])

