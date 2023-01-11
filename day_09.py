import streamlit as st
import time

st.title("st.progress")

with st.expander("About this app"):
    st.write("You can now display the progress of your calculations in a Streamlit app")

progress_bar = st.progress(0)
for pct_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(pct_complete)

st.balloons()
