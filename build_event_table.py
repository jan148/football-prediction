import json
import numpy as np
import pandas as pd
from leagues_seasons_list import league_seasons

event_cat_list = []
list = []
for league_season in league_seasons:
    league_id = league_season[0]
    season_id = league_season[1]
    filename_fixtures = f"Data/{league_id}_{season_id}.json"
    filename_events = f"Data/{league_id}_{season_id}_events.json"
    with open(filename_fixtures, "r") as f:
        fixtures = json.load(f)
    with open(filename_events, "r") as f:
        events_matches = json.load(f)
    for i,match_id in enumerate(events_matches):
        events = events_matches[match_id]
        home_team = fixtures["response"][i]["teams"]["home"]["id"]
        away_team = fixtures["response"][i]["teams"]["away"]["id"] # !!! Assumes a 1:1 ordered correspondence between matches and events
        event_array = []
        score_diff = 0
        for j, event in enumerate(events):
            home_away = 1 if home_team == event["team"]["id"] else -1
            minute = event["time"]["elapsed"]
            type = event["type"]
            type_detail = event["detail"]
            if type == "Goal": score_diff = score_diff + 1 if home_away == 1 else score_diff - 1
            event_cat_list.append(type)
            event_array.append([type, minute, home_away, score_diff])
        list.append(event_array)
event_cats = np.unique(np.array(event_cat_list))
print(np.array(event_cats))
print(list)