import streamlit as st

st.title("Customising the theme of streamlit apps.")
st.write("Contents of the '.streamlit/config.toml' file for this app:")
st.code(
    """
    [theme]
    primaryColor="#F39C12"
    backgroundColor="#2E86C1"
    secondaryBackgroundColor="#AED6F1"
    textColor="#FFFFFF"
    font="monospace"
    """
)

number = st.slider("Choose a number", 0, 10, 5)
st.write("You picked ", number, " from slider widget.")
