# Task - 3

# A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.

# User Input: Prompt the user to specify the desired length of the password.

# Generate Password: Use a combination of random characters to generate a password of the specified length.

# Display the Password: Print the generated password on the screen.

import string
import random

def generate_password(length, include_uppercase=True, include_numbers=True, include_special=True):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    special = '_$@.#' if include_special else ''

    password_chars = []

    if include_uppercase:
        password_chars.append(random.choice(upper))
    if include_numbers:
        password_chars.append(random.choice(digits))
    if include_special:
        password_chars.append(random.choice(special))

    all_characters = lower + upper + digits + special
    while len(password_chars) < length:
        password_chars.append(random.choice(all_characters))

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    return password

def main():
    print("Welcome to the Python Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    min_length = int(include_uppercase) + int(include_numbers) + int(include_special)
    if length < min_length:
        print(f"Password length must be at least {min_length} to include all selected character types.")
        return

    password = generate_password(length, include_uppercase, include_numbers, include_special)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
