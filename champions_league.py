import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_TOKEN = os.getenv("FOOTBALL_DATA_API_KEY")

# API Configuration
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_TOKEN}

def get_current_season():
    """Fetch current Champions League season"""
    response = requests.get(f"{BASE_URL}/competitions/CL", headers=HEADERS)
    return response.json()["currentSeason"]

def get_all_matches(season_id):
    """Get all matches for the season"""
    url = f"{BASE_URL}/competitions/CL/matches?season={season_id}"
    response = requests.get(url, headers=HEADERS)
    return response.json()["matches"]

def save_to_csv(matches, filename="cl_matches.csv"):
    """Save match data to CSV"""
    df = pd.DataFrame([{
        "date": match["utcDate"],
        "home_team": match["homeTeam"]["name"],
        "away_team": match["awayTeam"]["name"],
        "score": f"{match['score']['fullTime']['home']}-{match['score']['fullTime']['away']}" if match['score']['fullTime'] else "TBD",
        "stage": match["stage"],
        "status": match["status"]
    } for match in matches])
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    print("⚽ Fetching Champions League 2024/2025 Data...")
    season = get_current_season()
    print(f"📅 Season: {season['startDate']} to {season['endDate']}")
    
    matches = get_all_matches(season["id"])
    print(f"🔢 Found {len(matches)} matches.")
    
    save_to_csv(matches)