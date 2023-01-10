import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header("st.write")

# Example 1
st.subheader("Display test")
st.write("Hello *world!* :sunglasses:")

# Example 2
st.subheader("Display numbers")
st.write(1234)

# Example 3
st.subheader("Display dataframes")
df = pd.DataFrame(
    data={
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)
st.write(df)

# Example 4
st.subheader("Accept multiple arguments")
st.write("Below is a dataframe", df, "Above is a dataframe.")

# Example 5
st.subheader("Display plots")
df = pd.DataFrame(
    data=np.random.randn(200, 3),
    columns=["a", "b", "c"],
)
plot = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x="a",
        y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"],
    )
)
st.write(plot)
