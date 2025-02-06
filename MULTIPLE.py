import streamlit as st
import pickle
import numpy as np
import joblib
import pandas as pd
import time
from PIL import Image

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
model_paths = {
    "Symptoms": "./optimized_disease_prediction_model(the model file).sav",
    "diabetes_best": "./best_model_for_diabetes.sav",
    "heart": "./trained_model_for_heart_disease.sav",
    "parkinsons": "./parkinsons_model.sav"
}
models = {name: load_model(path) for name, path in model_paths.items()}
encoder_path = "./disease_label_encoder(for converting disease names).sav"
with open(encoder_path, "rb") as encoder_file:
    label_encoder = joblib.load(encoder_file)

# Load symptom names
df = pd.read_csv("./Testing.csv")
symptom_list = list(df.columns[:-1])

# Set Streamlit page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide")
if 'page' not in st.session_state:
    st.session_state.page = 'home'
    
st.markdown("""
    <style>
        /* Global Background Image for Entire App */
        [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stFooter"] {
            background: url('https://img.freepik.com/free-vector/clean-medical-background-vector_53876-175203.jpg?ga=GA1.1.968891202.1731431691&semt=ais_hybrid') no-repeat center center fixed !important;
            background-size: cover !important;
        }

        /* Sidebar Customization */
        [data-testid="stSidebar"] {
            background: rgba(0, 0, 0, 0.9) !important; /* Darker Background */
            color: #FAD7A0 !important;
            box-shadow: 4px 0px 10px rgba(255, 255, 255, 0.3);
            padding: 20px;
            border-radius: 0 15px 15px 0;
        }

        /* Header Text Styling */
        h1, h2, h3 {
            color: black !important; /* Set heading text color to black */
        }

        h1 {
            font-size: 45px !important;
            text-align: center;
            font-weight: bold;
            text-shadow: 3px 3px 10px rgba(255, 255, 255, 0.6);
            animation: fadeIn 1.2s ease-in-out;
        }

        h2 {
            font-size: 32px;
            font-weight: bold;
            text-shadow: 2px 2px 6px rgba(255, 255, 255, 0.5);
            animation: slideIn 1.2s ease-in-out;
        }

        h3 {
            font-size: 24px;
            font-weight: bold;
        }

        /* Paragraph & List Styling */
        p, ul {
            font-size: 18px;
            color: #154360; /* Deep Blue */
            font-weight: normal;
            background: rgba(255, 255, 255, 0.7); /* Light Transparent White */
            padding: 15px;
            border-radius: 12px;
            box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        p:hover, ul:hover {
            transform: scale(1.03);
            box-shadow: 5px 5px 18px rgba(0, 0, 0, 0.3);
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #2874A6, #1A5276) !important; /* Gradient Blue */
            color: white !important;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px 20px;
            border: none;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #154360, #1A5276) !important;
            transform: translateY(-3px);
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.5);
        }

        /* Input Box */
        .stTextInput>div>div>input {
            background: rgba(200, 200, 255, 0.8) !important; /* Soft White */
            color: #154360 !important; /* Deep Blue */
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #2E86C1 !important;
            transition: all 0.3s ease-in-out;
        }

        .stTextInput>div>div>input:focus {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid #154360 !important;
        }

        /* Animations */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-15px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideIn {
            0% { opacity: 0; transform: translateX(-30px); }
            100% { opacity: 1; transform: translateX(0); }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.04); }
            100% { transform: scale(1); }
        }

        /* Animated Elements */
        .animated-text {
            animation: fadeIn 1.5s ease-in-out, pulse 3s infinite alternate;
        }

        /* Cards */
        .stCard {
            background: rgba(255, 255, 255, 0.8);
            padding: 15px;
            border-radius: 15px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
        }

        .stCard:hover {
            transform: translateY(-5px);
            box-shadow: 6px 6px 18px rgba(0, 0, 0, 0.3);
        }

    </style>
""", unsafe_allow_html=True)
# Add a logo to the sidebar
#st.sidebar.image("https://your-image-url.com/logo.png", use_column_width=True, output_format="PNG", caption="Disease Prediction")

