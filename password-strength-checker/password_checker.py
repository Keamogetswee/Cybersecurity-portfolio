import re

def check_password_strength(password):
    # Define rules
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Collect errors
    errors = []
    if length_error:
        errors.append("Password must be at least 8 characters long.")
    if digit_error:
        errors.append("Password must contain at least one number.")
    if uppercase_error:
        errors.append("Password must contain at least one uppercase letter.")
    if lowercase_error:
        errors.append("Password must contain at least one lowercase letter.")
    if symbol_error:
        errors.append("Password must contain at least one special character.")

    if errors:
        return False, errors
    return True, ["Password is strong!"]

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strong, feedback = check_password_strength(password)
    for f in feedback:
        print(f)
