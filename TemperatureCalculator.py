#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Temperature converter
import streamlit as st

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == "Celsius (°C)":
        if to_unit == "Fahrenheit (°F)":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin (K)":
            return value + 273.15
    
    if from_unit == "Fahrenheit (°F)":
        if to_unit == "Celsius (°C)":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin (K)":
            return (value - 32) * 5/9 + 273.15
    
    if from_unit == "Kelvin (K)":
        if to_unit == "Celsius (°C)":
            return value - 273.15
        elif to_unit == "Fahrenheit (°F)":
            return (value - 273.15) * 9/5 + 32

# Streamlit UI
st.title("🌡️ Temperature Converter")

# User input
temperature = st.number_input("Enter Temperature:", value=0.0, step=0.1)

# Dropdown for unit selection
from_unit = st.selectbox("From:", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])
to_unit = st.selectbox("To:", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

# Convert button
if st.button("Convert"):
    result = convert_temperature(temperature, from_unit, to_unit)
    st.success(f"✅ {temperature} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.write("📌 Built with ❤️ using Streamlit")

   

