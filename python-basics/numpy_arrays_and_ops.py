# numpy_arrays_and_ops.py
# NumPy — Arrays & Operations Deeper Dive
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 12 of my learning journey

import numpy as np

# --- 1. ARRAY CREATION METHODS ---
print("=== ARRAY CREATION ===")

a = np.array([1, 2, 3, 4, 5], dtype=float)   # force float dtype
b = np.zeros(5)                                # five zeros
c = np.ones((3, 3))                            # 3x3 ones
d = np.eye(3)                                  # identity matrix (diagonal = 1)
e = np.random.randint(1, 10, size=(3, 3))      # random int matrix

print(f"Float array   : {a}")
print(f"Zeros         : {b}")
print(f"Ones 3x3:\n{c}")
print(f"Identity 3x3:\n{d}")
print(f"Random 3x3:\n{e}")

# --- 2. RESHAPING ---
print("\n=== RESHAPING ===")

flat   = np.arange(1, 13)                      # [1, 2, 3, ... 12]
matrix = flat.reshape(3, 4)                    # 3 rows x 4 cols
back   = matrix.flatten()                      # back to 1D
auto   = flat.reshape(2, -1)                   # -1 = NumPy figures out cols

print(f"Flat          : {flat}")
print(f"Reshaped 3x4:\n{matrix}")
print(f"Flattened     : {back}")
print(f"Reshape(2,-1):\n{auto}")

# --- 3. ARRAY OPERATIONS ---
print("\n=== ARRAY OPERATIONS ===")

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print(f"x + y     : {x + y}")
print(f"y - x     : {y - x}")
print(f"x * y     : {x * y}")
print(f"y / x     : {y / x}")
print(f"x ** 2    : {x ** 2}")
print(f"sqrt(y)   : {np.sqrt(y)}")

# --- 4. BROADCASTING ---
print("\n=== BROADCASTING ===")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row    = np.array([1, 2, 3])

print(f"Matrix + 10:\n{matrix + 10}")
print(f"Matrix + row:\n{matrix + row}")

# --- 5. AGGREGATE OPERATIONS ---
print("\n=== AGGREGATE OPERATIONS ===")

data = np.array([[4, 7, 2],
                 [1, 9, 5],
                 [8, 3, 6]])

print(f"Total sum     : {np.sum(data)}")
print(f"Row sums      : {np.sum(data, axis=1)}")
print(f"Col sums      : {np.sum(data, axis=0)}")
print(f"Global mean   : {np.mean(data):.2f}")
print(f"Global max    : {np.max(data)}")
print(f"Col max       : {np.max(data, axis=0)}")

# --- 6. DOT PRODUCT & MATRIX MULTIPLY ---
print("\n=== DOT PRODUCT & MATRIX MULTIPLY ===")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"Dot product   : {np.dot(a, b)}")      # 1*4 + 2*5 + 3*6 = 32

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A @ B:\n{A @ B}")                      # matrix multiplication
