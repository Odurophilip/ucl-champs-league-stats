import json
import pandas as pd
import os

# Path setup
input_path = "../data/full_response.json"
output_dir = "../data/ucl_stats_split"
os.makedirs(output_dir, exist_ok=True)

# Load your saved ESPN Champions League stats response
with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

stats = data.get("stats", [])
print(f"✅ Found {len(stats)} stat categories")

# Track all players for merging later
master_df = pd.DataFrame()

for stat_block in stats:
    category = stat_block.get("name")  # e.g. "goalsLeaders"
    leaders = stat_block.get("leaders", [])

    rows = []
    for leader in leaders:
        athlete = leader.get("athlete", {})
        row = {
            "player_id": athlete.get("id"),
            "player_name": athlete.get("displayName"),
            "team": athlete.get("team", {}).get("name") if athlete.get("team") else None,
            "stat_value": leader.get("value"),
            "stat_display": leader.get("displayValue")
        }
        rows.append(row)

    df = pd.DataFrame(rows)

    if not df.empty:
        # Save each stat group to its own file
        filename = os.path.join(output_dir, f"{category}.csv")
        df.to_csv(filename, index=False)
        print(f"📁 Saved: {filename}")

        # Merge into master df (by player_id)
        df = df.rename(columns={"stat_value": category})
        df = df[["player_id", category]]
        if master_df.empty:
            master_df = df
        else:
            master_df = pd.merge(master_df, df, on="player_id", how="outer")

# Optional: Save combined stats
if not master_df.empty:
    combined_path = os.path.join("../data", "ucl_combined_stats.csv")
    master_df.to_csv(combined_path, index=False)
    print(f"✅ Combined stats saved to {combined_path}")
else:
    print("❌ No player stats found in the JSON.")
