import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
import app

def get_text_from_pdf(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        first_page_text = pdf_reader.pages[0].extract_text()
        if "Medical Report" in first_page_text:
            for page in pdf_reader.pages:
                text += page.extract_text()
        else:
            st.error("Please upload a Medical Report file")
            return None
    return text


def get_text_from_txt(txt_docs):
    text = ""
    for txt in txt_docs:
        text += txt.getvalue().decode('utf-8') + "\n"

        # Check if the TXT contains the required heading
        if "Medical Report" not in text:
            st.error("Please upload a Medical Report file")
            return None
    return text


def get_text_content(uploaded_files):
    text = ""
    for file in uploaded_files:
        if file.type == 'application/pdf':
            text += get_text_from_pdf([file]) or ""
    
        elif file.type == 'text/plain':
            text += get_text_from_txt([file]) or ""
        else:
            st.error(f"File format '{file.type}' is not supported. Please upload a PDF, DOCX, or TXT file.")
            return None
    return text



def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    import os
    api_key = os.environ.get('OPENAI_API_KEY')
    print(f"API key received in upload.py: {api_key}")
    custom_css = """
<style>
.center-align {
    text-align: center;
}
</style>
"""
    st.set_page_config(page_title="Medical Report",
                       page_icon=":medical:")
    st.write(css, unsafe_allow_html=True)

    st.markdown(custom_css, unsafe_allow_html=True)
    st.header("Medical Report")
    uploaded_files = st.file_uploader("Upload your Medical Report:", accept_multiple_files=True)

    if uploaded_files:
        with st.spinner("Processing"):
            for uploaded_file in uploaded_files:
                text = get_text_content([uploaded_file])
                if text:
                    text_chunks = get_text_chunks(text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(
                            vectorstore)
    with st.form(key='user_input_form'):
        user_question = st.text_area("Enter a query according to your report:")
        generate_button = st.form_submit_button("Generate Response")
    if generate_button:
        if user_question:
            handle_userinput(user_question)
            
    
 
if __name__ == '__main__':
    main()