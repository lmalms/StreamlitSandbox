import streamlit as st

st.set_page_config(layout="wide")
st.title("How to layout your streamlit app")

with st.expander("About this app"):
    st.write(
        "This app show the various ways in which you can layout your streamlit app."
    )
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        width=250,
    )


st.sidebar.header("Input")
user_name = st.sidebar.text_input("What is your name?")
user_age = st.sidebar.slider("What is your age?", 1, 100, 25)
user_food = st.sidebar.selectbox(
    "What is your favourite food?",
    ["", "Tom Yum Kung", "Burrito", "Lasagna", "Hamburger", "Pizza"],
)

st.header("Output")
col1, col2, col3 = st.columns(3)
with col1:
    if user_name:
        st.write(f"Hello {user_name}!")
    else:
        st.write("Please enter your name.")

with col2:
    st.write(f"Cool, you are {user_age} years old!")

with col3:
    if user_food:
        st.write(f"**{user_food}** is your favourite food!")
    else:
        st.write(f"Please enter your favourite food!")
