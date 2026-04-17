# error_handling.py
# Demonstrating Python error handling

# Basic try/except
try:
    x = int(input("Enter a number: "))
    print(f"You entered: {x}")
except ValueError:
    print("That's not a valid number.")

# Multiple exceptions
try:
    result = 10 / int(input("Enter a divisor: "))
    print(f"Result: {result}")
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# finally block
try:
    f = open("test.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This always runs.")

# Raising exceptions
def check_age(ag
