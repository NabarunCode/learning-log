# numpy_indexing.py
# NumPy — Indexing, Boolean Masks, and Practical Exercises
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 13 of my learning journey

import numpy as np

# --- 1. BASIC INDEXING RECAP ---
print("=== BASIC INDEXING RECAP ===")

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(f"Full array     : {arr}")
print(f"Index 0        : {arr[0]}")
print(f"Index -1       : {arr[-1]}")
print(f"Slice [2:6]    : {arr[2:6]}")
print(f"Every 2nd      : {arr[::2]}")
print(f"Reversed       : {arr[::-1]}")

# --- 2. BOOLEAN INDEXING ---
print("\n=== BOOLEAN INDEXING ===")
# Think of this like a filter query in Excel or SQL WHERE clause

scores = np.array([45, 82, 61, 90, 38, 74, 55, 88, 42, 76])

print(f"All scores     : {scores}")

# Create a boolean mask
passed = scores >= 60
print(f"Passed mask    : {passed}")        # True/False array
print(f"Passing scores : {scores[passed]}")  # only True values returned

# Directly inline — more common in ML code
print(f"Scores > 80    : {scores[scores > 80]}")
print(f"Scores 60-80   : {scores[(scores >= 60) & (scores <= 80)]}")
print(f"Failed (< 60)  : {scores[scores < 60]}")

# --- 3. FANCY INDEXING ---
print("\n=== FANCY INDEXING ===")
# Select multiple specific positions using an index array

skills = np.array(["Python", "NumPy", "Pandas", "ML", "Docker", "MLOps"])

# Pick specific indices
pick = skills[[0, 2, 4]]
print(f"Skills array   : {skills}")
print(f"Picked [0,2,4] : {pick}")

# Works on 2D too
matrix = np.array([[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9, 10, 11, 12]])

print(f"\n2D Matrix:\n{matrix}")
print(f"Row 0 and 2    :\n{matrix[[0, 2]]}")
print(f"Specific cells : {matrix[[0, 1, 2], [1, 2, 3]]}")  # (0,1), (1,2), (2,3)

# --- 4. np.where() ---
print("\n=== np.where() ===")
# Like Excel IF() — condition → value_if_true, value_if_false
# Critical in ML for label assignment, thresholding, masking

scores = np.array([45, 82, 61, 90, 38, 74, 55, 88, 42, 76])

# Assign Pass/Fail labels
labels = np.where(scores >= 60, "Pass", "Fail")
print(f"Scores  : {scores}")
print(f"Labels  : {labels}")

# Replace values conditionally
boosted = np.where(scores < 60, scores + 10, scores)
print(f"Boosted : {boosted}")   # failed scores get +10, rest unchanged

# --- 5. argmax() and argmin() ---
print("\n=== argmax() and argmin() ===")
# Returns the INDEX (position) of max/min — not the value itself
# Used constantly in ML: "which class has highest probability?"

predictions = np.array([0.05, 0.12, 0.68, 0.10, 0.05])
# e.g. model output probabilities for 5 classes

print(f"Predictions    : {predictions}")
print(f"Max value      : {np.max(predictions):.2f}")
print(f"Predicted class: {np.argmax(predictions)}")   # → 2 (highest prob)
print(f"Min value      : {np.min(predictions):.2f}")
print(f"argmin         : {np.argmin(predictions)}")   # → 0

# On 2D
matrix = np.array([[3, 7, 1],
                   [9, 2, 5],
                   [4, 8, 6]])

print(f"\n2D Matrix:\n{matrix}")
print(f"Global argmax  : {np.argmax(matrix)}")          # flattened index
print(f"Col-wise argmax: {np.argmax(matrix, axis=0)}")  # which row has max per col
print(f"Row-wise argmax: {np.argmax(matrix, axis=1)}")  # which col has max per row

# --- 6. PRACTICAL EXERCISES ---
print("\n=== PRACTICAL EXERCISES ===")

# Exercise 1 — Student grade analyser
print("\n-- Exercise 1: Grade Analyser --")
grades = np.array([72, 45, 88, 91, 63, 55, 79, 84, 38, 95])

distinctions = grades[grades >= 85]
failures      = grades[grades < 50]
average       = np.mean(grades)
topper_index  = np.argmax(grades)

print(f"All grades     : {grades}")
print(f"Distinctions   : {distinctions}")
print(f"Failures       : {failures}")
print(f"Class average  : {average:.1f}")
print(f"Topper index   : {topper_index} → Score: {grades[topper_index]}")

# Exercise 2 — Temperature threshold alert
print("\n-- Exercise 2: Temperature Alert --")
temps = np.array([34.2, 36.8, 38.5, 37.1, 39.4, 35.6, 40.1, 36.2])

alerts  = np.where(temps >= 38.0, "🔴 HIGH", "🟢 OK")
hottest = np.argmax(temps)

print(f"Temps  : {temps}")
print(f"Alerts : {alerts}")
print(f"Hottest reading: index {hottest} → {temps[hottest]}°C")

# Exercise 3 — ML model prediction picker
print("\n-- Exercise 3: Model Prediction --")
class_names = np.array(["Cat", "Dog", "Bird", "Fish", "Rabbit"])
probs       = np.array([0.08, 0.61, 0.14, 0.03, 0.14])

predicted_index = np.argmax(probs)
top2_indices    = np.argsort(probs)[::-1][:2]   # argsort + reverse + take 2

print(f"Class probs    : {probs}")
print(f"Predicted      : {class_names[predicted_index]} ({probs[predicted_index]*100:.0f}%)")
print(f"Top 2 guesses  : {class_names[top2_indices]}")
