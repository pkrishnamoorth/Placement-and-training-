#1.Password Validation
import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return "Password length must be between 6 and 16 characters."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    if not re.search(r"[$#@]", password):
        return "Password must contain at least one special character from [$#@]."
    return "Password is valid."

passwords = ["Password123", "Pass123", "password", "PASSWORD123", "Pass@123"]
for pwd in passwords:
    print(f"Password: {pwd}, Validation: {validate_password(pwd)}")

#2.
Alphabet Pattern 'D'
for row in range(7):
    if row == 0 or row == 6:
        print("****")
    else:
        print("*   *")
