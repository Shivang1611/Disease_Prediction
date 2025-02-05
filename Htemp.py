# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:21:21 2025

@author: User
"""

import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('C:/Users/User/Desktop/Disease/trained_model_for_heart_disease.sav', 'rb'))

# Sample input data
input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

# Convert the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make prediction
prediction = loaded_model.predict(input_data_reshaped)  # Fixed the variable name

# Print prediction result
print(prediction)

if prediction[0] == 0:
    print('The Person does not have a Heart Disease')
else:
    print('The Person has Heart Disease')
