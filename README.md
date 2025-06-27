# 🏆 UEFA Champions League 2024/2025 Stats Extractor

This project extracts and processes **UEFA Champions League 2024/2025** season data using ESPN's internal API. It focuses on generating clean, structured datasets for analysis, research, or dashboarding.

> 📌 **Important:** All data captured is limited to the **2024/2025 Champions League season** only.

---

## 📊 Features

- ✅ Player statistics:
  - 🥅 **Top Goal Scorers**
  - 🎯 **Top Assist Providers**
- 🗓️ Match-by-match results:
  - Full-time scores
  - Competing teams and match dates
- 📁 Structured export to CSV files for easy analysis

---

## 🔧 Setup Instructions

```bash
# Clone the repository
git clone git@github.com:Odurophilip/ucl-champs-league-stats.git
cd ucl-champs-league-stats

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# .\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

🚀 How to Run
Run the main script to fetch and save data:

bash
python main.py
If you're running separate modules (like ratings or assists), you can do:

bash
python assists.py
python goals.py
python ratings.py

📁 Output Files
All CSVs are saved in the project root:

Filename	Description
match_results.csv	Match results (teams, date, scores)
goalsLeaders.csv	Top goal scorers
assistsLeaders.csv	Top assist providers
ucl_player_ratings.csv	Player ratings (where available)

Each player is assigned a unique identifier to enable easy merging across tables
```
> 📌 Notes
Data source: ESPN UEFA Champions League

Only includes matches and stats from the 2024/2025 UCL season

If player ratings are missing, it's likely due to ESPN not publishing boxscore data for that match.

✍️ Author
Philip Oduro
Data Engineer | Analytics Engineer
GitHub: @Odurophilip

