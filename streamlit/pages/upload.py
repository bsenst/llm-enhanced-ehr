import streamlit as st
import openai

st.title("File Upload")

# Create a file uploader widget that accepts multiple files
uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)

st.session_state["files "] = uploaded_files # Use this key if u want to migrate these files to another state

# Do something with the uploaded files
if uploaded_files is not None:
    # Loop through the uploaded files
    for uploaded_file in uploaded_files:
        # Display the file name and size
        st.write(f"File name: {uploaded_file.name}")
        st.write(f"File size: {uploaded_file.size} bytes")
