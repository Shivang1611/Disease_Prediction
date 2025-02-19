import streamlit as st

def show_first_aid_page():
    st.title("First Aid Guide")

    first_aid_data = {
        "Burns": "Cool the burn with running water for 10-15 minutes.  Do not use ice. Cover with a sterile bandage.",
        "Cuts": "Clean the wound with soap and water. Apply pressure to stop bleeding. Cover with a bandage.",
        "Sprains": "Rest, Ice, Compression, Elevation (RICE).",
        #... Add more first aid topics...
    }

    for topic, info in first_aid_data.items():
        st.subheader(topic)
        st.write(info)

    # Example: Add an image (you'll need to have the image file in the same directory or provide a URL)
    try:
        from PIL import Image
        image = Image.open("first_aid_image.png")  # Replace with your image file
        st.image(image, caption="First Aid Image", use_column_width=True)
    except FileNotFoundError:
        st.error("Image not found. Please place 'first_aid_image.png' in the same directory.")
    except ImportError:
        st.error("Pillow library not found. Install it: pip install Pillow")
    except Exception as e:
        st.error(f"An error occurred while loading the image: {e}")