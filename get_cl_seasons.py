import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_TOKEN = os.getenv("FOOTBALL_DATA_API_KEY")

BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_TOKEN}

def get_all_matches(season_year):
    url = f"{BASE_URL}/competitions/CL/matches?season={season_year}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    if "matches" not in data:
        print(f"⚠️ No matches found for season {season_year}")
        print("API response:", data)
        return []

    return data["matches"]

def save_to_csv(matches, filename):
    df = pd.DataFrame([{
        "utc_date": match["utcDate"],
        "home_team": match["homeTeam"]["name"],
        "away_team": match["awayTeam"]["name"],
        "home_score": match["score"]["fullTime"]["home"],
        "away_score": match["score"]["fullTime"]["away"],
        "status": match["status"],
        "stage": match["stage"]
    } for match in matches])
    df.to_csv(filename, index=False)
    print(f"✅ {len(df)} matches saved to {filename}")

if __name__ == "__main__":
    print("📥 Fetching 2024/2025 Champions League matches...")
    matches = get_all_matches(2024)

    if matches:
        save_to_csv(matches, "champions_league_2024_2025.csv")
