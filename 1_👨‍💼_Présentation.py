import streamlit as st
import re
import os
import shutil
import pandas as pd
from streamlit_timeline import timeline
import json
import base64
import json
from streamlit_lottie import st_lottie 


st.set_page_config(
    page_title="Kaci Makour - Portfolio ",
    page_icon="📖",
    layout="wide"
)

# Loading static files
@st.cache
def load_necessary_files():
    f_language = open('json_files/languages.json', encoding='utf-8')
    data_language = json.load(f_language)
    return data_language

data_language = load_necessary_files()

@st.cache
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f) 
        
lottie_hello = load_lottiefile("lottie_files/hello bubble.json")



# Choosing language
if 'language_chosen' not in st.session_state.keys():
    st.session_state['language_chosen'] = 'fr'

_no_1,_no_2,_no_3,_no_4,col_5_language,col_6_language = st.columns((1,1,1,1,0.5,0.5))    
with col_5_language:
    button_en = st.button(label='EN', key='en')
with col_6_language:
    button_fr = st.button(label='FR', key='fr')

if button_en :
    st.session_state['language_chosen'] = 'en'
elif button_fr: 
    st.session_state['language_chosen'] = 'fr'

# Downloading pdf
pdfFileObj = open(data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_file"], 'rb')


st.sidebar.download_button(
    label=data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_description"],
    data = pdfFileObj,
    file_name=data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_file"],
    mime='pdf'
)


column_1 , column_2, = st.columns((1,2))
with column_1:
    st.image("images/portrait without background.png")

with column_2:
    st_lottie( lottie_hello, speed=1,reverse=False,loop=True,quality="high", width=200)
    st.markdown(data_language[st.session_state['language_chosen']]['presentation']['name_presentation'], unsafe_allow_html=True)
    
st.markdown(data_language[st.session_state['language_chosen']]['presentation']['work_presentation'], unsafe_allow_html=True)

    