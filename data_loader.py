import http.client
import json
import ssl
import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
type = "leagues"

url = f"{base_url}/{type}"
payload = {}
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

# Save it to a file
with open(f"{type}.json", "w") as f:
    json.dump(data, f, indent=4)

print(json.dumps(response.json(), indent=4))

