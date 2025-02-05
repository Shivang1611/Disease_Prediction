import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

# Load the trained model
model_path = 'C:/Users/User/Desktop/Disease/trained_model.sav'
loaded_model = pickle.load(open(model_path, 'rb'))

# Define a StandardScaler (Use the same scaler that was used in training)
scaler = StandardScaler()

# Function to predict diabetes
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float).reshape(1, -1)
    input_data_scaled = scaler.fit_transform(input_data_as_numpy_array)
    prediction = loaded_model.predict(input_data_scaled)
    
    return '🩸 The person is diabetic' if prediction[0] == 1 else '✅ The person is not diabetic'

# Function to clear input fields
def clear_fields():
    for key in ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "diagnosis", "Gender"]:
        st.session_state[key] = ""  # Reset fields

# Main function for Streamlit App
def main():
    st.set_page_config(page_title="Diabetes Prediction App", layout="centered")  

    # Custom CSS styles
    st.markdown("""
    <style>
        body {
            background-color: #f4f8ff;
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            color: #2c3e50;
            font-weight: bold;
        }
        .header-box {
            background-color: #dff9fb;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }
        .stButton button {
            width: 100%;
            height: 50px;
            border-radius: 10px;
            font-size: 18px;
        }
        .result {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # App title
    st.markdown('<h1 class="main-title">Diabetes Prediction Web App 🏥</h1>', unsafe_allow_html=True)

    # Initialize session state variables
    if "diagnosis" not in st.session_state:
        st.session_state["diagnosis"] = ""
    if "Gender" not in st.session_state:
        st.session_state["Gender"] = "Male"

    # Gender selection as a dropdown
    gender = st.selectbox("Select Gender", ["Male", "Female"], key="Gender")

    # Input Fields
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            Glucose = st.text_input('Glucose Level', key="Glucose")
            BloodPressure = st.text_input('Blood Pressure Level', key="BloodPressure")
            SkinThickness = st.text_input('Skin Thickness Value', key="SkinThickness")
            BMI = st.text_input('BMI Value', key="BMI")

        with col2:
            Insulin = st.text_input('Insulin Level', key="Insulin")
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', key="DiabetesPedigreeFunction")
            Age = st.text_input('Age', key="Age")

            # Show Pregnancies only if Female is selected
            if gender == "Female":
                Pregnancies = st.text_input('Number of Pregnancies', key="Pregnancies")
            else:
                Pregnancies = "N/A"  

    # Container for Buttons
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button('🔍 Get Diabetes Test Result', key="predict"):
            try:
                input_data = [
                    float(Pregnancies) if Pregnancies != "N/A" else 0.0,  # If Male, set to 0
                    float(Glucose), float(BloodPressure),
                    float(SkinThickness), float(Insulin), float(BMI),
                    float(DiabetesPedigreeFunction), float(Age)
                ]
                
                # Log input data to the browser console using JavaScript
                st.markdown(f"""
                    <script>
                    console.log("Input Data: {{ 'Gender': '{gender}', 'Pregnancies': {Pregnancies}, 'Glucose': {Glucose}, 
                    'BloodPressure': {BloodPressure}, 'SkinThickness': {SkinThickness}, 
                    'Insulin': {Insulin}, 'BMI': {BMI}, 'DiabetesPedigreeFunction': {DiabetesPedigreeFunction}, 
                    'Age': {Age} }}");
                    </script>
                """, unsafe_allow_html=True)

                # Get Prediction
                diagnosis = diabetes_prediction(input_data)
                st.session_state["diagnosis"] = diagnosis  

            except ValueError:
                diagnosis = "❌ Invalid input. Please enter numerical values."
                st.session_state["diagnosis"] = diagnosis

    with col2:
        st.button("🗑 Clear Fields", on_click=clear_fields, key="clear")

    # Show Diagnosis Result
    if st.session_state["diagnosis"]:
        st.markdown(f'<p class="result">{st.session_state["diagnosis"]}</p>', unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
