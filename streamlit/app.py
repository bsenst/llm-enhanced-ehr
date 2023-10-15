import os
import streamlit as st
import openai
import pandas as pd

# from langchain.llms import Clarifai
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import AnalyzeDocumentChain

from dotenv import load_dotenv
load_dotenv()

st.title("LLM enhanced Medical Notes")

st.write("See the project description https://lablab.ai/event/ai-challenge-with-gpt-3-5-codex-dall-e-and-whisper-api/fritzlabs/llm-enhanced-medical-notes")

folder = "streamlit/assets/"
files = [file.split(".")[0] for file in os.listdir(folder)]

for file in files:
    with open(folder+file+".txt") as infile:
        st.session_state[file] = infile.read()

# USER_ID = "openai"
# APP_ID = "chat-completion"
# MODEL_ID = "GPT-3_5-turbo"

# llm = Clarifai(
#     pat=os.environ.get("CLARIFAI_PAT"), user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID
# )

medical_note = st.selectbox(
   "Which medical note do you want to query?",
   ([file for file in st.session_state.keys() if file != "key"]),
)

with st.sidebar:
    
    openai_api_key = os.environ.get("openai")

    if not openai_api_key.startswith("sk-"):
        openai_api_key = st.text_input("Enter your OpenAI API key here:", type="password")  
    
    if openai_api_key.startswith("sk-"):
        # Set the key for the OpenAI library
        openai.api_key = openai_api_key
        try:
            # Test if the key works by listing the available engines
            engines = openai.Engine.list()
            # Display a success message
            st.success("Your OpenAI API key is valid!")

            st.session_state["key"] = openai_api_key  # Assign the variable to a key
        except openai.error.AuthenticationError:
            # Display an error message
            st.error("Your OpenAI API key is invalid.")

if "key" in st.session_state:
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key, model="gpt-3.5-turbo")
    qa_chain = load_qa_chain(llm)
    qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)
    question = st.text_input("Enter your query for the medical note")
    if question:
        st.caption(f"Querying {medical_note} ...")
        st.write(qa_document_chain.run(input_document=st.session_state[medical_note], question=question))
else:
    st.warning("Please enter an OpenAI API key in the sidebar to proceed.")

st.markdown("### Medical Note")

st.write(st.session_state[medical_note])
