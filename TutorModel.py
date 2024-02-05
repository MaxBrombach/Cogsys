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

    def isSwapValid(self, selected_index1, selected_index2, current_index, current_list):
        new_list = current_list

        print("Current tries: "+ str(st.session_state['userModel'].current_tries()))

        if selected_index1 != current_index:
            st.session_state['userModel'].increaseAttempt()
            if st.session_state['userModel'].maxTriesachieved():
                st.error("Falsche Wahl der Zahlen: Du musst die Zahlen an den Stellen " + str(current_index+1) + " sowie " + str(current_index+2) + " tauschen")
            elif st.session_state['userModel'].current_tries() == 1:
                st.warning("Hast du eventuell noch die falschen Zahlen ausgewählt?")
            else:
                st.warning(
                    "Wahl der Zahlen zum tauschen war nicht ganz richtig, Momentan betrachtest du die Zahl an der Stelle " + str(
                        current_index + 1))
            return False
        elif new_list[selected_index1] > new_list[selected_index2]:
            return True
        else:
            st.session_state['userModel'].increaseAttempt()
            st.warning("Die Zahl an der Stelle " + str(current_index + 1) + " ist bereits eingeordnet.")
            return False

    def isAtCorrectPosition(self, current_index, current_array, sorted_index):
        #print("currentindex: " + str(current_index) + " curerntarray: " + str(current_array) + " sortedindex: " + str(sortedindex))
        st.session_state['userModel'].increaseAttempt()

        if current_index == -1:
            return True
        if current_index == 0 and current_array[current_index] > current_array[current_index + 1]:
            self.helpNotifications(current_index, current_array, sorted_index)
            return False
        elif current_index == sorted_index:
            self.helpNotifications(current_index, current_array, sorted_index)
            return False
        elif current_array[current_index] > current_array[current_index + 1]:
            self.helpNotifications(current_index, current_array, sorted_index)
            return False
        else:
            return True

    def helpNotifications(self, current_index, current_array, sorted_index):
        if st.session_state['userModel'].maxTriesachieved():
            st.error("Die Zahl " + str(current_array[current_index + 1]) + " muss mit der Zahl " + str(
                current_array[current_index]) + " getauscht werden")
        elif st.session_state['userModel'].current_tries() == 1:
            st.warning("Sortiere die Zahl " + str(current_index + 1) + " bis es sich an der richtigen Stelle befindet")
        else:
            st.warning("Sortiere das neue Element, bis es sich an der richtigen Stelle befindet.")