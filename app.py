import pickle
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load trained XGBoost model
with open("xgboost_model_pipeline.pkl", "rb") as file:

    model = pickle.load(file)

# Load dataset to get unique locations
data_path = r"D:\Programming\python\Python AI ML projects\House_Price_Prediction\backend\data\processed\combined_data.csv"
df = pd.read_csv(data_path)
unique_locations = sorted(df["location"].dropna().unique().tolist())

# Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route("/locations", methods=["GET"])
def get_locations():
    """Return list of unique locations"""
    return jsonify({"locations": unique_locations})

@app.route("/predict", methods=["POST"])
def predict_price():
    """Predict house price"""
    data = request.json

    # Extract input values from request
    bhk = int(data["bhk"])
    bath = int(data["bath"])
    sqft = float(data["sqft"])
    location = data["location"]
    status = data["status"]

    # Create a DataFrame for model input
    input_df = pd.DataFrame([{
        "bhk": bhk,
        "bath": bath,
        "sqft": sqft,
        "location": location,
        "status": status
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]

    return jsonify({"predicted_price": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
