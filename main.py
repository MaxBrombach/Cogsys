import streamlit as st

import UIstuff


header = st.empty()
text = st.empty()
explanation_button_box = st.empty()
exp_header = st.empty()
exercise_button_box = st.empty()
back_button_box = st.empty()
exp_text_box = st.empty()
exp_text = f'<p>Vor dir liegen verschiedene Zahlen. Einige sind schon sortiert, andere warten darauf, dass du sie an die richtige Stelle bringst.</p>\
<ol start="1" type="1">\
<li><strong>Startzustand:</strong> Du beginnst mit einer ungeordneten Liste von Zahlen. Die Liste ist in der Reihenfolge zu sehen, wie sie eingegeben wurde.</li>\
<li><strong>Unterteilung in Bereiche:</strong> Die Liste wird mental in zwei Teile geteilt: den "sortierten" Bereich am Anfang und den "unsortierten" Bereich. Zu Beginn ist der sortierte Bereich nur das erste Element der Liste, und der Rest der Liste ist unsortiert.</li>\
<li><strong>Auswahl des nächsten Elements:</strong> In jedem Schritt nimmst du das erste Element aus dem unsortierten Bereich und vergleichst es mit den Zahlen im sortierten Bereich, beginnend mit der größten Zahl im sortierten Bereich.</li>\
<li><strong>Einfügen:</strong> Verschiebe das ausgewählte Element rückwärts durch den sortierten Bereich, bis du auf ein Element triffst, das kleiner ist (oder bis du am Anfang der Liste ankommst). Füge das Element direkt nach dem kleineren Element ein (oder am Anfang, wenn kein kleineres Element gefunden wurde).</li>\
<li><strong>Wiederholung:</strong> Wiederhole diesen Prozess mit jedem nächsten Element im unsortierten Bereich, bis alle Elemente in den sortierten Bereich verschoben wurden und die Liste somit vollständig sortiert ist.</li>\
<li><strong>Sortierung bestätigen:</strong> Nach jedem Einfügen überprüfe die sortierte Liste, um sicherzustellen, dass die Reihenfolge korrekt ist.</li>\
<li><strong>Ende des Spiels:</strong> Das Spiel ist vorbei, wenn die gesamte Liste sortiert ist. Die Liste sollte jetzt in aufsteigender Reihenfolge sein.</li></ol>\
'


def main_page():
    header.header("Willkommen zum Sortier-Abenteuer!")
    text.write(
        "Heute werden wir ein spannendes Spiel namens \"Insertion Sort Adventure\" spielen! Bevor wir loslegen, "
        "lass uns einen Blick darauf werfen, was genau \"Insertion Sort\" ist. "
        "Insertion Sort ist ein einfacher Sortieralgorithmus. Denk an eine Liste von Zahlen. "
        "Deine Aufgabe ist es, sie in aufsteigender Reihenfolge zu bringen. "
        "Hier kommt Insertion Sort ins Spiel. Du gehst die Liste durch, vergleichst jedes Element mit "
        "den bereits sortierten Elementen und fügst es an die richtige Stelle ein. So entsteht Schritt "
        "für Schritt eine sortierte Liste.")
    explanation_button = explanation_button_box.button('Wie funktioniert Insertion Sort?')
    exercise_button = exercise_button_box.button('Los geht\'s!')

    if explanation_button:
        explanation()

    if exercise_button or st.session_state['exercisestart']:
        st.session_state['exercisestart'] = True
        exercise()


def explanation():
    exercise_button_box.empty()
    exp_header.header("Wie funktioniert Insertion Sort?")
    explanation_button_box.empty()
    exp_text_box.markdown(exp_text, unsafe_allow_html=True)
    st.button('Okay. Verstanden!')


def exercise():
    st.title("Insertion Sort")
    exp_header.empty()
    text.empty()
    explanation_button_box.empty()
    exercise_button_box.empty()
    exp_text_box.empty()
    UI.createButtonArray()



if __name__ == '__main__':
    if 'exercisestart' not in st.session_state:
        st.session_state['exercisestart'] = False
    UI = UIstuff.UIInsertionsort()
    # streamlit run main.py
    main_page()