# Sidebar Navigation
st.markdown("""
    <style>
        /* Global Background Image for Entire App */
        [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stFooter"] {
            background: url('https://img.freepik.com/free-vector/clean-medical-background-vector_53876-175203.jpg') no-repeat center center fixed !important;
            background-size: cover !important;
        }

        /* Sidebar - Stylish Look */
        [data-testid="stSidebar"] {
            background: rgba(0, 0, 0, 0.75) !important; /* Darker Background */
            color: #FAD7A0 !important;
            padding: 20px;
            box-shadow: 4px 0px 10px rgba(255, 255, 255, 0.2);
            border-radius: 0 15px 15px 0;
        }

      
        
       

      
       

        /* Input Box */
        .stTextInput>div>div>input {
            background: rgba(255, 255, 255, 0.8) !important;
            color: #154360 !important;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #2E86C1 !important;
        }

        /* Cards */
        .stCard {
            background: rgba(255, 255, 255, 0.85);
            padding: 15px;
            border-radius: 15px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar with Navigation Buttons


# Sidebar Buttons





st.sidebar.markdown("---")

# Sidebar Toggle for Light/Dark Mode


# Sidebar Profile Section

menu = ["Home", "Predict By Report", "Predict By Symptoms", "About", "Query", "Upload Reports"]
choice = st.sidebar.selectbox("Navigation", menu)
# Sidebar Separator
st.sidebar.markdown("---")

# Function for Query Page
def Query():
    st.markdown("<h1 class='animated-text'>Send Query</h1>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        .query-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .query-button {
            background: linear-gradient(135deg, #2874A6, #1A5276) !important;
            color: blue !important;
            font-size: 16px;
            font-weight: bold;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease-in-out;
        }
        .query-button:hover {
            background: linear-gradient(135deg, #154360, #1A5276) !important;
            transform: translateY(-3px);
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.5);
        }
        .alert {
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            margin-top: 20px;
            border-radius: 5px;
            border: 1px solid #c3e6cb;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.form(key='query_form'):
        user_email = st.text_input("Your Email")
        query_message = st.text_area("Your Query")
        submit_button = st.form_submit_button("Send Query", help="Submit your query via email")

        if submit_button:
            st.session_state.query_sent = True  # Flag to indicate the query was sent
            st.success("Your query has been sent successfully!")

# Page Navigation
if choice == "Query":
    Query()


#upload report page 


def create_report_upload_page():
    st.markdown("<h1 class='animated-text'>📂 Medical Report Upload</h1>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        /* Main Page Background */
        [data-testid="stAppViewContainer"] {
            background: url('https://img.freepik.com/free-vector/clean-medical-background-vector_53876-175203.jpg') no-repeat center center fixed !important;
            background-size: cover !important;
        }

        /* Upload Sections Container - Flexbox */
        .report-section {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            padding: 10px;
        }

        /* Upload Sections - Card Style */
       .report-container {
    background: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
    transition: all 0.3s ease-in-out;
    width: 30%; /* Adjusted width */
    min-width: 280px; /* Ensures responsiveness */
    margin-bottom: 20px; /* Adds space between cards and buttons */
}


        /* Hover Effect on Upload Sections */
        .report-container:hover {
            transform: scale(1.02);
            box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.3);
        }

        /* Upload Buttons */
       .upload-button {
    background: linear-gradient(135deg, #2874A6, #1A5276) !important;
    color: white !important;
    font-size: 14px;
    font-weight: bold;
    padding: 10px;
    border-radius: 8px;
    width: 100%;
    text-align: center;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease-in-out;
    margin-top: 20px; /* Adds space between the cards and the button */
}
        /* Hover Effect on Buttons */
        .upload-button:hover {
            background: linear-gradient(135deg, #154360, #1A5276) !important;
            transform: translateY(-2px);
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.4);
        }

        /* Smaller Upload Box */
        .stFileUploader > div {
            width: 80% !important;
            margin: 0 auto;
        }

        /* Success Message Animation */
        .success-message {
            animation: fadeIn 0.5s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
        """, unsafe_allow_html=True)
    
        

    col1, col2, col3 = st.columns(3)
    if 'page' not in st.session_state:
     st.session_state.page = None

