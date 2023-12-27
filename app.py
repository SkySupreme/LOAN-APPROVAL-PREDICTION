from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load your loan prediction model and data here
# For the sake of example, we'll use a simple RandomForestClassifier
interest_rates = pd.read_csv("C:/html/python/interest_rates.csv")
# Assume 'Loan_Status' is the target variable
data = pd.read_csv("C:/html/python/LoanApprovalPrediction.csv")
X = data.drop('Loan_Status', axis=1)
y = data['Loan_Status']
# Split the data into training and testing sets

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_term = float(request.form['loan_term'])
        credit_history = float(request.form['credit_history'])
        loan_type = request.form['loan_type']

        # Retrieve the interest rate based on the selected loan type
        interest_rate = interest_rates.get(loan_type, 0)  # Default to 0 if loan type not found

        # Create a DataFrame with the input values
        input_data = pd.DataFrame({
            'ApplicantIncome': [applicant_income],
            'CoapplicantIncome': [coapplicant_income],
            'LoanAmount': [loan_amount],
            'Loan_Amount_Term': [loan_term],
            'Credit_History': [credit_history],
            'Interest_Rate': [interest_rate]
        })
        return {
            'ApplicantIncome': [applicant_income],
            'CoapplicantIncome': [coapplicant_income],
            'LoanAmount': [loan_amount],
            'Loan_Amount_Term': [loan_term],
            'Credit_History': [credit_history],
            'Interest_Rate': [interest_rate]
        }
        # Make a prediction using the model
       # prediction = model.predict(input_data)

       # return render_template('index.html', prediction=prediction[0], loan_types=list(interest_rates.keys()), interest_rate=interest_rate)

if __name__ == '__main__':
    app.run(debug=True)
