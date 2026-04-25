# vectors.py
# Linear Algebra for ML — Vectors with NumPy
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 14 of my learning journey

import numpy as np

# --- 1. WHAT IS A VECTOR? ---
print("=== VECTORS ===")

# A vector is an ordered list of numbers
# In ML: represents a data point, word embedding, feature set, etc.

v1 = np.array([3, 4])           # 2D vector
v2 = np.array([1, 2, 3])        # 3D vector
v3 = np.array([0.5, 1.0, 1.5, 2.0])  # 4D vector (common in ML feature vectors)

print(f"2D vector  : {v1}")
print(f"3D vector  : {v2}")
print(f"4D vector  : {v3}")
print(f"Shape of v2: {v2.shape}")   # (3,) — 1D array of 3 elements

# --- 2. VECTOR ADDITION & SUBTRACTION ---
print("\n=== VECTOR ADDITION & SUBTRACTION ===")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"a         : {a}")
print(f"b         : {b}")
print(f"a + b     : {a + b}")    # element-wise
print(f"b - a     : {b - a}")

# --- 3. SCALAR MULTIPLICATION ---
print("\n=== SCALAR MULTIPLICATION ===")

print(f"a * 2     : {a * 2}")    # scale every element
print(f"a / 2     : {a / 2}")
print(f"-1 * a    : {-1 * a}")   # reverse direction

# --- 4. MAGNITUDE (LENGTH) OF A VECTOR ---
print("\n=== MAGNITUDE ===")

# Magnitude = sqrt(sum of squares) — Pythagoras in N dimensions
# In ML: used in normalisation, cosine similarity, distance metrics

v = np.array([3, 4])
magnitude = np.linalg.norm(v)
print(f"Vector    : {v}")
print(f"Magnitude : {magnitude}")   # 5.0 — classic 3-4-5 triangle

v2_mag = np.linalg.norm(v2)
print(f"||v2||    : {v2_mag:.4f}")

# --- 5. UNIT VECTOR (NORMALISATION) ---
print("\n=== UNIT VECTOR ===")

# Unit vector = vector / magnitude
# Direction preserved, length = 1
# In ML: normalising inputs so scale doesn't dominate

unit_v = v / np.linalg.norm(v)
print(f"Original  : {v}")
print(f"Unit vec  : {unit_v}")
print(f"Check mag : {np.linalg.norm(unit_v):.4f}")   # should be 1.0

# --- 6. DOT PRODUCT ---
print("\n=== DOT PRODUCT ===")

# dot(a, b) = sum of element-wise products
# In ML: used in matrix multiply, attention, cosine similarity, neurons

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)
print(f"a         : {a}")
print(f"b         : {b}")
print(f"dot(a, b) : {dot}")    # 1*4 + 2*5 + 3*6 = 32

# --- 7. ANGLE BETWEEN VECTORS (COSINE SIMILARITY) ---
print("\n=== COSINE SIMILARITY ===")

# cos(θ) = dot(a, b) / (||a|| * ||b||)
# = 1  → same direction (very similar)
# = 0  → perpendicular (unrelated)
# = -1 → opposite direction
# In ML: used in NLP to compare word/sentence embeddings

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

x = np.array([1, 0])
y = np.array([1, 0])   # identical
z = np.array([0, 1])   # perpendicular

print(f"cos(x, y) : {cosine_similarity(x, y):.2f}")   # 1.0
print(f"cos(x, z) : {cosine_similarity(x, z):.2f}")   # 0.0
print(f"cos(a, b) : {cosine_similarity(a, b):.4f}")
