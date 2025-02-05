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
diabetes_model_path = "C:/Users/User/Desktop/Disease/best_model_for_diabetes.sav"
heart_model_path = "C:/Users/User/Desktop/Disease/trained_model_for_heart_disease.sav"

diabetes_model = load_model(diabetes_model_path)
heart_model = load_model(heart_model_path)

# Set Streamlit page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background Image */
        .stApp {
            background: url('https://source.unsplash.com/1600x900/?medical,hospital') no-repeat center center fixed;
            background-size: cover;
        }

        /* Text Styling */
        h1 {
            font-size: 40px !important;
            color: #2c3e50;
            text-align: center;
            font-weight: bold;
        }

        h2 {
            font-size: 30px;
            color: #2980b9;
            font-weight: bold;
        }

        p, ul {
            font-size: 18px;
            color: #ffffff;
            font-weight: normal;
            background: rgba(44, 62, 80, 0.8);
            padding: 10px;
            border-radius: 10px;
        }

        /* Sidebar Customization */
        .css-18e3th9 {
            width: 180px !important;  /* Reduce sidebar size */
            background-color: #2c3e50 !important;
            padding-top: 10px;
        }

        /* Animation */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .animated-text {
            animation: fadeIn 1.5s ease-in-out;
        }

    </style>
""", unsafe_allow_html=True)

# Add a logo to the sidebar
#st.sidebar.image("https://your-image-url.com/logo.png", use_column_width=True, output_format="PNG", caption="Disease Prediction")

# Sidebar Navigation
menu = ["Home", "Disease Prediction", "About"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
import streamlit as st



# Home Page Content with Animations
def home_page():
    st.markdown("<h1 class='animated-text'>🏥 Welcome to Multiple Disease Prediction App</h1>", unsafe_allow_html=True)

    st.markdown("<h2>How It Works</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>💉 <b>Diabetes Prediction:</b> Predicts the likelihood of diabetes based on health metrics.</li>
        <li>❤️ <b>Heart Disease Prediction:</b> Assesses heart disease risk based on various factors.</li>
        <li>🔬 <b>AI-Based Prediction:</b> Uses machine learning algorithms for accurate results.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Key Features</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>⏱️ <b>Instant Results:</b> Get predictions immediately.</li>
        <li>🧠 <b>AI-Driven:</b> Advanced machine learning models.</li>
        <li>🔐 <b>Data Privacy:</b> Your information is secure.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Why This App?</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>🔍 <b>Early Detection:</b> Helps identify potential health risks early.</li>
        <li>🏥 <b>Medical Data-Based:</b> Uses medically validated health parameters.</li>
        <li>🌍 <b>Accessible:</b> Easy to use for everyone.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Important Notice</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>⚠️ <b>Not a Diagnosis Tool:</b> This app does not replace medical advice.</li>
        <li>💬 <b>Consult a Doctor:</b> Always seek professional healthcare.</li>
        <li>🛡️ <b>Confidentiality:</b> No personal data is stored.</li>
    </ul>
    """, unsafe_allow_html=True)

