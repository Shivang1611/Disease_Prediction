import streamlit as st
import pickle
import numpy as np
import joblib
import pandas as pd
import time

# Load the ML model
model_path = "C:/Users/User/Desktop/Disease/optimized_disease_prediction_model(the model file).sav"
encoder_path = "C:/Users/User/Desktop/Disease/disease_label_encoder(for converting disease names).sav"

with open(model_path, "rb") as model_file:
    model = joblib.load(model_file)

with open(encoder_path, "rb") as encoder_file:
    label_encoder = joblib.load(encoder_file)

# Load the dataset to get symptom names
df = pd.read_csv("C:/Users/User/Desktop/Disease/Testing.csv")
symptom_list = list(df.columns[:-1])  # Exclude the 'prognosis' column

# UI setup with custom styling
st.set_page_config(
    page_title="Disease Predictor",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .symptom-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .title-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .prediction-container {
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
        animation: fadeIn 0.5s ease-in;
    }
    .stSelectbox {
        margin-bottom: 1rem;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .disclaimer {
        margin-top: 2rem;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 10px;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.title("🩺 AI-Powered Disease Predictor")
st.markdown("""
    Get an instant preliminary disease prediction based on your symptoms.
    Please select Yes/No for each symptom below.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Yes/No selector for symptoms with progress bar
progress_bar = st.progress(0)
selected_symptoms = []
input_vector = np.zeros((1, len(symptom_list)))

st.markdown('<div class="symptom-container">', unsafe_allow_html=True)
for i, symptom in enumerate(symptom_list):
    col1, col2 = st.columns([3, 2])
    with col1:
        st.write(f"**{symptom.replace('_', ' ').title()}**")
    with col2:
        response = st.selectbox(
            "",
            ("No", "Yes"),
            key=f"symptom_{i}",
            label_visibility="collapsed"
        )
    if response == "Yes":
        input_vector[0, i] = 1
        selected_symptoms.append(symptom)
    
    # Update progress bar
    progress = (i + 1) / len(symptom_list)
    progress_bar.progress(progress)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("Predict Disease", key="predict_button"):
    if any(input_vector[0]):
        with st.spinner('Analyzing symptoms...'):
            time.sleep(1)  # Add slight delay for effect
            
            # Prediction
            prediction = model.predict(input_vector)
            disease = label_encoder.inverse_transform(prediction)[0]
            
            st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
            st.success(f"🔍 Predicted Disease: **{disease}**")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Display selected symptoms
            if selected_symptoms:
                st.markdown("### Selected Symptoms:")
                for symptom in selected_symptoms:
                    st.markdown(f"- {symptom.replace('_', ' ').title()}")
    else:
        st.error("⚠️ Please select at least one symptom.")

# Disclaimer
st.markdown("""
    <div class="disclaimer">
    <h4>⚠️ Disclaimer:</h4>
    This is an AI-powered prediction tool and should not be used as a substitute for professional medical advice. 
    Please consult with a healthcare provider for proper diagnosis and treatment.
    </div>
    """, unsafe_allow_html=True)