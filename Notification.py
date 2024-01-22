import streamlit as st


class Notification:

    def __init__(self):
        pass

    # input_number: einzuordnende Zahl
    # current_number: Zahl in sortierter Liste, mit welcher gerade verglichen wird
    def hint(self, input_number, current_number):
        # TODO: Füge Hilfstext ein: z.B. input ist größer, muss nicht getauscht werden bzw. ist kleiner,
        #  deshalb muss getauscht werden
        if input_number > current_number:
            # muss nicht getauscht werden
            st.info()
        else:
            # muss getauscht werden
            st.info()

    # Leere Liste info, eventuell danach zur nächsten Seite mit Auswahl (ob nochmal oder Zusammenfassung) weiterleiten?
    def end_of_list(self):
        # TODO: Füge Text ein, dass das Ende der Liste erreicht ist und der Algorithmus abgeschlossen ist
        st.info('')

    # Nutzer wählt falsch aus
    def error_message(self, input_number, current_number):
        # TODO: Errorinfo, dass Nutzer fälschlicherweise tauschen will bzw. nicht tauschen will
        if input_number > current_number:
            # hätte nicht getauscht werden müssen
            st.info()
        else:
            # hätte getauscht werden müssen
            st.info()

    def correct_answer(self, input_number, current_number):
        # TODO: Info, dass der Nutzer richtig gewählt hat mit evtl. kurzer erklärung warum (ähnlicher/glicher text wie bei hint?)
        if input_number > current_number:
            # wurde richtig "nicht getauscht"
            st.info()
        else:
            # richtig getauscht
            st.info()

    def custom_info(self, text):
        st.info(text)

    def custom_warning(self, text):
        st.warning(text)

    def custom_error(self, text):
        st.error(text)