# Disease Prediction
def disease_prediction():
    st.title("🔍 Disease Prediction")
    
    disease = st.selectbox("Select Disease", ["Diabetes", "Heart Disease"])
    
    if disease == "Diabetes":
        st.subheader("Diabetes Prediction")
        sex = st.selectbox("Sex", ["Female", "Male"])
        
        pregnancies = 0 if sex == "Male" else st.number_input("Number of Pregnancies", min_value=0)
        glucose = st.number_input("Glucose Level", min_value=0)
        blood_pressure = st.number_input("Blood Pressure Level", min_value=0)
        skin_thickness = st.number_input("Skin Thickness", min_value=0)
        insulin = st.number_input("Insulin Level", min_value=0)
        bmi = st.number_input("BMI", min_value=0.0)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
        age = st.number_input("Age", min_value=0)

        if st.button("Predict Diabetes"):
            input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

            prediction = diabetes_model.predict(input_data)
            result = "Positive for Diabetes. Consult a doctor!" if prediction[0] == 1 else "No Diabetes detected."

            st.success(result)

    else:
        st.subheader("Heart Disease Prediction")
        age = st.number_input("Age", min_value=1)
        sex = st.selectbox("Sex", ["Female", "Male"])
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
        trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200)
        chol = st.number_input("Serum Cholesterol", min_value=100, max_value=600)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2)
        thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=6.0)
        slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2)
        ca = st.number_input("Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4)
        thal = st.selectbox("Thalassemia (1-3)", [1, 2, 3])

        if st.button("Predict Heart Disease"):
            input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            prediction = heart_model.predict(input_data)
            result = "Has Heart Disease. Consult a doctor!" if prediction[0] == 1 else "No Heart Disease detected."
            st.success(result)

# About Page
# About Page
# About Page
def about_page():
    st.title("ℹ️ About the Team")

    # Team and Background Details
    st.markdown("""
    We are B.Tech students working on our mini project on **DISEASE PREDICTION WEB APP** using machine learning models.

    ### Team Members:
    - **<span class="hover-shadow">Shivang Shukla</span>**
    - **<span class="hover-shadow">Sukhwinder Singh</span>**
    - **<span class="hover-shadow">Nikita Singh</span>**
    - **<span class="hover-shadow">Tushar Bhati</span>**

    Together, we are working to harness the power of AI to predict health risks and provide valuable insights to users.
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Our Vision
    Our vision is to use cutting-edge machine learning techniques to predict health conditions, enabling early detection and intervention. We aim to make healthcare more accessible by leveraging technology for better outcomes.
    """, unsafe_allow_html=True)

    # Contact Information
    st.markdown("""
    ### Contact Information
    For any queries or feedback, feel free to reach out to us:

    - Email: [shivangshukla306@gmail.com](mailto:shivangshukla306@gmail.com)
    - GitHub: [Shivang1611](https://github.com/Shivang1611)
    """, unsafe_allow_html=True)

    # Add some styling
    st.markdown("""
    <style>
        /* Remove background color */
        .stApp {
            background: none;
        }

        /* Styling for headers */
        h1, h2, h3 {
            font-family: 'Roboto', sans-serif;
            color: #2c3e50;
        }

        h1 {
            font-size: 50px;
            text-align: center;
            font-weight: bold;
        }

        h2 {
            font-size: 30px;
            color: #2980b9;
            font-weight: bold;
        }

        /* Styling for content sections */
        p, ul {
            font-size: 18px;
            color: #ffffff;
            font-weight: normal;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Hover effect with shadow on text */
        .hover-shadow {
            display: inline-block;
            transition: all 0.3s ease;
        }

        .hover-shadow:hover {
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
            color: #1abc9c;
        }

        /* Animation for fading text */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .animated-text {
            animation: fadeIn 1.5s ease-in-out;
        }

        /* Styling for contact info box */
        .contact-info {
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-top: 20px;
        }

        .contact-info a {
            color: #1abc9c;
            font-weight: bold;
            text-decoration: none;
        }

        .contact-info a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)

    # Contact information with link styling
    st.markdown("""
    <div class="contact-info">
        <p>Contact us at: <a href="mailto:shivangshukla306@gmail.com">shivangshukla306@gmail.com</a></p>
        <p>GitHub: <a href="https://github.com/Shivang1611" target="_blank">Shivang1611</a></p>
    </div>
    """, unsafe_allow_html=True)

# Example of calling the about_page function


# Page Selection
if choice == "Home":
    home_page()
elif choice == "Disease Prediction":
    disease_prediction()
elif choice == "About":
    about_page()

# Footer
st.markdown("""
    <style>
        .footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #2c3e50;
            font-family: 'Arial', sans-serif;
            font-size: 12px;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
        }
        .footer .left {
            text-align: left;
        }
        .footer .right {
            text-align: right;
        }
        .footer p {
            margin: 2px 0;
        }
        .footer a {
            color: #1abc9c;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .footer .contact-info {
            margin-top: 8px;
            font-size: 12px;
            color: #7f8c8d;
        }
    </style>
    <div class="footer">
        <div class="left">
            <p>© 2025 Multiple Disease Prediction App</p>
            <p>Aims to Predict the Disease</p>
        </div>
        <div class="right">
            <div class="contact-info">
                <p>Developed by: <strong>Shivang Shukla</strong></p>
                <p>Contact: <a href="mailto:shivangshukla306@gmail.com">shivangshukla306@gmail.com</a></p>
                <p>GitHub: <a href="https://github.com/Shivang1611" target="_blank">Shivang1611</a></p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
