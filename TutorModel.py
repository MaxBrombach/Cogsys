import numpy as np
import streamlit as st
import Usermodel
import CustomExceptions

class TutorModel:

    def __init__(self):
        if 'userModel' not in st.session_state:
            st.session_state['userModel'] = Usermodel.Usermodel()
        #if 'updatedIndex' not in st.session_state:
        #    st.session_state['updatedIndex'] = 0

    def noSwapNeeded(self):
        st.session_state['userModel'].increaseAttempt()
        if st.session_state['userModel'].maxTriesachieved():
            #TODO was passiert wenn er komplett verkackt -> maxtries überschreitet
            # implement logic
            pass
        else:
            st.error("Es darf nicht getauscht werden")

    def swapNeeded(self):
        st.session_state['userModel'].increaseAttempt()
        if st.session_state['userModel'].maxTriesachieved():
            # TODO was passiert wenn er komplett verkackt -> maxtries überschreitet
            #  implement logic
            pass
        else:
            st.error("Es muss getauscht werden")

    def isSwapValid(self, selectedIndex1, selectedIndex2, currentIndex, currentList):
        newList = currentList

        print("index1: " + str(selectedIndex1) + " index2: " + str(selectedIndex2) + " current: " + str(currentIndex))
        print("Momentane Liste: " + str(newList))

        # check if the start of list was reached
        if newList[currentIndex] == 0:
            return "beginning of list"
        if selectedIndex1 != currentIndex:
            print("Shit goes wrong here")
            return "wrong swap"
        elif newList[selectedIndex1] > newList[selectedIndex2]:
            return "True"

        elif st.session_state['userModel'].maxTriesachieved():
            raise "wrong swap max"
        else:
            return "wrong swap"

    def isAtCorrectPosition(self, currentIndex, currentArray):
        if currentIndex == 0:
            return True
        elif currentArray[currentIndex] > currentArray[currentIndex-1]:
            return True
        else:
            return False




   

   


