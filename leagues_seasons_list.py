import numpy as np
import json

start = 2021
end = 2021
num_seasons = end - start + 1
seasons = np.linspace(start , end, num_seasons, dtype=int)

league_ids = [39] # [39, 78, 135, 186, 140]

league_seasons = []
for league_id in league_ids:
    for season in seasons:
        league_seasons.append([league_id, season])

# Get all event categories
event_cats = []
for league_season in league_seasons:
    league = league_season[0]
    season = league_season[1]
    with open(f"Data/{league}_{season}_events.json", "r") as f:
        data = json.load(f)
    for events in data:
        for event in data[events]:
            event_cats.append(event["detail"])

# with open("Data/detailed_event_cats.json", "w") as f:
#     json.dump(list(np.unique(np.array(event_cats))), f, indent=4)