import json
import requests
from leagues_seasons_list import league_seasons
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
type = "fixtures"

counter = 0
for league_season in league_seasons:
    league_id = league_season[0]
    season_id = league_season[1]
    filename = f"{league_id}_{season_id}.json"
    with open(filename, "r") as f:
        matches = json.load(f)
    ids = []
    events = {}
    for fixture in matches["response"]:
        ids.append(fixture["fixture"]["id"])
    for id in ids:
        if counter < 10:
            url = f"{base_url}/fixtures/events?fixture={id}"
            payload = {}
            headers = {
                'x-rapidapi-key': api_key,
                'x-rapidapi-host': 'v3.football.api-sports.io'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()
            event = data["response"]
            events[f"{id}"] = event
            counter = counter + 1
    with open(f"{league_id}_{season_id}_events.json", "w") as f:
        json.dump(events, f, indent=4)