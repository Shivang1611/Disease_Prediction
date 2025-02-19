import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import requests
import pandas as pd

def suggest_hospitals():
    """Main function to suggest nearby hospitals"""
    st.markdown("## 🏥 Find Nearby Hospitals")
    
    # Initialize session state for form submission
    if 'search_submitted' not in st.session_state:
        st.session_state.search_submitted = False
    
    # Create a form for the city input
    with st.form(key='hospital_search_form'):
        city = st.text_input("Enter your city name:")
        submit_button = st.form_submit_button("Search Hospitals")
        
        if submit_button:
            st.session_state.search_submitted = True
            st.session_state.city = city

    # Process the search if form was submitted
    if st.session_state.search_submitted:
        try:
            # Initialize Nominatim geocoder
            geolocator = Nominatim(user_agent="my_disease_app")
            
            with st.spinner("Finding your location..."):
                # Get coordinates for the city
                location = geolocator.geocode(st.session_state.city)
                
                if location:
                    # Fetch hospitals using Overpass API
                    overpass_url = "https://overpass-api.de/api/interpreter"
                    query = f"""
                    [out:json][timeout:25];
                    (
                        node["amenity"="hospital"](around:5000,{location.latitude},{location.longitude});
                        way["amenity"="hospital"](around:5000,{location.latitude},{location.longitude});
                    );
                    out body;
                    >;
                    out skel qt;
                    """
                    
                    with st.spinner("Searching for nearby hospitals..."):
                        response = requests.post(overpass_url, data=query)
                        
                        if response.status_code == 200:
                            data = response.json()
                            hospitals = []
                            
                            for element in data.get('elements', []):
                                if 'tags' in element:
                                    hospital = {
                                        'Name': element['tags'].get('name', 'Unknown Hospital'),
                                        'Address': element['tags'].get('addr:full', 
                                                 element['tags'].get('addr:street', 'Address not available')),
                                        'Phone': element['tags'].get('phone', 'Phone not available'),
                                        'lat': element.get('lat'),
                                        'lon': element.get('lon')
                                    }
                                    hospitals.append(hospital)
                            
                            if hospitals:
                                # Display hospitals in a table
                                st.markdown("### Nearby Hospitals:")
                                df = pd.DataFrame(hospitals)
                                st.dataframe(df[['Name', 'Address', 'Phone']], use_container_width=True)
                                
                                # Create and display map
                                m = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
                                
                                # Add user location marker
                                folium.Marker(
                                    [location.latitude, location.longitude],
                                    popup="Your Location",
                                    icon=folium.Icon(color='red', icon='info-sign')
                                ).add_to(m)
                                
                                # Add hospital markers
                                for hospital in hospitals:
                                    if hospital.get('lat') and hospital.get('lon'):
                                        folium.Marker(
                                            [hospital['lat'], hospital['lon']],
                                            popup=hospital['Name'],
                                            icon=folium.Icon(color='green', icon='plus', prefix='fa')
                                        ).add_to(m)
                                
                                st.markdown("### Map View:")
                                folium_static(m)
                            else:
                                st.warning("No hospitals found in the area.")
                        else:
                            st.error("Failed to fetch hospital data. Please try again.")
                else:
                    st.error("Could not find the specified city. Please try again.")
                    
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
