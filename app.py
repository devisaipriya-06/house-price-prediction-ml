
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the estimated sale price.")

st.divider()

# User inputs
st.subheader("Enter House Details")

overall_qual = st.slider(
    "Overall Quality",
    min_value=1,
    max_value=10,
    value=5
)

gr_liv_area = st.number_input(
    "Living Area (sq ft)",
    min_value=300,
    max_value=6000,
    value=1500
)

garage_cars = st.number_input(
    "Number of Garage Cars",
    min_value=0,
    max_value=5,
    value=2
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2000
)

full_bath = st.number_input(
    "Number of Full Bathrooms",
    min_value=0,
    max_value=5,
    value=2
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=0,
    max_value=10,
    value=3
)

st.divider()

# Prediction button
if st.button("Predict House Price", use_container_width=True):

    # Use the original training structure
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model.named_steps["preprocessor"].feature_names_in_
    )

    # Set user values
    input_data["OverallQual"] = overall_qual
    input_data["GrLivArea"] = gr_liv_area
    input_data["GarageCars"] = garage_cars
    input_data["YearBuilt"] = year_built
    input_data["FullBath"] = full_bath
    input_data["BedroomAbvGr"] = bedrooms

    # Prediction
    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated House Price: ${prediction:,.2f}"
    )

    st.info(
        "This prediction is generated using a machine learning model trained on the House Prices dataset."
    )
