# Python Basics — File Handling
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 6 of my learning journey

import os

# --- WRITE TO A FILE ---
print("=== WRITING TO FILE ===")

with open("learning_log.txt", "w") as f:
    f.write("My AI/ML Learning Log\n")
    f.write("=====================\n")
    f.write("Day 1: Variables and data types\n")
    f.write("Day 2: Loops and conditionals\n")
    f.write("Day 3: Functions\n")
    f.write("Day 4: Lists and dictionaries\n")
    f.write("Day 5: File handling\n")

print("File written successfully.")

# --- READ FROM A FILE ---
print("\n=== READING FROM FILE ===")

with open("learning_log.txt", "r") as f:
    contents = f.read()
    print(contents)

# --- APPEND TO A FILE ---
print("=== APPENDING TO FILE ===")

with open("learning_log.txt", "a") as f:
    f.write("Day 6: Modules and imports\n")

print("Content appended successfully.")

# --- READ LINE BY LINE ---
print("\n=== READING LINE BY LINE ===")

with open("learning_log.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.strip()}")

# --- CHECK IF FILE EXISTS ---
print("\n=== FILE EXISTS CHECK ===")

filename = "learning_log.txt"
if os.path.exists(filename):
    print(f"  '{filename}' exists.")
    print(f"  Size: {os.path.getsize(filename)} bytes")
else:
    print(f"  '{filename}' does not exist.")

# --- CLEANUP ---
os.remove("learning_log.txt")
print(f"\n  '{filename}' removed after demo.")
