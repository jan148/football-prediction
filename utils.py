import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

def request_sports_api(path, query):
    url = f"{base_url}/{path}?{query}"
    payload = {}
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


