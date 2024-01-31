import numpy as np
import streamlit as st
import Usermodel

class TutorModel:

    def __init__(self):
        if 'userModel' not in st.session_state:
            st.session_state['userModel'] = Usermodel.Usermodel()

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



   

   


