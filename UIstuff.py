import streamlit as st


class UIInsertionsort:

    def __init__(self):
        pass

    def createButtonArray(self):
        col1, col2, col3, col4, col5 = st.columns((1,1,1,1,1))
        columnlist = [col1, col2, col3, col4, col5]
        buttonvalues = list()
        for i in range(5):
            buttonvalues.append(columnlist[i].button("⠀"+str(i)+"⠀"))

        st.write(buttonvalues)