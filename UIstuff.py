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
            st.session_state['updatedIndex'] = -1
            st.session_state['selectedIndex1'] = -1
            st.session_state['selectedIndex2'] = -1

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
        if col3.button("Welche Zahl soll ich sortieren?"):
            if st.session_state['sortareaindex'] == 0:
                col4.info("Du muss die Zahl an folgender Position sortieren: " + str(st.session_state['sortareaindex'] + 2)+ " (Die 1. Zahl wird als sortiert angesehen :) )")
            else:
                col4.info("Du muss die Zahl an folgender Position sortieren: " + str(st.session_state['sortareaindex'] +2))


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


        # Variablen initiieren
        # -------------------------------------------------------------------------------------------------------------
        # Die Liste, die wir betrachten um die neue Zahl an die neue Stelle zu ordnen
        currentArray = st.session_state['startarray']
        # Die der index des "sortierten" bereiches (zahl vor der neu zu sortierenden Zahl)
        currentIndex = st.session_state['sortareaindex']
        ordingprocess = st.session_state

        # schaut, welches element nach noch verglichen werden muss in der liste (i--)
        # zum anfang schauen wir uns die aktuelle position an
        # danach wird dies reduziert um das vergleichen zu ermöglichen

        if st.session_state['updatedIndex'] == -1:
            st.session_state['updatedIndex'] = currentIndex

        updatedIndex = st.session_state['updatedIndex']

        # -------------------------------------------------------------------------------------------------------------

        # Wählen / neu wählen der Elemente durch klicken
        # -------------------------------------------------------------------------------------------------------------
        trueindx = np.where(st.session_state['buttonarray'])[0]

        #print(trueindx)

        if len(trueindx) == 2:
            st.session_state['selectedIndex1'] = trueindx[0]
            st.session_state['selectedIndex2'] = trueindx[1]

        selectedindex1 = st.session_state['selectedIndex1']
        selectedindex2 = st.session_state['selectedIndex2']

        # Ausgabe der momentan gewählten Zahlen (zum debuggen)
        if selectedindex1 == -1 or selectedindex2 == -1:
            st.info('Wähle 2 Zahlen zum Tauschen')
        else:
            st.info("Choice: Stelle1 = " + str(selectedindex1) + " und Stelle2 = "+ str(selectedindex2))
        # -------------------------------------------------------------------------------------------------------------

        if len(trueindx) == 2:
            if st.button("Zahlen neu wählen"):
                self.resetButtonarray()
                st.session_state['selectedIndex1'] = -1
                st.session_state['selectedIndex2'] = -1
                st.rerun()

        #Tauschprozess 'nach vorne'
        # -------------------------------------------------------------------------------------------------------------
        if st.button("Tauschen"):
            # checken, ob der user ueerhaupt die zahlen geklickt hat
            trueindx = np.where(st.session_state['buttonarray'])[0]
            if len(trueindx) < 2:
                st.info("Wähle 2 Zahlen durch das Klicken auf eine Zahl in der obigen Liste")
                pass
            # wenn ja, dann schauen wir ob der swap passt und durchgefuehrt werden darf
            else:
                result = self.tutor.isSwapValid(selectedindex1, selectedindex2, updatedIndex, currentArray)

                if result == "True":
                    updatedIndex = updatedIndex - 1
                    st.session_state['updatedIndex'] = updatedIndex
                    print("updated Index: " + str(updatedIndex))
                    self.tauschearray() # todo übergebe die indize zum tauschen (momentan wird nur das 1. und 2. element getauscht, alles andere wird missachtet)
                    #update den neuen index zum vergleichen mit der zahl davor
                    self.openTauschDialog()
                    return st.info("nice")
                elif result == "beginning of list":
                     st.info("Der Listenanfang ist erreicht")
                elif result == "wrong swap max":
                     st.info("Die Zahl ... ist größer als ...")
                elif result == "wrong swap":
                     st.info("Das stimmt leider nicht")

        if st.button("Korrekt eingeordnet?"):
            if self.tutor.isAtCorrectPosition(updatedIndex, currentArray):
                #wenn korrekt sortedarea wird inkrementiert
                #self.resetSelectedIndex()
                st.session_state['selectedIndex1'] = -1
                st.session_state['selectedIndex2'] = -1
                st.session_state['updatedIndex'] = -1
                st.session_state['sortareaindex'] += 1
                st.session_state['orderingprocess'] = False
                st.session_state['alreadypressed'] = False
                st.rerun()
            else:
                st.info("Das Element ist noch nicht richtig eingeordnet")
        # ------------------------------------------------------------------------------------------------------------


