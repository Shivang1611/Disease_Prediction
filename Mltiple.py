import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
model_filename = "C:/Users/User/Desktop/Multiple/parkinsons_model"
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

# UI Title
st.title("Parkinson's Disease Detection")

# User Input Type Selection
st.sidebar.header("Input Type")
input_type = st.sidebar.radio("Choose input type:", ["Manual Entry", "Upload CSV"])

# Function to make predictions
def predict_parkinsons(data):
    prediction = model.predict(data)
    return ["Parkinson's Detected" if p == 1 else "No Parkinson's" for p in prediction]

# Manual Input
if input_type == "Manual Entry":
    st.subheader("Enter Patient Data")
    
    # Dynamically create input fields
    num_features = 22  # Adjust based on actual dataset
    user_input = []
    
    for i in range(num_features):
        value = st.number_input(f"Feature {i+1}", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        user_input.append(value)
    
    if st.button("Predict"):
        user_data = np.array([user_input]).reshape(1, -1)  # Reshape for model
        result = predict_parkinsons(user_data)
        st.success(f"Prediction: {result[0]}")

# CSV Upload
elif input_type == "Upload CSV":
    st.subheader("Upload Patient Data CSV File")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:", data.head())

        if st.button("Predict for CSV"):
            predictions = predict_parkinsons(data)
            data["Prediction"] = predictions
            st.write("Prediction Results:", data)

            # Option to download results
            csv_download = data.to_csv(index=False).encode("utf-8")
            st.download_button("Download Results", csv_download, "predictions.csv", "text/csv")

