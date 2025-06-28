import os
import pandas as pd

# Step 1: Load all stat CSVs
stat_dir = "ucl_stat_tables"
all_stat_files = [f for f in os.listdir(stat_dir) if f.endswith(".csv")]

merged_df = None

for file in all_stat_files:
    stat_name = file.replace(".csv", "")
    df = pd.read_csv(os.path.join(stat_dir, file))
    
    # Rename stat_value to the actual stat (e.g. "goals")
    df = df.rename(columns={"stat_value": stat_name})
    
    if merged_df is None:
        merged_df = df
    else:
        # Merge on player_id, player_name, team_name
        merged_df = pd.merge(merged_df, df, on=["player_id", "player_name", "team_name"], how="outer")

# Step 2: Load ratings and calculate average rating per player
ratings_df = pd.read_csv("ucl_player_ratings.csv")

avg_ratings = (
    ratings_df.groupby(["player_id", "player_name", "team_name"])["rating"]
    .mean()
    .reset_index()
    .rename(columns={"rating": "avg_rating"})
)

# Step 3: Merge ratings into the stats table
final_df = pd.merge(merged_df, avg_ratings, on=["player_id", "player_name", "team_name"], how="left")

# Step 4: Save the result
final_df.to_csv("merged_ucl_player_stats.csv", index=False)
print("✅ Final merged file saved as 'merged_ucl_player_stats.csv'")
