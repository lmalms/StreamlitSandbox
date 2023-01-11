import streamlit as st

st.title("st.form")

st.header("1. Example of using with `with` notation (preferred)")
st.subheader("Coffee machine")
with st.form("my_form"):
    st.subheader("**Order your coffee**")

    # Input widgets
    coffee_beans = st.selectbox("Coffee beans", ["Arabica", "Robusta"])
    coffee_roast = st.selectbox("Coffee roast", ["light", "Medium", "Dark"])
    brewing = st.selectbox("Brewing method", ["Aeropress", "Drip", "French press"])
    serving_type = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    milk = st.select_slider("Milk", ["None", "Low", "Medium", "High"])
    owncup = st.checkbox("Bring own")

    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown(
        f"""
        You have ordered:
        - Coffee bean: `{coffee_beans}`
        - Coffee roast: `{coffee_roast}`
        - Brewing: `{brewing}`
        - Serving type: `{serving_type}`
        - Milk: `{milk}`
        - Bring own cup: `{owncup}`
        """
    )
else:
    st.write("Place your order.")


# Shorter example of using object notation
st.header("2. Example of object notation")
form = st.form("my_form_2")
selected_value = form.slider("Select value")
form.form_submit_button("Submit")
st.write("Selected value: ", selected_value)
