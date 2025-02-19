import streamlit as st

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

    # ... rest of your about page code ...