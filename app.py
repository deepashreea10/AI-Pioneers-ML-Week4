
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("house_price_model.joblib")
scaler = joblib.load("house_price_scaler.joblib")

# Feature order used during training
feature_names = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude"
]

@app.route("/")
def home():
    return jsonify({
        "message": "House Price Prediction API is running"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = [data[feature] for feature in feature_names]

        input_data = np.array(features).reshape(1, -1)

        # Apply the same preprocessing used during training
        input_scaled = scaler.transform(input_data)

        # Generate prediction
        prediction = model.predict(input_scaled)[0]

        return jsonify({
            "predicted_house_value": round(float(prediction), 4)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run()
