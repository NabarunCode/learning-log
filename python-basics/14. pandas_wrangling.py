# ============================================================
# 14. pandas_wrangling.py
# Pandas data wrangling — filtering, grouping, cleaning, merging
# Author: Nabarun Chakraborty
# Created: Wednesday, 03 June 2026 — 13:13 IST
# Part of: python-basics/ | learning-log
# Run in: Google Colab
# ============================================================

# !pip install pandas   # pre-installed in Colab, here for reference

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# 1. SAMPLE DATA — a small "IT team transitioning to AI" dataset
#    (built from a dict — same as Day 19, but messier on purpose)
# ------------------------------------------------------------
team_data = {
    "name":        ["Arijit", "Priya", "Rahul", "Sneha", "Vikram", "Meera"],
    "city":        ["Kolkata", "Pune", "Kolkata", "Bengaluru", "Pune", "Kolkata"],
    "experience":  [18, 12, 8, np.nan, 15, 6],          # years in IT (one missing)
    "ai_hours":    [120, 95, 200, 60, np.nan, 150],     # hours spent learning AI
    "track":       ["MLOps", "Data", "MLOps", "Data", "MLOps", "Data"],
}

team = pd.DataFrame(team_data)
print("RAW DATA:")
print(team)
print("\nShape (rows, cols):", team.shape)

# ------------------------------------------------------------
# 2. FILTERING ROWS — boolean masking
#    "Give me only the people I care about"
# ------------------------------------------------------------
# Single condition: experience above 10 years
veterans = team[team["experience"] > 10]
print("\nVeterans (10+ yrs):")
print(veterans)

# Multiple conditions: use & (and), | (or) — wrap each in ()
kolkata_mlops = team[(team["city"] == "Kolkata") & (team["track"] == "MLOps")]
print("\nKolkata + MLOps folks:")
print(kolkata_mlops)

# ------------------------------------------------------------
# 3. SELECTING COLUMNS — .loc (label-based) vs .iloc (position-based)
# ------------------------------------------------------------
# .loc → by name | rows, columns
print("\nName + AI hours only (.loc):")
print(team.loc[:, ["name", "ai_hours"]])

# .iloc → by integer position | first 3 rows, first 2 cols
print("\nFirst 3 rows, first 2 cols (.iloc):")
print(team.iloc[0:3, 0:2])

# ------------------------------------------------------------
# 4. HANDLING MISSING DATA (the np.nan values)
#    Real data ALWAYS has holes — this is non-negotiable cleanup
# ------------------------------------------------------------
print("\nMissing values per column:")
print(team.isna().sum())          # count NaNs in each column

# Strategy A — drop rows with any missing value
dropped = team.dropna()
print("\nAfter dropna() — rows with holes removed:")
print(dropped)

# Strategy B — fill missing with a sensible value (mean here)
team_filled = team.copy()         # never mutate the original carelessly
team_filled["experience"] = team_filled["experience"].fillna(
    team_filled["experience"].mean()
)
team_filled["ai_hours"] = team_filled["ai_hours"].fillna(0)   # 0 = "not started"
print("\nAfter fillna() — holes patched:")
print(team_filled)

# ------------------------------------------------------------
# 5. SORTING
# ------------------------------------------------------------
by_hours = team_filled.sort_values("ai_hours", ascending=False)
print("\nSorted by AI hours (most committed first):")
print(by_hours)

# ------------------------------------------------------------
# 6. ADDING / MODIFYING COLUMNS
#    Derive new signal from existing columns
# ------------------------------------------------------------
# AI hours per year of experience — a rough "intensity" score
team_filled["intensity"] = (
    team_filled["ai_hours"] / team_filled["experience"]
).round(1)
print("\nWith new 'intensity' column:")
print(team_filled[["name", "ai_hours", "experience", "intensity"]])

# ------------------------------------------------------------
# 7. GROUPBY + AGGREGATION — the workhorse of analysis
#    "Split → Apply → Combine" (like SQL GROUP BY)
# ------------------------------------------------------------
# Average AI hours per track
track_summary = team_filled.groupby("track")["ai_hours"].mean().round(1)
print("\nAvg AI hours by track:")
print(track_summary)

# Multiple aggregations at once per city
city_stats = team_filled.groupby("city").agg(
    avg_experience=("experience", "mean"),
    total_ai_hours=("ai_hours", "sum"),
    headcount=("name", "count"),
)
print("\nCity-wise stats:")
print(city_stats)

# ------------------------------------------------------------
# 8. MERGING TWO DATAFRAMES — like a SQL JOIN
#    Bring in extra info from a second table
# ------------------------------------------------------------
# Second table: target salary band per track
salary_bands = pd.DataFrame({
    "track":      ["MLOps", "Data"],
    "target_lpa": [28, 22],          # target salary in lakhs per annum
})

# Join on the shared 'track' column
merged = pd.merge(team_filled, salary_bands, on="track", how="left")
print("\nMerged with salary bands:")
print(merged[["name", "track", "target_lpa"]])

# ------------------------------------------------------------
# 9. apply() — run a custom function on each row/value
# ------------------------------------------------------------
# Tag readiness based on AI hours
def readiness_tag(hours):
    if hours >= 150:
        return "Job-ready"
    elif hours >= 80:
        return "Building"
    else:
        return "Early"

merged["status"] = merged["ai_hours"].apply(readiness_tag)
print("\nFinal wrangled table:")
print(merged[["name", "city", "ai_hours", "status", "target_lpa"]])

# ============================================================
# MENTAL MODEL (recap):
#   Filter  → pick the ROWS you want      (boolean mask)
#   Select  → pick the COLUMNS you want   (.loc / .iloc)
#   Clean   → handle NaN                  (dropna / fillna)
#   Derive  → make new columns            (arithmetic / apply)
#   Group   → split-apply-combine         (groupby + agg)
#   Merge   → join tables                 (pd.merge)
# This 6-step loop is ~80% of all data prep before any ML model.
# ============================================================
