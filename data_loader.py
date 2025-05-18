import http.client
import json
import ssl
import requests
import os
from utils import request_sports_api
from dotenv import load_dotenv, dotenv_values

type = "leagues"
response = request_sports_api(type, "")
data = response.json()
# Save it to a file
with open(f"{type}.json", "w") as f:
    json.dump(data, f, indent=4)

