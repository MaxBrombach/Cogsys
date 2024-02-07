from time import sleep

import streamlit as st
import numpy as np
import logic
import TutorModel
import random


class UIInsertionsort:

    def __init__(self):
        self.logic = logic.Logic()
        self.tutor = TutorModel.TutorModel()
        self.initializeSessionstates()

    def rand_array(self):
        list = []
        while len(list) != 5:
            random_number = random.randint(1,10)
            if random_number not in list:
                list.append(random_number)
        return list

    def initializeSessionstates(self):
        if 'alreadypressed' not in st.session_state or 'finished_run' in st.session_state:
            st.session_state['startarray'] = self.rand_array()
            st.session_state['sortareaindex'] = 0
            st.session_state['alreadypressed'] = False
            st.session_state['buttonarray'] = np.zeros(5, dtype=bool)
            st.session_state['orderingprocess'] = False
            st.session_state['updatedIndex'] = -2
            st.session_state['selectedIndex1'] = -1
            st.session_state['selectedIndex2'] = -1
            st.session_state['triggeronetimererun'] = True

    def createButtonArray(self):
        info_text = st.empty()
        info_text.write("Sortiere die Liste, bis alle Elemente an der richtigen Stelle stehen. "
                        "Bereits sortierte Zahlen werden mit spizen Klammern, z.B. <Zahl> gekennzeichnet. Viel Spaß!")
        columns = st.empty()
        col1, col2, col3, col4, col5 = columns.columns((1, 1, 1, 1, 1))
        columnlist = [col1, col2, col3, col4, col5]

        buttonvalues = np.zeros(5, dtype=bool)

        for i in range(5):
            if i > st.session_state['sortareaindex']:
                buttonvalues[i] = (columnlist[i].button("⠀" + str(st.session_state['startarray'][i]) + "⠀"))
            else:
                buttonvalues[i] = (columnlist[i].button("<" + str(st.session_state['startarray'][i]) + ">"))

        st.session_state['buttonarray'] = np.logical_or(st.session_state['buttonarray'], buttonvalues)

        if st.session_state['sortareaindex'] == len(st.session_state['startarray']) - 1:
            st.session_state['finished_run'] = True
            st.session_state['exercisestart'] = False
            self.initializeSessionstates()
            columns.empty()
            st.rerun()
            return()

        if not st.session_state['orderingprocess']:
            st.info("Muss getauscht werden?")
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

        current_number = st.session_state['startarray'][st.session_state['sortareaindex'] + 1]
        compare_number = st.session_state['startarray'][st.session_state['sortareaindex']]
        current_position = st.session_state['sortareaindex'] + 2

        # TODO wenn im ordering process disable buttons
        if col1.button("Ja", disabled=st.session_state['orderingprocess']) or st.session_state['orderingprocess']:
            st.session_state['alreadypressed'] = True

            # liegt der User richtig oder falsch? -> handlen
            if self.logic.swapneeded(st.session_state['sortareaindex'], st.session_state['startarray']) or \
                    st.session_state['orderingprocess']:
                #muss hier checken, ob der orderingprocess noch läuft, sonst kann während des tauschprozesses nicht das user modell verwendet werden
                if not st.session_state['orderingprocess']:
                    st.session_state['userModel'].reset_tries()
                self.openTauschDialog()
            else:
                self.tutor.noSwapNeeded(current_number, compare_number)

        if col2.button("Nein", disabled=st.session_state['orderingprocess']):
            if not self.logic.swapneeded(st.session_state['sortareaindex'], st.session_state['startarray']):
                st.session_state['sortareaindex'] += 1
                if not st.session_state['orderingprocess']:
                     st.session_state['userModel'].reset_tries()
                st.rerun()
            else:
                self.tutor.swapNeeded(current_number, compare_number)

        # if user needs help to know which number he currently needs to sort
        # todo Refactor into notifications
        if col3.button("Welche Zahl soll ich sortieren?"):
            if st.session_state['sortareaindex'] == 0:
                if st.session_state['orderingprocess']:
                    current_position = st.session_state['updatedIndex'] + 2
                    current_number = st.session_state['startarray'][st.session_state['updatedIndex'] + 1]
                col4.info("Du muss die Zahl " + str(current_number) +
                          " an Position " + str(current_position)
                          + " sortieren. (Die 1. Zahl wird als sortiert angesehen :)")
            else:
                if st.session_state['orderingprocess']:
                    current_position = st.session_state['updatedIndex'] + 2
                    current_number = st.session_state['startarray'][st.session_state['updatedIndex'] + 1]
                col4.info("Du muss die Zahl " + str(current_number) +
                          " an Position " + str(current_position)
                          + " sortieren.")

    def tauschearray(self):
        trueindx = np.where(st.session_state['buttonarray'])[0]
        temp = st.session_state['startarray'][trueindx[0]]
        st.session_state['startarray'][trueindx[0]] = st.session_state['startarray'][trueindx[1]]
        st.session_state['startarray'][trueindx[1]] = temp
        st.success(
            f"Die Zahlen {st.session_state['startarray'][trueindx[0]]} und {st.session_state['startarray'][trueindx[1]]} wurden getauscht")
        self.resetButtonarray()
        st.session_state['alreadypressed'] = False
        sleep(1)
        # reset array

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
        if st.session_state['triggeronetimererun']:
            st.session_state['triggeronetimererun'] = False
            st.rerun()

        # Variablen initiieren
        # -------------------------------------------------------------------------------------------------------------
        # Die Liste, die wir betrachten um die neue Zahl an die neue Stelle zu ordnen
        currentArray = st.session_state['startarray']
        # Die der index des "sortierten" bereiches (zahl vor der neu zu sortierenden Zahl)
        currentIndex = st.session_state['sortareaindex']

        # schaut, welches element nach noch verglichen werden muss in der liste (i--)
        # zum anfang schauen wir uns die aktuelle position an
        # danach wird dies reduziert um das vergleichen zu ermöglichen
        if st.session_state['updatedIndex'] == -2:
            st.session_state['updatedIndex'] = currentIndex

        updatedIndex = st.session_state['updatedIndex']

        # -------------------------------------------------------------------------------------------------------------

        # Wählen / neu wählen der Elemente durch klicken
        # -------------------------------------------------------------------------------------------------------------
        trueindx = np.where(st.session_state['buttonarray'])[0]

        # print(trueindx)

        if len(trueindx) == 2:
            st.session_state['selectedIndex1'] = trueindx[0]
            st.session_state['selectedIndex2'] = trueindx[1]

        selectedindex1 = st.session_state['selectedIndex1']
        selectedindex2 = st.session_state['selectedIndex2']

        # Ausgabe der momentan gewählten Zahlen (zum debuggen)
        if st.session_state['selectedIndex1'] == -1 or st.session_state['selectedIndex2'] == -1:
            st.info('Wähle 2 Zahlen zum Tauschen')
        else:
            st.info("Wahl: Position " + str(selectedindex1 + 1) + " = Zahl [" + str(st.session_state['startarray'][selectedindex1]) +
                    "] und Position " + str(selectedindex2 + 1) + " = Zahl [" + str(st.session_state['startarray'][selectedindex2]) + "]")
        # -------------------------------------------------------------------------------------------------------------

        if len(trueindx) == 2 or selectedindex1 != -1 or selectedindex2 != -1:
            if st.button("Zahlen neu wählen"):
                self.resetButtonarray()
                self.reset_selected_index()
                st.rerun()

        # Tauschprozess 'nach vorne'
        # -------------------------------------------------------------------------------------------------------------
        if st.button("Tauschen"):
            # checken, ob der user ueerhaupt die zahlen geklickt hat
            trueindx = np.where(st.session_state['buttonarray'])[0]
            if len(trueindx) < 2:
                st.info("Wähle 2 Zahlen durch das Klicken auf eine Zahl in der obigen Liste")
                pass
            # wenn ja, dann schauen wir ob der swap passt und durchgefuehrt werden darf
            else:
                valid = self.tutor.isSwapValid(selectedindex1, selectedindex2, updatedIndex, currentArray)

                if valid:
                    updatedIndex = updatedIndex - 1
                    st.session_state['updatedIndex'] = updatedIndex
                    print("updated Index: " + str(updatedIndex))
                    self.reset_selected_index()
                    self.tauschearray()  
                    self.openTauschDialog()
                    return st.info("nice")
                else:
                    pass

        if st.button("Korrekt eingeordnet?"):
            if self.tutor.isAtCorrectPosition(updatedIndex, currentArray, st.session_state['sortareaindex']):
                # wenn korrekt sortedarea wird inkrementiert
                # self.resetSelectedIndex()
                self.reset_selected_index()
                st.session_state['updatedIndex'] = -2
                st.session_state['sortareaindex'] += 1
                st.session_state['orderingprocess'] = False
                st.session_state['alreadypressed'] = False
                st.session_state['triggeronetimererun'] = True
                st.session_state['userModel'].reset_tries()
                st.rerun()
            else:
                pass
                #st.warning("Das Element ist noch nicht richtig eingeordnet")
        # ------------------------------------------------------------------------------------------------------------

    def reset_selected_index(self):
        st.session_state['selectedIndex1'] = -1
        st.session_state['selectedIndex2'] = -1