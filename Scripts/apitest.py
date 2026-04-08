import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Print response JSON
print("Response Data:", response.json())