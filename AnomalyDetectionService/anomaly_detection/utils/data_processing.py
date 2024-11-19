import pandas as pd
import numpy as np

def preprocess_data(data):
    """
    Preprocess incoming data for anomaly detection.
    :param data: List of dictionaries containing latitude, longitude, and speed.
    :return: Processed numpy array
    """
    df = pd.DataFrame(data)
    if 'latitude' not in df or 'longitude' not in df or 'speed' not in df:
        raise ValueError("Missing required fields: latitude, longitude, or speed.")
    
    # Normalize speed to avoid skewed results
    df['speed'] = df['speed'] / df['speed'].max()
    
    # Combine latitude, longitude, and speed as features
    return df[['latitude', 'longitude', 'speed']].to_numpy()
