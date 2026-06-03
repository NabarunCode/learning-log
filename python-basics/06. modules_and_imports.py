# modules_and_imports.py
# Demonstrating Python module imports

import os
import math
import datetime
from random import randint, choice
import sys as system

# --- Standard library examples ---
# os module
print(os.getcwd())
print(os.listdir("."))

# math module
print(math.sqrt(144))
print(math.pi)

# datetime module
today = datetime.date.today()
print(f"Today is: {today}")

# random module (selective import)
print(randint(1, 100))

# sys alias
print(system.version)
