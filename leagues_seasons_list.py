import numpy as np

start = 2021
end = 2023
num_seasons = end - start +1
seasons = np.linspace(start , end, num_seasons, dtype=int)

league_ids = [140] # [39, 78, 135, 186, 140]

league_seasons = []
for league_id in league_ids:
    for season in seasons:
        league_seasons.append([league_id, season])

print(league_seasons)