import streamlit as st

st.subheader("st.selectbox")
color = st.selectbox(
    "What is your favourite color?",
    ("Blue", "Red", "Green"),
)
st.write("Your favourite color is ", color)


st.subheader("st.multiselect")
colors = st.multiselect(
    "What are your favourite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.write("Your favourite colors are ", colors)


st.subheader("st.checkbox")
st.write("What would you like to order?")
icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
coke = st.checkbox("Coke")
if icecream:
    st.write("Great! Here is some ice cream.")
if coffee:
    st.write("Here is your coffee.")
if coke:
    st.write("Here is your coke.")
