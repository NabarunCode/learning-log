# eigenvalues.py
# Eigenvalues & Eigenvectors — Linear Algebra for ML
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 17 of my learning journey

import numpy as np

# --- WHAT ARE EIGENVALUES & EIGENVECTORS? ---
# If A is a square matrix, v is an eigenvector, λ (lambda) is an eigenvalue:
#     A @ v = λ * v
# Translation: multiplying matrix A by vector v only *scales* v — it doesn't rotate it.
# λ tells you HOW MUCH it scales. v tells you in WHICH DIRECTION.

# --- 1. COMPUTING EIGENVALUES & EIGENVECTORS ---
print("=== EIGENVALUES & EIGENVECTORS ===")

A = np.array([[4, 2],
              [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Matrix A:\n{A}")
print(f"\nEigenvalues  : {eigenvalues}")
print(f"Eigenvectors :\n{eigenvectors}")

# --- 2. VERIFY: A @ v = λ * v ---
print("\n=== VERIFICATION: A @ v = λ * v ===")

for i in range(len(eigenvalues)):
    lam = eigenvalues[i]
    v   = eigenvectors[:, i]           # each column is one eigenvector
    lhs = A @ v                        # left-hand side
    rhs = lam * v                      # right-hand side
    print(f"\nEigenvalue λ{i+1} = {lam:.4f}")
    print(f"  Eigenvector v{i+1}  = {v}")
    print(f"  A @ v           = {lhs.round(6)}")
    print(f"  λ * v           = {rhs.round(6)}")
    print(f"  Match?          = {np.allclose(lhs, rhs)}")

# --- 3. SYMMETRIC MATRIX (COMMON IN ML) ---
print("\n=== SYMMETRIC MATRIX ===")

S = np.array([[3, 1, 0],
              [1, 2, 1],
              [0, 1, 3]])

evals, evecs = np.linalg.eig(S)

print(f"Symmetric Matrix S:\n{S}")
print(f"\nEigenvalues  : {evals.round(4)}")
print(f"Eigenvectors :\n{evecs.round(4)}")

# --- 4. EIGENVALUES IN ML — VARIANCE INTUITION ---
print("\n=== EIGENVALUES & VARIANCE (PCA INTUITION) ===")

# In PCA, eigenvalues of a covariance matrix = variance explained by each direction
# Larger eigenvalue → more variance → more important direction

cov_matrix = np.array([[3.0, 1.5],
                        [1.5, 1.0]])

evals_cov, evecs_cov = np.linalg.eig(cov_matrix)

total_variance = np.sum(evals_cov)
explained      = evals_cov / total_variance * 100

print(f"Covariance Matrix:\n{cov_matrix}")
print(f"\nEigenvalues (variance per direction) : {evals_cov.round(4)}")
print(f"Total variance                        : {total_variance:.4f}")
print(f"Variance explained (%)               : {explained.round(2)}")
print(f"\n→ Direction 1 explains {explained[0]:.1f}% of variance (principal component 1)")
print(f"→ Direction 2 explains {explained[1]:.1f}% of variance (principal component 2)")
