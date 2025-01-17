import json

# Read and parse the JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Print keys and their corresponding values
for key, value in data.items():
    print(f"{key}: {value}")
