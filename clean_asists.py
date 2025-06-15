import pandas as pd
import re

# Load the assists leaders CSV
df = pd.read_csv("assistsLeaders.csv")

# Extract matches and assists from stat_display
df["matches_played"] = df["stat_display"].str.extract(r"Matches: (\d+)")
df["assists"] = df["stat_display"].str.extract(r"Assists: (\d+)")

# Convert to numeric
df["matches_played"] = pd.to_numeric(df["matches_played"])
df["assists"] = pd.to_numeric(df["assists"])

# Drop original stat_display column
df = df.drop(columns=["stat_display"])

# Save to new file
df.to_csv("assistsLeaders_cleaned.csv", index=False)
print("✅ Saved cleaned assists leaders to assistsLeaders_cleaned.csv")
