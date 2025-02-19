import streamlit as st
import numpy as np
from utils.model_loader import load_model
from hospital_finder import suggest_hospitals

def symptom_checker(model, label_encoder, symptom_list):
    st.markdown("<h1 class='animated-text'>Disease Prediction by Symptoms</h1>", unsafe_allow_html=True)
    
    # Multi-select for symptoms
    selected_symptoms = st.multiselect("Select Symptoms:", symptom_list)
    
    if st.button("Predict Disease", key="predict_button"):
        if selected_symptoms:
            # Create input vector
            input_vector = np.zeros((1, len(symptom_list)))
            for symptom in selected_symptoms:
                index = symptom_list.index(symptom)
                input_vector[0][index] = 1
                
            try:
                prediction = model.predict(input_vector)
                disease = label_encoder.inverse_transform(prediction)[0]
                
                st.success(f"Predicted Disease: {disease}")
                
                # Show hospital suggestion button
                st.markdown("### Need medical assistance?")
                if st.button("🏥 Find Nearby Hospitals"):
                    suggest_hospitals()
                    
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.warning("Please select at least one symptom.")