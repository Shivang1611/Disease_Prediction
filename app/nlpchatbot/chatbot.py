import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import requests
from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import threading

import os
from dotenv import load_dotenv
load_dotenv()
# OpenAI API configuration


# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize pyttsx3 engine globally
engine = pyttsx3.init()

# Set the voice to "Microsoft Ravi - English (India)"
voices = engine.getProperty('voices')
for voice in voices:
    if 'Ravi' in voice.name:  # Adjust based on the voice you want
        engine.setProperty('voice', voice.id)
        print(f"Voice set to: {voice.name}")
        break

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Function to shorten responses based on question complexity
def shorten_response(response, question, max_length=150):
    """Shorten response to appropriate length based on question complexity"""
    # Determine complexity by question length and structure
    question_words = len(question.split())
    
    # Very simple questions get very short answers
    if question_words < 5 or "?" not in question:
        max_length = 80
    # Longer questions might need more detailed responses
    elif question_words > 15:
        max_length = 200
        
    if len(response) <= max_length:
        return response
        
    # Try to find a natural cutoff point at sentence end
    cutoff = response[:max_length].rfind('. ')
    if cutoff > 0:
        return response[:cutoff+1]
    return response[:max_length] + "..."

# Function to recognize speech
def recognize_speech():
    try:
        with sr.Microphone() as source:
            # Adjust for ambient noise and set timeout
            recognizer.adjust_for_ambient_noise(source)
            st.info("Listening... Speak now!")
            audio = recognizer.listen(source, timeout=5)
            try:
                text = recognizer.recognize_google(audio)
                st.success(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                st.warning("Could not understand audio. Please try again.")
            except sr.RequestError as e:
                st.error(f"Speech recognition service error: {e}")
    except OSError as e:
        st.error(f"Microphone access error: {e}. Check your microphone settings.")
    return ""

# Function to speak text in a separate thread to prevent UI blocking
def speak_text(text):
    if "speaking_thread" in st.session_state and st.session_state.speaking_thread.is_alive():
        engine.stop()  # Stop any ongoing speech
        st.session_state.speaking_thread.join()  # Wait for thread to complete
    
    def speak_worker():
        engine.say(text)
        engine.runAndWait()
    
    st.session_state.speaking_thread = threading.Thread(target=speak_worker)
    st.session_state.speaking_thread.start()
    st.session_state.is_speaking = True

# Function to stop speech
def stop_speech():
    if "is_speaking" in st.session_state and st.session_state.is_speaking:
        engine.stop()
        if "speaking_thread" in st.session_state:
            st.session_state.speaking_thread.join()
        st.session_state.is_speaking = False
        return True
    return False

# Custom CSS for styling
st.markdown("""
    <style>
     [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stFooter"] {
            background: url('https://img.freepik.com/free-vector/clean-medical-background-vector_53876-175203.jpg?ga=GA1.1.968891202.1731431691&semt=ais_hybrid') no-repeat center center fixed !important;
            background-size: cover !important;
        }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .stTextInput input {
        padding: 10px;
        font-size: 16px;
    }
    .stExpander {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
    }
     .animated-text {
            animation: fadeIn 3s ease-in-out, pulse 3s infinite alternate;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app setup
st.markdown("<h1 class='animated-text'>Disease Prediction Chatbot</h1>", unsafe_allow_html=True)

st.write("Welcome to the Disease Prediction Chatbot. This chatbot uses the OpenAI GPT-4 API to provide health and medical advice.")

# Initialize session states
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if "talking_mode" not in st.session_state:
    st.session_state.talking_mode = False
    
if "is_speaking" not in st.session_state:
    st.session_state.is_speaking = False
    
if "speaking_thread" not in st.session_state:
    st.session_state.speaking_thread = None

# Toggle talking mode
if st.button("Toggle Talking Assistant"):
    st.session_state.talking_mode = not st.session_state.talking_mode
    if not st.session_state.talking_mode:
        stop_speech()

# Display current mode
st.write(f"Talking Assistant Mode: {'ON' if st.session_state.talking_mode else 'OFF'}")

# Stop speech button (always visible when speaking)
if "is_speaking" in st.session_state and st.session_state.is_speaking:
    if st.button("Stop Speaking"):
        if stop_speech():
            st.success("Speech stopped successfully")

# Voice input option in talking mode
if st.session_state.talking_mode:
    with st.expander("Voice Input", expanded=True):
        if st.button("Use Microphone"):
            voice_input = recognize_speech()
            if voice_input:
                st.session_state.voice_input = voice_input

# Text input for all modes
user_input = st.text_input("Type your health question:", key="user_input")

# Use voice input if available
if "voice_input" in st.session_state and st.session_state.voice_input:
    user_input = st.session_state.voice_input
    st.session_state.voice_input = None  # Clear after use

# Process user input
if user_input:
    try:
        # Call the OpenAI API to get a response
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in health and medical advice. Provide concise, accurate responses."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Get response and shorten it based on the question
        full_response = completion.choices[0].message.content.strip()
        shortened_response = shorten_response(full_response, user_input)
        
        # Display the conversation
        st.write(f"You: {user_input}")
        st.write(f"Bot: {shortened_response}")
        
        # Update the chat history
        st.session_state.chat_history.append({"user": user_input, "bot": shortened_response})
        
        # Speak the response if in talking mode
        if st.session_state.talking_mode:
            speak_text(shortened_response)
            
    except Exception as e:
        error_message = f"Sorry, there was an error with the OpenAI API: {e}"
        st.error(error_message)
        st.session_state.chat_history.append({"user": user_input, "bot": error_message})

# Display chat history
if st.session_state.chat_history:
    with st.expander("Chat History", expanded=False):
        for i, message in enumerate(st.session_state.chat_history):
            st.write(f"You: {message['user']}")
            st.write(f"Bot: {message['bot']}")
            st.write("---")