import streamlit as st 
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import pipeline
from components.constructors import Header, Sidebar
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

VectorDBcreate = pipeline.VectorDBCreator('db', OpenAIEmbeddings(), None)
VectorDBcreate.LoadVDBDisk()
retriever = VectorDBcreate.getRetrieverFromVDB()
ChainCreate = pipeline.ChainObj(None, retriever)
qa_chain = ChainCreate.ConstructChain()



Header()
Sidebar()
def get_text():
    input_text = st.text_input("Student: ", "", key="input")
    return input_text
input_container = st.container()
response_container = st.container()
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm Chat, How may I help you?"]
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']
with input_container:
    user_input = get_text()
with response_container:
    if user_input:
        llm_response = qa_chain(user_input)
        response = llm_response['result']
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))