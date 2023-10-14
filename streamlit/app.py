import os
import streamlit as st
import pandas as pd

from langchain.llms import Clarifai
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import AnalyzeDocumentChain

from dotenv import load_dotenv
load_dotenv()

st.title("LLM enhanced Medical Notes")

with open("streamlit/assets/medical_note1.txt") as infile:
    st.session_state["medical_note1"] = infile.read()

# USER_ID = "openai"
# APP_ID = "chat-completion"
# MODEL_ID = "GPT-3_5-turbo"

# llm = Clarifai(
#     pat=os.environ.get("CLARIFAI_PAT"), user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID
# )

llm = OpenAI(temperature=0, openai_api_key=os.environ.get("openai"))
qa_chain = load_qa_chain(llm)
qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)

medical_note = st.session_state["medical_note1"]
question = st.text_input("Enter your query for the medical note")

if question:

    st.write(qa_document_chain.run(input_document=medical_note, question=question))
