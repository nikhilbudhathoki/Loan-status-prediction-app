from flask import Flask, request, jsonify#The core Flask class used to create the application.
#request used to http request ,jsonify for json response
import numpy as np
import pickle#it is used as load of  predefine ml model
import os#for environment variable




app = Flask(__name__)#creates a flask app instant
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY', 'default_secret_key')#ets the Flask app's secret key for sessions and security. It reads the key from the environment variable

# Load the model
model_path = 'train_model.sav'
if os.path.exists(model_path):
    with open(model_path, 'rb') as file:#if model existed on the path load it 
        loaded_model = pickle.load(file)
else:
    raise FileNotFoundError(f"Model file not found: {model_path}")#else raise errors



@app.route('/predict', methods=['POST'])# Defines an endpoint /predict that accepts POST requests
def predict():
    try:#using exception 
        # Get data from the request
        data = request.json.get('input_data', [])#receives input data from json
        print(f"Received data: {data}")  # Debug print

        if not data or len(data) < 7:
            return jsonify({'error': 'Invalid input data. At least 7 elements are required.'}), 400



        # Process the data
        # Combine ApplicantIncome and CoapplicantIncome
        if len(data) >= 7:
            data.append(data[5] + data[6])  # Add combined income
            data.pop(5)  # Remove ApplicantIncome
            data.pop(5)  # Remove CoapplicantIncome
        
        # Convert list to numpy array and reshape for prediction
        input_data = np.asarray(data).reshape(1, -1)
        print(f"Processed data: {input_data}")  # Debug print
        
        
        # Make prediction
        result = loaded_model.predict(input_data)
        print(f"Model prediction: {result}")  # Debug print
        
        
        
        # Interpret the result
        status = "✅ Loan Accepted" if result[0] == 1 else "❌ Loan Not Accepted"
        
        return jsonify({'status': status})#gives the status in a json way 
    except Exception as e:
        print(f"Exception: {e}")  # Debug print
        return jsonify({'error': str(e)}), 400#print for error



if __name__ == '__main__':#Ensures this block runs only if the script is executed directly (not imported as a module).
    app.run(host='0.0.0.0', port=10000, debug=True)#enabling debug mode provide error messages if nay
