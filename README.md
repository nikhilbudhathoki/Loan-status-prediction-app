# Loan Status Prediction App

This is a web application that predicts the approval status of a bank loan based on user-provided information. It uses a machine learning model for prediction and is built with Flask for the API and Streamlit for the frontend.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nikhilbudhathoki/Loan-status-prediction-app.git

Loan Status Prediction App

This project is a web application for predicting bank loan approval using a machine learning model. It includes a Flask API for backend processing and a Streamlit frontend for user interaction.

Installation:
1. Clone the repository:
   git clone https://github.com/nikhilbudhathoki/Loan-status-prediction-app.git
2. Navigate to the project directory:
   cd Loan-status-prediction-app
3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install dependencies:
   pip install -r requirements.txt

Running the Application:
1. Run Flask API:
   - Navigate to the Flask folder:
     cd path/to/flask_folder
   - View `flask1.py` for the Flask API code.
   - Start the Flask server:
     python flask1.py
   - API accessible at http://127.0.0.1:10000/predict

2. Run Streamlit App:
   - Navigate to the Streamlit folder:
     cd path/to/loan_status_folder
   - View `main.py` for the Streamlit code.
   - Start the Streamlit app:
     streamlit run main.py
   - Access the app at http://localhost:8501

Using the Application:
1. Open the Streamlit app in your browser.
2. Fill out the form with your details.
3. Click "Check Loan Status" to get the prediction.
4. Results will be displayed on the app interface.

API Documentation:
- Endpoint: http://127.0.0.1:10000/predict
- Method: POST
- Payload: JSON object with input data
- Example Request:
  {
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 2000,
    "LoanAmount": 150000,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": "Urban"
  }
- Example Response:
  {
    "prediction": "Approved"
  }

Contributing:
- Contributions are welcome! Submit pull requests or open issues.

License:
- MIT License. See LICENSE for details.
