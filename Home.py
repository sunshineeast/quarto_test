import streamlit as st
from streamlit import session_state as ss
import pandas as pd
import polars as pl
import shlex, subprocess
import os
import uuid
from plotnine import *
import plotly.io as pio
import shutil
import yaml
import sys
from plotnine import *
# import time

st.set_page_config(page_title="Health Quant Analysis",
                    layout='wide',
                    initial_sidebar_state="expanded")


# Setting configuration to diable plotly zoom in plots
config = dict({'scrollZoom': False})

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')


def get_session_id():
    """
    Gets a unique identifier for the current Streamlit session.

    This function returns a UUID that is unique to the current Streamlit session.
    If the "_session_id_" key does not exist in the session state, it is created
    with a new UUID value.

    Returns:
        str: A unique identifier for the current Streamlit session.
    """

    if "_session_id_" not in st.session_state:
        st.session_state["_session_id_"] = uuid.uuid4()

    return st.session_state["_session_id_"]


st.markdown("<h1 style='text-align: center; font-size: 50px;color: black;letter-spacing: 4px;'>Analytics Report Download</h1>", unsafe_allow_html=True) #  \n\nDATA SCIENCE
st.markdown("<h1 style='text-align: center; font-size: 38px;color: black;letter-spacing: 3px;'>(Under Construction)</h1>", unsafe_allow_html=True)

# st.write(f"Session ID: {get_session_id()}")

plt_test = (ggplot() + # 
            annotate('text', x = 1, y = 4, label = str(90) + '%', size=70, color="#988275",family="fantasy") +
            annotate('text', x = 3, y = 4, label = str(92) + '%', size=70, color="#988275",family="fantasy") +
            
            annotate('text', x = 1, y = 4.7, label = "Normal \nTest Results\nOn Overall\n Test Data", 
                     size=24, color="#988275",family="fantasy") +
            
            
            annotate('path', x=[.5, 1.5], y=[4.35, 4.35], color="#988275",size=3) +
            annotate('path', x=[.5, 1.5], y=[3.7, 3.7], color="#988275",size=3) +
            
            
            annotate('text', x = 3, y = 4.7, label = "Normal \nTest Results\nOn Latest\n Test Data", 
                     size=24, color="#988275",family="fantasy") +
            
            annotate('path', x=[2.5, 3.5], y=[4.35, 4.35], color="#988275",size=3) +
            annotate('path', x=[2.5, 3.5], y=[3.7, 3.7], color="#988275",size=3) +
            
            geom_vline(xintercept=2, color="#988275", linetype="dashed") +
            
            coord_cartesian(xlim=(0.5, 4.5), ylim=(3.5, 5)) 
            + theme_void()
            )

st.pyplot(plt_test)

v_spacer(6)


st.subheader("Generate & Download html report with interactive charts & content.")
report_col1, report_col2, report_col3 = st.columns(3)

with report_col1:

    ss.user_name = st.text_input("Enter Your Name that you want on report", "Mr. /Ms. xxx")

    # if a user enter blank name then replace it with space to avoid error
    if ss.user_name == "":
        ss.user_name = " "

st.write(f"python path: {sys.executable}")

st.session_state.Gen_Report = st.button("Generate Report")

if st.session_state.Gen_Report:

    st.write(os.listdir())
    ss.cmd_str = "quarto render Report-test.qmd --output Report-test.html"
    st.write(ss.cmd_str)

    # subprocess.run(shlex.split(f"{sys.executable} -m quarto render Report-test.qmd --output Report-test.html"))
    subprocess.run(["bash", "./bash_file2.sh", "Report-test.qmd", "Report-test.html"])

  
    st.subheader("Report Generated")
    st.write(os.listdir())

    with open('Report-test.html', "rb") as file: # ss.output_file_name
                st.download_button(
                    label="Download Report",
                    data=file,
                    file_name="Analytics_Report.html",
                    mime="text/html")
                
