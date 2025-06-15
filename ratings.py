import requests
import csv
import time

# Define the date range when Champions League games were played
dates = ["20240501", "20240515", "20240531"]  # You can add more if needed

match_ids = []

# Step 1: Collect match IDs from multiple dates
for date in dates:
    url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard?dates={date}"
    resp = requests.get(url)
    data = resp.json()
    for event in data.get("events", []):
        match_ids.append(event["id"])

print(f"✅ Found {len(match_ids)} total matches")

ratings = []

# Step 2: For each match, get player ratings
for match_id in match_ids:
    url = f"https://site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/summary?event={match_id}"
    r = requests.get(url)
    data = r.json()

    boxscore = data.get("boxscore", {})
    players_data = boxscore.get("players", [])

    if not players_data:
        print(f"⚠️ No boxscore data for match {match_id}")
        continue

    for team in players_data:
        team_name = team.get("team", {}).get("displayName")
        for category in team.get("statistics", []):
            for athlete in category.get("athletes", []):
                player = athlete.get("athlete", {})
                stats = athlete.get("stats", [])
                rating = None
                for stat in stats:
                    if "Rating" in stat:
                        try:
                            rating = float(stat.split(":")[-1].strip())
                        except:
                            continue
                if rating is not None:
                    ratings.append({
                        "match_id": match_id,
                        "player_id": player.get("id"),
                        "player_name": player.get("displayName"),
                        "team_name": team_name,
                        "rating": rating
                    })

    time.sleep(1)  # Be nice to ESPN's servers

# Step 3: Save to CSV
if ratings:
    with open("ucl_player_ratings.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["match_id", "player_id", "player_name", "team_name", "rating"])
        writer.writeheader()
        writer.writerows(ratings)
    print("✅ Player ratings saved to ucl_player_ratings.csv")
else:
    print("❌ No valid player ratings found.")
