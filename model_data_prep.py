import json
import pickle
import numpy as np
import pandas as pd
from leagues_seasons_list import league_seasons, event_cats
from sklearn.preprocessing import OneHotEncoder

# Ohc event_cats (Ohc = one-hot-encoding)
event_cat_expandend = np.array(event_cats).reshape(len(event_cats), 1)
# One-hot-encoding of event-cats
enc_event_cats = OneHotEncoder(sparse_output=False).fit(event_cat_expandend)

features = []
results = []
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
        end_score_diff = fixtures["response"][i]["goals"]["home"] - fixtures["response"][i]["goals"]["away"]
        results.append([end_score_diff])
        event_array = []
        score_diff = 0
        for j, event in enumerate(events):
            home_away = 1 if home_team == event["team"]["id"] else -1
            minute = event["time"]["elapsed"]
            type = event["type"]
            type_detail = event["detail"]
            type_detail_enc = enc_event_cats.transform([[type_detail]])[0].tolist()
            feature = type_detail_enc
            if type == "Goal":
                score_diff = score_diff + 1 if home_away == 1 else score_diff - 1
            feature.extend([minute, home_away, score_diff])
            event_array.append(feature)
        features.append(event_array)
print(features)
print(results)
with open("Data/Model_input/features.pkl", "wb") as f:
    pickle.dump(features, f)
with open("Data/Model_input/results.pkl", "wb") as f:
    pickle.dump(results, f)