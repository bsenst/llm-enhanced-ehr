import streamlit as st

st.title("Medical Note 2")

st.write(st.session_state["medical_note_2"])

st.title("Example LLM Questions & Answers")

with st.expander("What surgeries did the patient undergo?"):
    st.write("The patient underwent a laparoscopic cholecystectomy and a hernia repair.")
    st.caption("This is actually wrong.")

with st.expander("Which antihypertensive drugs did the patient take in past or present?"):
    st.write("The patient has taken amlodipine and lisinopril in the past.")
    st.caption("This is actually wrong.")
