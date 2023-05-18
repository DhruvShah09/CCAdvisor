import streamlit as st 
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

def Header():
    st.set_page_config(page_title="Advisor :P")
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.header("GT Advising Chat!") 
    colored_header(label = '', description='', color_name='blue-30')
    response_container = st.container()
def Sidebar():
    with st.sidebar:
        st.title("GT CC Robotic Advisor!")
        st.markdown('This is a simple application to communicate with the widely available Georgia Tech College of Computing and Catalog knowledge base!')
    