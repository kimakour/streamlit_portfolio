import streamlit as st
import re
import os
import shutil
import pandas as pd
import plotly.express as px
from streamlit_timeline import timeline
import json
import base64

_no_1,_no_2,_no_3,_no_4,col_5_language,col_6_language = st.columns((1,1,1,1,0.25,0.25))    
with col_5_language:
    button_en = st.button(label='EN', key='en')
with col_6_language:
    button_fr = st.button(label='FR', key='fr')


if button_en :
    st.session_state['language_chosen'] = 'en'
elif button_fr: 
    st.session_state['language_chosen'] = 'fr'


f_language = open('json_files/languages.json', encoding='utf-8')
data_language = json.load(f_language)


pdfFileObj = open('./{}'.format(data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_file"]), 'rb')
st.sidebar.download_button(
    label=data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_description"],
    data = pdfFileObj,
    file_name=data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_file"],
    mime='pdf'
)

st.markdown(data_language[st.session_state['language_chosen'] ]["litterature"], unsafe_allow_html=True)

