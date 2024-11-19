# Stage 1: Base image
FROM python:3.9-slim as builder
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime image
FROM python:3.9-slim
WORKDIR /app

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Set the entry point
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
