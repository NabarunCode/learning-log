# Python Basics — Lists and Dictionaries
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 5 of my learning journey

# --- LISTS ---
skills_learning = ["Python", "Machine Learning", "Deep Learning", "MLOps"]

print("=== LISTS ===")
print(f"All skills: {skills_learning}")
print(f"First skill: {skills_learning[0]}")
print(f"Last skill: {skills_learning[-1]}")

# Add and remove
skills_learning.append("Docker")
print(f"After adding Docker: {skills_learning}")

skills_learning.remove("Docker")
print(f"After removing Docker: {skills_learning}")

# Loop through list
print("\nSkills I'm building:")
for skill in skills_learning:
    print(f"  → {skill}")

# List slicing
print(f"\nFirst two skills: {skills_learning[:2]}")

# --- DICTIONARIES ---
print("\n=== DICTIONARIES ===")

profile = {
    "name": "Nabarun",
    "background": "IT Infrastructure",
    "experience_years": 18,
    "current_focus": "AI/ML & MLOps",
    "location": "Kolkata",
    "is_transitioning": True
}

print(f"Name: {profile['name']}")
print(f"Background: {profile['background']}")
print(f"Experience: {profile['experience_years']}+ years")
print(f"Focus: {profile['current_focus']}")

# Add new key
profile["github"] = "github.com/NabarunCode"
print(f"GitHub: {profile['github']}")

# Loop through dictionary
print("\nFull Profile:")
for key, value in profile.items():
    print(f"  {key}: {value}")

# --- LIST OF DICTIONARIES ---
print("\n=== LEARNING ROADMAP ===")

roadmap = [
    {"month": 1, "focus": "Python Basics", "status": "Active"},
    {"month": 2, "focus": "NumPy + Pandas + Linear Algebra", "status": "Upcoming"},
    {"month": 3, "focus": "Beginner ML Projects", "status": "Upcoming"},
    {"month": 4, "focus": "Intermediate ML", "status": "Upcoming"},
    {"month": 5, "focus": "MLOps + Docker", "status": "Upcoming"},
    {"month": 6, "focus": "Portfolio Polish", "status": "Upcoming"},
]

for item in roadmap:
    print(f"  Month {item['month']}: {item['focus']} [{item['status']}]")
