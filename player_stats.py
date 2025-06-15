import requests
import csv
import os

# API endpoint
url = "https://site.web.api.espn.com/apis/site/v2/sports/soccer/UEFA.CHAMPIONS/statistics"
params = {
    "region": "us",
    "lang": "en",
    "contentorigin": "espn"
}

# Fetch data
response = requests.get(url, params=params)
data = response.json()

# Get list of categories
stats = data['stats']

# Create output directory
output_dir = "ucl_player_stats"
os.makedirs(output_dir, exist_ok=True)

# Process each category separately
for category in stats:
    stat_name = category['name'].lower().replace(" ", "_")
    filename = f"{output_dir}/{stat_name}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["player_id", "player_name", "team_name", "value"])

        for entry in category.get("athletes", []):
            athlete = entry["athlete"]
            player_id = athlete["id"]
            player_name = athlete["displayName"]
            team_name = entry["team"]["displayName"]
            value = entry["value"]

            writer.writerow([player_id, player_name, team_name, value])
