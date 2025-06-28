import requests
import json

match_id = "xxxxx"  
url = f"https://site.web.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/summary?event={match_id}"
resp = requests.get(url)
data = resp.json()

# View structure
print("Top-level keys:", data.keys())
print("Has boxscore?", "boxscore" in data)

if "boxscore" in data:
    boxscore = data["boxscore"]
    players_data = boxscore.get("players", [])
    print(f"Teams found: {len(players_data)}")
    
    for team in players_data:
        print("== Team:", team.get("team", {}).get("displayName"))
        for cat in team.get("statistics", []):
            print("Stat category:", cat.get("name"))
            for athlete in cat.get("athletes", []):
                print("-", athlete.get("athlete", {}).get("displayName"))
                print("  Stats:", athlete.get("stats"))
