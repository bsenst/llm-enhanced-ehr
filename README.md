# llm-enhanced-ehr

Contribution to the [LabLabAI AI Challenge Hackathon](https://lablab.ai/event/ai-challenge-with-gpt-3-5-codex-dall-e-and-whisper-api) October 2023. The application should allow the user to interact with a large language model (GPT-3.5, GPT-4) and support working on synthetic health data that comes in the electronic health record interoperability format FHIR.

[Project Team Page](https://lablab.ai/event/ai-challenge-with-gpt-3-5-codex-dall-e-and-whisper-api/fritzlabs) &
[Project Submission Page](https://lablab.ai/event/ai-challenge-with-gpt-3-5-codex-dall-e-and-whisper-api/fritzlabs/llm-enhanced-medical-notes)

![application-architecture](https://github.com/bsenst/llm-enhanced-ehr/assets/8211411/5a946f4b-8ac1-469a-a145-0aa9e7576e28)

# Run the application

```bash
git clone https://github.com/bsenst/llm-enhanced-ehr
```

```bash
cd llm-enhanced-ehr
```

```bash
pip install -r streamlit/requirements.txt
```

```bash
streamlit run streamlit/app.py
```

# ToDo

- [X] explore [synthea dataset](https://github.com/synthetichealth/synthea)
- [X] create a user interface to display (parts of the) synthea data ([streamlit](https://streamlit.io), [openehr](https://openehr.org), [openemr](https://www.open-emr.org))
- [X] integrate LLM ([clarifai](https://www.clarifai.com), [sketch](https://pypi.org/project/sketch/))
- [X] connect synthea data with LLM ([langchain](https://www.langchain.com/), [llama-index](https://www.llamaindex.ai/), RAG)
- [X] define workflows/queries, document examples
- [X] prepare submission - screenrecording, presentation

Optional features:
- [ ] set up free database to store user feedback ([streamlit feedback](https://github.com/trubrics/streamlit-feedback))
- [ ] implement [LangChain extraction pipeline](https://python.langchain.com/docs/use_cases/extraction) to turn unstructured to structured medical notes (ideally FHIR format)
