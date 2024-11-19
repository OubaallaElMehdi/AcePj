from flask import Flask, request, jsonify
from anomaly_detection.utils.data_processing import preprocess_data
from anomaly_detection.utils.anomaly_detection import AnomalyDetector

app = Flask(__name__)

# Load the pre-trained Isolation Forest model
detector = AnomalyDetector('anomaly_detection/models/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to predict anomalies.
    Expects JSON payload with trajectory data.
    """
    try:
        data = request.get_json()
        processed_data = preprocess_data(data)
        predictions = detector.predict(processed_data)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
