import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("bankmarketing_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("Bank Marketing Prediction")
st.write("Predict whether a customer is likely to subscribe to a term deposit.")

# Customer inputs
age = st.number_input("Age", min_value=18, max_value=100, value=40)

job = st.selectbox(
    "Job",
    ["admin.", "blue-collar", "entrepreneur", "housemaid",
     "management", "retired", "self-employed", "services",
     "student", "technician", "unemployed", "unknown"]
)

marital = st.selectbox(
    "Marital Status",
    ["married", "single", "divorced"]
)

education = st.selectbox(
    "Education",
    ["primary", "secondary", "tertiary", "unknown"]
)

default = st.selectbox("Has Credit Default?", ["no", "yes"])

balance = st.number_input("Account Balance", value=0)

housing = st.selectbox("Has Housing Loan?", ["no", "yes"])

loan = st.selectbox("Has Personal Loan?", ["no", "yes"])

contact = st.selectbox(
    "Contact Type",
    ["cellular", "telephone", "unknown"]
)

day = st.number_input(
    "Last Contact Day of Month",
    min_value=1,
    max_value=31,
    value=15
)

month = st.selectbox(
    "Last Contact Month",
    ["jan", "feb", "mar", "apr", "may", "jun",
     "jul", "aug", "sep", "oct", "nov", "dec"]
)

duration = st.number_input(
    "Last Contact Duration (seconds)",
    min_value=0,
    value=100
)

campaign = st.number_input(
    "Number of Contacts During Campaign",
    min_value=1,
    value=1
)

pdays = st.number_input(
    "Days Since Previous Campaign Contact",
    value=-1
)

previous = st.number_input(
    "Previous Campaign Contacts",
    min_value=0,
    value=0
)

poutcome = st.selectbox(
    "Previous Campaign Outcome",
    ["failure", "other", "success", "unknown"]
)

# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "job": [job],
        "marital": [marital],
        "education": [education],
        "default": [default],
        "balance": [balance],
        "housing": [housing],
        "loan": [loan],
        "contact": [contact],
        "day": [day],
        "month": [month],
        "duration": [duration],
        "campaign": [campaign],
        "pdays": [pdays],
        "previous": [previous],
        "poutcome": [poutcome]
    })

    prediction = model.predict(input_data)[0]

    if prediction == "yes":
        st.success("Prediction: Customer is likely to subscribe.")
    else:
        st.error("Prediction: Customer is unlikely to subscribe.")