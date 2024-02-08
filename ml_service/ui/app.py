import requests
import streamlit as st


st.title("Iris classification model")

st.markdown("List iris characteristics:")
sepal_width = st.number_input(label="Sepal width", min_value=0, max_value=10, value=5)
sepal_height = st.number_input(label="Sepal height", min_value=0, max_value=10, value=5)
petal_width = st.number_input(label="Petal width", min_value=0, max_value=10, value=5)
petal_height = st.number_input(label="Petal height", min_value=0, max_value=10, value=5)

if st.button("Predict"):
    response = requests.get(
        "http://api:8000/predict",
        params={
            "sepal_width": sepal_width,
            "sepal_height": sepal_height,
            "petal_width": petal_width,
            "petal_height": petal_height,
        }
    )
    st.success(f"This iris is {response.text}.")
