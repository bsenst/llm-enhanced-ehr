import streamlit as st
import openai

st.title("Upload")

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


openai_api_key = st.text_input("Enter your OpenAI API key here:", "")
# Validate the user's key
if openai_api_key.startswith("sk-"):
    # Set the key for the OpenAI library
    openai.api_key = openai_api_key
    try:
        # Test if the key works by listing the available engines
        engines = openai.Engine.list()
        # Display a success message
        st.success("Your OpenAI API key is valid!")
        # On page 1
        st.session_state["key"] = openai_api_key  # Assign the variable to a key

    except openai.error.AuthenticationError:
        # Display an error message
        st.error("Your OpenAI API key is invalid!")
else:
    # Display a warning message
    st.warning("Please enter a valid OpenAI API key!")
