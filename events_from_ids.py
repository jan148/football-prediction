import json
import requests

with open("config.json") as f:
    api_key = json.load(f)["api_key"]

with open("ids.json") as ids:
    data = json.load(ids)

print(data)

arr = []
for i in range(len(data["ids"])):
    id = data["ids"][i]
    if id == 1331226:
        url = f"https://v3.football.api-sports.io/fixtures/events?fixture={id}"
        payload = {}
        headers = {
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.json()
        print(response_json)
        arr.append(response_json["response"])

print(arr)