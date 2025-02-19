import streamlit as st

def home_page():
    st.markdown("<h1 class='animated-text'>🏥 Welcome to Disease Prediction System</h1>", unsafe_allow_html=True)
    
    # Main Features Section
    st.markdown("<h2>Main Features</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='feature-container'>
        <div class='feature-item'>
            <h3>💉 Disease Prediction</h3>
            <ul>
                <li>Heart Disease Analysis</li>
                <li>Parkinson's Disease Detection</li>
                <li>Diabetes Risk Assessment</li>
            </ul>
        </div>
        
        <div class='feature-item'>
            <h3>🔍 Symptom Analysis</h3>
            <ul>
                <li>Input your symptoms</li>
                <li>Get possible conditions</li>
                <li>Severity assessment</li>
            </ul>
        </div>
        
        <div class='feature-item'>
            <h3>📊 Report Analysis</h3>
            <ul>
                <li>Upload medical reports</li>
                <li>Automated analysis</li>
                <li>Detailed insights</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("<h2>How It Works</h2>", unsafe_allow_html=True)
    st.markdown("""
    1. **Choose Prediction Method**
       - By Symptoms
       - By Medical Reports
       - By Health Parameters
    
    2. **Input Your Data**
       - Enter symptoms or upload reports
       - Provide required health metrics
       - Answer relevant questions
    
    3. **Get Results**
       - Receive prediction results
       - View detailed analysis
       - Get recommended actions
    """)
    
    # Additional Information
    st.markdown("<h2>Why Choose Us?</h2>", unsafe_allow_html=True)
    st.markdown("""
    - 🎯 **High Accuracy**: Advanced ML models trained on large datasets
    - ⚡ **Quick Results**: Get instant predictions and analysis
    - 🔒 **Secure**: Your health data remains private and secure
    - 📱 **Accessible**: Use on any device, anytime
    """)

if __name__ == "__main__":
    home_page()