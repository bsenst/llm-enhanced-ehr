import streamlit as st
from htmlTemplates import css, bot_template, user_template

st.title("Medical Note 2")
st.write(css, unsafe_allow_html=True)

if "medical_note_2" not in st.session_state:
    st.session_state.medical_note_2 = None

st.write(st.session_state["medical_note_2"])

st.title("Example LLM Questions & Answers")

with st.expander("What surgeries did the patient undergo?"):
    st.write("The patient underwent an appendectomy at age 26 due to acute appendicitis and coronary artery stenting at age 38 due to a minor heart attack.")

with st.expander("Which antihypertensive drugs did the patient take in past or present?"):
    st.write("The patient has been taking lisinopril to manage hypertension since age 30.")
