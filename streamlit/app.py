import os
import streamlit as st
import openai
#from streamlit_feedback import streamlit_feedback
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import AnalyzeDocumentChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain
import json

schema = {
    "properties": {
        "patient_name": {"type": "string"},
        "age": {"type": "integer"},
        "gender": {"type": "string"},
        "medical_record_number": {"type": "integer"},
        "date_of_visit": {"type": "string"},
        "reason_for_visit": {"type": "string"},
        "medical_history": {
            "type": "object",
            "properties": {
                "childhood_adolescence": {
                    "type": "string",
                },
                "teenage_years": {
                    "type": "string",
                },
                "early_adulthood": {
                    "type": "string",
                },
                "mid_adulthood": {
                    "type": "string",
                },
                "late_adulthood": {
                    "type": "string",
                },
                "recent_years": {
                    "type": "string",
                }
            }
        },
        "current_symptoms": {"type": "string"},
        "vital_signs": {
            "type": "object",
            "properties": {
                "blood_pressure": {"type": "string"},
                "heart_rate": {"type": "integer"},
                "respiratory_rate": {"type": "integer"},
                "temperature": {"type": "string"},
            },
            "required": ["blood_pressure", "heart_rate", "respiratory_rate", "temperature"]
        },
        "allergies": {"type": "string"},
        "medications": {"type": "string"},
        "physical_examination": {"type": "string"},
        "neurological_examination": {"type": "string"},
        "assessment_and_plan": {"type": "string"},
        "chronic_medical_conditions": {"type": "string"},
        "acute_issue": {"type": "string"},
        "plan_for_conservative_management": {"type": "string"},
        "patient_education": {"type": "string"},
        "follow_up": {"type": "string"},
        "date_of_birth": {"type": "string"},
        "medical_history": {
            "type": "object",
            "properties": {
                "childhood_adolescence": {
                    "type": "string",
                },
                "teenage_years": {
                    "type": "string",
                },
                "early_adulthood": {
                    "type": "string",
                },
                "mid_adulthood": {
                    "type": "string",
                },
                "late_adulthood": {
                    "type": "string",
                },
                "recent_years": {
                    "type": "string",
                }
            }
        }
    },
    "required": [
        "patient_name", "age", "gender", "medical_record_number", "date_of_visit",
        "reason_for_visit", "medical_history", "current_symptoms", "vital_signs",
        "allergies", "medications", "physical_examination", "neurological_examination",
        "assessment_and_plan", "chronic_medical_conditions", "acute_issue",
        "plan_for_conservative_management", "patient_education", "follow_up",
        "date_of_birth"
    ]
}



from dotenv import load_dotenv
load_dotenv()

st.title("LLM enhanced Medical Notes")

folder = "streamlit/assets/"
files = [file.split(".")[0] for file in os.listdir(folder)]

for file in files:
    with open(folder+file+".txt") as infile:
        st.session_state[file] = infile.read()

# USER_ID = "openai"
# APP_ID = "chat-completion"
# MODEL_ID = "gpt-3.5-turbo"
# os.environ["CLARIFAI_PAT"] = "a78c469c2434401d9b99330924e6a4e0"

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
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    qa_chain = load_qa_chain(llm)
    qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)
    question = st.text_input("Enter your query for the medical note")
    if question:
        st.caption(f"Querying {medical_note} ...")
        st.write(qa_document_chain.run(input_document=st.session_state[medical_note], question=question))
        # feedback = streamlit_feedback(
        #     feedback_type="thumbs",
        #     optional_text_label="[Optional] Please provide an explanation", )
        #
        # Run chain
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo",openai_api_key=openai_api_key)
        chain = create_extraction_chain(schema, llm)
        data = chain.run(medical_note)
        with open("data.json", "w") as f:  # open the file in write mode
            json.dump(data, f, indent= 4)  # dump the Python object to the file

else:
    st.warning("Please enter an OpenAI API key in the sidebar to proceed.")

st.markdown("### Medical Note")

st.write(st.session_state[medical_note])
