def check_password_strength(password):
    """
    Function to check the strength of a password based on various criteria.
    A strong password contains:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character
    - A length of 8 or more characters
    """

    # Initialize flags for each criterion
    has_lowercase = False  # Checks if the password has at least one lowercase letter
    has_uppercase = False  # Checks if the password has at least one uppercase letter
    has_digit = False      # Checks if the password has at least one digit
    has_special = False    # Checks if the password has at least one special character
    min_length = 8         # Minimum required length for a strong password

    # List of special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    # Check each character in the password
    for char in password:
        if char.islower():  # Check for lowercase letters
            has_lowercase = True
        elif char.isupper():  # Check for uppercase letters
            has_uppercase = True
        elif char.isdigit():  # Check for digits
            has_digit = True
        elif char in special_characters:  # Check for special characters
            has_special = True

    # Check if the password meets all criteria
    if len(password) >= min_length and has_lowercase and has_uppercase and has_digit and has_special:
        return "Strong password! 👍"
    else:
        return "Weak password. Make sure it has:\n" \
               "- At least 8 characters\n" \
               "- At least one lowercase letter\n" \
               "- At least one uppercase letter\n" \
               "- At least one digit\n" \
               "- At least one special character"

# Example usage
user_password = input("Enter your password to check its strength: ")
result = check_password_strength(user_password)
print(result)
