import requests
import csv
import os

# API endpoint and params
url = "https://site.web.api.espn.com/apis/site/v2/sports/soccer/UEFA.CHAMPIONS/statistics"
params = {
    "region": "us",
    "lang": "en",
    "contentorigin": "espn"
}

# Fetch data
response = requests.get(url, params=params)
data = response.json()

# Get all stat categories
stats = data.get("stats", [])

# Define output path relative to this script's parent directory
output_dir = os.path.join("..", "data", "ucl_player_stats")
os.makedirs(output_dir, exist_ok=True)

# Loop through each stat category and save to CSV
for category in stats:
    stat_name = category['name'].lower().replace(" ", "_")
    filename = os.path.join(output_dir, f"{stat_name}.csv")

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["player_id", "player_name", "team_name", "value"])

        for entry in category.get("athletes", []):
            athlete = entry["athlete"]
            player_id = athlete.get("id")
            player_name = athlete.get("displayName")
            team_name = entry.get("team", {}).get("displayName", "")
            value = entry.get("value")

            writer.writerow([player_id, player_name, team_name, value])

print(f"✅ Saved {len(stats)} stat categories to {output_dir}")
