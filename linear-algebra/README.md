# 📐 Linear Algebra for ML

Math foundations needed for Machine Learning.

---

## 📋 Topics Checklist

- [x] Vectors & matrices
- [x] Matrix multiplication
- [x] Eigenvalues & eigenvectors
- [x] Applications in ML

---

## 🗂️ File Index

| File | What It Does | Key Concepts |
|---|---|---|
| `vectors.py` | Vector creation, arithmetic, magnitude, dot product, cosine similarity | np.array, norm, dot, unit vector |
| `matrices.py` | Matrix creation, shape inspection, arithmetic, transpose, reshape | ndarray, shape, T, reshape, broadcasting |
| `matrix_operations.py` | Dot product, matrix multiply, inverse, determinant | np.dot, @, linalg.inv, linalg.det |
| `eigenvalues.py` | Eigenvalues, eigenvectors, covariance matrix, PCA preview | linalg.eig, covariance, variance explained |
| `linear_algebra_in_ml.py` | How linear algebra powers real ML — regression, embeddings, PCA end-to-end | lstsq, cosine similarity, PCA, weight matrices |

---

## ▶️ How to Run

All scripts run in Google Colab (NumPy pre-installed) or locally:

```bash
python vectors.py
python matrices.py
python matrix_operations.py
python eigenvalues.py
python linear_algebra_in_ml.py
```

---

## 🧠 Why This Matters

Every neural network forward pass is a matrix multiplication.
Every embedding comparison is a dot product.
Every dimensionality reduction is eigendecomposition.
This folder is the math behind the magic.

---

[← Back to Main README](../README.md)
