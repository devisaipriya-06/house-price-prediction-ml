# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts house prices using Machine Learning techniques.

The project uses the Kaggle House Prices dataset and applies data preprocessing, feature engineering, model training, evaluation, and prediction.

A Streamlit web application is also created to allow users to enter house details and get an estimated house price.

## 🎯 Objective

To build a Machine Learning model that can predict house sale prices based on different property features.

## 📊 Dataset

Dataset: Kaggle House Prices – Advanced Regression Techniques

The dataset contains information about residential properties and their sale prices.

Target variable:

`SalePrice`

## 🔄 Project Workflow

1. Data Collection
2. Data Loading
3. Data Cleaning
4. Handling Missing Values
5. Feature Selection
6. Encoding Categorical Features
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Final Model Training
11. House Price Prediction
12. Streamlit Web Application

## 🤖 Machine Learning Models

The following models were evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The final deployed model in the Streamlit application is the Gradient Boosting model.

## 📈 Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

## 🌐 Streamlit Application

The Streamlit application allows users to enter:

- Overall Quality
- Living Area
- Number of Garage Cars
- Year Built
- Number of Full Bathrooms
- Number of Bedrooms

The trained Machine Learning model then generates an estimated house price.

## 📁 Project Structure

```text
house-price-prediction-ml/
│
├── app.py
├── house_price_model.pkl
├── house_price_predictions.csv
├── requirements.txt
└── README.md
