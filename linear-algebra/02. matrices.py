# matrices.py
# Linear Algebra — Matrices
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 15 of my learning journey

import numpy as np

# --- 1. CREATING MATRICES ---
print("=== CREATING MATRICES ===")

A = np.array([[1, 2, 3],
              [4, 5, 6]])              # 2x3 matrix

B = np.zeros((3, 3))                  # 3x3 zeros
C = np.ones((2, 4))                   # 2x4 ones
I = np.eye(3)                         # 3x3 identity matrix

print(f"Matrix A (2x3):\n{A}")
print(f"Zeros (3x3):\n{B}")
print(f"Ones (2x4):\n{C}")
print(f"Identity (3x3):\n{I}")

# --- 2. MATRIX PROPERTIES ---
print("\n=== MATRIX PROPERTIES ===")

print(f"Shape of A  : {A.shape}")     # (2, 3)
print(f"Dimensions  : {A.ndim}")      # 2
print(f"Total elems : {A.size}")      # 6
print(f"Data type   : {A.dtype}")     # int64

# --- 3. MATRIX ADDITION & SUBTRACTION ---
print("\n=== ADDITION & SUBTRACTION ===")

X = np.array([[1, 2],
              [3, 4]])

Y = np.array([[5, 6],
              [7, 8]])

print(f"X + Y:\n{X + Y}")
print(f"Y - X:\n{Y - X}")

# --- 4. SCALAR MULTIPLICATION ---
print("\n=== SCALAR MULTIPLICATION ===")

print(f"X * 3:\n{X * 3}")
print(f"X / 2:\n{X / 2}")

# --- 5. MATRIX MULTIPLICATION ---
print("\n=== MATRIX MULTIPLICATION ===")

P = np.array([[1, 2],
              [3, 4]])

Q = np.array([[5, 6],
              [7, 8]])

print(f"P @ Q (matrix multiply):\n{P @ Q}")
print(f"np.dot(P, Q):\n{np.dot(P, Q)}")

# Non-square: (2x3) @ (3x2) → (2x2)
M = np.array([[1, 2, 3],
              [4, 5, 6]])             # 2x3

N = np.array([[7, 8],
              [9, 10],
              [11, 12]])              # 3x2

print(f"\nM (2x3):\n{M}")
print(f"N (3x2):\n{N}")
print(f"M @ N → (2x2):\n{M @ N}")

# --- 6. TRANSPOSE ---
print("\n=== TRANSPOSE ===")

T = np.array([[1, 2, 3],
              [4, 5, 6]])

print(f"Original (2x3):\n{T}")
print(f"Transposed (3x2):\n{T.T}")
print(f"Shape before: {T.shape} → after: {T.T.shape}")
