# Stage 1: Use a lightweight Python base image
FROM python:3.10-slim as builder
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Run the Flask application
CMD ["python", "anomaly_detection/main.py"]
