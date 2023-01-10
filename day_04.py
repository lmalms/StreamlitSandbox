from datetime import datetime, time

import streamlit as st

st.header("st.slider")

# Slider
st.subheader("Slider")
age = st.slider("How old are you?", min_value=0, max_value=130, value=45)
st.write("You are ", age, " years old.")

# Range slider
st.subheader("Range slider")
values = st.slider(
    "Select range of values:",
    min_value=0.0,
    max_value=100.0,
    value=(25.00, 75.00),
)
st.write("Values: ", values)

# Time slider
st.subheader("Time range slider")
appointment = st.slider(
    "Schedule your appointment:",
    min_value=time(0, 0),
    max_value=time(23, 59),
    value=(time(11, 30), time(12, 45)),
)
st.write("You are scheduled for ", appointment)

# Datetime slider
st.subheader("Datetime range slider")
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time: ", start_time)
