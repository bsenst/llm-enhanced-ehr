import streamlit as st
import openai

st.title("File Upload")

# Create a file uploader widget that accepts multiple files
uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)

# Do something with the uploaded files
if uploaded_files is not None:
    # Loop through the uploaded files
    for i, uploaded_file in enumerate(uploaded_files):
        # Display the file name and size
        st.write(f"{i+1} {uploaded_file.name} {uploaded_file.size} bytes")
        st.session_state[uploaded_file.name.split(".")[0]] = uploaded_file.read().decode("utf-8")
