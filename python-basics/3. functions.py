# Python Basics — Functions
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 4 of my learning journey

# --- BASIC FUNCTION ---
def greet(name):
    return f"Hello, {name}! Welcome to the AI/ML world."

print(greet("Nabarun"))

# --- FUNCTION WITH MULTIPLE PARAMETERS ---
def calculate_experience(start_year, end_year):
    return end_year - start_year

years = calculate_experience(2004, 2025)
print(f"Total IT experience: {years} years")

# --- FUNCTION WITH DEFAULT PARAMETER ---
def describe_skill(skill, level="beginner"):
    return f"Skill: {skill} | Level: {level}"

print(describe_skill("Python"))
print(describe_skill("Machine Learning"))
print(describe_skill("Active Directory", "expert"))

# --- FUNCTION RETURNING MULTIPLE VALUES ---
def profile_summary(name, background, goal):
    years = 18
    return name, background, goal, years

name, bg, goal, exp = profile_summary(
    "Nabarun",
    "IT Infrastructure",
    "MLOps Engineer"
)
print(f"\n--- Profile Summary ---")
print(f"Name: {name}")
print(f"Background: {bg}")
print(f"Goal: {goal}")
print(f"Experience: {exp}+ years")
