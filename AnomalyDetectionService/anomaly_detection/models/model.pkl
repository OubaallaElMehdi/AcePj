from sklearn.ensemble import IsolationForest
import numpy as np
import pickle

# Generate synthetic data
data = np.random.rand(1000, 3)  # 1000 samples, 3 features (latitude, longitude, speed)

# Train the Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(data)

# Save the trained model
with open('anomaly_detection/models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
