#5.Check if a password contains at least 1 uppercase letter, 1 lowercase letter, 1 digit, and is at least 8 characters long.
password = input("Enter your password: ")
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8

if has_upper and has_lower and has_digit and is_long_enough:
    print("Password is strong.")
else:
    print("Password is weak. Make sure it has at least:")
    print("- 1 uppercase letter")
    print("- 1 lowercase letter")
    print("- 1 digit")
    print("- Minimum 8 characters")
