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
            st.session_state['orderingprocess'] = False

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

        # Todo maybe hide these buttons as long as the user swaps one number beneath
        st.info("Muss getauscht werden?")
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
        if col1.button("Ja") or st.session_state['alreadypressed'] or st.session_state['orderingprocess']:
            st.session_state['alreadypressed'] = True

            # liegt der User richtig oder falsch? -> handlen
            if self.logic.swapneeded(st.session_state['sortareaindex'], st.session_state['startarray']) or st.session_state['orderingprocess']:
                self.openTauschDialog()
            else:
                self.tutor.noSwapNeeded()

        if col2.button("Nein"):
            if not self.logic.swapneeded(st.session_state['sortareaindex'], st.session_state['startarray']):
                st.session_state['sortareaindex'] += 1
                st.rerun()
            else:
                self.tutor.swapNeeded()

        # if user needs help to know which number he currently needs to sort
        # todo Refactor into notifications
        if col3.button("Which number do i need to sort next?"):
            col4.info("You have to sort the number at position " + str(st.session_state['sortareaindex']))


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
        st.session_state['orderingprocess'] = True

        # Die Liste, die wir betrachten um die neue Zahl an die neue Stelle zu ordnen
        currentArray = st.session_state['startarray']
        # Die der index des "sortierten" bereiches (zahl vor der neu zu sortierenden Zahl)
        currentIndex = st.session_state['sortareaindex']
        ordingprocess = st.session_state
        selectedIndex1 = 0
        selectedIndex2 = 0


        if st.button("Tauschen"):
            # checken, ob der user ueerhaupt die zahlen geklickt hat
            trueindx = np.where(st.session_state['buttonarray'])[0]
            if len(trueindx) == 0:
                st.info("Choose 2 numbers by clicking on them in the list above")
                pass
            # wenn ja, dann schauen wir ob der swap passt und durchgefuehrt werden darf
            else:
                try:
                    if self.tutor.isSwapValid(selectedIndex1, selectedIndex2, currentIndex, currentArray):
                        self.tauschearray()
                        self.openTauschDialog()
                        return st.info("nice")
                # bei fehlern werden exceptions ausgegeben, welche dann die richtige information weiterleiten soll
                except Exception as e:
                    print(e)
                    st.info("Das ist nicht ganz richtig, versuche es nochmal")

        if st.button("Korrekt eingeordnet?"):
            if self.tutor.isAtCorrectPosition(currentIndex, currentArray):
                #wenn korrekt sortedarea wird inkrementiert
                st.session_state['sortareaindex'] += 1
                st.session_state['orderingprocess'] = False
                st.session_state['alreadypressed'] = False
                st.rerun()
            else:
                st.info("Das Element ist noch nicht richtig eingeordnet")






