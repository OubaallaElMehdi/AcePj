import pickle
import numpy as np

class AnomalyDetector:
    def __init__(self, model_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, data):
        """
        Predict anomalies in the given data.
        :param data: Numpy array of preprocessed data.
        :return: List of anomaly predictions (1 = anomaly, -1 = normal).
        """
        if not isinstance(data, np.ndarray):
            raise ValueError("Data must be a numpy array.")

        return self.model.predict(data)
