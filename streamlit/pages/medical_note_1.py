import streamlit as st

st.title("Medical Note 1")

# Initialize st.session_state if it hasn't been initialized yet
if "medical_note1" not in st.session_state:
    st.session_state.medical_note1 = None

# Now you can use st.session_state["medical_note1"] safely

st.write(st.session_state["medical_note1"])

st.title("Example LLM Questions & Answers")

with st.expander("What conditions does the patient have?"):
    st.write("Hypertension, Hyperlipidemia, Type 2 Diabetes Mellitus.")

with st.expander("What medications does the patient take?"):
    st.write("Lisinopril 20 mg daily, Atorvastatin 40 mg daily, and Metformin 1000 mg twice daily")

with st.expander("List the medical conditions and medications for each!"):
    st.write("Medical Conditions: Hypertension, Hyperlipidemia, Type 2 Diabetes Mellitus. Medications: Lisinopril 20 mg daily, Atorvastatin 40 mg daily, Metformin 1000 mg twice daily, Naproxen 500 mg twice daily as needed.")
    st.caption("Interesting: the previous disc herniation is not listed")

with st.expander("What is the recent complaint of the patient?"):
    st.write("The patient's recent complaint is lower back pain on the right side of his lower back, described as a dull ache with an intensity of 6/10 on the pain scale.")