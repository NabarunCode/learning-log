# ===============================================================
# 13. pandas_intro.py
# Topic   : Pandas fundamentals — Series, DataFrame, inspection,
#           selection, filtering
# Author  : Nabarun Chakraborty (NabarunCode)
# Created : Wednesday, 03 June 2026 — 08:37 IST
# Repo    : github.com/NabarunCode/learning-log/python-basics
# ===============================================================

# Colab note: pandas comes pre-installed. Locally, run:
# pip install pandas
import pandas as pd   # 'pd' is the universal alias — always use it


# ---------------------------------------------------------------
# 1. SERIES — a single labelled column (1D)
# ---------------------------------------------------------------
# A Series = values + an index (the labels on the left)
weekly_commits = pd.Series(
    [18, 23, 44, 53],
    index=["Week 1", "Week 2", "Week 3", "Week 4"]
)
print("Series — weekly commits:")
print(weekly_commits)
print("Value for Week 3:", weekly_commits["Week 3"])   # label-based lookup
print()


# ---------------------------------------------------------------
# 2. DATAFRAME — the main object (2D table)
# ---------------------------------------------------------------
# Built from a dictionary: each key = column name, each list = column data
learning_log = pd.DataFrame({
    "week":     ["Week 1", "Week 2", "Week 3", "Week 4"],
    "topic":    ["Python basics", "File + errors", "NumPy", "Linear algebra"],
    "commits":  [18, 23, 44, 53],
    "hours":    [9, 11, 14, 16],
})
print("DataFrame — learning_log:")
print(learning_log)
print()


# ---------------------------------------------------------------
# 3. INSPECTION — first thing you ALWAYS do with new data
# ---------------------------------------------------------------
print("head(2) — top rows:")
print(learning_log.head(2))            # first n rows (default 5)

print("\nshape (rows, cols):", learning_log.shape)
print("columns:", list(learning_log.columns))

print("\ninfo() — dtypes + non-null counts:")
learning_log.info()

print("\ndescribe() — quick stats on numeric columns:")
print(learning_log.describe())
print()


# ---------------------------------------------------------------
# 4. SELECTION — grabbing columns and rows
# ---------------------------------------------------------------
# Single column → returns a Series
print("Just the 'topic' column:")
print(learning_log["topic"])

# Multiple columns → pass a list → returns a DataFrame
print("\nTwo columns (week + commits):")
print(learning_log[["week", "commits"]])

# Row selection:
#   .loc[] → by LABEL   |   .iloc[] → by INTEGER position
print("\n.iloc[0] — first row by position:")
print(learning_log.iloc[0])

print("\n.loc[2, 'topic'] — row 2, topic column:")
print(learning_log.loc[2, "topic"])
print()


# ---------------------------------------------------------------
# 5. FILTERING — the real power (boolean masking)
# ---------------------------------------------------------------
# Step 1: build a condition → gives True/False per row
high_output = learning_log["commits"] > 30
print("Boolean mask (commits > 30):")
print(high_output)

# Step 2: feed the mask back into the DataFrame → keeps only True rows
print("\nWeeks where commits > 30:")
print(learning_log[high_output])

# Combine conditions: & = and, | = or  (wrap each in brackets!)
busy_weeks = learning_log[(learning_log["commits"] > 20) & (learning_log["hours"] >= 14)]
print("\nBusy weeks (commits > 20 AND hours >= 14):")
print(busy_weeks)


# ---------------------------------------------------------------
# 6. SAMPLE OUTPUT (what you should see)
# ---------------------------------------------------------------
# Series → Week 3 = 44
# describe() → commits mean = 34.5
# Filter (commits > 30) → Week 3 and Week 4 rows only
# ===============================================================
