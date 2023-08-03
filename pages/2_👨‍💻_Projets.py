import streamlit as st
import re
import os
import shutil
import pandas as pd
import plotly.express as px
from streamlit_timeline import timeline
import json
import base64


st.set_page_config(
    page_title="Kaci Makour - Portfolio ",
    page_icon="📖",
    layout="wide"
)

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


f_timeline = open(data_language[st.session_state['language_chosen']]["projects"]["timeline"]["path_timeline"], encoding='utf-8')
data_timeline = json.load(f_timeline)

f_pipeline = open('./json_files/pipeline.json', encoding='utf-8')
data_pipeline = json.load(f_pipeline)

pdfFileObj = open('./{}'.format(data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_file"]), 'rb')
st.sidebar.download_button(
    label=data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_description"],
    data = pdfFileObj,
    file_name=data_language[st.session_state['language_chosen']]["side_bar"]["download_button"]["download_file"],
    mime='pdf'
)

st.markdown(data_language[st.session_state['language_chosen']]["projects"]["timeline"]["header_timeline"], unsafe_allow_html=True)
timeline(data_timeline, height=500)


st.markdown(data_language[st.session_state['language_chosen']]["projects"]["pipeline"]["hearder_pipeline"], unsafe_allow_html=True)

option_pipeline = st.selectbox(
    data_language[st.session_state['language_chosen']]["projects"]["pipeline"]["option_pipeline_question"],
    tuple(data_language[st.session_state['language_chosen']]["projects"]["pipeline"]["option_pipeline_project"]))

column_keyword_1, column_keyword_2, column_keyword_3, column_keyword_4 = st.columns(4)

with column_keyword_1:
    st.button(data_language[st.session_state['language_chosen']]["projects"]["pipeline"]['pipeline_keywords'][option_pipeline][0], disabled=True)
with column_keyword_2:
    st.button(data_language[st.session_state['language_chosen']]["projects"]["pipeline"]['pipeline_keywords'][option_pipeline][1], disabled=True)
with column_keyword_3:
    st.button(data_language[st.session_state['language_chosen']]["projects"]["pipeline"]['pipeline_keywords'][option_pipeline][2], disabled=True)
with column_keyword_4:
    st.button(data_language[st.session_state['language_chosen']]["projects"]["pipeline"]['pipeline_keywords'][option_pipeline][3], disabled=True)


_1_pipeline, column_pipeline_2, _3_pipeline = st.columns(3)
with column_pipeline_2:
    st.image(data_pipeline[option_pipeline], caption="Pipeline : {}".format(option_pipeline))


st.markdown(data_language[st.session_state['language_chosen']]["projects"]["dashboards"]["hearder_dashboard"], unsafe_allow_html=True)
st.markdown(data_language[st.session_state['language_chosen']]["projects"]["dashboards"]["markdown_dashboard_remark"])

col1_choose_dashboard, _col2_no_use = st.columns((1, 2))

with col1_choose_dashboard:
    option_dashboard = st.selectbox(
        data_language[st.session_state['language_chosen']]["projects"]["dashboards"]["option_dashboard_question"],
        tuple(data_language[st.session_state['language_chosen']]["projects"]["dashboards"]["option_dashboard_framework"]))



file_ = open(data_language[st.session_state['language_chosen']]["projects"]["dashboards"]["framework_demo"][option_dashboard], "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


col1_dashboard, col2_dashboard = st.columns((2, 1))

with col1_dashboard:
    st.markdown(
        "<img src='data:image/gif;base64,{}' alt='demo gif'>".format(data_url),
        unsafe_allow_html=True,
        )
with col2_dashboard:
    st.markdown(data_language[st.session_state['language_chosen']]["projects"]["dashboards"]["framework_explanation"][option_dashboard], unsafe_allow_html=True)