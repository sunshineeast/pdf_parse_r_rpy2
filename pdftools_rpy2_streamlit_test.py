import streamlit as st
st.text(os.environ.get("R_HOME", "Undefined"))

import pandas as pd
import datetime
import os
os.environ["R_HOME"] = "/usr/local/bin/R"

import pdftotext
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

utils = importr('utils')
base = importr('base')

utils.install_packages('pdftools')
pdftools = importr('pdftools')



st.set_page_config(
    page_title="Health Quant Analysis",
    # page_icon="👋",
    layout='wide',
)


# title
st.markdown("<h1 style='text-align: center; font-size: 70px;color: black;letter-spacing: 4px;'>PDF Parsing</h1>", unsafe_allow_html=True)


with st.container(border=True):

    st.write("Note: Upload pdf files one by one. When one is Parsed & Processed then only upload another.")
    st.session_state.uploaded_file = st.file_uploader('Choose your **.pdf** file to upload', type="pdf")

    if st.session_state.uploaded_file is not None:
        # st.write(st.session_state.uploaded_file.name)
        st.success("File is uploaded")

if st.session_state.uploaded_file:

  

    st.session_state.doc_parsed = st.session_state.uploaded_file.getvalue()

    with open(st.session_state.doc_parsed, "rb") as f:
        # st.session_state.pdf = pdftotext.PDF(f)
        st.session_state.pdf = pdftools.pdf_text(f)


    st.write(st.session_state.pdf)

    
