import streamlit as st
import requests

def suggest_hospitals():
    """
    Function to help users find nearby hospitals using location input.
    """
    st.markdown("### 🏥 Find Nearby Hospitals")
    
    # Get user location
    location = st.text_input("Enter your location (city, state, or zip code):")
    
    if location:
        st.info("""
        Based on your location, here are some suggested steps:
        1. Open Google Maps
        2. Search for "hospitals near {location}"
        3. Check reviews and contact information
        4. Call ahead to verify availability
        """.format(location=location))
        
        # Add a direct link to Google Maps search
        maps_url = f"https://www.google.com/maps/search/hospitals+near+{location.replace(' ', '+')}"
        st.markdown(f"[🗺️ Open Google Maps]({maps_url})")
        
        st.markdown("---")
        st.markdown("""
        ### Emergency Contacts:
        - Emergency Services: 911 (US)
        - National Emergency Hotline: Your country's emergency number
        """)