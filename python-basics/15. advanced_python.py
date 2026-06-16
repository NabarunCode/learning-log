# ============================================================
# 15. advanced_python.py
# Python Advanced Fundamentals
# Topics: *args, **kwargs, map, filter, comprehensions, generators
# Day 21 — AI/ML Transition · github.com/NabarunCode/learning-log
# ============================================================


# ============================================================
# SECTION 1: *args — Variable Positional Arguments
# Use when you don't know how many values will be passed in
# ============================================================

def log_metrics(*metric_names):
    """Accept any number of metric names and print them."""
    print("📋 Metrics to track:")
    for name in metric_names:
        print(f"  - {name}")

log_metrics("accuracy", "loss", "f1_score")
log_metrics("precision", "recall")          # fewer args — still works


# ============================================================
# SECTION 2: **kwargs — Variable Keyword Arguments
# Use when you don't know what named params will be passed in
# ============================================================

def configure_model(**hyperparams):
    """Accept any number of named hyperparameters."""
    print("\n⚙️  Model configuration:")
    for param, value in hyperparams.items():
        print(f"  {param}: {value}")

configure_model(learning_rate=0.001, epochs=10, batch_size=32)
configure_model(optimizer="adam", dropout=0.2)   # different params — still works


# ============================================================
# SECTION 3: *args + **kwargs together
# Real-world: a training summary function
# ============================================================

def training_summary(model_name, *dataset_splits, **settings):
    print(f"\n🚀 Model     : {model_name}")
    print(f"   Splits    : {dataset_splits}")
    print("   Settings  :")
    for key, value in settings.items():
        print(f"     {key}: {value}")

training_summary("ResNet50", "train", "val", "test", lr=0.01, epochs=5, device="cuda")


# ============================================================
# SECTION 4: map() — Apply a function to EVERY item
# Returns a lazy map object → wrap in list() to see results
# ============================================================

raw_scores = [0.67, 0.82, 0.91, 0.55, 0.74]

# Convert fractions to percentages
percentages = list(map(lambda score: round(score * 100, 1), raw_scores))
print(f"\n📊 Raw scores    : {raw_scores}")
print(f"   Percentages  : {percentages}")

# With a named function instead of lambda
def grade_label(score):
    return "PASS" if score >= 0.70 else "FAIL"

labels = list(map(grade_label, raw_scores))
print(f"   Labels       : {labels}")


# ============================================================
# SECTION 5: filter() — Keep only items that match a condition
# Returns a lazy filter object → wrap in list() to see results
# ============================================================

model_accuracies = [0.55, 0.71, 0.63, 0.88, 0.92, 0.48]
passing_threshold = 0.70

strong_models = list(filter(lambda acc: acc >= passing_threshold, model_accuracies))
print(f"\n🔍 All accuracies   : {model_accuracies}")
print(f"   Above threshold : {strong_models}")


# ============================================================
# SECTION 6: List Comprehensions — Concise list building
# Mental model: [expression for item in iterable if condition]
# ============================================================

errors = [0.1, 0.3, 0.2, 0.5, 0.05]

# Verbose loop version:
squared_verbose = []
for e in errors:
    squared_verbose.append(e ** 2)

# Comprehension — same result, one line:
squared_errors = [e ** 2 for e in errors]
print(f"\n📐 Squared errors       : {squared_errors}")

# With condition — keep only large errors:
large_errors = [e for e in errors if e > 0.2]
print(f"   Errors above 0.2   : {large_errors}")


# ============================================================
# SECTION 7: Dictionary Comprehensions
# ============================================================

feature_names = ["age", "income", "credit_score", "loan_amount"]

# Build a feature → index lookup in one line:
feature_index = {feature: idx for idx, feature in enumerate(feature_names)}
print(f"\n🗂️  Feature index map : {feature_index}")

# Flip it — index → feature:
index_to_feature = {idx: feature for feature, idx in feature_index.items()}
print(f"   Index to feature  : {index_to_feature}")


# ============================================================
# SECTION 8: Set Comprehensions — Unique values, no duplicates
# ============================================================

raw_labels = ["cat", "dog", "cat", "bird", "dog", "fish", "bird"]
unique_classes = {label for label in raw_labels}
print(f"\n🏷️  Unique class labels : {unique_classes}")   # order not guaranteed


# ============================================================
# SECTION 9: Generators — Memory-efficient iteration
# Key difference: list loads all data → generator yields ONE item at a time
# ============================================================

# Generator FUNCTION — uses yield instead of return
def batch_loader(dataset, batch_size):
    """Yield one batch at a time — never loads the full dataset into RAM."""
    for start in range(0, len(dataset), batch_size):
        yield dataset[start : start + batch_size]

training_samples = list(range(1, 21))   # 20 samples
print("\n🔁 Batching training data (batch_size=5):")
for batch in batch_loader(training_samples, batch_size=5):
    print(f"   Batch: {batch}")

# Generator EXPRESSION — lazy version of a list comprehension
# 1 million values — a list would use ~8MB RAM; generator uses almost nothing
million_samples = range(1, 1_000_001)
milestone_squares = (n ** 2 for n in million_samples if n % 200_000 == 0)
print("\n⚡ Generator — every 200,000th sample squared (zero memory spike):")
for value in milestone_squares:
    print(f"   {value}")


# ============================================================
# MENTAL MODEL RECAP
# ============================================================
print("""
╔═══════════════════════════════════════════════════════════╗
║               WHEN TO USE WHAT                           ║
╠═══════════════════════════════════════════════════════════╣
║  Small data, one-liner   →  List / Dict comprehension    ║
║  Large / streaming data  →  Generator  (yield)           ║
║  Tabular / ML data       →  Pandas                       ║
║  Transform every item    →  map()                        ║
║  Keep matching items     →  filter()                     ║
║  Flexible function args  →  *args / **kwargs             ║
╚═══════════════════════════════════════════════════════════╝
""")
