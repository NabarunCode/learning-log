# matrix_operations.py
# Linear Algebra — Matrix Operations: Dot Product, Inverse, Determinant
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 16 of my learning journey

import numpy as np

# --- 1. DOT PRODUCT ---
print("=== DOT PRODUCT ===")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

dot = A @ B   # preferred over np.dot for matrices

print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"A @ B:\n{dot}")

# --- 2. TRANSPOSE ---
print("\n=== TRANSPOSE ===")

C = np.array([[1, 2, 3],
              [4, 5, 6]])

print(f"C:\n{C}")
print(f"C.T:\n{C.T}")
print(f"Shape before: {C.shape} → after: {C.T.shape}")

# --- 3. DETERMINANT ---
print("\n=== DETERMINANT ===")

M = np.array([[3, 8],
              [4, 6]])

det = np.linalg.det(M)
print(f"Matrix M:\n{M}")
print(f"Determinant: {det:.2f}")
# det = (3*6) - (8*4) = 18 - 32 = -14
print(f"Manual check: (3×6) - (8×4) = {(3*6) - (8*4)}")

# --- 4. INVERSE ---
print("\n=== INVERSE ===")

# Invertible matrix (det ≠ 0)
P = np.array([[2., 1.],
              [5., 3.]])

P_inv = np.linalg.inv(P)
print(f"P:\n{P}")
print(f"P inverse:\n{P_inv}")

# Verify: P @ P_inv should give identity matrix
identity_check = np.round(P @ P_inv, decimals=10)
print(f"P @ P_inv (should be identity):\n{identity_check}")

# --- 5. SINGULAR MATRIX (not invertible) ---
print("\n=== SINGULAR MATRIX ===")

S = np.array([[2, 4],
              [1, 2]])

det_s = np.linalg.det(S)
print(f"S:\n{S}")
print(f"Determinant of S: {det_s:.2f}")
print("Det = 0 → singular matrix → no inverse exists")

# --- 6. SOLVING A LINEAR SYSTEM ---
print("\n=== SOLVING LINEAR SYSTEM: Ax = b ===")

# Example: 2x + y = 5 and x + 3y = 10
A_sys = np.array([[2., 1.],
                  [1., 3.]])
b_sys = np.array([5., 10.])

x = np.linalg.solve(A_sys, b_sys)
print(f"A:\n{A_sys}")
print(f"b: {b_sys}")
print(f"Solution x: {x}")
print(f"Verify A @ x: {A_sys @ x}")
