import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "No character types selected!"

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User Input
print("Welcome to Password Generator!")
length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and display password
password = generate_password(length, use_upper, use_digits, use_symbols)
print("\nGenerated Password:", password)
