import streamlit as st
import os
from PIL import Image
from utils.style_loader import load_css 


def show_first_aid_page():
    st.title("First Aid Guide")
    load_css()
    
    
    first_aid_data = {
        "Burns": {
            "description": "Cool the burn with running water for 10-15 minutes. Do not use ice. Cover with a sterile bandage.",
            "image": "https://media.istockphoto.com/id/157501585/photo/closeup-of-steam-burn-on-mans-forearm.jpg?s=612x612&w=0&k=20&c=se9Pm0-wZI05JfToN3ePYAOgt0hHoSLUGLX_H-T7Zc4="
        },
        "Cuts": {
            "description": "Clean the wound with soap and water. Apply pressure to stop bleeding. Cover with a bandage.",
            "image": "https://cdn.wecanbeaeros.com/wp-content/uploads/cut-1024x683.jpg"
        },
        "Sprains": {
            "description": "Rest, Ice, Compression, Elevation (RICE).",
            "image": "sprain_image.gif"
        },
        "Nosebleeds": {
            "description": "Sit upright and lean forward. Pinch your nostrils just below the bony bridge of your nose for 5-10 minutes. Breathe through your mouth.",
            "image": "nosebleed_image.jpg"
        },
        "Choking": {
            "description": "If someone is choking and cannot speak or breathe, perform the Heimlich maneuver. If unconscious, begin CPR.",
            "image": "choking_image.jpg"
        },
        "Allergic Reactions": {
            "description": "If someone has a severe allergic reaction (anaphylaxis), use an epinephrine auto-injector (EpiPen) if available and call emergency services immediately.",
            "image": "allergy_image.jpg"
        },
        "Heart Attack": {
            "description": "Recognize the signs: chest pain, shortness of breath, sweating, nausea. Call emergency services immediately.",
            "image": "heart_attack_image.jpg"
        },
        "Fainting": {
            "description": "If someone faints, lay them on their back and elevate their legs. Ensure they have fresh air. If they don't regain consciousness quickly, seek medical attention.",
            "image": "fainting_image.jpg"  # Replace with your image
        },
        "Head Injuries": {
            "description": "If someone has a head injury, keep them still and call for emergency medical help, especially if they lose consciousness, vomit, or have a seizure.",
            "image": "head_injury_image.jpg" # Replace with your image
        },
        "Insect Stings": {
            "description": "Remove the stinger if visible. Wash the area with soap and water. Apply a cold compress to reduce swelling. Watch for signs of an allergic reaction.",
            "image": "sting_image.jpg" # Replace with your image
        },
        "Poisoning": {
            "description": "If someone has ingested poison, call your local poison control center or emergency services immediately. Do not induce vomiting unless instructed to do so.",
            "image": "poisoning_image.jpg" # Replace with your image
        },
    }
    
    # Create columns for better layout
    for topic, info in first_aid_data.items():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader(topic)
            with st.expander("Show Details"):
                st.write(info["description"])
        
        with col2:
            # Simplified image handling
            try:
                image_path = info.get("image", "")
                if image_path and os.path.exists(image_path):
                    image = Image.open(image_path)
                    st.image(image, caption=f"{topic} First Aid", use_column_width=True)
                else:
                    st.write("Image not available")
            except Exception as e:
                st.write(f"Unable to load image: {str(e)}")

