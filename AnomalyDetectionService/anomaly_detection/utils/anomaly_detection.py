import requests
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

VEHICLE_SERVICE_URL = "http://localhost:8081/api/trajectories/vehicle"

# Fetch trajectory data for a vehicle
def fetch_trajectory_data(vehicle_id):
    response = requests.get(f"{VEHICLE_SERVICE_URL}/{vehicle_id}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch trajectory data for vehicle ID: {vehicle_id}")
        return []

# Train the anomaly detection model
def train_anomaly_model(data):
    # Prepare the data
    df = pd.DataFrame(data)
    features = ['latitude', 'longitude', 'speed', 'heading']
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])

    # Train Isolation Forest
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(scaled_data)

    # Save the model
    joblib.dump(model, "anomaly_detection/models/model.pkl")
    print("Model trained and saved.")

# Detect anomalies
def detect_anomalies(vehicle_id):
    # Fetch data
    data = fetch_trajectory_data(vehicle_id)
    if not data:
        return

    df = pd.DataFrame(data)
    features = ['latitude', 'longitude', 'speed', 'heading']
    model = joblib.load("anomaly_detection/models/model.pkl")

    # Predict anomalies
    predictions = model.predict(df[features])
    df['anomaly'] = predictions
    print(df[df['anomaly'] == -1])  # Print anomalies
