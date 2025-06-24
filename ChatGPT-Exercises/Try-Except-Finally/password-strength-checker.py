# Password Strength Checker

# Concepts: for-else, raise, try-except

# 📝 Task:

# Ask the user to input a password.

# Use a loop to check if it has at least one uppercase, one lowercase, one digit, and one special character.

# If it passes all, print "Strong password!".

# If not, raise a custom error like WeakPasswordError.

class WeakPasswordError(Exception):
    pass

def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    specials = "!@#$%^&*()-_+=<>?/|"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in specials:
            has_special = True

    if not (has_upper and has_lower and has_digit and has_special):
        raise WeakPasswordError("Password must have upper, lower, digit, and special character.")
    else:
        print("✅ Strong password!")

try:
    pwd = input("Enter your password: ")
    check_password(pwd)
except WeakPasswordError as e:
    print("❌", e)
finally:
    print("Password check complete.")
