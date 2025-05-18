import json
from leagues_seasons_list import league_seasons
from utils import request_sports_api

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
            data = request_sports_api("fixtures/events", f"fixture={id}").json()
            event = data["response"]
            events[f"{id}"] = event
            counter = counter + 1
    with open(f"{league_id}_{season_id}_events.json", "w") as f:
        json.dump(events, f, indent=4)