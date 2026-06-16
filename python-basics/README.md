# 🐍 Python Basics

Scripts from my hands-on Python learning — part of my transition from 18+ years in IT Infrastructure into AI/ML & MLOps.

Each file is a focused, runnable script covering one core concept. Written daily as part of my public learning journal.

---

## ✅ Topics Covered

- [x] Variables & data types
- [x] Loops & conditionals
- [x] Functions
- [x] Lists & dictionaries
- [x] File handling
- [x] Modules & imports
- [x] Error handling
- [x] Automation scripts (file_organiser.py, log_reader.py)
- [x] NumPy basics
- [x] NumPy arrays & operations (numpy_arrays_and_ops.py)
- [x] NumPy indexing, boolean masks & practical exercises (numpy_indexing.py)
- [x] Pandas intro — Series, DataFrames, selection & filtering (pandas_intro.py)
- [x] Pandas wrangling — filtering, grouping, merging, missing data (pandas_wrangling.py)
- [x] Advanced Python Fundamentals — *args, **kwargs, map, filter, comprehensions, generators (15. advanced_python.py)

---

## 📂 File Index

| File | What It Does | Key Concepts |
|------|-------------|--------------|
| `01. variables_and_types.py` | Declares and prints variables of different types | Strings, integers, booleans, lists |
| `02. loops_and_conditionals.py` | Filters skills using loops and conditions | for, while, if/elif/else |
| `03. functions.py` | Builds reusable functions with parameters and return values | def, defaults, multiple returns |
| `04. lists_and_dictionaries.py` | Models a learning roadmap using lists and dicts | append, remove, dict iteration |
| `05. file_handling.py` | Writes, reads, appends, and deletes a text file | open, read, write, append, os |
| `06. modules_and_imports.py` | Demonstrates standard library imports | os, math, datetime, random, sys |
| `07. error_handling.py` | Handles common runtime errors gracefully | try, except, finally, raise |
| `08. file_organiser.py` | Organises files in a folder by extension | os, shutil, automation |
| `09. log_reader.py` | Reads a log file and extracts lines by keyword | file I/O, filtering, reporting |
| `10. numpy_basics.py` | Intro to NumPy arrays, properties, and math functions | np.array, shape, indexing, stats |
| `11. numpy_arrays_and_ops.py` | Deeper dive — reshaping, broadcasting, matrix ops | reshape, dot product, aggregation |
| `12. numpy_indexing.py` | Boolean masks, fancy indexing, np.where(), argmax/argmin, practical exercises | boolean indexing, np.where, argmax, argsort |
| `13. pandas_intro.py` | Intro to Pandas — Series, DataFrames, inspection, selection, filtering | Series, DataFrame, .loc/.iloc, boolean masks |
| `14. pandas_wrangling.py` | Pandas data wrangling — filter, clean, group, merge | dropna, fillna, groupby, agg, merge, apply |
| `15. advanced_python.py` | Advanced Python patterns used across all ML code | *args, **kwargs, map, filter, list/dict/set comprehensions, generators, yield |

---

## 🛠️ How to Run

```bash
# Clone the repo
git clone https://github.com/NabarunCode/learning-log.git
cd learning-log/python-basics

# Run any script
python "01. variables_and_types.py"
python "09. log_reader.py"    # requires sample.log in same folder
```

> NumPy scripts are best run in **Google Colab** — NumPy is pre-installed, no setup needed.

---

## 🧠 Concepts This Folder Demonstrates

- Core Python syntax — variables, control flow, functions, data structures
- File I/O and basic automation scripting
- Error handling for robust, production-style code
- NumPy fundamentals — the foundation for all ML/data work

---

## 🔗 Back to Main

[← learning-log/README.md](../README.md)