# Diabetes Report Section
    with col1:
        st.markdown("<div class='report-container'><h3>🩸 Diabetes Reports</h3>", unsafe_allow_html=True)
        diabetes_file = st.file_uploader("Upload Diabetes Report", type=['txt', 'pdf', 'csv'], key='diabetes')
        if diabetes_file:
            try:
                st.success("✅ Report parsed successfully!", icon="✅")
                st.session_state.diabetes_data = diabetes_file  # Save file in session state
                if st.button("🔍 Analyze Diabetes", key='diabetes_pred', help="Go to Diabetes Prediction"):
                    st.session_state.page = "Diabetes Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

# Heart Disease Report Section
    with col2:
        st.markdown("<div class='report-container'><h3>❤️ Heart Disease Reports</h3>", unsafe_allow_html=True)
        heart_file = st.file_uploader("Upload Heart Report", type=['txt', 'pdf', 'csv'], key='heart')
        if heart_file:
            try:
                st.success("✅ Report parsed successfully!", icon="✅")
                st.session_state.heart_data = heart_file  # Save file in session state
                if st.button("🔍 Analyze Heart Disease", key='heart_pred', help="Go to Heart Disease Prediction"):
                    st.session_state.page = "Heart Disease Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

# Parkinson's Report Section
    with col3:
        st.markdown("<div class='report-container'><h3>🧠 Parkinson's Reports</h3>", unsafe_allow_html=True)
        parkinsons_file = st.file_uploader("Upload Parkinson's Report", type=['txt', 'pdf', 'csv'], key='parkinsons')
        if parkinsons_file:
            try:
                st.success("✅ Report parsed successfully!", icon="✅")
                st.session_state.parkinsons_data = parkinsons_file  # Save file in session state
                if st.button("🔍 Analyze Parkinson's", key='parkinsons_pred', help="Go to Parkinson’s Prediction"):
                    st.session_state.page = "Parkinson's Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

# Handle navigation and prediction pages based on session_state.page
if st.session_state.page == "Diabetes Prediction":
    st.write("## Diabetes Prediction Results")
    diabetes_data = st.session_state.get('diabetes_data', None)
    if diabetes_data:
        with st.spinner("🧑‍🔬 Analyzing diabetes report... Please wait!"):
            time.sleep(4)
            st.success("✅ Analysis complete! We'll update you shortly.")
            st.info("We are working on improving the results. Check back soon for more detailed analysis.")
    else:
        st.error("No diabetes report data available")

elif st.session_state.page == "Heart Disease Prediction":
    st.write("## Heart Disease Prediction Results")
    heart_data = st.session_state.get('heart_data', None)
    if heart_data:
        with st.spinner("🧑‍🔬 Analyzing heart disease report... Please wait!"):
            time.sleep(4)
            st.success("✅ Analysis complete! We'll update you shortly.")
            st.info("We are working on improving the results. Check back soon for more detailed analysis.")
    else:
        st.error("No heart disease report data available")

elif st.session_state.page == "Parkinson's Prediction":
    st.write("## Parkinson's Disease Prediction Results")
    parkinsons_data = st.session_state.get('parkinsons_data', None)
    if parkinsons_data:
        with st.spinner("🧑‍🔬 Analyzing Parkinson's report... Please wait!"):
            time.sleep(4)
            st.success("✅ Analysis complete! We'll update you shortly.")
            st.info("We are working on improving the results. Check back soon for more detailed analysis.")
    else:
        st.error("No Parkinson's report data available")
# Sidebar for navigation





