import requests
import random
import datetime

# Vehicle Service URL
VEHICLE_SERVICE_URL = "http://localhost:8081/vehicles"
TRAJECTORY_API_URL = "http://localhost:8081/api/trajectories"

# Function to fetch vehicles from Vehicle Service
def fetch_vehicles():
    response = requests.get(f"{VEHICLE_SERVICE_URL}/vehicles")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch vehicles.")
        return []

# Function to generate a trajectory for a vehicle
def generate_trajectory(vehicle_id):
    # Example start and end points (New York coordinates)
    start = [40.7128, -74.0060]
    end = [40.7306, -73.9352]
    steps = 10

    trajectory = []
    timestamp = datetime.datetime.now()

    for step in range(steps):
        lat = start[0] + (step / steps) * (end[0] - start[0])
        lon = start[1] + (step / steps) * (end[1] - start[1])
        speed = random.uniform(20, 80)  # Random speed in km/h
        heading = random.randint(0, 360)  # Random heading

        trajectory.append({
            "vehicle": {"id": vehicle_id},
            "latitude": lat,
            "longitude": lon,
            "speed": speed,
            "heading": heading,
            "timestamp": (timestamp + datetime.timedelta(seconds=step * 10)).isoformat()
        })

    return trajectory

# Function to post trajectories to the Vehicle Service
def post_trajectories(trajectory):
    for point in trajectory:
        response = requests.post(f"{TRAJECTORY_API_URL}", json=point)
        if response.status_code != 200:
            print(f"Failed to post trajectory point: {point}")
        else:
            print(f"Posted trajectory point: {point}")

# Main function to simulate and post trajectories
def simulate_and_post_trajectories():
    vehicles = fetch_vehicles()
    if not vehicles:
        print("No vehicles found.")
        return

    for vehicle in vehicles:
        print(f"Generating trajectory for vehicle ID: {vehicle['id']}")
        trajectory = generate_trajectory(vehicle['id'])
        post_trajectories(trajectory)
