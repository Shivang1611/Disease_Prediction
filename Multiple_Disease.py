import numpy as np
import pickle
import joblib
import streamlit as st

# Load models
def load_model(path):
    try:
        with open(path, "rb") as file:
            return pickle.load(file)
    except (pickle.UnpicklingError, EOFError):
        try:
            return joblib.load(path)
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None

# Paths to trained models
diabetes_model_path = "C:/Users/User/Desktop/Disease/trained_model.sav"
heart_model_path = "C:/Users/User/Desktop/Disease/trained_model_for_heart_disease.sav"

diabetes_model = load_model(diabetes_model_path)
heart_model = load_model(heart_model_path)

# Set Streamlit page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide")

# Custom CSS for navbar, background, and UI enhancements
st.markdown("""
    <style>
        /* Navbar styling */
       .navbar {
            display: flex;
            justify-content: center;
            background: linear-gradient(to right, #42a5f5, #1e88e5);
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .navbar button {
            color: white;
            background: transparent;
            border: 2px solid white;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin: 0 10px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }
        .navbar button:hover, .navbar button.active {
            background-color: white;
            color: #1e88e5;
            transform: scale(1.1);
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 12px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .services {
            margin-top: 30px;
        }
        .service-item {
            background: #e3f2fd;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
        }
        .stApp {
            background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjmUMCvxMaA1-ZiwzpJB6bkgt9OYAg3dmi-w&s');
            background-size: cover;
            background-position: center;
            color: #333;
        }
        input, select, .stNumberInput, .stSelectbox {
            background-color: #ffffff !important;
            color: #333 !important;
            border-radius: 8px !important;
            padding: 10px !important;
            font-size: 16px !important;
            border: 1px solid #ccc;
        }
        .footer {
            text-align: center;
            padding: 6px;
            position: fixed;
            bottom: 0;
            width: 100%;
            background: #e3f2fd;
            color: #333;
            font-weight: bold;
            border-radius: 10px 10px 0 0;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar with Streamlit buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "home"
with col2:
    if st.button("🩺 Disease Prediction"):
        st.session_state.page = "disease"
with col3:
    if st.button("ℹ️ About"):
        st.session_state.page = "about"

# Navigation handling
if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("🏥 Welcome to Multiple Disease Prediction App")
    st.write("Use this app to predict Diabetes and Heart Disease based on medical parameters.")
elif st.session_state.page == "disease":
    st.title("🔍 Disease Prediction")
    disease = st.selectbox("Select Disease", ["Diabetes", "Heart Disease"], key='disease')
    
    if disease == "Diabetes":
        st.subheader("Diabetes Prediction")
        sex = st.selectbox("Sex", ["Female", "Male"], key='sex')
        pregnancies = 0 if sex == "Male" else st.number_input("Number of Pregnancies", min_value=0, key='pregnancies')
        glucose = st.number_input("Glucose Level", min_value=0, key='glucose')
        blood_pressure = st.number_input("Blood Pressure Level", min_value=0, key='bp')
        skin_thickness = st.number_input("Skin Thickness", min_value=0, key='skin')
        insulin = st.number_input("Insulin Level", min_value=0, key='insulin')
        bmi = st.number_input("BMI", min_value=0.0, key='bmi')
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, key='dpf')
        age = st.number_input("Age", min_value=0, key='age')
        
        if st.button("Predict Diabetes"):
            input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
            prediction = diabetes_model.predict(input_data)
            st.success("Diabetic" if prediction[0] == 1 else "Not Diabetic")
    
    else:
        st.subheader("Heart Disease Prediction")
        
        # Collect all 13 input features
        age = st.number_input("Age", min_value=1, key='age2')
        sex = st.selectbox("Sex", ["Female", "Male"], key='sex2')
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, key='cp')
        trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, key='trestbps')
        chol = st.number_input("Serum Cholesterol", min_value=100, max_value=600, key='chol')
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], key='fbs')
        restecg = st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=2, key='restecg')
        maxhr = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=220, key='maxhr')
        exang = st.selectbox("Exercise Induced Angina", [0, 1], key='exang')
        oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, step=0.1, key='oldpeak')
        st_slope = st.number_input("ST Slope", min_value=0, max_value=2, key='st_slope')
        
        # Additional features if necessary, such as 'thal' (Thalassemia)
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3], key='thal')

        # Ensure you're passing all 13 features in the correct order
        if st.button("Predict Heart Disease"):
            input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, maxhr, exang, oldpeak, st_slope, thal]])
            prediction = heart_model.predict(input_data)
            st.success("Has Heart Disease" if prediction[0] == 1 else "No Heart Disease")

# Footer
st.markdown("""
    <div class='footer'>
        <p>© 2025 Multiple Disease Prediction App</p>
        <p>Aims to Predict the Disease</p>
    </div>
""", unsafe_allow_html=True)