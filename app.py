# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)
# Load saved model and encoders

try:
    model = joblib.load('house_price_model.joblib')
    label_encoders = joblib.load('label_encoders.joblib')
    features = joblib.load('features.joblib')
    print("Model and encoders loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'API is running',
        'message': 'Welcome to House Price Prediction API'
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'})

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        # Get data from request
        data = request.get_json()
        
        # Create DataFrame with the same structure as training data
        input_data = pd.DataFrame({
            'BHK': [data['BHK']],
            'Size': [data['Size']],
            'Current Floor': [data['Current Floor']],
            'Total Floors': [data['Total Floors']],
            'Area Type': [data['Area Type']],
            'City': [data['City']],
            'Furnishing Status': [data['Furnishing Status']],
            'Bathroom': [data['Bathroom']]
        })
        
        # Encode categorical variables
        categorical_columns = ['Area Type', 'City', 'Furnishing Status']
        for column in categorical_columns:
            if column in input_data.columns:
                input_data[column] = label_encoders[column].transform(input_data[column])
        
        # Make prediction
        predicted_price = model.predict(input_data)[0]
        
        return jsonify({
            'predicted_price': float(predicted_price),
            'input_received': data,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)