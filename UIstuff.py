import streamlit as st
import numpy as np
import Notification
import logic


class UIInsertionsort:


    def __init__(self):
        self.no = Notification.Notification()
        self.logic = logic.Logic()
        if 'startarray' not in st.session_state:
            st.session_state['startarray'] = [2, 4, 3, 8, 7]

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]

        #initialisiere session state
        if 'buttonarray' not in st.session_state:
            st.session_state['buttonarray'] = np.zeros(5, dtype=bool)

        buttonvalues = np.zeros(5, dtype=bool)

        for i in range(5):
            buttonvalues[i] = (columnlist[i].button("⠀" + str(st.session_state['startarray'][i]) + "⠀"))

        st.session_state['buttonarray'] = np.logical_or(st.session_state['buttonarray'], buttonvalues)

        st.info("Muss getauscht werden?")
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
        if col1.button("Ja"):
            # liegt der User richtig oder falsch? -> handlen
            if self.logic.iscorrect():

                self.openTauschDialog()
            else:
                self.no.custom_error()
        if col2.button("Nein"):
            if self.logic.iscorrect():
                pass
            else:
                self.no.custom_error()




    def tauschearray(self, boolarray: np.array):
        trueindx = np.where(boolarray)[0]
        st.session_state['startarray'][trueindx[0]], st.session_state['startarray'][trueindx[1]] = st.session_state['startarray'][trueindx[1]], st.session_state['startarray'][trueindx[0]]
        #reset array
        st.session_state['buttonarray'] = np.zeros(5, dtype=bool)
        st.rerun()

    def resetButtonarray(self):
        """
        sets the array to false
        :return:
        """
        st.session_state['buttonarray'] = np.zeros(5, dtype=bool)

    def openTauschDialog(self):
        self.no.custom_info("Welche zwei Zahlen müssen getauscht werden")

