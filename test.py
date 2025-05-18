import json
import os
import requests
from leagues_seasons_list import league_seasons
from dotenv import load_dotenv, dotenv_values

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

def create_match_ids(league_id, season):
    url = f"{base_url}/fixtures?league={league_id}&season={season}"
    payload = {}
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    # Save it to a file
    with open(f"{league_id}_{season}.json", "w") as f:
        json.dump(data, f, indent=4)

for league_season in league_seasons:
    create_match_ids(league_season[0], league_season[1])