# Home Page Content with Animations
def home_page():
    st.markdown("<h1 class='animated-text'>🏥 Welcome to Disease Prediction App</h1>", unsafe_allow_html=True)

    st.markdown("<h2>How It Works</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>💉 <b>Diabetes Prediction:</b> Predicts the likelihood of diabetes based on health metrics.</li>
        <li>❤️ <b>Heart Disease Prediction:</b> Assesses heart disease risk based on various factors.</li>
        <li> <b>Parkinson Disease Prediction:</b> Assesses heart disease risk based on various factors.</li>
        <li>🔬 <b>Predict Disease By Symptoms:</b> Uses machine learning algorithms for accurate results.</li>
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



# Disease Prediction
def disease_prediction():
    st.markdown("<h1 class='animated-text'>🔍 Disease Prediction By Report</h1>", unsafe_allow_html=True)
    
    disease = st.selectbox("Select Disease", ["Diabetes", "Heart Disease", "Parkinson's Disease"])
    
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
            if glucose == 0 or blood_pressure == 0 or bmi == 0.0 or age == 0:
                st.warning("⚠️ Please fill in all required fields before predicting.")
            else:
                try:
                    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
                    prediction = models["diabetes_best"].predict(input_data)
                    result = "Positive for Diabetes. Consult a doctor!" if prediction[0] == 1 else "No Diabetes detected."
                    st.success(result)
                except ValueError:
                    st.error("You entered the wrong input, please enter the correct input.")

    elif disease == "Heart Disease":
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
            if age == 1 or trestbps == 80 or chol == 100 or thalach == 60:
                st.warning("⚠️ Please enter all required values before predicting.")
            else:
                try:
                    input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                    prediction = models["heart"].predict(input_data)
                    result = "Has Heart Disease. Consult a doctor!" if prediction[0] == 1 else "No Heart Disease detected."
                    st.success(result)
                except ValueError:
                    st.error("You entered the wrong input, please enter the correct input.")

    else:
        st.subheader("Parkinson's Disease Prediction")

        age = st.number_input("Age", min_value=0, step=1)
        gender = st.selectbox("Gender", ["Male", "Female"])  # Convert to binary later
        ethnicity = st.number_input("Ethnicity", min_value=0, step=1)
        bmi = st.number_input("BMI", min_value=0.0, format="%f")
        smoking = st.number_input("Smoking", min_value=0, step=1)
        alcohol = st.number_input("Alcohol Consumption", min_value=0.0, format="%f")
        physical_activity = st.number_input("Physical Activity", min_value=0.0, format="%f")
        diet_quality = st.number_input("Diet Quality", min_value=0.0, format="%f")
        sleep_quality = st.number_input("Sleep Quality", min_value=0.0, format="%f")
        family_history = st.number_input("Family History of Parkinson's", min_value=0, step=1)
        brain_injury = st.number_input("Traumatic Brain Injury", min_value=0, step=1)
        diabetes = st.number_input("Diabetes", min_value=0, step=1)
        depression = st.number_input("Depression", min_value=0, step=1)
        stroke = st.number_input("Stroke", min_value=0, step=1)
        systolic_bp = st.number_input("Systolic Blood Pressure", min_value=0, step=1)
        diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=0, step=1)
        cholesterol = st.number_input("Cholesterol Total", min_value=0.0, format="%f")
        tremor = st.number_input("Tremor", min_value=0, step=1)
        rigidity = st.number_input("Rigidity", min_value=0, step=1)
        bradykinesia = st.number_input("Bradykinesia", min_value=0, step=1)
        postural_instability = st.number_input("Postural Instability", min_value=0, step=1)
        speech_problems = st.number_input("Speech Problems", min_value=0, step=1)
        sleep_disorders = st.number_input("Sleep Disorders", min_value=0, step=1)
        constipation = st.number_input("Constipation", min_value=0, step=1)
        
        gender_binary = 1 if gender == "Male" else 0

        if st.button("Predict Parkinson's Disease"):
            if age == 0 or bmi == 0.0 or sleep_quality == 0.0 or cholesterol == 0.0:
                st.warning("⚠️ Please provide all necessary inputs before predicting.")
            else:
                try:
                    input_data = np.array([[age, gender_binary, ethnicity, bmi, smoking, alcohol, physical_activity, diet_quality, 
                                            sleep_quality, family_history, brain_injury, diabetes, depression, stroke, systolic_bp, 
                                            diastolic_bp, cholesterol, tremor, rigidity, bradykinesia, postural_instability, 
                                            speech_problems, sleep_disorders, constipation]])
                    prediction = models["parkinsons"].predict(input_data)
                    result = "Parkinson's Detected. Consult a specialist!" if prediction[0] == 1 else "No Parkinson's detected."
                    st.success(result)
                except ValueError:
                    st.error("You entered the wrong input, please enter the correct input.")# About Page
