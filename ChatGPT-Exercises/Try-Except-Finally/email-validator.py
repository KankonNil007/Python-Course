# Email Validator

# Concepts: for-else, raise, try-except

# 📝 Task:

# Input an email from the user.

# Use a for loop to check if it contains '@' and '.'.

# If it's valid, print "Valid Email".

# If not, raise InvalidEmailError.

# Handle the error using try-except.

class InvalidEmailError(Exception):
    pass

def validate_email(email):
    special_chars = ['@', '.']
    for char in special_chars:
        if char not in email:
            break
    else:
        print("✅ Valid Email!")
        return

    raise InvalidEmailError("Email must contain '@' and '.'")

try:
    email_input = input("Enter your email: ")
    validate_email(email_input)
except InvalidEmailError as e:
    print("❌", e)
finally:
    print("📬 Email validation complete.")
