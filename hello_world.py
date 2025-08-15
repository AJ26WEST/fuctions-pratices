# Flask Backend for Weather Prediction API
# This connects your Python ML model with the web frontend

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import os
import json

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Global variables for model and scaler
model = None
scaler = None
feature_names = ['Temperature', 'Humidity', 'Pressure', 'Wind_Speed', 'Cloud_Cover']

# Your original weather data generation function
def create_sample_weather_data(n_samples=1000):
    """Create realistic sample weather data for training"""
    np.random.seed(42)
    
    data = []
    for i in range(n_samples):
        temperature = np.random.normal(22, 8)
        humidity = np.random.uniform(30, 95)
        pressure = np.random.normal(1013, 20)
        wind_speed = np.random.exponential(8)
        cloud_cover = np.random.uniform(0, 100)
        
        # Create realistic rain probability
        rain_probability = 0
        
        if humidity > 70: rain_probability += 0.3
        if humidity > 85: rain_probability += 0.3
        if pressure < 1010: rain_probability += 0.2
        if pressure < 1000: rain_probability += 0.3
        if cloud_cover > 70: rain_probability += 0.2
        if cloud_cover > 90: rain_probability += 0.2
        if 15 < temperature < 30: rain_probability += 0.1
        
        rain_probability += np.random.uniform(-0.2, 0.2)
        will_rain = 1 if rain_probability > 0.5 else 0
        
        data.append({
            'Temperature': round(temperature, 1),
            'Humidity': round(humidity, 1),
            'Pressure': round(pressure, 1),
            'Wind_Speed': round(wind_speed, 1),
            'Cloud_Cover': round(cloud_cover, 1),
            'Rain_Tomorrow': will_rain
        })
    
    return pd.DataFrame(data)

def train_model():
    """Train the weather prediction model"""
    global model, scaler
    
    print("🤖 Training weather prediction model...")
    
    # Create sample data
    df = create_sample_weather_data(1000)
    
    # Prepare features and target
    X = df[feature_names]
    y = df['Rain_Tomorrow']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        max_depth=10
    )
    model.fit(X_train, y_train)
    
    # Calculate accuracy
    accuracy = model.score(X_test, y_test)
    print(f"✅ Model trained with accuracy: {accuracy:.2%}")
    
    return accuracy

def save_model():
    """Save the trained model and scaler"""
    if model and scaler:
        with open('weather_model.pkl', 'wb') as f:
            pickle.dump({'model': model, 'scaler': scaler}, f)
        print("💾 Model saved successfully!")

def load_model():
    """Load previously trained model"""
    global model, scaler
    try:
        with open('weather_model.pkl', 'rb') as f:
            data = pickle.load(f)
            model = data['model']
            scaler = data['scaler']
        print("📁 Model loaded successfully!")
        return True
    except FileNotFoundError:
        print("❌ No saved model found. Training new model...")
        return False

# Initialize model on startup
if not load_model():
    train_model()
    save_model()

# API Routes
@app.route('/')
def home():
    """Serve the main web page"""
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌦️ Weather Prediction API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
            text-align: center;
            padding: 50px;
            margin: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        h1 { font-size: 3em; margin-bottom: 20px; }
        .api-info {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: left;
        }
        code {
            background: rgba(0,0,0,0.3);
            padding: 2px 6px;
            border-radius: 4px;
        }
        .endpoint {
            margin: 15px 0;
            font-size: 1.1em;
        }
        a {
            color: #fdcb6e;
            text-decoration: none;
        }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌦️ Weather Prediction API</h1>
        <p>Your Python ML model is running and ready to predict rain!</p>
        
        <div class="api-info">
            <h3>📡 API Endpoints:</h3>
            <div class="endpoint">
                <strong>POST /predict</strong> - Predict rain based on weather data
            </div>
            <div class="endpoint">
                <strong>GET /model-info</strong> - Get model information
            </div>
            <div class="endpoint">
                <strong>GET /retrain</strong> - Retrain the model with new data
            </div>
        </div>
        
        <div class="api-info">
            <h3>📊 Usage Example:</h3>
            <code>
                POST /predict<br>
                {<br>
                &nbsp;&nbsp;"temperature": 25.5,<br>
                &nbsp;&nbsp;"humidity": 78,<br>
                &nbsp;&nbsp;"pressure": 1008,<br>
                &nbsp;&nbsp;"wind_speed": 15.2,<br>
                &nbsp;&nbsp;"cloud_cover": 85<br>
                }
            </code>
        </div>
        
        <p><a href="/web-app" target="_blank">🌐 Open Full Web App</a></p>
    </div>
