import streamlit as st
import numpy as np
import Notification


class UIInsertionsort:
    no = Notification.Notification()

    def __init__(self):
        if 'startarray' not in st.session_state:
            st.session_state['startarray'] = [2, 4, 3, 8, 7]

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]

        #initialisiere session state
        if 'buttonarray' not in st.session_state:
            st.session_state['buttonarray'] = np.zeros(5, dtype=bool)

        buttonvalues = np.zeros(5, dtype=bool)
        st.write("Sessions", st.session_state['buttonarray'])

        for i in range(5):
            buttonvalues[i] = (columnlist[i].button("⠀" + str(st.session_state['startarray'][i]) + "⠀"))

        st.session_state['buttonarray'] = np.logical_or(st.session_state['buttonarray'], buttonvalues)
        st.write(st.session_state['buttonarray'])

        # Test Notifications
        self.no.custom_info("this is an info")
        self.no.custom_warning("this is a warning")
        self.no.custom_error("this is an error")

        if st.button("Tausche"):
            self.tauschearray(st.session_state['buttonarray'])

    def tauschearray(self, boolarray: np.array):
        trueindx = np.where(boolarray)[0]
        st.session_state['startarray'][trueindx[0]], st.session_state['startarray'][trueindx[1]] = st.session_state['startarray'][trueindx[1]], st.session_state['startarray'][trueindx[0]]
        #reset array
        st.session_state['buttonarray'] = np.zeros(5, dtype=bool)
        st.rerun()

