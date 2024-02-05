import streamlit as st
import Usermodel
class TutorModel:

    def __init__(self):
        if 'userModel' not in st.session_state:
            st.session_state['userModel'] = Usermodel.Usermodel()
        # if 'updatedIndex' not in st.session_state:
        #    st.session_state['updatedIndex'] = 0

    def noSwapNeeded(self, current_number, compare_number):
        st.session_state['userModel'].increaseAttempt()
        if st.session_state['userModel'].maxTriesachieved():
            st.error(str(current_number) + " ist größer als  " + str(compare_number) +
                     ": es muss also nicht getauscht werden.")
        else:
            if st.session_state['userModel'].current_tries() == 1:
                st.warning("Schau nochmal genauer hin. Muss wirklich getauscht werden?")
            else:
                st.warning("Vergleiche die " + str(current_number) + " mit " + str(compare_number) + ". ")

    def swapNeeded(self, current_number, compare_number):
        st.session_state['userModel'].increaseAttempt()
        if st.session_state['userModel'].maxTriesachieved():
            st.error(str(current_number) + " ist kleiner als  " + str(compare_number) +
                     ": es muss also getauscht werden.")
        else:
            if st.session_state['userModel'].current_tries() == 1:
                st.warning("Schau nochmal genauer hin. Muss wirklich nicht getauscht werden?")
            else:
                st.warning("Vergleiche die " + str(current_number) + " mit der " + str(compare_number) + ". ")

    def isSwapValid(self, selectedIndex1, selectedIndex2, currentIndex, currentList):
        newList = currentList

        print("index1: " + str(selectedIndex1) + " index2: " + str(selectedIndex2) + " current: " + str(currentIndex))

        # check if the start of list was reached
        if newList[currentIndex] == 0:
            return "beginning of list"
        if selectedIndex1 != currentIndex:
            return "wrong swap"
        elif newList[selectedIndex1] > newList[selectedIndex2]:
            return "True"

        elif st.session_state['userModel'].maxTriesachieved():
            return "wrong swap max"
        else:
            return "wrong swap"

    def isAtCorrectPosition(self, current_index, current_array, sortedindex):
        print("currentindex: " + str(current_index) + " curerntarray: " + str(current_array) + " sortedindex: " + str(sortedindex))
        if current_index == 0 and current_array[current_index] > current_array[current_index +1]:
            return False
        elif current_index == sortedindex:
            return False
        elif current_array[current_index] > current_array[current_index +1]:
            return False
        else:
            return True