</body>
</html>
    """)

@app.route('/predict', methods=['POST'])
def predict_rain():
    """API endpoint to predict rain"""
    try:
        # Get JSON data from request
        data = request.json
        
        # Extract weather parameters
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        pressure = float(data['pressure'])
        wind_speed = float(data['wind_speed'])
        cloud_cover = float(data['cloud_cover'])
        
        # Validate input ranges
        if not (0 <= humidity <= 100):
            return jsonify({'error': 'Humidity must be between 0-100%'}), 400
        if not (0 <= cloud_cover <= 100):
            return jsonify({'error': 'Cloud cover must be between 0-100%'}), 400
        if wind_speed < 0:
            return jsonify({'error': 'Wind speed cannot be negative'}), 400
        
        # Prepare input for model
        input_data = np.array([[temperature, humidity, pressure, wind_speed, cloud_cover]])
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]
        
        # Get feature importance
        feature_importance = dict(zip(feature_names, model.feature_importances_))
        
        # Prepare response
        response = {
            'prediction': {
                'will_rain': bool(prediction),
                'rain_probability': float(probability[1]),
                'no_rain_probability': float(probability[0])
            },
            'input_data': {
                'temperature': temperature,
                'humidity': humidity,
                'pressure': pressure,
                'wind_speed': wind_speed,
                'cloud_cover': cloud_cover
            },
            'model_info': {
                'feature_importance': feature_importance,
                'confidence': float(max(probability))
            },
            'status': 'success'
        }
        
        return jsonify(response)
        
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}', 'status': 'error'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid data type: {str(e)}', 'status': 'error'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}', 'status': 'error'}), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    """Get information about the trained model"""
    if model is None:
        return jsonify({'error': 'Model not trained'}), 500
    
    # Get feature importance
    feature_importance = dict(zip(feature_names, model.feature_importances_))
    
    info = {
        'model_type': 'RandomForestClassifier',
        'features': feature_names,
        'feature_importance': feature_importance,
        'n_estimators': model.n_estimators,
        'max_depth': model.max_depth,
        'status': 'ready'
    }
    
    return jsonify(info)

@app.route('/retrain', methods=['GET'])
def retrain_model():
    """Retrain the model with new data"""
    try:
        accuracy = train_model()
        save_model()
        return jsonify({
            'message': 'Model retrained successfully',
            'accuracy': accuracy,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': f'Retraining failed: {str(e)}', 'status': 'error'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'scaler_loaded': scaler is not None
    })

# Serve the updated web app that connects to this API
@app.route('/web-app')
def web_app():
    """Serve the complete web application"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Predictor AI</title>
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #74b9ff, #0984e3); color: white; text-align: center; padding: 50px; }
        .container { max-width: 600px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; }
        input { width: 100%; padding: 15px; margin: 10px 0; border: none; border-radius: 8px; font-size: 1.1em; }
        button { width: 100%; padding: 18px; background: #00b894; color: white; border: none; border-radius: 8px; font-size: 1.3em; cursor: pointer; margin-top: 20px; }
        button:hover { background: #00a085; }
        .result { margin-top: 30px; padding: 20px; border-radius: 10px; font-size: 1.5em; }
        .rain { background: rgba(253, 121, 168, 0.3); }
        .no-rain { background: rgba(253, 203, 110, 0.3); }
    </style>
</head>
<body>
    <div class="container">
        <h1>Weather Predictor AI</h1>
        <p>Powered by AJ 26WEST PRED</p>
        
        <input type="number" id="temperature" placeholder="Temperature (°C)" step="0.1">
        <input type="number" id="humidity" placeholder="Humidity (%)" min="0" max="100">
        <input type="number" id="pressure" placeholder="Pressure (hPa)" step="0.1">
        <input type="number" id="windSpeed" placeholder="Wind Speed (km/h)" step="0.1" min="0">
        <input type="number" id="cloudCover" placeholder="Cloud Cover (%)" min="0" max="100">
        
        <button onclick="predictRain()">Predict Rain Tomorrow</button>
        
        <div id="result" style="display: none;"></div>
    </div>

    <script>
        async function predictRain() {
            const data = {
                temperature: parseFloat(document.getElementById('temperature').value),
                humidity: parseFloat(document.getElementById('humidity').value),
                pressure: parseFloat(document.getElementById('pressure').value),
                wind_speed: parseFloat(document.getElementById('windSpeed').value),
                cloud_cover: parseFloat(document.getElementById('cloudCover').value)
            };

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                const resultDiv = document.getElementById('result');

                if (result.status === 'success') {
                    const willRain = result.prediction.will_rain;
                    const confidence = (result.prediction.rain_probability * 100).toFixed(1);
                    
                    resultDiv.className = 'result ' + (willRain ? 'rain' : 'no-rain');
                    resultDiv.innerHTML = willRain 
                        ? `It WILL RAIN tomorrow! (${confidence}% confidence)`
                        : `It will NOT rain tomorrow! (${(100-confidence).toFixed(1)}% confidence)`;
                } else {
                    resultDiv.className = 'result';
                    resultDiv.innerHTML = `Error: ${result.error}`;
                }
                
                resultDiv.style.display = 'block';
            } catch (error) {
                document.getElementById('result').innerHTML = `Connection Error: ${error.message}`;
                document.getElementById('result').style.display = 'block';
            }
        }
    </script>
</body>
</html>
    """

if __name__ == '__main__':
    print("🌦️ Weather Prediction API Starting...")
    print("📡 API will be available at: http://localhost:5000")
    print("🌐 Web App will be available at: http://localhost:5000/web-app")
    print("📚 API Documentation: http://localhost:5000")
    
    # Alternative way to run Flask (VS Code friendly)
    import os
    os.environ['FLASK_APP'] = 'hello_world.py'
    os.environ['FLASK_ENV'] = 'development'
    
    try:
        app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)
    except Exception as e:
        print(f"Error starting server: {e}")
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")