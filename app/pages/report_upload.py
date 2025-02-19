import streamlit as st

def create_report_upload_page():
    st.markdown("<h1 class='animated-text'>📂 Medical Report Upload</h1>", unsafe_allow_html=True)
    
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
                st.session_state.diabetes_data = diabetes_file
                if st.button("🔍 Analyze Diabetes", key='diabetes_pred', help="Go to Diabetes Prediction"):
                    st.session_state.page = "Diabetes Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ... rest of your report upload code ...