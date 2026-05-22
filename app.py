# STEP 1: Import the libraries

import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd
import pickle as pk

# STEP 2: Load the trained model
with open("Insurance_pipeline.pkl", "rb") as f:
    model = pk.load(f)


# STEP 4: Configure streamlit page
st.set_page_config(
    page_title = "Insurance Charge Predictor",
    page_icon = "💰"
)
st.title("💰 Insurance Charge Predictor ")
st.write("Fill in the details below to estimate your insurance charge")

# STEP 5: Form input
with st.form("Prediction Form"):
    age = st.number_input("Age", min_value = 18, max_value = 100, value = 20)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI", min_value = 10.0, max_value = 60.0, value = 25.0, step = 0.1)
    children = st.number_input("Children", min_value = 0, max_value = 10, value = 0)
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

    submitted = st.form_submit_button("Predict Insurance Charge")

    if submitted:
        
        input_df = pd.DataFrame([{
            "age" : age,
            "sex" : sex,
            "bmi" : bmi,
            "children" : children,
            "smoker" : smoker,
            "region" : region
        }]) 
        prediction = model.predict(input_df)[0]
        st.success(f"Estimate Insurance Charge: ${prediction:,.2f}")
        st.subheader("Input Summary")
        st.dataframe(input_df)

