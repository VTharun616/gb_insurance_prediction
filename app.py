import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("gb_model.pkl","rb") as f:
    model = pickle.load(f)

st.title("US HEALTH INSURANCE CHARGES PREDICTION")

sex = st.selectbox("sex",['female', 'male'])
smoker = st.selectbox("smoker",['yes', 'no'])
region = st.selectbox("region",['southwest', 'southeast', 'northwest', 'northeast'])

age = st.number_input("age")
bmi = st.number_input("bmi")
children = st.number_input("children")

if st.button("Prediction"):

    sex_map = {"female":0, "male":1}
    smoker_map = {"no":0, "yes":1}
    region_map = {"southwest":0, "southeast":1, "northwest":2, "northeast":3}

    sex = sex_map[sex]
    smoker = smoker_map[smoker]
    region = region_map[region]

    input_df = pd.DataFrame({
        "sex":[sex],
        "smoker":[smoker],
        "region":[region],
        "age":[age],
        "bmi":[bmi],
        "children":[children]
    })

    result = model.predict(input_df)[0]

    st.success(f"Estimated Insurance charges: {result:.2f}")