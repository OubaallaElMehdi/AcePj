from flask import Flask, jsonify, request
from anomaly_detection.utils.data_generation import simulate_and_post_trajectories
from anomaly_detection.utils.anomaly_detection import detect_anomalies


app = Flask(__name__)

# Simulate and post trajectories
@app.route("/simulate", methods=["POST"])
def simulate():
    simulate_and_post_trajectories()
    return jsonify({"message": "Trajectories simulated and posted."})

# Detect anomalies for a specific vehicle
@app.route("/anomalies/<int:vehicle_id>", methods=["GET"])
def anomalies(vehicle_id):
    detect_anomalies(vehicle_id)
    return jsonify({"message": "Anomalies detected. Check logs for details."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
