import streamlit as st
import pandas as pd
from src.model_training import train_and_save_model
from src.predict import predict_single
import os

DATA_PATH = 'data/credit_risk_dataset.csv'
MODEL_PATH = 'model.pkl'

st.title("Credit Card Risk Prediction App")

# Train model if not present
if not os.path.exists(MODEL_PATH):
    st.info("Training model for the first time...")
    train_and_save_model(DATA_PATH, MODEL_PATH)

# Load CSV to get columns
df = pd.read_csv(DATA_PATH)
input_features = [col for col in df.columns if col != 'Risk' and col != 'id']

st.header("Enter Applicant Data:")

user_input = {}
for col in input_features:
    if pd.api.types.is_numeric_dtype(df[col]):
        user_input[col] = st.number_input(col, float(df[col].min()), float(df[col].max()), float(df[col].mean()))
    else:
        options = df[col].unique().tolist()
        user_input[col] = st.selectbox(col, options)

if st.button("Predict Risk"):
    pred, prob = predict_single(user_input, MODEL_PATH)
    st.write(f"**Predicted Risk:** {pred}")
    st.write(f"**Confidence:** {prob:.2f}")