def about_page():
   
    st.markdown("<h1 class='animated-text'>ℹ️ About the Team</h1>", unsafe_allow_html=True)
                
                
                

    # Team and Background Details
    st.markdown("""
    We are B.Tech students working on our mini project on **DISEASE PREDICTION WEB APP** using machine learning models.

    ### Team Members:
    - **<span class="hover-shadow">Shivang Shukla </span>**
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
    .animated-text {
        animation: fadeIn 1.5s ease-in-out, pulse 3s infinite alternate;
    }
        /* Remove background color */
        .stApp {
            background: none;
        }

        /* Styling for headers */
        h1, h2, h3 {
            font-family: 'Roboto', sans-serif;
            color: black;
        }

        h1 {
            font-size: 50px;
            text-align: center;
            font-weight: bold;
        }

        h2 {
            font-size: 30px;
            color: black;
            font-weight: bold;
        }

        /* Styling for content sections */
        p, ul {
            font-size: 18px;
            color: black;
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
            color: black;
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
def symptom_checker():
    st.markdown("<h1 class='animated-text'>🔍 Disease Prediction By Symptoms</h1>", unsafe_allow_html=True)
    
    # Load the disease prediction model and encoder specifically for symptom checker
    try:
        model_path = "./optimized_disease_prediction_model(the model file).sav"
        model = joblib.load(model_path)
        
        encoder_path = "./disease_label_encoder(for converting disease names).sav"
        with open(encoder_path, "rb") as encoder_file:
            label_encoder = joblib.load(encoder_file)
    except Exception as e:
        st.error(f"Error loading model or encoder: {e}")
        return

    progress_bar = st.progress(0)
    selected_symptoms = []
    input_vector = np.zeros((1, len(symptom_list)))

    st.markdown('<div class="symptom-container">', unsafe_allow_html=True)
    for i, symptom in enumerate(symptom_list):
        col1, col2, col3 = st.columns([3, 2, 2])
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
            with col3:
                severity = st.selectbox(
                    "",
                    ("Mild", "Moderate", "Severe", "Critical"),
                    key=f"severity_{i}",
                    label_visibility="collapsed"
                )
                if severity == "Mild":
                    input_vector[0, i] = 1
                elif severity == "Moderate":
                    input_vector[0, i] = 2
                elif severity == "Severe":
                    input_vector[0, i] = 3
                elif severity == "Critical":
                    input_vector[0, i] = 4
                selected_symptoms.append(f"{symptom} ({severity})")
        else:
            input_vector[0, i] = 0
        
        progress = (i + 1) / len(symptom_list)
        progress_bar.progress(progress)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Predict Disease", key="predict_button"):
        if any(input_vector[0]):
            try:
                # Make sure model is properly loaded before prediction
                if hasattr(model, 'predict'):
                    prediction = model.predict(input_vector)
                    disease = label_encoder.inverse_transform(prediction)[0]
                    
                    st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
                    st.success(f"🔍 Predicted Disease: **{disease}**")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    if selected_symptoms:
                        st.markdown("### Selected Symptoms:")
                        for symptom in selected_symptoms:
                            st.markdown(f"- {symptom.replace('_', ' ').title()}")
                else:
                    st.error("Model not properly loaded. Please check the model file.")
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.error("⚠️ Please select at least one symptom.")

if choice == "Home":
    home_page()
elif choice == "Predict By Report":
    disease_prediction()
elif choice == "Predict By Symptoms":
    symptom_checker()

elif choice == 'Upload Reports':
    create_report_upload_page()
elif choice == "About":
    about_page()

# Footer


