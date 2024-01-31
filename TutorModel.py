import numpy as np
import streamlit as st
import Usermodel
import CustomExceptions

class TutorModel:

    def __init__(self):
        if 'userModel' not in st.session_state:
            st.session_state['userModel'] = Usermodel.Usermodel()
        if 'updatedIndex' not in st.session_state:
            st.session_state['updatedIndex'] = 0

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
        # keep track of the new index while comparing the list from the current element to the first element smaller than new element
        if st.session_state['updatedIndex'] == 0:
            st.session_state['updatedIndex'] = currentIndex

        # todo handle wrongly selected indexes
        indexToCompare =  st.session_state['updatedIndex']

        # check if the start of list was reached
        if newList[indexToCompare] == 0:
            st.session_state['updatedIndex'] = 0
            raise CustomExceptions.StartOfListIsReached
        elif newList[currentIndex] > newList[indexToCompare+1]:
            st.session_state['updatedIndex'] = indexToCompare - 1
            return True

        elif st.session_state['userModel'].maxTriesachieved():
            raise CustomExceptions.WrongSwapAfterMaxTries
        else:
            raise CustomExceptions.WrongSwapException

    def isAtCorrectPosition(self, currentIndex, currentArray):
        if currentIndex == 0:
            return True
        elif currentArray[currentIndex] > currentArray[currentIndex-1]:
            return True
        else:
            return False




   

   


