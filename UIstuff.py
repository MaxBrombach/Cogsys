from time import sleep

import streamlit as st
import numpy as np
import Notification
import logic
import TutorModel



class UIInsertionsort:


    def __init__(self):
        self.no = Notification.Notification()
        self.logic = logic.Logic()
        self.tutor = TutorModel.TutorModel()
        self.initializeSessionstates()


    def initializeSessionstates(self):
        if 'alreadypressed' not in st.session_state:
            st.session_state['startarray'] = [2, 4, 3, 8, 1]
            st.session_state['sortareaindex'] = 0
            st.session_state['alreadypressed'] = False
            st.session_state['buttonarray'] = np.zeros(5, dtype=bool)

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]


        buttonvalues = np.zeros(5, dtype=bool)

        for i in range(5):
            if i > st.session_state['sortareaindex']:
                buttonvalues[i] = (columnlist[i].button("⠀" + str(st.session_state['startarray'][i]) + "⠀"))
            else:
                buttonvalues[i] = (columnlist[i].button("<" + str(st.session_state['startarray'][i]) + ">"))

        st.session_state['buttonarray'] = np.logical_or(st.session_state['buttonarray'], buttonvalues)

        st.info("Muss getauscht werden?")
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
        if col1.button("Ja") or st.session_state['alreadypressed']:
            st.session_state['alreadypressed'] = True

            # liegt der User richtig oder falsch? -> handlen
            if self.logic.swapneeded(st.session_state['sortareaindex'], st.session_state['startarray']):
                self.openTauschDialog()
            else:
                self.tutor.noSwapNeeded()

        if col2.button("Nein"):
            if not self.logic.swapneeded(st.session_state['sortareaindex'], st.session_state['startarray']):
                st.session_state['sortareaindex'] += 1
                st.rerun()
            else:
                self.tutor.swapNeeded()





    def tauschearray(self):

        trueindx = np.where(st.session_state['buttonarray'])[0]
        temp = st.session_state['startarray'][trueindx[0]]
        st.session_state['startarray'][trueindx[0]] = st.session_state['startarray'][trueindx[1]]
        st.session_state['startarray'][trueindx[1]] = temp
        st.success(f"Die Zahlen {st.session_state['startarray'][trueindx[0]]} und {st.session_state['startarray'][trueindx[1]]} wurden getauscht")
        self.resetButtonarray()
        st.session_state['alreadypressed'] = False
        sleep(1)
        #reset array


        st.rerun()

    def resetButtonarray(self):
        """
        sets the array to false
        :return:
        """
        st.session_state['buttonarray'] = np.zeros(5, dtype=bool)

    def openTauschDialog(self):
        st.info("Tausche bis die Zahl korrekt eingeordnet ist")
        if st.button("Tauschen"):
            if self.tutor.isSwapValid():
                self.tauschearray()
            else:
                pass

        if st.button("Korrekt eingeordnet?"):
            if self.tutor.isatCorrectPosition():
                #wenn korrekt sortedarea wird inkrementiert
                st.session_state['sortareaindex'] += 1







