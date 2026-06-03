# linear_algebra_in_ml.py
# Day 18 — Linear Algebra in ML Applications
# Topic: How vectors, matrices, dot products, and eigenvalues power real ML

import numpy as np

print("=" * 60)
print("LINEAR ALGEBRA IN MACHINE LEARNING — APPLICATIONS")
print("=" * 60)

# ─────────────────────────────────────────────
# 1. DATASET AS A MATRIX
# ─────────────────────────────────────────────
# In ML, every dataset is a matrix.
# Rows = samples (data points), Columns = features

print("\n📦 1. Dataset as a Matrix")
print("-" * 40)

# 4 house listings: [area_sqft, bedrooms, price_lakhs]
house_data = np.array([
    [1200, 2, 45],
    [1800, 3, 68],
    [900,  1, 30],
    [2200, 4, 95]
])

num_samples, num_features = house_data.shape
print(f"Dataset shape: {house_data.shape}")
print(f"Samples (houses): {num_samples}")
print(f"Features (area, bedrooms, price): {num_features}")
print(f"\nDataset:\n{house_data}")

# ─────────────────────────────────────────────
# 2. DOT PRODUCT — THE HEART OF NEURAL NETWORKS
# ─────────────────────────────────────────────
# y = X @ W  (matrix multiply inputs by weights)
# This is literally what every dense/linear layer does

print("\n⚡ 2. Dot Product — Heart of Neural Networks")
print("-" * 40)

# Input features for one house (normalised)
input_features = np.array([0.6, 0.5, 0.7])   # area, bedrooms, locality score

# Weights a neuron has learned
neuron_weights = np.array([0.8, 0.3, 0.5])

# Bias term
bias = 0.1

# What a single neuron computes
neuron_output = np.dot(input_features, neuron_weights) + bias
print(f"Input features : {input_features}")
print(f"Neuron weights : {neuron_weights}")
print(f"Bias           : {bias}")
print(f"Neuron output  : {neuron_output:.4f}")
print("(This is: sum of input × weight + bias — the core of every layer)")

# ─────────────────────────────────────────────
# 3. LINEAR REGRESSION — SOLVING WITH MATRICES
# ─────────────────────────────────────────────
# The closed-form solution: W = (X^T X)^(-1) X^T y
# Numpy solves this with lstsq (least squares)

print("\n📈 3. Linear Regression via Matrix Math")
print("-" * 40)

# Features: area and bedrooms
X_features = house_data[:, :2].astype(float)   # area, bedrooms
y_prices    = house_data[:, 2].astype(float)    # price in lakhs

# Add bias column (column of 1s) — standard trick
X_with_bias = np.column_stack([np.ones(len(X_features)), X_features])
print(f"X (with bias column):\n{X_with_bias}")

# Solve: weights = (X^T X)^-1 X^T y
weights, residuals, rank, sv = np.linalg.lstsq(X_with_bias, y_prices, rcond=None)
print(f"\nLearned weights: {weights}")
print(f"  bias     = {weights[0]:.2f}")
print(f"  w_area   = {weights[1]:.4f}  (price change per sqft)")
print(f"  w_beds   = {weights[2]:.2f}  (price change per bedroom)")

# Predict price for a new house: 1500 sqft, 3 bedrooms
new_house = np.array([1, 1500, 3])
predicted_price = np.dot(new_house, weights)
print(f"\nPrediction for 1500 sqft / 3 bed: ₹{predicted_price:.1f} lakhs")

# ─────────────────────────────────────────────
# 4. COSINE SIMILARITY — WORD/DOCUMENT MATCHING
# ─────────────────────────────────────────────
# In NLP, words and sentences are vectors (embeddings).
# How similar two texts are = cosine similarity of their vectors.

print("\n🔍 4. Cosine Similarity — Text/Embedding Matching")
print("-" * 40)

# Simplified word embeddings (in reality these are 768 or 1536-dim)
embedding_cat = np.array([0.9, 0.1, 0.8, 0.2])   # "cat" vector
embedding_dog = np.array([0.8, 0.2, 0.7, 0.3])   # "dog" vector
embedding_car = np.array([0.1, 0.9, 0.2, 0.8])   # "car" vector

def cosine_similarity(vec_a, vec_b):
    dot   = np.dot(vec_a, vec_b)
    norm  = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    return dot / norm

sim_cat_dog = cosine_similarity(embedding_cat, embedding_dog)
sim_cat_car = cosine_similarity(embedding_cat, embedding_car)

print(f"Similarity (cat vs dog): {sim_cat_dog:.4f}  ← should be HIGH")
print(f"Similarity (cat vs car): {sim_cat_car:.4f}  ← should be LOW")
print("(This is how search engines and LLMs find 'related' content)")

# ─────────────────────────────────────────────
# 5. PCA — EIGENVALUES FOR DIMENSIONALITY REDUCTION
# ─────────────────────────────────────────────
# PCA finds the directions of maximum variance in data.
# Those directions are the eigenvectors of the covariance matrix.
# Their eigenvalues tell you how much variance each direction captures.

print("\n🔽 5. PCA — Eigenvalues for Dimensionality Reduction")
print("-" * 40)

# Synthetic dataset: 10 samples, 3 features
np.random.seed(42)
raw_data = np.random.randn(10, 3)
raw_data[:, 2] = raw_data[:, 0] * 0.9 + np.random.randn(10) * 0.1  # feature 3 ≈ feature 1

# Step 1: Mean-center the data
data_centered = raw_data - raw_data.mean(axis=0)

# Step 2: Covariance matrix
cov_matrix = np.cov(data_centered.T)
print(f"Covariance matrix shape: {cov_matrix.shape}")

# Step 3: Eigendecomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort by eigenvalue descending
sort_order   = np.argsort(eigenvalues)[::-1]
eigenvalues  = eigenvalues[sort_order]
eigenvectors = eigenvectors[:, sort_order]

variance_explained = eigenvalues / eigenvalues.sum() * 100
print(f"\nVariance explained by each component:")
for i, (ev, var) in enumerate(zip(eigenvalues, variance_explained)):
    print(f"  PC{i+1}: eigenvalue={ev:.3f}  →  {var:.1f}% of variance")

# Step 4: Project to top 2 components (3D → 2D)
top2_components = eigenvectors[:, :2]
data_2d = data_centered @ top2_components
print(f"\nOriginal shape : {raw_data.shape}   (3 features)")
print(f"Reduced shape  : {data_2d.shape}  (2 components, {variance_explained[:2].sum():.1f}% variance kept)")

# ─────────────────────────────────────────────
# 6. SUMMARY — WHERE EACH CONCEPT APPEARS IN ML
# ─────────────────────────────────────────────
print("\n📊 6. Where Linear Algebra Lives in ML")
print("-" * 40)

summary = {
    "Vectors"         : "Every data sample, word embedding, model weight",
    "Matrices"        : "Datasets, weight matrices, transformations",
    "Dot product"     : "Every neuron computation, attention scores",
    "Matrix multiply" : "Forward pass in neural networks (X @ W + b)",
    "Transpose"       : "Backpropagation gradient calculations",
    "Inverse"         : "Linear regression closed-form solution",
    "Eigenvalues"     : "PCA, understanding data variance, stability",
    "Eigenvectors"    : "Principal components, feature directions",
    "Cosine sim"      : "Embedding similarity, NLP retrieval, RAG",
}

for concept, usage in summary.items():
    print(f"  {concept:<18} → {usage}")

print("\n✅ Day 18 complete — Linear Algebra in ML Applications")
