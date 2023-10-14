import streamlit as st

st.write(st.session_state["medical_note1"])

st.expander("What conditions does the patient have?"):
    st.write("Hypertension, Hyperlipidemia, Type 2 Diabetes Mellitus.")

st.expander("What medications does the patient take?"):
    st.write("Lisinopril 20 mg daily, Atorvastatin 40 mg daily, and Metformin 1000 mg twice daily")

st.expander("List the medical conditions and medications for each!"):
    st.write("Medical Conditions: Hypertension, Hyperlipidemia, Type 2 Diabetes Mellitus. Medications: Lisinopril 20 mg daily, Atorvastatin 40 mg daily, Metformin 1000 mg twice daily, Naproxen 500 mg twice daily as needed.")