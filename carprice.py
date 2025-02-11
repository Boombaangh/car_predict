import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
model_filename = "price_model.pkl"
with open(model_filename, "rb") as file:
    model_pipeline = pickle.load(file)


# Streamlit UI
def main():
    st.title("Car Price Prediction")
    st.write("Enter Price.")
    
    # User Inputs
    brand = st.selectbox("Select the Brands", ['Honda', 'BMW', 'Toyota', 'Audi', 'Others'])
    model_year = st.number_input("Model Year", min_value=1990, max_value=2024, value=2015)
    milage = st.number_input("Mileage (in miles)", min_value=0, value=50000)
    fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
    transmission = st.selectbox("Transmission Type", ['Automatic', 'Manual'])
    ext_col = st.selectbox("Exterior Color", ['Black', 'White', 'Red', 'Other'])
    accident = st.radio("Any Accidents?", ['Yes', 'No'])
    clean_title = st.radio("Clean Carfax", ['Yes', 'No'])
    
    # Convert inputs to DataFrame
    input_data = pd.DataFrame({
        'brand': [brand],
        'model_year': [model_year],
        'milage': [milage],
        'fuel_type': [fuel_type],
        'transmission': [transmission],
        'ext_col': [ext_col],
        'accident': [accident],
        'clean_title': [clean_title]
    })
    
    # Predict button
    if st.button("Predict Price"):
        predicted_price = model_pipeline.predict(input_data)[0]
        st.success(f"Estimated Price: ${predicted_price:,.2f}")

if __name__ == "__main__":
    main()
