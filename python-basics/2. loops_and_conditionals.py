# Python Basics — Loops and Conditionals
# Nabarun Chakraborty | IT Infra → AI/ML Transition
# Day 3 of my learning journey

# --- IF / ELIF / ELSE ---
years_experience = 20

if years_experience >= 15:
    print("Senior IT professional — strong foundation for AI/ML transition")
elif years_experience >= 5:
    print("Mid-level professional — good base to build on")
else:
    print("Early career — lots of runway ahead")

# --- FOR LOOP ---
skills_learning = ["Python", "Machine Learning", "FastAI", "MLOps", "Docker"]

print("\nSkills I'm currently learning:")
for skill in skills_learning:
    print(f"  → {skill}")

# --- WHILE LOOP ---
print("\nCounting down to my first ML project:")
countdown = 5
while countdown > 0:
    print(f"  {countdown} weeks to go...")
    countdown -= 1
print("  🚀 First ML project launched!")

# --- LOOP WITH CONDITION ---
print("\nFiltering AI-related skills:")
all_skills = ["Windows Server", "Active Directory", "Python", 
              "Machine Learning", "Virtualization", "MLOps", "Azure"]

ai_skills = []
for skill in all_skills:
    if skill in ["Python", "Machine Learning", "MLOps"]:
        ai_skills.append(skill)

print(f"  AI/ML skills so far: {ai_skills}")
