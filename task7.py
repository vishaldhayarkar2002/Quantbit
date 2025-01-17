import requests

def fetch_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"  

    try:
        response = requests.get(url)  # Send a GET request

        if response.status_code == 200:  # Check for successful response
            data = response.json()  # Parse response as JSON
            print(data)  # Display the data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle exceptions

# Fetch and display data from the API
fetch_data_from_api()
