# 🏠 House Price Prediction API

## Overview
This project is a machine learning-powered REST API developed for ABZ Company, a leading real estate software firm in Kigali, Rwanda. The API predicts house rental prices based on various features such as size, location, and amenities, helping ensure fair and accurate property pricing in the market.

## 🌟 Key Features
- Real-time house price predictions
- Support for multiple property features
- RESTful API design
- Built-in input validation
- Error handling and monitoring
- Fast response times
- Easy deployment on Render

## 🛠️ Technology Stack
- **Backend Framework:** Flask
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Storage:** Joblib
- **Deployment:** Render
- **Server:** Gunicorn

## 📊 Model Details
- **Algorithm:** Random Forest Regressor
- **Features Used:**
  - BHK (Bedrooms, Hall, Kitchen)
  - Size (Square feet)
  - Floor Information
  - Area Type
  - City
  - Furnishing Status
  - Bathroom Count

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
Virtual environment (recommended)
```

### Installation
```bash
# Clone repository
git clone https://github.com/codeWithEdison/house-price-prediction-model.git
cd house-price-prediction-model

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
python app.py
```

## 📡 API Endpoints

### Health Check
```http
GET /health
```

### Price Prediction
```http
POST /predict
```

#### Request Body Example
```json
{
    "BHK": 2,
    "Size": 1000,
    "Current Floor": 2,
    "Total Floors": 4,
    "Area Type": "Super Area",
    "City": "Mumbai",
    "Furnishing Status": "Furnished",
    "Bathroom": 2
}
```

#### Response Example
```json
{
    "predicted_price": 25000.00,
    "input_received": {...},
    "status": "success"
}
```

## 🔍 Model Training

Train your own model using:
```bash
python train_model.py
```

## 🚀 Deployment

### Deploy to Render
1. Fork this repository
2. Connect to Render
3. Configure build settings:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```

## 📈 Performance Metrics
- Training Score: XX%
- Testing Score: XX%
- Average Response Time: <100ms

## 🛡️ Error Handling
The API includes comprehensive error handling for:
- Invalid input values
- Missing parameters
- Server errors
- Model prediction errors

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Future Improvements
- [ ] Add user authentication
- [ ] Implement caching
- [ ] Add more property features
- [ ] Improve model accuracy
- [ ] Add batch prediction support

## 👥 Authors
- Your Name - Initial work - [GitHub Profile](https://github.com/codewithedison)

## 📞 Support
For support:
- Open an issue
- Contact: your.email@example.com

---
⭐ Star this repository if you find it helpful!

[View Demo](your-deployed-api-url) | [Report Bug](issues-url) | [Request Feature](issues-url)

This project was created as part of the ABZ Company's initiative to improve property pricing accuracy in the Rwandan real estate market.