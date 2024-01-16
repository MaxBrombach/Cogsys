import streamlit as st
import numpy as np


class UIInsertionsort:

    def __init__(self):
        pass

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]
        if 'buttonarray' not in st.session_state:
            st.session_state['buttonarray'] = np.zeros(6)
        sesbuttonvalues = st.session_state['buttonarray']
        print("jooo",sesbuttonvalues)

        for i in range(1, 6):
            sesbuttonvalues[i-1] = (columnlist[i-1].button("⠀" + str(i) + "⠀"))

        st.write(sesbuttonvalues)

