#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# currency converter
import streamlit as st

# Exchange rates (static for now, can be updated manually or via API)
exchange_rates = {
    "US Dollar (USD)": 0.0036,  # Example: 1 PKR = 0.0036 USD
    "Euro (EUR)": 0.0033,       # Example: 1 PKR = 0.0033 EUR
    "British Pound (GBP)": 0.0028,  # Example: 1 PKR = 0.0028 GBP
    "UAE Dirham (AED)": 0.0132, # Example: 1 PKR = 0.0132 AED
    "Saudi Riyal (SAR)": 0.0135 # Example: 1 PKR = 0.0135 SAR
}

# Streamlit UI
st.title("💰 Currency Converter")

# User input for amount in PKR
amount_pkr = st.number_input("Enter Amount in Pakistani Rupees (PKR):", min_value=1.0, step=1.0)

# Dropdown for currency selection
selected_currency = st.selectbox("Convert to:", list(exchange_rates.keys()))

# Convert button
if st.button("Convert"):
    converted_amount = amount_pkr * exchange_rates[selected_currency]
    st.success(f"✅ {amount_pkr} PKR = {converted_amount:.2f} {selected_currency}")

# Footer
st.markdown("---")
st.write("📌 Built with ❤️ using Streamlit")

