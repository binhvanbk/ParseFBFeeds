import requests
import json

# Facebook Graph API endpoint for retrieving news feeds
api_endpoint = "https://graph.facebook.com/v14.0/me/feed"

# Access token obtained from Facebook's developer portal
access_token = "YOUR_ACCESS_TOKEN"

# Parameters for the API request
params = {
    "access_token": access_token,
    "fields": "message,created_time",
    "limit": 10  # Number of news feed items to retrieve
}

# Send GET request to the Graph API
response = requests.get(api_endpoint, params=params)
data = json.loads(response.text)

# Check for errors in the response
if "error" in data:
    error_message = data["error"]["message"]
    print(f"Error: {error_message}")
else:
    # Parse and display the news feed items
    for post in data["data"]:
        message = post.get("message", "")
        created_time = post.get("created_time", "")
        print(f"Message: {message}")
        print(f"Created Time: {created_time}")
        print("---")
