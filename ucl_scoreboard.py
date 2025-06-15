import requests
import csv

# Champions League matchdays (customize as needed)
ucl_dates = [
    "20240917", "20240918", "20241001", "20241002",  # Group Stage (example dates for next season)
    "20241105", "20241106",
    "20241210", "20241211",
    "20250218", "20250219",  # Knockouts
    "20250225", "20250226",
    "20250311", "20250312",
    "20250408", "20250409",
    "20250429", "20250430",
    "20250531"  # Final
]

# Prepare CSV file
with open("ucl_matches_all.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Date", "Match", "Status", "Home Team", "Home Score",
        "Away Team", "Away Score", "Match Link"
    ])

    for match_date in ucl_dates:
        url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard?dates={match_date}"
        response = requests.get(url)
        data = response.json()

        for event in data.get('events', []):
            name = event['name']
            status = event['status']['type']['description']
            date = event['date']
            competitors = event['competitions'][0]['competitors']
            link = event['links'][0]['href'] if event.get("links") else "N/A"

            teams = {c['homeAway']: c['team']['name'] for c in competitors}
            scores = {c['homeAway']: c.get('score', 'N/A') for c in competitors}

            print(f"{match_date}: {name} - {status}")
            writer.writerow([
                date, name, status,
                teams.get('home'), scores.get('home'),
                teams.get('away'), scores.get('away'),
                link
            ])
