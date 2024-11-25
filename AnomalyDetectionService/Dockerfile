# Base Image
FROM python:3.9-slim

# Set Working Directory
WORKDIR /app

# Copy Dependencies
COPY ./anomaly_detection/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Application
COPY anomaly_detection ./anomaly_detection
COPY ./anomaly_detection/main.py .

# Expose Port
EXPOSE 5000

# Command to Run the App
CMD ["python", "main.py"]
