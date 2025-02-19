import pickle
import joblib
import streamlit as st

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