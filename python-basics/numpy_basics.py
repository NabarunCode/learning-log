# numpy_basics.py
# NumPy Basics — Arrays, Operations, Indexing
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 11 of my learning journey

import numpy as np

# --- 1. CREATING ARRAYS ---
print("=== CREATING ARRAYS ===")

a = np.array([1, 2, 3, 4, 5])          # 1D array
b = np.array([[1, 2, 3],               # 2D array
              [4, 5, 6]])

print(f"1D array: {a}")
print(f"2D array:\n{b}")

# --- 2. ARRAY PROPERTIES ---
print("\n=== ARRAY PROPERTIES ===")

print(f"Shape of a: {a.shape}")        # (5,)
print(f"Shape of b: {b.shape}")        # (2, 3)
print(f"Dimensions of b: {b.ndim}")    # 2
print(f"Data type of a: {a.dtype}")    # int64
print(f"Total elements in b: {b.size}")# 6

# --- 3. SPECIAL ARRAYS ---
print("\n=== SPECIAL ARRAYS ===")

zeros = np.zeros((3, 3))              # 3x3 matrix of zeros
ones  = np.ones((2, 4))              # 2x4 matrix of ones
rng   = np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]
lin   = np.linspace(0, 1, 5)         # 5 evenly spaced values 0→1

print(f"Zeros:\n{zeros}")
print(f"Ones:\n{ones}")
print(f"Arange: {rng}")
print(f"Linspace: {lin}")

# --- 4. BASIC OPERATIONS ---
print("\n=== BASIC OPERATIONS ===")

x = np.array([10, 20, 30, 40, 50])
y = np.array([1, 2, 3, 4, 5])

print(f"x + y     = {x + y}")
print(f"x - y     = {x - y}")
print(f"x * y     = {x * y}")
print(f"x / y     = {x / y}")
print(f"x * 2     = {x * 2}")         # scalar operation
print(f"x squared = {x ** 2}")

# --- 5. INDEXING & SLICING ---
print("\n=== INDEXING & SLICING ===")

arr = np.array([10, 20, 30, 40, 50])
print(f"First element : {arr[0]}")
print(f"Last element  : {arr[-1]}")
print(f"Slice [1:4]   : {arr[1:4]}")
print(f"Every 2nd     : {arr[::2]}")

# 2D indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(f"\n2D Matrix:\n{matrix}")
print(f"Row 0         : {matrix[0]}")
print(f"Element [1,2] : {matrix[1, 2]}")   # row 1, col 2 → 6
print(f"Column 1      : {matrix[:, 1]}")   # all rows, col 1

# --- 6. USEFUL MATH FUNCTIONS ---
print("\n=== MATH FUNCTIONS ===")

data = np.array([4, 8, 15, 16, 23, 42])
print(f"Sum    : {np.sum(data)}")
print(f"Mean   : {np.mean(data)}")
print(f"Max    : {np.max(data)}")
print(f"Min    : {np.min(data)}")
print(f"Std Dev: {np.std(data):.2f}")
