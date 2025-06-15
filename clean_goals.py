import pandas as pd

# Load the goals leaders CSV
df = pd.read_csv("goalsLeaders.csv")

# Extract matches played and goals from stat_display
df["matches_played"] = df["stat_display"].str.extract(r"Matches: (\d+)")
df["goals"] = df["stat_display"].str.extract(r"Goals: (\d+)")

# Convert to numeric
df["matches_played"] = pd.to_numeric(df["matches_played"])
df["goals"] = pd.to_numeric(df["goals"])

# Drop original stat_display
df = df.drop(columns=["stat_display"])

# Save cleaned version
df.to_csv("goalsLeaders_cleaned.csv", index=False)
print("✅ Saved cleaned goals leaders to goalsLeaders_cleaned.csv")
