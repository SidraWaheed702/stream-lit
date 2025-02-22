#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Age calculator
import streamlit as st
from datetime import date

# Set page title
st.title("🕰️ Age Calculator")

# Get today's date
today = date.today()

# User input for Date of Birth with a proper range
dob = st.date_input("Select your Date of Birth:", min_value=date(1900, 1, 1), max_value=today)

# Add a button to calculate age
if st.button("Calculate Age"):
    if dob > today:
        st.error("🚨 Date of Birth cannot be in the future!")
    else:
        # Calculate age
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day

        # Adjust for negative values
        if age_days < 0:
            age_months -= 1
            age_days += 30  # Approximate days in a month
        if age_months < 0:
            age_years -= 1
            age_months += 12

        # Display the result
        st.subheader("🎉 Your Age is:")
        st.write(f"📅 **{age_years} years, {age_months} months, and {age_days} days** old.")

# Footer
st.markdown("---")
st.write("📌 Built with ❤️ using Streamlit")

